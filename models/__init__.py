#!/usr/bin/python3
"""
make directory an module
"""
from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
