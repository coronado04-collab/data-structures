from slistH import SList
from slistH import SNode

import sys

class SList2(SList):
    
    def delLargestSeq(self): 
        # check if the list is empty
        if self.isEmpty():
            raise ValueError("List is empty")

        node = self._head
        count = 1
        max_count = 0
        start_pos = 0
        position = 0
        while node.next:
            if node.elem == node.next.elem:
                count += 1
            else:
                count = 1
            position += 1
            # new largest sequence of max_count elements, starting at start_pos
            if count >= max_count:
                max_count = count
                start_pos = position - max_count
            node = node.next

        # Remove the sequence
        if start_pos == 0:
            # first node
            node = self._head
            for _ in range(max_count):
                node = node.next
            self._head = node
        elif start_pos + max_count == self._size:
            # whole list
            node = self._head
            for _ in range(self._size - max_count):
                node = node.next
            node.next = None
        else:
            node1 = self._head
            for _ in range(start_pos):
                node1 = node1.next
            node2 = node1
            for _ in range(max_count):
                node2 = node2.next
            node1.next = node2

    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next        
        current.next = start_node

    def fix_loop(self):
        """is to detect if the calling list contains a loop and, if so, to break it"""
        # cases where we can't have a loop
        if self._head == None or self._head.next == None:
            return

        slowPointer = fastPointer = self._head
        while slowPointer and fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
            # if the pointers coincide it's because there's a loop
            if slowPointer == fastPointer:
                # find the loop
                slowPointer = self._head
                while slowPointer != fastPointer:
                    slowPointer = slowPointer.next
                    fastPointer = fastPointer.next

                # fatsPointer.next is where the loop starts
                fastPointer.next = None








    def leftrightShift(self,left,n):
        """This method left shifts (left =True) or right shifts (left =False) the single linked list by n nodes when n is
        smaller than or equal to the length of the linked list."""
        if self.isEmpty() or n not in range(0, len(self)):
            return self

        if left:
            while n>0:
                first = self._head
                e = first.elem
                # create and establish the original first node as the last
                self.addLast(e)
                # remove the original first node
                self.removeFirst()

                n -= 1

        else:
            while n>0:
                last = self._head
                prev = None
                # reach the last node to store the element
                while last.next:
                    prev = last
                    last = last.next

                # establish last as the new first node
                e = last.elem
                self.addFirst(e)
                # delete the last node
                prev.next = None

                n -= 1



























l = SList2()
l.addLast(1)
l.addLast(2)
l.addLast(3)
l.addLast(4)
l.addLast(5)
l.addLast(6)
l.addLast(7)
print(l)
l.leftrightShift(False, 2)
print(l)
l.leftrightShift(True, 2)
print(l)
print("In case of performing a shift of n=0: ", l.leftrightShift(True, 0))

l2 = SList2()
print("list:", str(l2))
print("len:", len(l2))

for i in range(7):
    l2.addLast(i + 1)



print(l2)
print()

# No loop yet, no changes applied
l2.fix_loop()
print("No loop yet, no changes applied")
print(l2)
print()

# We force a loop
l2.create_loop(position=3)
l2.fix_loop()
print("Loop fixed, changes applied")
print(l2)
print()
print()