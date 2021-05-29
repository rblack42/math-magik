from mmdesigner.OpenSCAD import OpenSCAD


def test_OSC_version():
    mgr = OpenSCAD()
    version = mgr.get_version()
    year, rel = version.split(".")
    assert int(year) >= 2019
