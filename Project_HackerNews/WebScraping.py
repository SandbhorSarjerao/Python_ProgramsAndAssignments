import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
# print(response)
# print(response.text)
# print(response.headers)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find('Python'))

links = soup.select('.storylink')
votes = soup.select('.score')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hacker_news(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hacker_news(links, votes))
