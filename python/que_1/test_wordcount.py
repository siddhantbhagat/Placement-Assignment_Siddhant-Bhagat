from wordcount import wordcount


# used Pytest for testing

def test_wordcount():
    s=' write write write all the number from from from 1 to 100 '
    assert wordcount(s) == 5

'''Explanation - From the given string we can note that the most frequent words are “write” and “from” and
the maximum value of both the values is “write” and its corresponding length is 5'''

def test_wordcount1():
    s=' write write write all the number from from from 1 to 100 from '
    assert wordcount(s) == 4

'''Explanation - From the given string we can note that the most frequent words is “from” and its corresponding length is 4'''


def test_wordcount2():
    s=''
    assert wordcount(s) == 0
'''Explanation - There are no words in the string so the length of most frequent word is zero'''