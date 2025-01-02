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
    checking if letter char is present in word.
    
    parameter:
    
    char: any character 
    word: any word 
    
    return:
    
    boolean: True or False
    
    Example:
    >>> is_char_present("a", "word")
    False
    >>> is_char_present("w", "word")
    """
    return char in word
