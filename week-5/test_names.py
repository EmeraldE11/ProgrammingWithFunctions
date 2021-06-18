from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Qui-Gon", "Jynn") == "Jynn; Qui-Gon"
    assert make_full_name("Luke", "Skywalker") == "Skywalker; Luke"
    assert make_full_name("Iris", "West-Allen") == "West-Allen; Iris"
    assert make_full_name("Napoleon", "Dynamite") == "Dynamite; Napoleon"

def test_extract_family_name():
    assert extract_family_name("Jynn; Qui-Gon") == "Jynn"
    assert extract_family_name("Skywalker; Luke") == "Skywalker"
    assert extract_family_name("West-Allen; Iris") == "West-Allen"
    assert extract_family_name("Dynamite; Napoleon") == "Dynamite"

def test_extract_given_name():
    assert extract_given_name("Jynn; Qui-Gon") == "Qui-Gon"
    assert extract_given_name("Skywalker; Luke") == "Luke"
    assert extract_given_name("West-Allen; Iris") == "Iris"
    assert extract_given_name("Dynamite; Napoleon") == "Napoleon"


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])