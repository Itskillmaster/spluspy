from .client.soroushclient import SoroushClient as Client
from .network import connection
from .tl.custom import Button
from .tl import patched as _  # import for its side-effects
from . import version, events, utils, errors, functions, custom
from .filters import filters
from .enums import MessageMediaType

__version__ = version.__version__

__all__ = [
    'Client', 'Button', 'filters', 'MessageMediaType',
    'functions', 'custom', 'errors',
    'events', 'utils', 'connection'
]
