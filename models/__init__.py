#!/usr/bin/python3
'''Module: __init__.py
    treat models directory as packages, handle global variables'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
