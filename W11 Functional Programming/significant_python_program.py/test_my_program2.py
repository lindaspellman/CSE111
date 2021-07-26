# Significant Program Final Project Spring 2021
# Linda Spellman

"""IMPORTANT: THIS FILE TESTS THE FUNCTIONS IN my_program2.py, WHICH ARE DERIVED FROM my_program.py"""

import pytest
import collections 
from my_program2 import main, print_counted_words, print_certain_words, list_keys

# tests the main function
def test_main():
    sample_list = ['Mango', 'Banana', 'Apple', 'Pear', 'Banana', 
    'Grapes', 'Strawberry', 'Apple', 'Pear', 'Mango', 'Banana', 
    'Kiwi', 'Apple', 'Mango', 'Strawberry']
    # assert that passing the argument "sample.txt" into main() outputs sample_list 
    assert main("sample.txt") == sample_list

# tests the print_counted_words function
def test_print_counted_words():
    sample_list = ['Mango', 'Banana', 'Apple', 'Pear', 'Banana', 
    'Grapes', 'Strawberry', 'Apple', 'Pear', 'Mango', 'Banana', 
    'Kiwi', 'Apple', 'Mango', 'Strawberry']
    occurrence_count = collections.Counter(sample_list)
    assert print_counted_words(occurrence_count) == occurrence_count

# tests the print_certain_words function
def test_print_certain_words():
    sample_list = ['Mango', 'Banana', 'Apple', 'Pear', 'Banana', 
    'Grapes', 'Strawberry', 'Apple', 'Pear', 'Mango', 'Banana', 
    'Kiwi', 'Apple', 'Mango', 'Strawberry']
    occurrence_count = collections.Counter(sample_list)
    assert print_certain_words("mango", occurrence_count) == 3
    assert print_certain_words("banana", occurrence_count) == 3
    assert print_certain_words("apple", occurrence_count) == 3
    assert print_certain_words("pear", occurrence_count) == 2
    assert print_certain_words("strawberry", occurrence_count) == 2
    assert print_certain_words("grapes", occurrence_count) == 1
    assert print_certain_words("kiwi", occurrence_count) == 1

# tests the list_keys function
def test_list_keys():
    sample_list2 = ["Mango", "Banana", "Apple", "Pear", "Grapes", "Strawberry", "Kiwi"]
    occurrence_count = collections.Counter(sample_list2)
    assert list_keys(occurrence_count) == sample_list2


pytest.main(["-v", "--tb=line", "-rN", "test_my_program2.py"])