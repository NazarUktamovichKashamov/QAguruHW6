import pytest

import os.path
import shutil
from zipfile import ZipFile

from set_path import ZIP_DIR, RESOURCES_DIR, ZIP_FILE

@pytest.fixture(scope='session', autouse=True)
def test_pack_files_to_zipchick():
    if not os.path.exists(ZIP_DIR):
        os.mkdir(ZIP_DIR)
    with ZipFile(ZIP_FILE, 'w') as zipfile:
        for file in os.listdir(RESOURCES_DIR):
            ZipFile.write(os.path.join(RESOURCES_DIR, file), file)


    yield

    shutil.rmtree(ZIP_DIR)