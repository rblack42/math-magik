import os
import pytest


@pytest.fixture(scope='function')
def testenv():
    os.environ['MMDESIGNER_PATH'] = 'tests/test_data'
    os.environ['MMDESIGNER_MDEL'] = 'model'

