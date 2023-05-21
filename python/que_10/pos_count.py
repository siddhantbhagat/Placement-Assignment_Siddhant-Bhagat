import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

# you might have to download averaged_perceptron_tagger punkt using nltk.download() function

def count_pos_tags(text):
    # Tokenize the text into words as pos_tag takes list of words
    words = word_tokenize(text)

    # Perform part-of-speech tagging where each word is categoried into parts of speech
    tagged_words = pos_tag(words)

    counts = {
        'verb': 0,
        'noun': 0,
        'pronoun': 0,
        'adjective': 0
    }

    # Count the number of verbs, nouns, pronouns, and adjectives
    for word, tag in tagged_words:
        if tag.startswith('VB'):
            counts['verb'] += 1
        elif tag.startswith('NN'):
            counts['noun'] += 1
        elif tag.startswith('PRP'):
            counts['pronoun'] += 1
        elif tag.startswith('JJ'):
            counts['adjective'] += 1

    return counts