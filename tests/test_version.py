import mmdesigner
from mmdesigner import __version__


def test_version():
    """Return current application version string"""
    mm = mmdesigner
    assert mm.version() == __version__
