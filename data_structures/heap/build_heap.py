# uses python 3


class heap:
    def __init__(self):
        self.queue = []
        self.current_size = 0
        self.maxsize = 1000

    def parent(self, i):
        return i/2

    def left(self, i):
        return 2*i

    def right(self, i):
        return 2*i+1

    def size(self):
        return len(self.queue)

    def insert(self, p):
        if(self.current_size == self.maxsize):
            return IndexError
        current_size = self.current_size+1
        self.shiftup(current_size)

    def extract_max(self):
        # swap the first and last, remove the last, then shiftdown

        result = self.queue[0]
        self.queue[0] = self.queue[self.current_size]
        self.shifdown(0)
        return result

    def change_priority(self, i, p):
        pass

    def remove(self, i):
        pass

    def get_max(self):
        return self.queue[0]

    def shiftup(self, i):
        while (i > 0 and self.queue[self.parent(i)] < self.queue[i]):
            parent = self.queue[self.parent(i)]
            self.queue[i/2] = self.queue[i]
            self.queue[i] = parent
            i = i/2

    def shiftdown(self, i):
        maxindex = i
        size = self.size()
        left = self.left(i)
        right = self.right(i)
        if(left < size and self.queue[maxindex] < self.queue[left]):
            maxindex = left
        if(right < size and self.queue[maxindex] < self.queue[right]):
            maxindex = right

        if(i != maxindex):

            temp = self.queue[i]
            self.queue[i] = self.queue[maxindex]
            self.queue[maxindex] = temp
            self.shiftdown(self, maxindex)


def make_heap(arr):
    heaper = heap()
    for i in range(len(arr)):
        heaper.insert(arr[i])
    return heaper


def heap_sort(arr):
    heaper = make_heap(arr)
    sort_arr = []
    for i in range(len(arr), 0):
        sort_arr[len(arr)-i] = heaper.extract_max()
    print(sort_arr)
