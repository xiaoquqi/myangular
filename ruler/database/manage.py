#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2016. This file is confidential and proprietary.
# All Rights Reserved, Huron Technologies (http://www.hihuron.com)

import os
import sys

possible_topdir = os.path.normpath(os.path.join(
    os.path.abspath(sys.argv[0]), os.pardir, os.pardir, os.pardir))
if os.path.exists(os.path.join(possible_topdir, "ruler", "__init__.py")):
    sys.path.insert(0, os.path.join(possible_topdir))

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from ruler import app, db
#from ruler.helpers import utils
from ruler.database.models import *

#utils.load_configs()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
