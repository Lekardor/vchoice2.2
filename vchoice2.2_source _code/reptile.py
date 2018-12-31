import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import time
import datetime
from selenium import webdriver
import os
import random
from shutil import copyfile
import sys
from pyvirtualdisplay import Display


class Reptile:
    def __init__(self, sleeptime=2, starttime='2015', endtime='2018'):
        self.years = []
        if int(starttime) > int(endtime):
            starttime, endtime = endtime, starttime
        while (1):
            self.years.append(starttime)
            starttime = str(int(starttime) + 1)
            if int(starttime) > int(endtime):
                break
        self.years.reverse()
        self.sleeptime = sleeptime
        self.actorsex = {}
        self.iplist = [{'https': '180.106.112.62'}, {'https': '175.150.4.89'}, {'https': '121.58.13.125'},
                       {'https': '180.116.46.172'}, {'https': '182.39.31.143'},
                       {'https': '123.133.206.223'}, {'https': '123.97.57.73'}, {'https': '60.187.171.46'},
                       {'https': '175.165.209.45'}, {'https': '60.188.47.234'},
                       {'https': '117.89.181.100'}, {'https': '113.76.18.240'}, {'https': '223.199.200.66'},
                       {'https': '221.2.119.161'}, {'https': '123.158.3.253'},
                       {'https': '115.202.47.32'}, {'https': '27.204.105.149'}, {'https': '121.227.57.12'},
                       {'https': '123.134.109.90'}, {'https': '121.228.223.2'},
                       {'https': '60.187.48.171'}, {'https': '123.97.40.153'}, {'https': '117.86.37.122'},
                       {'https': '101.73.255.70'}, {'https': '49.64.57.116'},
                       {'https': '121.225.71.70'}, {'https': '60.187.39.1'}, {'https': '60.188.47.234'},
                       {'https': '121.27.210.102'}, {'https': '123.163.121.228'}]
        if os.path.exists("data") is False:
            os.makedirs("data")

    def get_html_text(self, url):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        }
        # proxies = {"http" : "118.190.94.224:9001" }
        res = requests.get(url, headers=header, proxies=random.choice(self.iplist))
        res.raise_for_status()
        res.encoding = "utf-8"
        return res.text


class MaoYanReptile(Reptile):
    def get_film_list(self, html):
        # html = self.get_html_text(url)
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        a = list(map(lambda x: [x['data-com'].split('/')[-1].strip("'"), x.find('p', class_="first-line").string] \
            if x.find('p', class_="second-line").string[0:4] in ['2018', '2017', '2016', '2015'] else None,
                     soup.find_all('ul', class_="row")[1:]))
        a = list(filter(None, a))
        time.sleep(self.sleeptime)
        return a

    def get_one_page(self, url, name):
        html = self.get_html_text('http://piaofang.maoyan.com/movie/' + url)
        soup = BeautifulSoup(html, 'html.parser')
        try:
            genre = soup.find('p', class_="info-category").get_text().strip("\n").strip(' ').split('\n')[0].split(',')
            Time = soup.find("span", string=re.compile(r"\d+-\d+")).string[0:7]
            year = Time[0:4]
            month = Time[5:7]
            if soup.find("span", class_="detail-unit").string == "亿":
                boxoffice = float(soup.find("span", class_="detail-num").string) * 100
            else:
                boxoffice = float(soup.find("span", class_="detail-num").string) / 100
            score = soup.find('span', class_='rating-num').string
            html = self.get_html_text('http://piaofang.maoyan.com/movie/' + url + '/celebritylist')
            soup = BeautifulSoup(html, 'html.parser')
            role = soup.find_all("dl", class_="panel-main category")[0:2]
            director = list(map(lambda x: x.find('p', class_="p-item-name ellipsis-1").string,
                                role[0].find_all("div", class_="p-desc")))
            actor = list(map(lambda x: x.find('p', class_="p-item-name ellipsis-1").string,
                             role[1].find_all("div", class_="p-desc")[0:5]))
            for x in role[1].find_all("div", class_="p-item")[0:5]:
                if x.find('p', class_="p-item-name ellipsis-1").string not in self.actorsex.keys():
                    self.actorsex[x.find('p', class_="p-item-name ellipsis-1").string] = [x.find('a', class_='p-link')[
                                                                                              'data-id'], 0]
                else:
                    self.actorsex[x.find('p', class_="p-item-name ellipsis-1").string][1] = \
                        self.actorsex[x.find('p', class_="p-item-name ellipsis-1").string][1] + 1
            # time.sleep(self.sleeptime)
            rel = [name, year, month, boxoffice, ','.join(director), ','.join(actor), ','.join(genre), score]
            return rel
        except:
            return ["a", "b", "c", 0, [], [], []]

    def save_file(self, filmList, year, path="data\\maoyan\\"):
        if os.path.exists("data\\maoyan") is False:
            os.makedirs("data\\maoyan")
        df = pd.DataFrame([x for x in filmList if x[1] == year],
                          columns=["name", "year", "month", "boxfile", "director", "actor", "genre", "score"])
        df.to_csv(path + "data_" + year + ".csv", encoding='gbk', index=0)
        if os.path.exists("data\\data_" + year + ".csv") is False:
            copyfile(path + "data_" + year + ".csv", "data\\data_" + year + ".csv")
        # copyfile(path + "data_" + year + ".csv", "data\\data_" + year + ".csv")
        print('finish save ' + year + ' film file')
        return list(x for x in filmList if x[1] != year)

    def get_year_list(self, url, exe_path):
        try:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')
            browser = webdriver.Chrome(
                executable_path=exe_path,chrome_options=option)
            browser.get(url)
            time.sleep(3)
            yearList = []
            for i in range(2,2+len(self.years)):
                browser.find_element_by_xpath('//*[@id="tab-year"]/ul/li[' + str(i) + ']').click()
                time.sleep(3)
                yearList.append(self.get_film_list(browser.page_source))
            browser.close()
            return yearList
        except:
            return self.get_year_list(url, exe_path)

    def save_actorsex(self, year, path="data\\maoyan\\"):
        #
        # print(self.actorsex)
        self.actorsex = dict(
            (x[0], x[1]) for x in sorted(self.actorsex.items(), key=lambda dic: dic[1][1], reverse=True)[0:50])
        i = 0
        for k, v in self.actorsex.items():
            time.sleep(self.sleeptime)
            html = self.get_html_text('http://piaofang.maoyan.com/celebrity?id=' + v[0])
            soup = BeautifulSoup(html, 'html.parser')
            # print(html)
            try:
                self.actorsex[k] = soup.find('span', string=re.compile('男|女')).string
            except:
                self.actorsex[k] = "unknown"
            print("finish " + year + ' ' + str(i) + "th actor")
            i = i + 1
        pd.DataFrame(list(self.actorsex.items()), columns=['姓名', '性别']).to_csv(path + "actors_sex" + year + ".csv",
                                                                               encoding='gbk',
                                                                               index=0)
        if os.path.exists("data\\actors_sex" + year + ".csv") is False:
            copyfile(path + "actors_sex" + year + ".csv", "data\\actors_sex" + year + ".csv")
        # copyfile(path + "actors_sex" + year + ".csv", "data\\actors_sex" + year + ".csv")
        print("finish save actors sex")

    def start(self, url="http://piaofang.maoyan.com/rankings/year",
              exe_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'):
        filmYearList = self.get_year_list(url, exe_path)
        # year = ["2018", "2017", "2016", "2015"]
        i = 0
        j = 0
        templist = []
        print(self.years)
        for films in filmYearList:
            filmList = []
            print(len(films))
            for x in films:
                time.sleep(self.sleeptime)
                filmList.append(self.get_one_page(x[0], x[1]))
                print("finish " + self.years[i] + ' ' + str(j) + "th film:" + x[1])
                j = j + 1
            for x in templist:
                if x not in filmList:
                    filmList.append(x)
            templist = self.save_file(sorted(filmList, key=lambda x: x[3], reverse=True), self.years[i])
            self.save_actorsex(self.years[i])
            self.actorsex = {}
            i = i + 1
            j = 0


class BaiDuReptile(Reptile):
    def get_one_page(self, url, name):
        html = self.get_html_text(url)
        soup = BeautifulSoup(html, 'html.parser')
        for x in soup.find_all('a', class_="title title-link"):
            if x.attrs['title'] == name:
                return x.next_sibling.next_sibling.find('b', class_="newest").string
        return soup.find('b', class_="newest").string

    def get_inf(self, year):
        films = pd.read_csv("data\\maoyan\\data_" + year + ".csv", encoding='gbk')
        films['score'] = films['name'].apply(lambda x: self.get_one_page(
            'http://v.baidu.com/v?word=' + x + '&ct=301989888&rn=67&pn=0&db=0&s=0&fbl=800&ie=utf-8', x))
        if os.path.exists("data\\baidu") is False:
            os.makedirs("data\\baidu")
        films.to_csv("data\\baidu\\data_" + "data_" + year + ".csv", encoding='gbk', index=0)

    def start(self):
        for year in self.years:
            self.get_inf(year)
            if os.path.exists("data\\" + "data_" + year + ".csv") is False:
                copyfile("data\\baidu\\data_" + "data_" + year + ".csv", "data\\" + "data_" + year + ".csv")
            # copyfile("data\\baidu\\data_" + "data_" + year + ".csv", "data\\" + "data_" + year + ".csv")
            print("finish" + year)


def main(m=30, kind='maoyan', starttime='2015',endtime='2018',driverPath='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'):
    # kind is the web that you want to get data
    # m is the time how minutes start again
    # reset: when first installed ,you need check the path of chromedriver

    # driverPath='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
    if kind == "maoyan":
        try:
            while (1):
                print('start time:', datetime.datetime.now())
                r = MaoYanReptile(0,starttime=starttime,endtime=endtime)
                r.start(r.start(exe_path=driverPath))
                time.sleep(60 * m)
        except KeyboardInterrupt:
            print('exit time:', datetime.datetime.now())
            sys.exit()
    if kind == "baidu":
        try:
            while (1):
                print('start time:', datetime.datetime.now())
                r = BaiDuReptile(0)
                r.start()
                time.sleep(60 * m)
        except KeyboardInterrupt:
            print('exit time:', datetime.datetime.now())
            sys.exit()


if __name__=='__main__':
    if len(sys.argv) < 3:
        print('You must input the reptile mode you want to start and the sleeptime')
        sys.exit()
    print('start')
    print(' '.join(sys.argv[3:]))
    kind = sys.argv[1]
    minutes=sys.argv[2]
    starttime = sys.argv[3]
    endtime = sys.argv[4]
    driverPath = ' '.join(sys.argv[5:])
    main(minutes,kind,starttime,endtime,driverPath)
