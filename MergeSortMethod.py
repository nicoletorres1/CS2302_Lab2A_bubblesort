def mergeSort(self):
    # temp = self.head
    if temp is None or temp.next is None:
        return temp
    linkedlist1, linkedlist2, divdeLists(temp)
    linkedlist1 = solution3(linkedlist1)
    linkedlist2 = solution3(linkedlist2)
    temp = mergeLists(linkedlist1, linkedlist2)
    return temp


def divideLists(self):
    temper = self.head
    slow = temper  # slow is a pointer to reach the mid of ll
    fast = temper  # fast is a pointer to read the end of ll

    if fast:
        fast = fast.next
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return temper, mid


def mergeLists(linkedlist1, linkedlist2):
    if linkedlist1 == None and linkedlist2 == None:
        return None
    if linkedlist1 == None:
        return linkedlist2
    if linkedlist2 == None:
        return linkedlist1
    if linkedlist1.id > linkedlist2.id
        tmp = linkedlist1
        linkedlist1 = linkedlist1.next
    else:
        tmp = linkedlist2
        linkedlist2 = linkedlist2.next
        self.head = tmp
    while linkedlist1 != None and linkedlist2 != None:
        if linkedlist1.data > linkedlist2.data:
            lastNode.next = linkedlist1
        linkedlist1 = linkedlist1.next
    else:
        lastNode.next = linkedlist2
        linkedlist2 = linkedlist2.next
        lastNode = lastNode.next
    if linkedlist1 != None:
        lastNode.next = linkedlist1
    elif linkedlist2 != None:
        lastNode.next = linkedlist2
    return tmp