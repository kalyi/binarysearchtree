#!/usr/bin/env python
#
# Copyright (C) 2015 Kathrin Hanauer
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" A very simple testing script for the BinarySearchTree class. """

from BinarySearchTree import *

import itertools
import random

t = BinarySearchTree()
print t
print

n = random.randint(5, 15)

for _ in itertools.repeat(None, n):
    x = random.randint(1, 100)
    print "Adding %d..." % x
    t.insert(x)

print
print "Tree of size %d:" % t.getSize()
print t

print 
print "Inorder:"
print t.inOrder()

print
for i in range(10,100,10):
    if t.contains(i):
        print "Tree contains %d." % i
        print "Removing value %d." %i
        t.remove(i)
        print t
        print t.inOrder()

print

