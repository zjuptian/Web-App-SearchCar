import requests
from bs4 import BeautifulSoup
import itchat

#search for the brand page
def searchcar(brand):
    url = 'https://car.autohome.com.cn/#pvareaid=3311246'
    headers={
        'Cookie':'__ah_uuid=F42DE465-F453-499E-811E-87FF6F74F8E3; fvlid=1553087721884GkokeCj2Cc; sessionid=5B6F42D3-A397-40DF-837A-1AFB8C8722EF%7C%7C2019-03-20+21%3A15%3A25.278%7C%7Cwww.baidu.com; area=330102; ahpau=1; sessionuid=5B6F42D3-A397-40DF-837A-1AFB8C8722EF%7C%7C2019-03-20+21%3A15%3A25.278%7C%7Cwww.baidu.com; sessionip=122.225.220.143; mallsfvi=1553164306190uZT8ezOO%7Cwww.autohome.com.cn%7C3311247; mallslvi=3311247%7Cwww.autohome.com.cn%7C1553164306190uZT8ezOO; sessionvid=E9355E2E-DFE1-4D3C-82C5-76647DF4368D; __ah_uuid_ng=u_75382044; ahpvno=15; pvidchain=2042204,3311247,3311246,2042111,2042204,2042204,2042204; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1553164169,1553166574,1553166587,1553166599; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1553166599; ahsids=3230_4658_66; ref=127.0.0.1%7C0%7C2042204%7Cwww.baidu.com%7C2019-03-21+19%3A10%3A01.463%7C2019-03-21+19%3A09%3A34.647; ahrlid=1553164799198JyNj8zA7vJ-1553167145875',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Upgrade-Insecure-Requests':'1',
        'Host':'car.autohome.com.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    page = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    dic_name_page={}
    for link in soup.find_all('span',class_= 'open-name'):
        result = link.find('a')
        name = result.text.encode("latin1").decode("gbk")
        name_page = 'https://car.autohome.com.cn'+ result.attrs['href']
        if name not in dic_name_page.keys():
            dic_name_page[name] = name_page
    print(dic_name_page)
    car_required = brand
    car_required_url = dic_name_page[car_required]
    print(car_required_url)

    #search for the price of the exact car that you want
    car_required_page = requests.get(url=car_required_url,headers=headers)
    car_required_soup = BeautifulSoup(car_required_page.content,'html.parser')
    content = []
    print(car_required_soup)
    for car_required_link in car_required_soup.find_all('div',class_= 'list-cont-main'):
        car_required_name = car_required_link.find('div',class_ = 'main-title').find('a').text.encode("latin1").decode("gbk")
        #car_required_official_price = car_required_link.find('div',class_ = 'main-lever')
        car_required_web = 'https://car.autohome.com.cn' + car_required_link.find('div',class_ = 'main-title').find('a').attrs['href']
        content.append({'car_name':car_required_name,'car_web':car_required_web})
    print(content)
    return content

def main():
    brand=input()
    result = searchcar(brand)

if __name__ == '__main__':
    main()






