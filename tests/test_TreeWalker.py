import os
from mmdesigner.TreeWalker import TreeWalker


def test_bad_model_path():
    """Check bad model path returns None"""
    root = "bad"
    tw = TreeWalker(root)
    assert tw.get_model_path()== None


def test_valid_model_path():
    """Test good model path returns path"""
    root = 'tests/test_data/model'
    tw = TreeWalker(root)
    assert tw.get_model_path() == root


def test_dir_has_no_scad_file():
    """Test directory with no scad files returns None"""
    root = 'tests'
    tw = TreeWalker(root)
    assert tw.get_model_path() == None


def test_treewalker_extension():
    """Test extension is registered"""
    root = "tests/test_data/model"
    tw = TreeWalker(root, "scad", "gen_stl")
    assert tw.get_extension() == "scad"

def test_treewalker_callback():
    """Check callback is registered"""
    root = "tests/test_data/model"
    tw = TreeWalker(root, "scad", "gen_stl")
    assert tw.get_callback() == "gen_stl"

def test_model_file_list():
    """Check file list is correct"""
    root = "tests/test_data/model"
    tw = TreeWalker(root, "scad","")
    files = tw.get_file_list()
    assert len(files) == 6

def test_leaf_file_list():
    """Test that leaf list is correct"""
    root = "tests/test_data/model"
    tw = TreeWalker(root, "scad","")
    files = tw.get_leaf_file_list()
    assert len(files) == 4
