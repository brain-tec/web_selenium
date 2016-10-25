============
Web Selenium
============

This module extends Odoo user interface with tags to enable Selenium Builder (http://sebuilder.github.io/se-builder/) and record use cases.

Install
=======

To install Selenium Builder:

* Download Selenium Builder from https://github.com/sebuilder/se-builder/archive/master.zip and unpack it (creates directory se-builder-master).
* Change to directory se-builder-master and apply the patch in patches with patch -p0 < /path/to/web_selenium/patch/se-builder/se-builder-master.patch
* Create a textfile named "seleniumbuilder@saucelabs.com" with the absolute pathname to the se-builder-master directory, e.g. /Users/zar/Projects/SeBuilder/se-builder/se-builder/seleniumbuilder/
* Save this file in your profile folder, e.g. /Users/zar/Library/Application Support/Firefox/Profiles/k3xrgtby.dev/extensions/seleniumbuilder@saucelabs.com
* Restart Firefox and you get prompted if you want to install the Builder.
* Record the use cases and save the file in testfile.robot