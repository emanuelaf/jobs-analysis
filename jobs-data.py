import requests
from bs4 import BeautifulSoup

#print(soup.prettify())
#type(soup.get_text())
#soup.find_all('h3')
#soup.find_all('p')

urls = ['https://www.amazon.jobs/en/jobs/1119430/applied-scientist-machine-learning',
'https://www.amazon.jobs/en/jobs/1119253/applied-scientist',
'https://www.amazon.jobs/en/jobs/1119252/applied-scientist',
'https://www.amazon.jobs/en/jobs/1117843/applied-scientist',
'https://www.amazon.jobs/en/jobs/1117288/applied-scientist',
'https://www.amazon.jobs/en/jobs/1115886/research-scientist-amazon-devices',
'https://www.amazon.jobs/en/jobs/1114449/data-scientist',
'https://www.amazon.jobs/en/jobs/1113491/data-scientist',
'https://www.amazon.jobs/en/jobs/1113186/senior-applied-scientist-machine-learning',
'https://www.amazon.jobs/en/jobs/1112070/senior-applied-scientist',
'https://www.amazon.jobs/en/jobs/1112066/sr-research-scientist',
'https://www.amazon.jobs/en/jobs/1112069/applied-scientist-manager',
'https://www.amazon.jobs/en/jobs/1111457/data-scientist-ii',
'https://www.amazon.jobs/en/jobs/1111340/sr-applied-scientist',
'https://www.amazon.jobs/en/jobs/1110720/applied-scientist',
'https://www.amazon.jobs/en/jobs/1109846/sr-applied-scientist',
'https://www.amazon.jobs/en/jobs/1108713/data-scientist-ww-ops-analytics',
'https://www.amazon.jobs/en/jobs/1108117/data-scientist-community-trust',
'https://www.amazon.jobs/en/jobs/1108105/sr-applied-scientist',
'https://www.amazon.jobs/en/jobs/1120400/senior-research-scientist-alexa',
'https://www.amazon.jobs/en/jobs/1120442/data-scientist-alexa',
'https://www.amazon.jobs/en/jobs/1120443/applied-scientist-alexa-nlu']

len(urls)
jobs = {}
d = {'Job Name': ''}
text = {}

for url in urls:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    d['Job Name'] = soup.title.get_text().split('- Job ID:')[0]
    jobs[soup.title.get_text().split('Job ID:')[1].split('|')[0].strip()]= d.copy()
    sections = soup.find_all('div',attrs={'class':'section'})
    for i in sections:
        if len(i.find_all('h3')) > 0:
            text[i.find_all('h3')[0].get_text()] = i.find_all('p')[0].get_text()
    jobs[soup.title.get_text().split('Job ID:')[1].split('|')[0].strip()].update(text.copy())

jobs

