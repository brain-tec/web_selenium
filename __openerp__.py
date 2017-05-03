# b-*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2013 brain-tec AG (http://www.brain-tec.ch) 
#    All Right Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Extension to record testcases with selenium",
    "version" : "1.0",
    "author" : "Andreas Stauder, brain-tec AG <andreas.stauder@brain-tec.ch>",
    "description": """
    Extends HTML with tags to enable selenium builder (http://sebuilder.github.io/se-builder/) to record use cases.

    To install the selenium builder:

    1. Download Selenium Builder from https://github.com/sebuilder/se-builder/archive/master.zip
       and unpack it (creates directory se-builder-master).

    2. Change to directory se-builder-master and apply the patch in patches with
    patch -p0 < /path/to/web_selenium/patch/se-builder/se-builder-master.patch

    3. Create a textfile named "seleniumbuilder@saucelabs.com"
    with the absolute pathname to the se-builder-master directory, e.g.
    /Users/zar/Projects/SeBuilder/se-builder/se-builder/seleniumbuilder/

    4. Save this file in your profile folder, e.g.
    /Users/zar/Library/Application Support/Firefox/Profiles/k3xrgtby.dev/extensions/seleniumbuilder@saucelabs.com

    5. Restart Firefox and you get prompted if you want to install the Builder.

    6. Record the use cases and save the file in

    """,
    "category" : "Hidden",
    "website" : "http://www.brain-tec.ch",
    "depends" : ["web"],
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : [],
    "data" : [
        'assets.xml'
    ],
    "js" : [],
    "css" : [],
    "qweb" : [
        'static/src/xml/base_ext.xml',
    ],
    "active": False,
    "installable": True,
    'bootstrap': True,
}
