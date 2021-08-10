#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()


def convert_to_dict(my_list):
        kwarks = {}

        for i in my_list:
            list_tmp = i.split("=")
            key = list_tmp[0]
            value = list_tmp[1]

            if value[0] == '"':
                value = value.strip('"')
                value = value.replace("_", " ")
            else:
                value = eval(value)

            kwarks[key] = value

        return kwarks
