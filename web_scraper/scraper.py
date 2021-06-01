import requests
from bs4 import BeautifulSoup


URL ='https://en.wikipedia.org/wiki/History_of_Mexico'

page =requests.get(URL)
def get_citations_needed_report():
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find_all(title='Wikipedia:Citation needed')

    data=[]
    for  res in results :
        if not res in data :
            data.append(res.parent.parent.parent.text)
    return data

def get_citations_needed_count():
    soup = BeautifulSoup(page.content,'html.parser')
    results = soup.find_all(title='Wikipedia:Citation needed')
    return len(results)

get_citations_needed_count()
print (get_citations_needed_report())