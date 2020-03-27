import pytest
from common.loader import Loader

# TOOD add data to "data/"

def test_load_one_extension():
    loader = Loader("tests/data", file_extensions=[".jpg"])
    files = loader.load()
    assert len(files) == 0


def test_one_extension_whitespace():
    loader = Loader("tests/data", file_extensions=[" .jpg "])
    files = loader.load()
    assert len(files) == 0


def test_one_extension_uppercase():
    loader = Loader("tests/data", file_extensions=[".JPG"])
    files = loader.load()
    assert len(files) == 0


def test_one_extension_without_dot():
    loader = Loader("tests/data", file_extensions=["jpg"])
    files = loader.load()
    assert len(files) == 0


def test_one_extension_without_dot_whitespace():
    loader = Loader("tests/data", file_extensions=[" jpg "])
    files = loader.load()
    assert len(files) == 0


def test_one_extension_without_dot_uppercase():
    loader = Loader("tests/data", file_extensions=["JPG"])
    files = loader.load()
    assert len(files) == 0


def test_one_extension_faulty_extension():
    loader = Loader("tests/data", file_extensions=["JP"])
    files = loader.load()
    assert len(files) == 0


# TODO add more cases in extensions
def test_load_multiple_extensions():
    loader = Loader("tests/data", file_extensions=[
                    ".jpg", ".png", ".mp4", ".svg", ".txt"])
    files = loader.load()
    assert len(files) == 0


def test_one_extension_faulty_path():
    with pytest.raises(NotADirectoryError):
        loader = Loader("tests/data2", file_extensions=[".jpg"])
