import logging
import os
import shutil

import pytest

LOGGER = logging.getLogger(__name__)

TESTS_DIR = os.path.dirname(__file__)
WORKING_DIR = os.path.join(TESTS_DIR, "__temp__")

MONTH_QTR_DATA = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (6, 2),
    (7, 3),
    (8, 3),
    (9, 3),
    (10, 4),
    (11, 4),
    (12, 4),
]


@pytest.fixture(scope="function")
def temp_location():

    # Setup
    if not os.path.exists(WORKING_DIR):
        os.mkdir(WORKING_DIR)

    yield

    # Teardown / Cleanup
    try:
        shutil.rmtree(WORKING_DIR)
    except OSError as ex:  # if failed, report it back to the user
        LOGGER.error(f"Error: {ex.filename} - {ex.strerror}.")
