#By creating object of Hashtables

class HashTable:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = []  # Assignment : Replace with Your LinkedList Implementation
        for i in range(capacity):
            self.table.append(None)

    def hashCode(self, data):
        idx = id(data) % self.capacity    #we create a hashcode of data --> id(data) and then create an hashcode again
        return idx

    def put(self, data):

        idx = self.hashCode(data)

        if self.table[idx] == None:
            self.size += 1
        else:
            print(">> COLLISION DETECTED FOR", data)

        self.table[idx] = data
        print(">> Data {} Inserted at Index {}".format(data, idx))

    def find(self, data):
        idx = self.hashCode(data)
        if self.table[idx] == data:
            return idx
        else:
            return -1

    def delete(self, data):
        idx = self.hashCode(data)
        if self.table[idx] == data:
            self.table[idx] = None
            self.size -= 1
            print("Data Deleted", data)
        else:
            print("Data Not Found", data)

    def iterate(self):
        for data in self.table:
            if data != None:
                print(data)

def main():

    htable = HashTable(13)

    htable.put(21)
    htable.put(10)
    htable.put(3)
    htable.put(10)
    htable.put(41)
    htable.put(20)
    # htable.put(111)
    # htable.put(87)
    # htable.put(66)
    # htable.put(210)
    # htable.put(40)
    # htable.put(1)

    print("====================")

    htable.iterate()

    print("====================")
    print(htable.size)

if __name__ == '__main__':
    main()
