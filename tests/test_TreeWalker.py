import os
import shutil
from mmdesigner.TreeWalker import TreeWalker

count = 0


def test_bad_model_path():
    """Check bad model path returns None"""
    root = "bad"
    tw = TreeWalker(root)
    assert tw.get_model_path() is None


def test_valid_model_path():
    """Test good model path returns path"""
    root = 'tests/test_data/model'
    tw = TreeWalker(root)
    assert tw.get_model_path() == root


def test_dir_has_no_scad_file():
    """Test directory with no scad files returns None"""
    root = 'tests'
    tw = TreeWalker(root)
    assert tw.get_model_path() is None


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
    tw = TreeWalker(root, "scad", "")
    files = tw.get_file_list()
    assert len(files) == 6


def test_leaf_file_list():
    """Test that leaf list is correct"""
    root = "tests/test_data/model"
    tw = TreeWalker(root, "scad", "")
    files = tw.get_leaf_file_list()
    assert len(files) == 4


def test_non_lesf_file_list():
    """Test that non-leaf file list is correct"""
    root = "tests/test_data/model"
    tw = TreeWalker(root, "scad", "")
    files = tw.get_non_leaf_file_list()
    assert len(files) == 2


def bump_count(path):
    global count

    count += 1


def test_process_files():
    """Check all selected files get processed"""
    global count

    root = "tests/test_data/model"
    count = 0
    tw = TreeWalker(root, "scad", bump_count)
    tw.process_files()
    assert count == 6


def test_process_leaf_files():
    """Check all selected leaf files get processed"""
    global count

    root = "tests/test_data/model"
    count = 0
    tw = TreeWalker(root, "scad", bump_count)
    tw.process_leaf_files()
    assert count == 4


def test_delete_files():
    """Check that clean removes selected files"""
    root = "tests/test_data/model"
    p1 = "tests/test_data/model"
    p2 = "tests/test_data/model/wing"
    f1 = os.path.join(p1, "clean1.tst")
    f2 = os.path.join(p2, "clean2.tst")
    with open(f1, "w") as fout:
        fout.write("testing")
    shutil.copyfile(f1, f2)
    tw = TreeWalker(root, "scad", None)
    current_ext = tw.get_extension()
    tw.clean("tst")
    assert not os.path.isfile(f1)
    assert not os.path.isfile(f2)
    assert tw.get_extension() == current_ext
