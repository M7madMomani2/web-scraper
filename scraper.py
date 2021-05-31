import requests


URL ='https://en.wikipedia.org/wiki/History_of_Mexico'

page =requests.get(URL)
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content,'html.parser')
results = soup.find_all(title='Wikipedia:Citation needed')
def get_citations_needed_report(results):
    data=[]
    for  res in results :
        if not res in data :
            data.append(res.parent.parent.parent.text)
    return data

def get_citations_needed_count(arr):
    return len(arr)

get_citations_needed_count(results)
get_citations_needed_report(results)