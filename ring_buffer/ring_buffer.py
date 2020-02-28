from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current is self.storage.tail or self.current is None:
                self.current = self.storage.head
            else:
                self.current = self.current.next

            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        cur_node = self.storage.head
        while cur_node:
            list_buffer_contents.append(cur_node.value)
            cur_node = cur_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.cur_item_idx = 0
        self.storage = [None] * capacity

    def append(self, item):
        if None in self.storage:
            self.storage[self.storage.index(None)] = item
        else:
            self.storage[self.cur_item_idx] = item
            if self.cur_item_idx == len(self.storage) - 1:
                self.cur_item_idx = 0
            else:
                self.cur_item_idx += 1

    def get(self):
        return self.storage[0:self.storage.index(None)] if None in self.storage else self.storage
