#!/usr/bin/env python
# Copyright (C) 2010-2014 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import re


def valid_serial_key(serial_key):
    """Determines whether `serial_key` has a valid encoding."""
    parts = serial_key.split('-')
    if len(parts) != 5:
        return False

    for part in parts:
        if not re.match('[A-Z0-9]{5}$', part):
            return False

    return True