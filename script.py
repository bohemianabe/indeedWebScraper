# requirements - pip3 install beautifulsoup4 / requests / mysql-connector-python

import requests
from bs4 import BeautifulSoup
import mysql.connector


# setup up to call the page and make the soup!
number = 0
URL = 'https://www.indeed.com/jobs?q=junior+web+developer&l=maryland&start=' + str(number)
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# create a results var to find the div we want for the job search. use a while loop to gen multipule pages
while number < 30:
    results = soup.find_all('div', attrs={'data-tn-component':'organicJob'}) 
    # create a for loop to go through each organicJob div
    for job_data in results:
        company = job_data.find('span', attrs={"class":"company"})
        # strip the company text
        company_final = company.text.strip()
        job = job_data.find('a', attrs={"data-tn-element":"jobTitle"})
        job_final = job.text.strip()

        print('company:' + company_final)
        print('job title: ' + job_final)
    number += 10