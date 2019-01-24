#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, glob, pathlib

wh_extension = [".txt", ".png", ".pdf", ".jpeg", ".odp", ".zip", ".rar",".bmp"]


def check_extension_file(file):
    """ Check if the file is valid against the white list

    Args:
        file(file): file system

    Returns: valid file extension

    """

    for extension in wh_extension:
        if extension == pathlib.PurePosixPath(file).suffix:
            print("Fichier Valide")
            return True
    return False


