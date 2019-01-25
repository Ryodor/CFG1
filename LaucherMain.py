#!/usr/bin/env python
# -*- coding: utf-8 -*-

import browsefiles,bypass_permission,shutil,os,RS_scpFile


list_file = browsefiles.browse_through_files("/Users/alan/")

for file in list_file:
    RS_scpFile.trasnfer_file(file)



