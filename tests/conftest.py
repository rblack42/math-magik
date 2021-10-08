import os
import pytest
from mmdesigner.Gui import Gui


@pytest.fixture(scope='function')
def testenv():
    os.environ['MMDESIGNER_PATH'] = 'tests/test_data'
    os.environ['MMDESIGNER_MDEL'] = 'model'

@pytest.fixture
def window(qtbot):
    test_window = Gui()
    qtbot.add_widget(test_window)
    test_window.show()
    return test_window

