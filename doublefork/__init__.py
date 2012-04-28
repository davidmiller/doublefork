"""
doublefork

namespacing and packageability
"""
from doublefork.daemon import Daemon
from doublefork._version import __version__

__all__ = [
    '__version__',
    'Daemon'
    ]
