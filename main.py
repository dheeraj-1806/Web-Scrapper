from bs4 import BeautifulSoup
import requests
import time

print("Skills that you are not familiar with:")
unfamiliar_skills = input('>>')
print(f"jobs that dont require {unfamiliar_skills} :")
print("")

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text
            skills = job.find('span', class_= 'srp-skills').text
            more_info = job.header.h2.a['href']

            if unfamiliar_skills not in skills:
                with open(f'post/{index}.txt', 'w') as f:
                    f.write(f"Company name: {company_name.strip()}\n")
                    f.write(f"Required skills: {skills.strip()}\n")
                    f.write(f"More info: {more_info}\n")

                print(f"File Saved Successfuly as: {index}.txt")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Updating after {time_wait} minutes....")
        time.sleep(time_wait * 60)