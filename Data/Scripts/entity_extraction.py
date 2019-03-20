import os
import urllib2
from bs4 import BeautifulSoup
import re
import glob
import time
import csv

if __name__ == "__main__":
    # with open("2018-company_name.txt","r") as f:
    #     data = f.read().splitlines()

    private = []
    with open('private_companies_database.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # row = row[0].split("|")[0]
            if len(row) > 1:
                row = reduce(lambda x,y: x+y,row)
            else:
                row = row[0]
            private.append(row)
    private.pop(0)
    # Only use US
    us = filter(lambda x:x.split("|")[-1]=="US",private)
    us = map(lambda x:x.split("|")[0],us)
    us = set(us)

    public = []
    with open('public_companies_database.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # row = row[0].split("|")[0]
            if len(row) > 1:
                row = reduce(lambda x,y: x+y,row)
            else:
                row = row[0]
            public.append(row.split("|")[1])
    public = set(public)

    data = us | public
    
    # data = set(data)
    print "Num of names:",len(data)

    # # all_names = set([])
    # cnt = 0
    # cnt_8k = 0
    # # There are total 1625 8-K fillings contains Item 2.01 from 2017
    # for start in range(1,1601,100):
    #     url = 'https://searchwww.sec.gov/EDGARFSClient/jsp/EDGAR_MainAccess.jsp?search_text=%22Item+2.01%22&sort=Date&startDoc=' + str(start) + '&numResults=100&isAdv=true&formType=Form8K&fromDate=01/01/2017&toDate=12/31/2017&stemming=true'
    #     content = urllib2.urlopen(url).read()
    #     soup = BeautifulSoup(content, "lxml")
        
    #     for link in soup.find_all(id='viewFiling'):    
    #         if link.string[:3] == '8-K':            # Ensures that only 8-K filings, and no attachments are downloaded.
    #             #print link.string
    #             pos_arr = []                        # To find the position of the url and the company name
    #             a = (link.get('href'))
    #             for i in range(len(a)):
    #                 if a[i] == "'":
    #                     pos_arr.append(i)
    #             url = a[pos_arr[0]+1:pos_arr[1]]
    #             company_name = a[pos_arr[2]+1:pos_arr[3]]
    #             # all_names.add(company_name)
    #             cnt_8k += 1
    #             cnt += 1 if company_name in data else 0
    #             print cnt_8k,company_name,"yes" if company_name in data else "no"
    
    # print "All CNT:",cnt_8k
    # print "CNT:",cnt
    # # By using the company names collected in 2018, 1146/1551 fillings in 2017 can be parsed (names has been collected)

    # special_chars = ".!@#$%^&*()[]{}|_+-=/"
    # # Make special charactors generalizable if we can.
    # def special_chars_handler(res):
    #     # res is a string
    #     l = [c for c in res]
    #     for i in range(len(l)):
    #         if l[i] in special_chars:
    #             l[i] = "("+"("+"\\"+l[i]+")?"+"| )"

    def remove_tail(name):
        group = name.split()
        i = -1
        while group[-1].upper().replace(",","").replace(".","") in ["INC","LLC","CORP","CO","LTD","CORPORATION"]:
            if len(group) <= 3:
                group[-1] = group[-1].replace(",","").replace(".","")
                break
            group.pop()
        res = " ".join(group)
        res = re.escape(res)
        # res = special_chars_handler(res)
        return r"\b" + res + r"\b" 

    data = filter(lambda x:len(x.split())>1,data)
    data = map(remove_tail,data)

    data_re = re.compile("|".join(data),re.IGNORECASE)

    start_time = time.time()
    companies = []
    # path = '../Item_2.01_filings_2018_html/Q1/'
    path = "../raw_8_K_filings"
    for file in glob.glob(os.path.join(path, '*.txt')):
        file_start = time.time()
        print file
        with open(file,"r") as f:
            content = f.read()
        matches = data_re.findall(content)
        matches = set(map(lambda x:x.upper(),matches))
        companies.append(matches)
        print "RE for this file takes:",time.time() - file_start
        print "Num of companies detected:\t",len(matches)
        print "Companies are:",matches
        print "\n"
    print "RE takes time:",time.time() - start_time

    companies = map(set,map(lambda x:map(lambda y:y.upper(),x),companies))
    # filename = "Companies_Q1.txt"
    filename = "Companies_raw_8k.txt"
    with open(filename, "w") as f:
        for item in companies:
            item = [i for i in item]
            f.write("%s\n" % item)
    print "More than 2 companies/All companies: {0}/{1}".format(len(filter(lambda x:len(x)>1,companies)),len(companies))