from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if at capacity, replace current with item
        if self.storage.length == self.capacity:
            if self.current is None:
                # make the head the oldest since we're adding to tail
                self.current = self.storage.head
            # overwrite the value of current
            self.current.value = item
            # if a current exists, make it the next value because it would have been replaced
            if self.current.next:
                self.current = self.current.next
            else:
                # when we run out of next, head becomes the oldest again
                self.current = self.storage.head
        else:
            self.storage.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # don't return None values
        current_node = self.storage.head
        while current_node:
            if current_node.value is not None:
                list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = [None] * capacity

    def append(self, item):
        if self.current is None:
            self.current = 0

        self.storage[self.current] = item

        if self.current == self.capacity - 1:
            self.current = 0

        else:
            self.current += 1

    def get(self):
        return [item for item in self.storage if item is not None]
