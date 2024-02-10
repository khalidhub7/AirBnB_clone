#!/usr/bin/python3
"""make my directory an module"""
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
