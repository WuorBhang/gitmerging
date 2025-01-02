#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for determining whether the present of a str in in the given word:.

Module contents:
    - the present of a str in in the given word:

Created on XX XX XX

@author: WUOR BHANG GATWECH

Challenge is from the Codewars website.

Defining the present of a str in in the given word:

"""

def char_present_in_word(char, word):
    """
    Check if a character is present in a given word.

    Parameters:
    char (str): The character to check.
    word (str): The word to check in.

    Returns:
    boolean: True or False
    
    Example:
    >>> char_present_in_word("a", "word")
    False
    >>> char_present_in_word("w", "word")
    True
    """
    return char in word
