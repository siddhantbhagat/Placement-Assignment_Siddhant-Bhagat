from checkvalidity import check_validity

# used Pytest for testing

def test_check_validity1():
    s='abc'
    assert check_validity(s) == 'Yes'

'''Explanation - as all characters of the string appear the same number of times the string is valid'''

def test_check_validity2():
    s='abcc'
    assert check_validity(s) == 'NO'

'''Explanation - As all characters of the string does not appear the same number of times and removing the last character
changes the values in the dictionary it is not valid'''


def test_check_validity3():
    s='aabbccd'
    assert check_validity(s) == 'Yes'
'''Explanation - as all characters of the string appear the same number of times after removing the last character 
this is valid string'''

def test_check_validity4():
    s=''
    assert check_validity(s) == 'Please enter a valid string'
'''Explanation - empty string could have caused problem'''