# Implementation using SortedSet 

class NumberContainers:

    def __init__(self):
        self.containers = defaultdict(SortedSet)
        self.index_to_num = {}

    def change(self, index: int, number: int) -> None:

        if index in self.index_to_num:
            old_mapping = self.index_to_num[index]
            self.containers[old_mapping].remove(index)

            if not self.containers[old_mapping]:
                del self.containers[old_mapping]
        
        self.index_to_num[index] = number
        self.containers[number].add(index)


    def find(self, number: int) -> int:
        if number not in self.containers or not self.containers[number]:
            return -1
        else:
            return self.containers[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)