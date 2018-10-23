
'''
Nicole Torres
CS2302: Lab 2A
Purpose: to practice linked list
Last modified: 10/18/18
'''

import copy


# Node class
class Node:
    def __init__(self, id, next=None):  # defaulted as None if none passed
        self.id = id
        self.next = next


# linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


# method that adds to end of the list keeping track of list size as added
    def add(self, node):
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

# utility method to print list
    def print(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.id, end=" -> ")
            tmp = tmp.next


# SOLUTION 1; Compares numbers in list
    def solution1(self):
        numDuplicates = 0
        numComparisons = 0
        tmp = self.head
        while tmp is not None:
            tmp2 = tmp.next
            while tmp2 is not None:
                numComparisons += 1
                if tmp.id == tmp2.id:
                    numDuplicates += 1
                tmp2 = tmp2.next
            tmp = tmp.next
        return {"comparisons": numComparisons, "duplicates": numDuplicates}


# SOLUTION 2: Bubble sort to sort through list
    def solution2(self):
        numComparisons = 0
        numDuplicates = 0
        tmpOuter = self.head

        # Just sorting the list first!
        for i in range(self.size-1,0,-1):
            tmp1 = tmpOuter
            for j in range(i):
                # print("i is ", i, "j is ", j)
                numComparisons += 1
                # print('t1 = ',tmp1.id, "t1.n = ",tmp1.next.id)
                if tmp1.id > tmp1.next.id:
                    tmp1Val = tmp1.id
                    tmp1.id = tmp1.next.id
                    tmp1.next.id = tmp1Val
                # print('t1 = ', tmp1.id, "t1.n = ", tmp1.next.id)
                # exit(0)
                tmp1 = tmp1.next
        self.print()
        # print()
        # Now we count duplicates
        tmp = self.head
        print(self.head.id)
        for i in range(self.size-1):
            numComparisons += 1
            if tmp.id == tmp.next.id:
                numDuplicates += 1
            tmp = tmp.next

        return {"comparisons": numComparisons, "duplicates":numDuplicates}

    # Solution 3: Use merge sort to sort list


    # Solution 4: A boolean array to compare doubles
    def solution4(self):
        numDuplicates = 0
        numComparisons = 0
        seenBefore = [False]*6001
        tmp = self.head
        while tmp is not None:
            numComparisons += 1
            if seenBefore[tmp.id] == True:
                numDuplicates += 1
            else:
                seenBefore[tmp.id] = True
            tmp = tmp.next

        return {"comparison": numComparisons, "duplicates": numDuplicates}


def main():

    # original list
    ll = LinkedList()

    # clone list ll to not mess up original linked list
    llcopy = copy.copy(ll)
    print(llcopy)
    print()

    # File 1
    f = open("activision.txt")
    for line in f:
        ll.add(Node(int(line)))  # add takes a node, node takes an int
    f.close()

    # File 2
    f = open("vivendi.txt")
    for line in f:
        ll.add(Node(int(line)))  # add takes a node, node takes an int
    f.close()

    # ORIGINAL LIST
    print('\n' + "this is the original linked list")
    ll.print()
    print()  # prints None

    print('\n' + "Solution 1 is: ")
    print(ll.solution1())

    # SOLUTION 2:  BUBBLE SORT
    print('\n' + "Solution 2 is sorted in Ascending order with Bubble Sort: ")
    print(ll.solution2())

    # SOLUTION 3:  MERGE SORT

    # SOLUTION 4:  BOOLEAN ARRAY
    print('\n' + "Solution 4 using a boolean array: ")
    print(ll.solution4())


main()
