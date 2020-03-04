# THIS SESSION IS BASICALLY AN INTRO TO BEAUTIFUL SOUP WHICH IS USED TO PARSE THE HTML AND XML DOCUMENTS IN PYTHON
import requests as rq
from bs4 import BeautifulSoup

url ="https://twitter.com/dna"
response = rq.get(url)

# we have extracted HTML response from the given url
#print(response.text)  # this brings the code in the not so arranged format

#we will perform HTML parsing here,by creating a reference to the BeautifulSoup
soup = BeautifulSoup(response.text,"html.parser")
#print(soup) # this command will print all the html code in a very HTML like format

#print(soup.prettify()) # function used to view html code only

# print("TITLE")
# print(soup.text.title()) # this command will print all the titles in the webpage shown followed by immenseful text data
#
# print("----CHILDREN-----")
# children = soup.children  # children is a tag in beautiful soup---> inbuilt
# for child in children:
   # print(child)

# print("-----------P TAGS----------------->>>")
# ptags = soup.find_all("p")  # this find_all will find all p-tags i.e para tags in the html script
# for tags in ptags:
#     print(tags) # prints all the para tags

print("---------------DIV TAGS------------------->>>")
#divTags = soup.find_all("div")  # simply finds all the tags in the HTML script and prints it
divTags = soup.find_all("div",class_= "js-tweet-text-container")  # to find the div tags in js-tweet-text-container class--->
for tags in divTags:
    print(tags) #this prints all the tags and data within it
    print(tags.text) # where as this works wonder that is it prints all the textual data in div tags--->


