"""
1.thinking about the objects
Song: title ,artist, duration
2. write its class




"""
class Song:
    def __init__(self,title,artist,duration):
        self.title = title #self.title is property of object, title in RHS is input to  __init__
        self.artist = artist
        self.duration = duration
        self.nextSong = None # nonmandotry attributes
        self.previousSong = None
    def showSong(self):
        print("{}\t{}\t{}".format(self.title,self.artist,self.duration))


# creating objects of Song class

song1 = Song("1.Muqabla","Yash","2:56")
song2 = Song("2Mubarakan","Neha Kakkar","2:56")
song3 = Song("3.EkToh","Yash","2:55")
song4 = Song("4.Nai Jeena","Yash","2:56")
song5 = Song("5.Gulabi 2.0","Ammal Malik","2:50")
#each having different hashcodes
print(">>song1:",song1)
print(">>song2:",song2)
print(">>song3:",song3)
print(">>song4:",song4)
print(">>song5:",song5)
# following is the implentation of Linked List Data Structure
#reference copy operation---> song1.method is referring to song 2
song1.nextSong = song2# memory representation---> song2 hashcode is copied to song1 .nextSong i.e song1 nextsong is pointing to song2
print("song1--hashcode",song1.nextSong) # prints the hashcode of
song2.nextSong = song3
print("song2--hashcode",song2.nextSong)
song3.nextSong = song4
song4.nextSong = song5
song5.nextSong = song1
# previous songs linking
song1.previousSong = song5
print("song1 previous song hascode is:",song1.previousSong) # hashcode in previousSong  should be of song5
song2.previousSong = song1
song3.previousSong = song2
song4.previousSong = song3
song5.previousSong = song4

song1.nextSong.showSong()
song1.previousSong.showSong()

# using while loop to loop thru the linked list of song

start = song1

while start.nextSong != song1: #i.e when song5 will point to song1 loop will stop
      print("----------------------")
      start.showSong() # shows showSong of song1 for instance
      start =  start.nextSong

song5.showSong()
print("-------previous song series-------")

end = song5
while end.previousSong != song5:
    print("-------------")
    end.showSong()
    end = end.previousSong

song1.showSong()
