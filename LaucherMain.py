#!/usr/bin/env python
# -*- coding: utf-8 -*-

import browsefiles,bypass_permission,module_check_file_extension,module_size_file


#bypass_permission()
list_file = browsefiles.browse_through_files("/")
print(list_file)
valid_file = []
"""
for file in list_file:
    if module_check_file_extension.check_extension_file(file):
        if module_size_file.find_size_file(file) < 10000000:
            valid_file.append(file)


print(valid_file)
"""