from bs4 import BeautifulSoup
import requests



class Clubs:
    def __init__(self, page):
        page = str(page)
        url = "https://infonews.nctu.edu.tw/index.php?SuperType=3&action=moreclub&pagekey=" + page + "&categoryid=all"
        try:
            self.page = requests.get(url)
            self.page.encoding = 'big5'
        except:
            print("Unable to open the web....")
        self.soup = BeautifulSoup(self.page.text, "lxml")
        self.club = []
        self.parse()

    def parse(self):
        self.club = []
        self.soup = self.soup.table.find_all("tr")
        tmp = {}
        for idx, i in enumerate(self.soup[1:]):
            if idx % 3 == 0:
                tmp['title'] = i.find_all("td")[1].string
            if idx % 3 == 1:
                date = i.find_all("td")[1].string.split('-')
                tmp['start'] = date[0]
                tmp['end'] = date[1]
            if idx % 3 == 2:
                tmp['club'] = i.find_all("td")[1].string
                self.club.append(tmp)

    def print(self):
        print(self.club)


class News:
    def __init__(self, year, month, idx):
        url = "https://infonews.nctu.edu.tw/view/bulletinDetail_go.php?id="
        self.base = "https://infonews.nctu.edu.tw"
        year = '{0:04}'.format(year)
        month = '{0:02}'.format(month)
        idx = '{0:05}'.format(idx)
        self.index = str(year) + str(month) + str(idx)
        url += self.index
        print(url)
        try:
            self.page = requests.get(url)
            self.page.encoding = 'big5'
        except:
            print("Unable to open the web....")
        self.soup = BeautifulSoup(self.page.text, "lxml")
        self.news = {}
        self.parse()

    def parse(self):
        b = self.soup.find(id="BulletinDtl")
        self.news['type'] = b.img['alt']
        table = b.table.find_all('tr')
        self.news['title'] = table[1].string
        provider = table[2].string.split('：')[1]
        p = provider.split('/')
        self.news['user'] = p[0]
        self.news['department'] = p[1]
        meta = self.soup.find('tr', {"class": "style6"}).find_all('td')
        self.news['category'] = meta[0].string
        self.news['target'] = meta[1].string
        self.news['start'] = meta[2].string
        self.news['end'] = meta[3].string
        if meta[4].a:
            self.news['pos'] = meta[4].a.string.strip()
        else:
            self.news['pos'] = ""
        self.news['content'] = self.soup.find(style="max-width:680px").div
        self.news['attach'] = []
        for i in self.soup.findAll('a', {"target": "_BLANK"}):
            a = {}
            a['attach_url'] = self.base + i['href'][2:]
            a['attach_name'] = i.string
            self.news['attach'].append(a)

    def __str__(self):
        return self.index

    def print(self):
        print(self.index, self.news)

n = News(2015, 7, 210)
#n.print()
c = Clubs(1)
c.print()
