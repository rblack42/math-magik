import os
from mmdesigner.Generator import Generator
from mmdesigner.TreeWalker import TreeWalker


def test_generate_stl():
    """Check generator builds all STL files"""
    root = "tests/test_data/model"
    gen = Generator(root)
    tw = TreeWalker(root, "stl",None)
    tw.clean("stl")
    gen.run_leaf_stl("stl")
    assert os.path.isfile(os.path.join(root, "wing/wing.stl"))

def test_generate_mass_properties():
    """Check creates json file with mass properties"""
    root = "tests/test_data/model"
    gen = Generator(root)
    tw = TreeWalker(root, "stl",None)
    tw.clean("json")
    gen.run_leaf_stl("mass")
    assert os.path.isfile(os.path.join(root, "wing/wing.json"))

def test_generates_excel():
    """Check generation of excel file"""
    root = "tests/test_data/model"
    gen = Generator(root)
    gen.gen_excel()
    assert os.path.isfile(os.path.join(root, "model.xlsx"))

def test_run_all():
    root = "tests/test_data/model"
    gen = Generator(root)
    tw = TreeWalker(root, 'scad',None)
    gen.run_all('stl')
    gen.run_all('mass')
    assert os.path.isfile(os.path.join(root,"body/rudder/rudder.stl"))
    assert os.path.isfile(os.path.join(root,"body/rudder/rudder.json"))
