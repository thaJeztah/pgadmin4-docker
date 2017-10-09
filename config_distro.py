# -*- coding: utf-8 -*-

##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2016, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
# config_local.py - Core application configuration settings
#
##########################################################################

import os
from distutils.util import strtobool
from logging import *

# Data directory for storage of config settings etc. This shouldn't normally
# need to be changed - it's here as various other settings depend on it.
DATA_DIR = os.getenv('PG_ADMIN_DATA_DIR', '/pgadmin/')


##########################################################################
# Log settings
##########################################################################

DEBUG = strtobool(os.getenv('DEBUG', "False"))

# Log to stdout so that logging is handled by Docker logging drivers
LOG_FILE = '/dev/stdout'

##########################################################################
# Server settings
##########################################################################

SERVER_MODE = False

DEFAULT_SERVER = '0.0.0.0'
DEFAULT_SERVER_PORT = int(os.getenv('PG_ADMIN_PORT', 5050))


##########################################################################
# User account and settings storage
##########################################################################

SQLITE_PATH = os.path.join(DATA_DIR, 'config', 'pgadmin4.db')

SESSION_DB_PATH = '/dev/shm/pgAdmin4_session'

##########################################################################
# Upgrade checks
##########################################################################

# Disable upgrade checks; container should be immutable
UPGRADE_CHECK_ENABLED = False

##########################################################################
# Storage Manager storage url config settings
# If user sets STORAGE_DIR to empty it will show all volumes if platform
# is Windows, '/' if it is Linux, Mac or any other unix type system.

# For example:
# 1. STORAGE_DIR = get_drive("C") or get_drive() # return C:/ by default
# where C can be any drive character such as "D", "E", "G" etc
# 2. Set path manually like
# STORAGE_DIR = "/path/to/directory/"
##########################################################################
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
