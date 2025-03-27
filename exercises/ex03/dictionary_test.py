"""Unit Test on Dictionaries for exercise 03"""

__author__: "730649767"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_base():
    """Test basic key-value pairs inverse"""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_edge():
    """Test Invert of empy dictionary"""
    assert invert({}) == {}


def test_invert_same():
    """test inverted dictionary with repeated values"""
    try:
        invert({"a": "1", "b": "1"})
    except ValueError:
        assert True
    else:
        assert False


def test_count_basic():
    """Test count occurence"""
    assert count(["apple", "banana", "apple"]) == {"apple": 2, "banana": 1}


def test_count_edge():
    """Test Counting occurencies in empty list"""
    assert count([]) == {}


def test_count_unique():
    """Test counting when unique elements"""
    assert count(["1", "2", "3", "4"]) == {"1": 1, "2": 1, "3": 1, "4": 1}


def test_favorite_color_base():
    """Test finding the most frequent color"""
    assert favorite_color({"Alice": "blue", "Bob": "red", "charlie": "blue"}) == "blue"


def test_favorite_color_edge():
    """Test with only one person's favorite color"""
    assert favorite_color({"Alice": "green"}) == "green"


def test_favoirte_color_tie():
    """Test handling a tie"""
    assert (
        favorite_color(
            {"Alice": "blue", "Bob": "red", "Charlie": "blue", "Dave": "red"}
        )
        == "blue"
    )


def test_bin_len_basic():
    """Test binning trings by length"""
    assert bin_len(["hi", "hello", "hey", "yo"]) == {
        2: {"hi", "yo"},
        5: {"hello"},
        3: {"hey"},
    }


def test_bin_len_edge():
    """Test binning an empty list"""
    assert bin_len([]) == {}


def test_bin_len_same():
    """Test binning where same length"""
    assert bin_len(["cat", "dog", "bat"]) == {3: {"cat", "dog", "bat"}}


if __name__ == "__main__":
    import pytest

    pytest.main()
