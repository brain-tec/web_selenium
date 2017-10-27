# -*- coding: utf-8 -*-
# Copyright (c) 2013 brain-tec AG (http://www.brain-tec.ch)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Web Selenium",
    "summary": "Record your testcases with Selenium",
    "version": "11.0.1.0.0",
    "category": "Hidden",
    "website": "http://www.brain-tec.ch",
    "author": "Andreas Stauder <andreas.stauder@brain-tec.ch> and Alejandro Sanchez <alejandro.sanchez@braintec-group.com>",
    "depends": ["web"],
    "data": [
        'views/webclient_templates.xml'
    ],
    "qweb": [
        'static/src/xml/base_ext.xml',
    ],
    "active": False,
    "installable": True,
    'bootstrap': True,
}
