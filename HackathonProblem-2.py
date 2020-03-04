import hashlib
"""
class CountReview:
    def __init__(self, review):
        self.review = review
        self.frequency = 0
        self.capacity = len(review)
        self.table = []
        self.words = self.review.split(" ")
        for i in range(self.capacity):
            self.table.append(self.words)

    def hashCode(self):
        for word in self.words:
            idx = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16)%self.capacity
            return idx

    def hashCode2(self):
        self.string = "institution"
        sizeofString = len(self.string)
        idx2 = int(hashlib.sha256(self.string.encode("utf-8")).hexdigest(), 16)%sizeofString
        print(idx2)

    def comparison(self):
        idx = self.hashCode()
        idx2 = self.hashCode2()
        for i in range(idx):
            if self.table[idx] == self.string:
                self.frequency += 1
                print(" Word {} found {} times ".format(idx, self.frequency))

        print(" Word  not found")
    def print(self):
        print("{},{}".format(self.review,self.length))
"""


class reviewCounting:
    size = 0
    def __init__(self,review):
        self.review = review
        self.capacity = len(self.review)
        # print("Length of review = ",self.capacity)  # 155
        self.table = []
        self.words = self.review.split(" ")  # we split the review into the words
        for i in range(self.capacity):
             self.table.append(None)
#hashlib.sha256(word.encode("utf-8")).hexdigest(), 16) --> this code is used to create a hexadecimal hashcode
    def hashCode(self):
        for word in self.words:
             idx = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16) % self.capacity
             #print("Index {} of word '{}' ".format(idx,word))
             print(idx)

    def hashCode2(self,word="institution"):
        idx = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16) % self.capacity
        print("index2: ",idx)

    def frequencyOfWords(self,word):
        idx = hashCode()






review1=reviewCounting("Really good institution, teachers are very helpful and caring,"
                      " Also the environment of this college is very attractive, proud to be a part of this company.")
review1.hashCode()
review1.hashCode2()