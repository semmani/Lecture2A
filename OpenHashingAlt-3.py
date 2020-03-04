class HashTable:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = []  # Assignment : Replace with Your LinkedList Implementation
        for i in range(capacity):
            self.table.append([])  # we can append empty list in place of appending None(means same tho)

    def hashCode(self, data):
        idx = id(data) % self.capacity    # we create a hashcode of data --> id(data) and then create an hashcode again
        return idx

    def put(self, data):
        idx = self.hashCode(data)
        self.table[idx].append(data)  # to append data in the list
        print("Data {} Inserted at {}".format(data, idx))
        self.size += 1

    def find(self,data):




    def delete(self):
         pass




    def iterate(self):
        for i in range(self.capacity):
            if len(self.table[i]) != 0:
                print("Data In Bucket is ",i)

                for data in self.table[i]:
                    print(data)



htable2 = HashTable()

htable2.put(20)
htable2.put(12)
htable2.put(13)
htable2.put(14)
htable2.put(19)
htable2.put(24)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")

htable2.iterate()

