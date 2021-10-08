import mmdesigner
import pytest


def test_window_title(window):
    assert window.windowTitle() == "Math Magik Designer"


