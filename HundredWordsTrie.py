#!/usr/bin/python

'''
I want to create a trie structure of the 100 most commonly used words,
and create a GraphViz diagram of it.

Usage:
$ python HundredWordsTrie.py > HundredWordsTrie.dot
$ dot -Tpng HundredWordsTrie.dot
'''

HundredWords = [ "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
                 "it", "for", "not", "on", "with", "he", "as", "you", "do",
                 "at", "this", "but", "his", "by", "from", "they", "we", "say",
                 "her", "she", "or", "an", "will", "my", "one", "all", "would",
                 "there", "their", "what", "so", "up", "out", "if", "about",
                 "who", "get", "which", "go", "me", "when", "make", "can",
                 "like", "time", "no", "just", "him", "know", "take", "people",
                 "into", "year", "your", "good", "some", "could", "them", "see",
                 "other", "than", "then", "now", "look", "only", "come", "its",
                 "over", "think", "also", "back", "after", "use", "two", "how",
                 "our", "work", "first", "well", "way", "even", "new", "want",
                 "because", "any", "these", "give", "day", "most", "us"
                 ]

class Node(object):
    # Using a class attribute variable to give each node a unique
    # identifier. GraphViz defaults to using the node label as the
    # node Id, but here letters will be repeated, so a unique node Id
    # is required.
    count = 0
    
    def __init__(self, letter='', final=False):
        self.letter = letter
        self.final = final
        self.children = {}
        self.number = self.__class__.count
        self.__class__.count += 1
    def add(self, letters):
        node = self
        for index, letter in enumerate(letters):
            if letter not in node.children:
                node.children[letter] = Node(letter, index==len(letters)-1)
            node = node.children[letter]
    def print_nodes(self):
        periph = ''
        if self.final:
            periph = ',peripheries=2'
        if self.letter:
            print '	N%03d [label="%c"%s];' % (self.number, self.letter, periph)
        else:
            print '	N%03d [label="ROOT"];' % self.number
        for letter in self.children:
            node = self.children[letter]
            node.print_nodes()
    def print_links(self):
        for letter in self.children:
            node = self.children[letter]
            print '	N%03d -> N%03d;' % (self.number, node.number)
            node.print_links()
            
def load_words():
    result = Node()
    for word in HundredWords:
        result.add(word)
    return result

HundredWords.sort()
root = load_words()
print "digraph G {"
print '	rankdir="LR";'
root.print_nodes()
root.print_links()
print "}"
