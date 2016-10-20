# -*- coding: utf-8 -*-
"""
The module :mod:`openerp.tests.common` provides unittest test cases and a few
helpers and classes to write tests.

"""
import errno
import logging
import os
import select
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta

from openerp.tests.common import HttpCase, get_db_name, HOST, PORT
from openerp.modules.module import get_module_path

_logger = logging.getLogger(__name__)


class RobotframeworkTest(HttpCase):
    """ Transactional HTTP TestCase with url_open and robotframework helpers.
    """

    def robot_poll(self, robot, timeout):
        """ Robot Framework Test protocol.

        Use console.log in pybot to output test results:

        - for a success: console.log("ok")
        - for an error:  console.log("error")

        Other lines are relayed to the test log.

        """
        t0 = datetime.now()
        td = timedelta(seconds=timeout)
        buf = bytearray()
        failed = False
        while True:
            # timeout
            msg = "Robot tests should take less than %s seconds" %  timeout
            self.assertLess(datetime.now() - t0, td, msg)

            # read a byte
            try:
                ready, _, _ = select.select([robot.stdout], [], [], 0.5)
            except select.error, e:
                # In Python 2, select.error has no relation to IOError or
                # OSError, and no errno/strerror/filename, only a pair of
                # unnamed arguments (matching errno and strerror)
                err, _ = e.args
                if err == errno.EINTR:
                    continue
                raise

            if ready:
                s = robot.stdout.read(1)
                if not s:
                    _logger.info("robot_poll end")
                    return failed
                buf.append(s)

            # process lines
            if '\n' in buf:
                line, buf = buf.split('\n', 1)
                line = str(line)
                lline = line.lower().strip()

                _logger.info("pybot: %s", line)

                # the output ends with "report.html"
                if lline.endswith('report.html'):
                    return failed

                elif lline.endswith("| fail |"):
                    failed = True
                    _logger.error("pybot: %s", line)


    def robot_run(self, cmd, timeout):
        _logger.info('robot_run executing %s', ' '.join(cmd))

        failed = False
        try:
            robot = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None)
            _logger.debug("Spawned process")
        except OSError as err:
            raise unittest.SkipTest("pybot not found")
        try:
            failed = self.robot_poll(robot, timeout)
        finally:
            # kill pybot if robot.exit() wasn't called in the test
            if robot.poll() is None:
                robot.terminate()
                robot.wait()
            self._wait_remaining_requests()

            # we ignore pybot return code as we kill it as soon as we have ok
            _logger.info("robot_run execution finished")
            if failed:
                self.fail("Robot test failed")


    def robot(self, url_path, testfile, login=None, timeout=6000,
              failfast=False, **kw):
        """ Test js code running in the browser
        - optionally log as 'login'
        - load page given by url_path
        - wait for ready object to be available
        - eval(code) inside the page

        To signal success test do:
        console.log('ok')

        To signal failure do:
        console.log('error')

        If neither are done before timeout test fails.
        """

        # transform the testfile path into a absolut path by
        # searching for the addon
        addon_name = str(self.__class__.__module__)[len('openerp.addons.'):]
        addon_name = addon_name[:addon_name.find('.')]
        testfile_path = os.path.join(get_module_path(addon_name), testfile)

        self.authenticate(login, login)

        # the log directory is odoo so it works best in runbot
        # normally /home/openerp/odoo
        odoo_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
        log_directory = os.path.join(odoo_directory, '..', 'logs', 'robot')
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        log_prefix = '%s.%s.%s_' % (addon_name,
                                    str(self.__class__.__name__),
                                    self._testMethodName)
        log_directory = tempfile.mkdtemp(prefix=log_prefix, dir=log_directory)

        cmd = ['pybot',
               "-v URL:%s" % "http://%s:%s%s" % (HOST, PORT, url_path),
               "-v COOKIE_NAME:session_id",
               "-v COOKIE_VALUE:%s" % self.session_id,
               "-d", log_directory,
               testfile_path]
        if failfast:
            cmd.append('--exitonerror')
        self.robot_run(cmd, timeout)
