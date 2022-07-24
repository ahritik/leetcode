"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""

def reverseWords(sentence):
    return " ".join([word[::-1] for word in sentence.split()])