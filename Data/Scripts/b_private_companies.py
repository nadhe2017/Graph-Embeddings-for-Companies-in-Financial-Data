# This script retrieves names of private companies worldwide from the bloomberg website
# There are 10,347 pages with a number of companies listed on each page
# Recommended that pages be split up and run across different machines


from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

first_page = 1
last_page = 10348 # Pages belong to [1,10348)

url = 'https://www.bloomberg.com/bcom/sitemaps/private-companies-index.xml'
content = urlopen(url)
soup = BeautifulSoup(content,"lxml")

alltags = soup.find_all('loc')

curr = first_page
flag = 1

def extract_names(url):
    #print('Going to sleep for 5 seconds')  
    time.sleep(5)
    with open('bloomberg_private_'+str(first_page)+'to'+str(last_page)+'.txt','a',encoding='utf-8')as g:
        page_content = urlopen(url)
        page_soup = BeautifulSoup(page_content,"lxml")
        nametags = page_soup.find_all('loc')
        for tag in nametags:
            company_url = tag.text
            text = company_url[company_url.index(':')+1:]
            text = text[text.index(':')+1:].split('-')
            country = text[0]
            name = ''
            for i in range(1,len(text)):
                name += text[i].capitalize()+' '
            name = name.strip()
            #print (country,name)
            g.write(name+'|'+country+'\n')
    #print('page has been processed')


while (flag):
    try:
        while curr<last_page:    
            page_url = alltags[curr].text
            print ('Processing page ',str(curr+1),'/'+str(last_page))    
            extract_names(page_url)
            curr += 1
        if curr == last_page:
            flag = 0
            print ('All pages have been scraped')
    except:
    	
        #print(page_url) 
        #print('Going to sleep for 10 seconds')      
        time.sleep(10)

exit()
