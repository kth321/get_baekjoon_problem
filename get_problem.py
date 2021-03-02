from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.request import urlopen
import requests

page_url = 'https://www.acmicpc.net/problem/'
index = 1000
problem_boundary = 3000
problem_boundary += 1

with open('problem_list.txt', 'w', encoding='utf-8') as f:
    while index != problem_boundary:
        url = page_url + str(index)
        try:
            main_url = urlopen(url)
        except HTTPError:
            index += 1
            continue
        main_page = BeautifulSoup(main_url, 'html.parser')
        description = main_page.findAll('div', {'class', 'problem-text'})
        
        f.write("<문제 "+str(index)+">\n")
        f.write(description[0].get_text().strip())
        f.write("\n<입력값>\n")
        f.write(description[1].get_text().strip())
        f.write("\n<출력값>\n")
        f.write(description[2].get_text().strip())
        f.write('\n\n')
        index += 1