import requests
from bs4 import BeautifulSoup
import pandas as pd

# 爬取網頁HTML內容
url = "https://pokemongaole.com.tw/stores/"
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML內容，提取出<address>標籤內的文本內容
soup = BeautifulSoup(html_content, "html.parser")
city_all=soup.find("div", {"class": "city"})

# 取得所有城市
city_list={}
for city in city_all.find_all("option"):
    if "選擇" not in city.get_text():
        city_list[city.get_text()]=None

for city in city_list:
    url = "https://pokemongaole.com.tw/stores/" + city
    response = requests.get(url)
    html_content = response.text

    # 使用BeautifulSoup解析HTML內容，提取出<address>標籤內的文本內容
    soup = BeautifulSoup(html_content, "html.parser")
    district_all=soup.find("div", {"class": "district"})

    #取得所有城市中的區域
    district_list=[]
    for district in district_all.find_all("option"):
        district_list.append(district.get_text())
    
    # 把第一筆drop掉
    district_list=district_list[1:]

    city_list[city]=district_list

# 要處理的地址列表
address_list = []
store_list = []

for city in city_list:
    for district in city_list[city]:
        url = "https://pokemongaole.com.tw/stores/" + city + "/" + district
        response = requests.get(url)
        html_content = response.text

        soup = BeautifulSoup(html_content, "html.parser")

        # 地址
        address_all = soup.find_all("address")
        for address in address_all:
            address_list.append(address.text.strip()[:-4])
        
        # 店名
        stores_all=soup.find_all("div", {"class": "store-name"})
        for store in stores_all:
            store_list.append(store.find("span", {"class": "font-bold"}).text[5:])

x={}
x["地址"]=address_list
x["店名"]=store_list
df = pd.DataFrame(x)
df.to_csv("addresses.csv", encoding="utf_8_sig")