# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_trie.ipynb.

# %% auto 0
__all__ = ['TrieNode', 'Trie']

# %% ../nbs/01_trie.ipynb 3
class TrieNode:
    "Stores the hashtable of the letters and the if that node is an end of a word."
    def __init__(self) -> None:
        self.end = False
        self.letters = {}
#| export
class Trie:
    "Trie data structure. Can store multiple words in a graph linking each consecutive letters and make branches in them."
    def __init__(self) -> None:
        self.head = TrieNode()
    "Insert a word into the trie"
    def insert(self, 
                word: str) -> None: # word to store in the trie
        actual_iteration = self.head
        for letter in word:
            actual_iteration_letters = actual_iteration.letters
            if not letter in actual_iteration_letters:
                actual_iteration_letters[letter] = TrieNode()
            actual_iteration=actual_iteration_letters[letter]
        actual_iteration.end = True
    "Check if a word exist in the trie"
    def search(self, 
                word:str) -> bool: # check if the word is stored in the trie
        actual_iteration = self.head
        for letter in word:
            actual_iteration_letters = actual_iteration.letters
            if not letter in actual_iteration_letters:
                return False
            actual_iteration=actual_iteration_letters[letter]
        return actual_iteration.end
