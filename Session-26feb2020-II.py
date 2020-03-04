import requests as rq
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt

url = "https://www.imdb.com/india/top-rated-indian-movies"
response = rq.get(url)  #i can simply write the whole damn url at the place of url

soup = BeautifulSoup(response.text,"html.parser") # simply prints all of the HTML script
print(soup.prettify())

tags = soup.find_all("td", class_="titleColumn")

movies = []
years = []
count = 0
for tag in tags:
    movieTitle = tag.text.strip() #finds all the data of each movie title ----> then stores them in a movies[] list
    movies.append(movieTitle)
    count += 1
print("-------<<<<<--------movies------------->>>>>----------------")
for movie in movies:  # this loop prints the data appended in the movies list
    print(movie)# prints everything

count1 = 0
tags2 = soup.find_all("span", class_="secondaryInfo")
print("------------------------Years--------------------------------->>>>")
for tag in tags2:
    yearTitle = tag.text.strip()
    years.append(yearTitle)
    count1 += 1

for year in years:
    print(year)
print("total movies are:",count) # provides the total of movies and years we have in our list
print("total years are:",count1)


print("----------<<end>>----------------------")

plt.hist2d()
# plt.xlabel = "MOVIES"
# plt.ylabel = "YEARS"

plt.legend()
plt.show()