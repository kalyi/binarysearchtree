# -*- coding: utf-8; -*-
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

class BinarySearchTree(object):
    """A simple demo implementation of a binary search tree."""
    
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 0 if data is None else 1

    def setData(self, data):
        if self.data is None:
            self.size = 1
        self.data = data

    def getData(self):
        return self.data

    def isEmpty(self):
        return self.data is None

    def hasChildren(self):
        return self.left is not None or self.right is not None

    def getSize(self):
        return self.size

    def isRoot(self):
        return self.parent is None

    def isLeftChild(self):
        return not self.isRoot() and self.parent.left is self
    
    def isRightChild(self):
        return not self.isRoot() and self.parent.right is self

    def _insertInSubTree(self,tree,value):
        if tree is None:
            return BinarySearchTree(value)
        else:
            tree.insert(value)
            return tree

    def insert(self, value):
        if self.isEmpty():
            self.data = value
        elif value < self.getData():
            self.left = self._insertInSubTree(self.left,value)
            self.left.parent = self
        else:
            self.right = self._insertInSubTree(self.right,value)
            self.right.parent = self
        self.size += 1

    def find(self, value):
        if self.data is value:
            return self
        elif value < self.data and self.left is not None:
            return self.left.find(value)
        elif value >= self.data and self.right is not None:
            return self.right.find(value)
        return None

    def contains(self, value):
        return self.find(value) is not None

    def clear(self):
        self.data = None
        self.left = None
        self.right = None
        self.parent = None
        self.size = 0

    def cut(self):
        if not self.isRoot():
            self.parent.size -= self.size
        if self.isLeftChild():
            self.parent.left = None
        elif self.isRightChild():
            self.parent.right = None
        self.clear()
            
    def removeSelf(self):
        if not self.hasChildren():
            self.cut()
        elif self.left is not None and self.right is None:
            if self.isLeftChild():
                self.parent.left = self.left
            else:
                self.parent.right = self.left
            self.left.parent = self.parent
            self.clear()
        elif self.left is None and self.right is not None:
            if self.isLeftChild():
                self.parent.left = self.right
            else:
                self.parent.right = self.right
            self.right.parent = self.parent
            self.clear()
        else:
            maxKeyLeft = self.left.findMax()
            self.data = maxKeyLeft.data
            maxKeyLeft.removeSelf()


    def remove(self, value):
        t = self.find(value)
        if t is not None:
            t.removeSelf()

    def findMin(self):
        if self.left is None:
            return self
        return self.left.findMin()

    def findMax(self):
        if self.right is None:
            return self
        return self.right.findMax()

    def __str__(self):
        if self.isEmpty():
            return "Tree is empty."
        nodeReps = []
        self._prettyPrint(0, "", "", nodeReps)
        return '\n'.join(nodeReps)

    def _prettyPrint(self, depth, ownprefix, childprefix, nodeReps):
        if not self.isEmpty():
            leader = "+- " if depth is not 0 else ""
            indent = " " * (depth - 1)*3  
            rep = "%s%s[%s] (%s, %s)" % (
                        ownprefix, leader, str(self.data), 
                        "parent: " + str(self.parent.data) 
                            if not self.isRoot() 
                            else "root", 
                        "left child" 
                            if self.isLeftChild() 
                            else "right child" 
                                if self.isRightChild() 
                                else "parentless")
            nodeReps.append(rep)

            if self.hasChildren():
                if self.left is not None:
                    self.left._prettyPrint(depth + 1, 
                        childprefix, childprefix + "|   ", nodeReps)
                else:
                    nodeReps.append(childprefix + "+- [*]")
                if self.right is not None:
                    self.right._prettyPrint(depth + 1, 
                        childprefix, childprefix + "    ", nodeReps)
                else:
                    nodeReps.append(childprefix + "+- [*]")
        return nodeReps
        
    def inOrder(self):
        dfs = []
        if not self.isEmpty():
            if self.left is not None:
                dfs += self.left.inOrder()
            dfs.append(self.data)
            if self.right is not None:
                dfs += self.right.inOrder()
        return dfs

