#testing sorting algorithm
import random
from src.utils.minheap import MinHeap

class Node:
    def __init__(self,f_value):
        self.name = ""
        self.f_value = f_value
    def set_name(self):
        self.name = f"Node[{self.f_value}]"


sorted_nodes = MinHeap("tile")

while len(sorted_nodes.min_heap) != 10:
    random_f = random.randint(1,15)
    new_node = Node(random_f)
    new_node.set_name()
    sorted_nodes.push(new_node)


while not len(sorted_nodes.min_heap) == 0:
    node = sorted_nodes.pop()
    print(node.name)

    #this proves that when adding items to the minheap, the items are sorted upon being added.
    #when popping, minheap maintains validity.