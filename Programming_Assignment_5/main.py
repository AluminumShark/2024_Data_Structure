import json
import time
import argparse

# --- TODO START --- #
# You can define any class or function
# You can import any python standard library : https://docs.python.org/3/library/
# However, you are not allowed to import any libraries other than python standard library, (such as numpy)
class MinHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def getSize(self):
        return self.size
    def insert(self, item):
        self.array.append(item)
        self.__swim(len(self.array) - 1)
        self.size += 1
    def peek(self):
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMin(self): 
        if self.size == 0:
            return None
        value = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.size -= 1
        if self.size > 0:
            self.__sink(0)
        return value
    def showMinHeap(self):
        return self.array
    def __swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]
    def __swim(self, i):
        while (i > 0) and (self.array[(i - 1) // 2] > self.array[i]):
            self.__swap(i, (i - 1) // 2)
            i = (i - 1) // 2
    def __sink(self, i):
        while i * 2 + 1 < len(self.array):
            left = i * 2 + 1
            right = i * 2 + 2
            smallest = i
            if left < len(self.array) and self.array[left] < self.array[smallest]:
                smallest = left
            if right < len(self.array) and self.array[right] < self.array[smallest]:
                smallest = right
            if smallest != i:
                self.__swap(i, smallest)
                i = smallest
            else:
                break
# --- TODO END --- #

def find_top_k_sums(array, k):
    n = len(array)
    prefix_sums = [0] * (n + 1)
    
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + array[i]
    
    min_heap = MinHeap()
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            subarray_sum = prefix_sums[j] - prefix_sums[i]
            if min_heap.getSize() < k:
                min_heap.insert(subarray_sum)
            else:
                if subarray_sum > min_heap.peek():
                    min_heap.removeMin()
                    min_heap.insert(subarray_sum)
    
    result = []
    while min_heap.getSize() > 0:
        result.append(min_heap.removeMin())
    
    result.reverse() 
    return result

def solution(json_input):
    array = json_input['array']
    topk = json_input['topk']
    
    result = find_top_k_sums(array, topk)
    
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input_1.json')
    parser.add_argument('--output', default='output_1.json')
    args = parser.parse_args()
    json_input = json.load(open(args.input, "r"))
    t1 = time.time()
    json_output = solution(json_input)
    t2 = time.time()
    json.dump(json_output, open(args.output, "w"))
    print("runtime of %s : %s" % (args.input, t2 - t1))
