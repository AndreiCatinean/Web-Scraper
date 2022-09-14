#Importing libraries
import requests
import bs4

#Setting up
url='http://quotes.toscrape.com/page/{}/'
page=1
last_page=False
authors=[]

#Navigating through the pages and appending the author names to a list
#The loop is stopping when there is no 'next' button on the page

while not last_page:
    res=requests.get(url.format(page))
    soup=bs4.BeautifulSoup(res.text,'lxml')
    aux=soup.select('.author')
    for author in aux:
        nume=author.text
        authors.append(nume)
    if len(soup.select('.next'))==0:
        last_page=True
    else:
        page+=1

#Converting the list which could have duplicates to a set(a list of unique elements)
authors=set(authors)
