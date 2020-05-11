import requests
from bs4 import BeautifulSoup

#CLI

print("Enter a job")
job = input()

print("Select a location")
location = input()

############################

URL = "https://www.monster.com/jobs/search/?q="+job+"&where="+location
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_= 'card-content')

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    search_jobs = results.find_all('h2', string=lambda text: job in text.lower())
    if None in (title_elem, company_elem, location_elem):
        continue
    
    link = job_elem.find('a')['href']
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(f"Apply here: {link}\n")
    print()
