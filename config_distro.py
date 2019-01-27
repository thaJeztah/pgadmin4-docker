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

if strtobool(os.getenv('SERVER_MODE', "false")) and "PGADMIN_SETUP_EMAIL" in os.environ and "PGADMIN_SETUP_PASSWORD" in os.environ:
    SERVER_MODE = True
else:
    SERVER_MODE = False

DEFAULT_SERVER = '0.0.0.0'
DEFAULT_SERVER_PORT = int(os.getenv('PG_ADMIN_PORT', 5050))


##########################################################################
# User account and settings storage
##########################################################################

SQLITE_PATH = os.path.join(DATA_DIR, 'config', 'pgadmin4.db')

SESSION_DB_PATH = os.getenv('PG_ADMIN_SESSION_DIR', '/dev/shm/pgAdmin4_session')

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

##########################################################################
# Default locations for binary utilities (pg_dump, pg_restore etc)
#
# These are intentionally left empty in the main config file, but are
# expected to be overridden by packagers in config_distro.py.
#
# A default location can be specified for each database driver ID, in
# a dictionary. Either an absolute or relative path can be specified.
# In cases where it may be difficult to know what the working directory
# is, "$DIR" can be specified. This will be replaced with the path to the
# top-level pgAdmin4.py file. For example, on macOS we might use:
#
# $DIR/../../SharedSupport
#
##########################################################################
DEFAULT_BINARY_PATHS = {
    "pg":   "/usr/local/bin",
    "ppas": "/usr/local/bin",
    "gpdb": "/usr/local/bin"
}
