import mmdesigner
from mmdesigner import __version__


def test_version():
    mm = mmdesigner
    assert mm.version() == __version__
