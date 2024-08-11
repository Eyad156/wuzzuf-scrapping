import requests
from bs4 import BeautifulSoup
import sys
def main():
    job_search = 'fullstack'
    urls = [
        f'https://wuzzuf.net/search/jobs/?q={job_search}&a=hpb',
        f'https://wuzzuf.net/search/jobs/?a=hpb&q={job_search}&start=1',
        f'https://wuzzuf.net/search/jobs/?a=hpb&q=programming&start=2'
        f'https://wuzzuf.net/search/jobs/?a=hpb&q=programming&start=3'
    ]

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            doc = BeautifulSoup(response.text, 'html.parser')
            find_jobs = doc.find_all('div', {'class': 'css-pkv5jc'})
            find_jobs1 = doc.find_all('div', {'class': 'css-1gatmva e1v1l3u10'})
            find_jobs2 = doc.find_all('div', {'class': 'css-1gatmva e1v1l3u10'})
            for job in find_jobs + find_jobs1:
                print(job.text.strip(), '\n')
    
        else:
            print(f"Failed to retrieve the page: {url}. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
    input()
