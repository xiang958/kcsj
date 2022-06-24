import pymysql
import requests

#连接数据库
def commetdb():
    conn = pymysql.connect(host='localhost',user='root',password='123456',db='MovieData',autocommit=True)   # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。)
    return conn

#获取相应url的数据
def getData(url,year):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
        }
        data = {
            'keyword': '',
            'pageIndex': '1',
            'pageSize': '20',
            'searchType': '0',
            'locationId': '290',
            'genreTypes': '',
            'area': '',
            'year': year}
        data = requests.get(url=url, data=data,headers=headers)
        data.raise_for_status()
        data.encoding='utf-8'
        return data.text
    except:
        return ""

#将从url中的数据插入到mysql中
def insertData():
    url = 'http://front-gateway.mtime.com/mtime-search/search/unionSearch2'
    for year in ['2020','2021','2022']:
        getData(url,year)

