import os

def is_anagram(input1, input2):
    """Check if two functions are anagrams of each other."""
    return sorted(input1.upper()) == sorted(input2.upper())

def lambda_handler(event, context):
    return is_anagram(event['input1'], event['input2'])
