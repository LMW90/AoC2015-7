# Advent of Code 2015 Day 1
from email.quoprimime import body_length
import re

# class GraphNode:
#     def __init__(self, gdict = None):
#         if gdict == None:
#             gdict = {}
#         self.gdict = gdict

rgx = re.compile(r'([a-z]+)$')
nodeList = []
filename = 'inputday-7.txt'
with open(filename) as file:
    for line in file:
        print(line, end='')
        m = rgx.search(line)
        if m is not None:
            print(m.group(1) + '\n')
            nodeList.append(m.group(1))

nodeList = sorted(nodeList)
print(nodeList)
print(len(nodeList))
# d = {'a': {'d'},
# 'b': {'c'},
# 'c': {'b', 'd', 'e'},
# 'd': {'a'},
# 'e': {}}
# test = GraphNode(d)
# print(test.gdict)



   
