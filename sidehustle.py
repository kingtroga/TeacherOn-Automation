import os
import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get('https://www.teacheron.com/online-python-tutor-jobs')
response.raise_for_status()


switch = True

job_titles = []
job_descriptions = []
job_links = []
for i in range(1, 4):
    if i == 1:
        response = requests.get(
            'https://www.teacheron.com/online-python-tutor-jobs')
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, features="lxml")
        span_tags = soup.select('a > span')
        
        switch = True
        
        if switch:
            span_tags = span_tags[1:]
            switch = False
            
        for j in span_tags:
            title = j.text
            title = title.replace('\r','')
            title = title.replace('\n','')
            title = title.strip()
            job_titles.append(title)

        p_tags = soup.find_all("p",{"class": "job-description"})

        
        for k in p_tags:
            description = k.text
            description = description.replace('\r', '')
            description = description.replace('\n', '')
            description = description.strip()
            job_descriptions.append(description)

        a_tags = soup.select('h3 > a')
        for m in a_tags:
            job_links.append(f"{m['href']}")

    else:
        response = requests.get(
            'https://www.teacheron.com/online-python-tutor-jobs?p=' + f'{i}'
        )
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, features="lxml")
        span_tags = soup.select('a > span')
        
        switch = True
        
        if switch:
            span_tags = span_tags[1:]
            switch = False
            
        for j in span_tags:
            title = j.text
            title = title.replace('\r','')
            title = title.replace('\n','')
            title = title.strip()
            job_titles.append(title)
            
        p_tags = soup.find_all("p",{"class": "job-description"})

        
        for k in p_tags:
            description = k.text
            description = description.replace('\r', '')
            description = description.replace('\n', '')
            description = description.strip()
            job_descriptions.append(description)

        a_tags = soup.select('h3 > a')
        for m in a_tags:
            job_links.append(f"{m['href']}")
        
        


data = {
    'job_titles': job_titles,
    'job_descriptions': job_descriptions,
    'job_links': job_links,
}

df_sidehustle = pd.DataFrame(data)



df_sidehustle.to_csv("sidehustle.csv", index=None, mode='w')
