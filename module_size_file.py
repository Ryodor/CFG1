#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def find_size_file(filename):
    """ Find size the file

    Args:
        filename(file): file

    Returns:

    """

    if os.path.isfile(filename):
        return os.path.getsize(filename)
    return "ERROR : is not valid file"

