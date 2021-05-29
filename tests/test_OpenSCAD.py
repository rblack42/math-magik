from mmdesigner.OpenSCAD import OpenSCAD
import os


def test_OSC_version():
    mgr = OpenSCAD()
    version = mgr.get_version()
    assert version == "2019.05"

