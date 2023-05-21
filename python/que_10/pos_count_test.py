from pos_count import count_pos_tags

# used pytest for testing purposes

def test_pos_count1():
    s= 'My name is Mark'
    assert count_pos_tags(s) == {'verb': 1, 'noun': 2, 'pronoun': 1, 'adjective': 0}

# checking how it performs on empty strings
def test_pos_count2():
    s=''
    assert count_pos_tags(s) == {'verb': 0, 'noun': 0, 'pronoun': 0, 'adjective': 0}

# all verbs
def test_pos_count3():
    s='am is are be run playing'
    assert count_pos_tags(s) == {'verb': 6, 'noun': 0, 'pronoun': 0, 'adjective': 0}