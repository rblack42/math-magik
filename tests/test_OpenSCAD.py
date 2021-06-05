import os
import json
from mmdesigner.OpenSCAD import OpenSCAD


def test_OSC_version():
    """Test app returns installed OpenSCAD version"""
    mgr = OpenSCAD()
    version = mgr.get_version()
    year, rel = version.split(".")
    assert int(year) >= 2019


def test_OSC_STL_generator():
    """Test generation of STL file from specified SCAD file"""
    mgr = OpenSCAD()
    scad_file = "tests/test_data/spar.scad"
    stl_file = "tests/test_data/spar.stl"
    if os.path.exists(stl_file):
        os.remove(stl_file)
    mgr.gen_stl(scad_file)
    assert os.path.isfile(stl_file)


def test_OSC_STL_bad_file():
    """Test error return on bad file name"""
    mgr = OpenSCAD()
    assert mgr.gen_stl("bad") == 1


def test_OSC_STL_bad_stl_name():
    """Test error return on non-scad file name"""
    stl_file = "tests/test_data/spar.stl"
    mgr = OpenSCAD()
    assert mgr.gen_stl(stl_file) == 1


def test_mass_properties():
    mgr = OpenSCAD()
    scad_file = "tests/test_data/spar.scad"
    err_code = mgr.get_properties(scad_file)
    assert err_code == 0
    assert mgr.get_bounds() == [1.0, 0.0, 5.0, 0.0, 1.0, 0.0]


def test_OSC_json():
    mgr = OpenSCAD()
    scad_file = "tests/test_data/spar.scad"
    json_file = "tests/test_data/spar.json"
    err_code = mgr.get_properties(scad_file)
    assert err_code == 0
    mgr.dump_to_json(json_file)
    with open(json_file) as jin:
        jdata = json.load(jin)
        assert float(jdata["maxy"]) == 5.0
