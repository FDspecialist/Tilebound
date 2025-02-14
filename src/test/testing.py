#testing sorting algorithm
import random
from src.utils.minheap import MinHeap

class Node:
    def __init__(self,f_value):
        self.name = ""
        self.f_value = f_value
    def set_name(self):
        self.name = f"Node[{self.f_value}]"

unsorted_nodes = []

while len(unsorted_nodes) != 10:
    random_f = random.randint(1,15)
    new_node = Node(random_f)
    new_node.set_name()
    unsorted_nodes.append(new_node)

sorted_nodes = MinHeap()

for node in unsorted_nodes:
    sorted_nodes.push(node)

while not len(sorted_nodes.min_heap) == 0:
    node = sorted_nodes.pop()
    print(node.name)