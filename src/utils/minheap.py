from operator import truediv


class MinHeap:
    # Data structure for sorting by size for either tiles or units

    #Important:
    #root element at index 0


    #for any ith node in array
    #parent node index = [(i-1)/2]
    #left child node = [(2*i) + 1]
    #right child node = [(2*i) + 2]

    def __init__(self, setting):
        self.min_heap = []
        self.setting = setting

    def sort_pushed(self,index):
        if self.setting == "tile":
            #move the node at the given index upwards until heap is valid
            parent_index = (index - 1) // 2
            while index > 0 and self.min_heap[index].f_value < self.min_heap[parent_index].f_value:
                #swap nodes / tiles
                self.min_heap[index], self.min_heap[parent_index] = self.min_heap[parent_index], self.min_heap[index]
                index = parent_index
                parent_index = (index - 1) // 2
        else:
            parent_index = (index - 1) // 2
            while index > 0 and self.min_heap[index] < self.min_heap[parent_index]:
                self.min_heap[index], self.min_heap[parent_index] = self.min_heap[parent_index], self.min_heap[index]
                index = parent_index
                parent_index = (index - 1) // 2


    def sort_popped(self, index):
        if self.setting == "tile":
            #move node at index downwards to maintain heap validity
            smallest = index
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            #if left child exists and is smaller than current smallest
            if left_child_index < len(self.min_heap) and self.min_heap[left_child_index].f_value < self.min_heap[smallest].f_value:
                smallest = left_child_index
            if right_child_index < len(self.min_heap) and self.min_heap[right_child_index].f_value< self.min_heap[smallest].f_value:
                smallest = right_child_index
            if smallest != index:
                #swap
                self.min_heap[index], self.min_heap[smallest] = self.min_heap[smallest], self.min_heap[index]
                self.sort_popped(smallest)
        else:
            smallest = index
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            if left_child_index < len(self.min_heap) and self.min_heap[left_child_index] < self.min_heap[
                smallest]:
                smallest = left_child_index
            if right_child_index < len(self.min_heap) and self.min_heap[right_child_index] < self.min_heap[
                smallest]:
                smallest = right_child_index
            if smallest != index:
                self.min_heap[index], self.min_heap[smallest] = self.min_heap[smallest], self.min_heap[index]
                self.sort_popped(smallest)
        #continue recursively until heap is valid

    def push(self, node):
        # add node to min_heap then sort accordingly
        self.min_heap.append(node)
        self.sort_pushed(len(self.min_heap) - 1)
    def pop(self):
        #return and remove node with lowest F-cost
        if len(self.min_heap) == 1:
            return self.min_heap.pop()
        root = self.min_heap[0]
        self.min_heap[0] = self.min_heap.pop()
        self.sort_popped(0)
        return root
    def size(self):
        return len(self.min_heap)
    def is_empty(self):
        if len(self.min_heap) == 0:
            return True
        else:
            return False
