from words import prefix, suffix
import pytest

def test_prefix():
    assert "" == prefix("", "")
    assert "" == prefix("", "correct")
    assert "" == prefix("clear", "")
    assert "" == prefix("happy", "funny")
    assert "cat" == prefix("cat", "catalog")
    assert "dog" == prefix("dogmatic", "dog")
    assert "j" == prefix("jump", "joyous")
    assert "un" == prefix("unwise", "ungrateful")
    assert "dis" == prefix("Disable", "dIstasteful")

def test_suffix():
    assert "" == suffix("", "")
    assert "" == suffix("", "correct")
    assert "" == suffix("clear", "")
    assert "" == suffix("angelic", "awesome")
    assert "found" == suffix("found", "profound")
    assert "itch" == suffix("ditch", "itch")
    assert "y" == suffix("happy", "funny")
    assert "ed" == suffix("tired", "fatigued")
    assert "ing" == suffix("swimming", "FLYING")

pytest.main(["-v", "--tb=line", "-rN", "test_words.py"])