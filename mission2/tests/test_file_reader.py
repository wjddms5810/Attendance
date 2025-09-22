import pytest
from mission2.file_reader import FileReader


@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_file.txt"
    file.write_text("user1 monday\nuser2 tuesday\nuser3 wednesday\n")
    return file

def test_read_valid_file(temp_file):
    reader = FileReader(file_name=str(temp_file), max_lines=5)
    result = list(reader.read())

    assert result == [
        ("user1", "monday"),
        ("user2", "tuesday"),
        ("user3", "wednesday"),
    ]

def test_read_file_not_found():
    reader = FileReader(file_name="non_existent_file.txt", max_lines=5)

    with pytest.raises(FileNotFoundError):
        list(reader.read())