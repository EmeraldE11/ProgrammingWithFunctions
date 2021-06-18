from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    singular_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(20):
        word = get_noun(1)

        assert word in singular_nouns

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    for _ in range(20):
        word = get_noun(2)

        assert word in plural_nouns


def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(20):
        word = get_verb(1, "past")

        assert word in past_verbs

    singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(20):
        word = get_verb(1, "present")

        assert word in singular_verbs

    plural_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(20):
        word = get_verb(2, "present")

        assert word in plural_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(20):
        word = get_verb(1, "future")

        assert word in future_verbs

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.


def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for _ in range(100):
        word = get_preposition()
        assert word in prepositions


def test_get_prepositional_phrase():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    singular_determiners = ["the", "one"]
    plural_determiners = ["some", "many"]
    singular_nouns = ["adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    plural_nouns = ["adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    
    singular_phrase = get_prepositional_phrase(1)
    singular_list = singular_phrase.split()
    plural_phrase = get_prepositional_phrase(2)
    plural_list = plural_phrase.split()

    for _ in range(100):
        singular_preposition = singular_list[0]
        assert singular_preposition in prepositions

        plural_preposition = plural_list[0]
        assert plural_preposition in prepositions

        singular_determiner = singular_list[1]
        assert singular_determiner in singular_determiners

        plural_determiner = plural_list[1]
        assert plural_determiner in plural_determiners

        singular_noun = singular_list[2]
        assert singular_noun in singular_nouns

        plural_noun = plural_list[2]
        assert plural_noun in plural_nouns

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])