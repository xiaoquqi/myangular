#!/usr/bin/env python
# -*- coding: utf-8 -*-

# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2016. This file is confidential and proprietary.
# All Rights Reserved, Huron Technologies (http://www.hihuron.com)

from ruler import app
from ruler.helpers import utils

from ruler.controllers.hosts import hosts_page
from ruler.controllers.root import root_page
from ruler.controllers.salt_masters import salt_masters_page
from ruler.controllers.settings import settings_page
from ruler.controllers.datacenters import datacenters_page
from ruler.controllers.openstacks import openstacks_page
from ruler.controllers.tasks import tasks_page
from ruler.controllers.users import users_page

DEFAULT_PORT = 8080

# Load config from file
utils.load_configs()

# setup logging
utils.setup_logging()

utils.setup_language(app)

# setup login manager
utils.setup_login_manager()

# setup admin user
utils.setup_user()

# Register Blueprint
app.register_blueprint(root_page)
app.register_blueprint(hosts_page)
app.register_blueprint(salt_masters_page)
app.register_blueprint(settings_page)
app.register_blueprint(datacenters_page)
app.register_blueprint(openstacks_page)
app.register_blueprint(tasks_page)
app.register_blueprint(users_page)

if __name__ == "__main__":
    port = int(app.config.get("PORT", DEFAULT_PORT))
    app.run("0.0.0.0", port=port)
