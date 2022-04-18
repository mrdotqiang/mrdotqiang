import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
import os

# -*- coding:utf-8 -*-

#UA伪装  user-agent   UA检测
if __name__ == '__main__':
    '''url = 'https://www.sogou.com/web'
    response = requests.get(url=url)
    page_text = response.text
    print(page_text)'''
    ''' headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    kw = input('enter a word')
    param = {
        'query':kw
    }
    response = requests.get(url=url,params=param,headers=headers)

    page_text = response.text
    print(page_text)'''
    #----------------------------------------------------------------------------------
    ''' headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    url = 'https://fanyi.baidu.com/sug'
    word = input('enter a word:')
    data = {
        'kw':word
    }
    response = requests.post(url=url,data=data,headers=headers)
    dog_json = response.json()
    #print(dog_json)
    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dog_json,fp=fp,ensure_ascii=False)'''

    '''headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/chart/top_list' #?type=24&interval_id=100:90&action=&start=20&limit=20
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '21',
    }
    response = requests.get(url=url,params=param,headers=headers)
    response_list = response.json()
    print(response_list)'''

    #
    '''headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []
    all_data_info = []  # 存储所有企业的详情数据
    for page in range(1,6):
        date = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName' : '',
            'conditionType': '1',
            'applyname' : '',
            'applysn': '',
        }
        response = requests.post(url=url, data=date, headers=headers)
        json_ids = response.json()
        
        for dic in json_ids['list']:
            id_list.append(dic['ID'])
            #print(id_list,len(id_list))

    #获取企业详细数据
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data={
            'id':id
        }
        detail_json = requests.post(url=url,data=data,headers=headers).json()
        all_data_info.append(detail_json)
        print(detail_json)
    fp = open('./allData.json','w',encoding='utf-8')
    json.dump(all_data_info,fp=fp,ensure_ascii=False)'''

    #get the images from Internet
    #bs4 demo
    '''
     headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text
    #page_text.encoding = 'utf-8'
    #page_text.encode('gb18030')
    soup = BeautifulSoup(page_text, 'lxml',exclude_encodings=['utf-8'])
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        book_title = li.a.string
        book_url = 'https://www.shicimingju.com/' + li.a['href']
        # 对每条url发起请求，解析每章节内容
        # print(book+' '+book_url)
        book_text = requests.get(url=book_url, headers=headers).text
        #book_text.encoding = 'utf-8'
        #book_text.encode('gb18030')
        book_soup = BeautifulSoup(book_text, 'lxml',exclude_encodings=['utf-8'])
        div_tag = book_soup.find('div', class_='chapter_content')
        book_content = div_tag.text
        fp.write(book_title + ':' + book_content + '\n')
        print(book_title , '抓取成功!')
        break
    '''

    #xpath demo
    ''' headers = {
        #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    url = 'https://bj.58.com/ershoufang/'
    page_text = requests.get(url=url,headers=headers).text

    tree = etree.HTML(page_text)
    div_list = tree.xpath('//section[@class="list-main"]//section[@class="list"]/div')
    print(len(div_list)) '''

    # get images from internet
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    }
    url = 'https://pic.netbian.com/4kmeinv/'
    response = requests.get(url=url, headers=headers)
    #response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)

    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_src = 'https://pic.netbian.com/4kmeinv/'+li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        #print(img_name,img_src)
        img_data = requests.get(url=img_src,headers=headers).content
        img_path = 'picLibs/'+img_name
        with open(img_path,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功!')
    '''

    # another xpath demo
    '''headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    #print(page_text)
    li_list = tree.xpath('//div[@class="bottom"]/ul/li')
    all_city_names = []
    #print(len(li_list))
    for li in li_list:
        city_url = 'https://www.aqistudy.cn/historydata/' + li.xpath('./a/@href')[0]
        city_name = li.xpath('./a/text()')[0]
        all_city_names.append(city_name)
        #print(city_name+' '+city_url)
    all_city_list = tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    #解析全部城市名称
    for ali in all_city_list:
        all_city_name = ali.xpath('./a/text()')[0]
        all_city_names.append(all_city_name)

    #print(all_city_names,len(all_city_names))'''

    '''headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    #print(page_text)
    all_city_names = []
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)

    print(all_city_names,len(all_city_names))
    '''

    #get the free resume template
    ''' headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    url = 'https://sc.chinaz.com/jianli/free.html'
    page_text = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_text)
    div_list = tree.xpath('/html/body/div[4]/div[3]/div/div/div')
    if not os.path.exists('./doc'):
        os.mkdir('./doc')
    for dl in div_list:
        resume_url = 'https:'+dl.xpath('./a/@href')[0]
        resume_title = dl.xpath('./p/a/text()')[0]
        resume_str = str(resume_title)
        resume_t = resume_str.encode('iso-8859-1').decode('utf-8')
        #print(resume_t,resume_url)
        resume_data = requests.get(url=resume_url,headers=headers).content
        resume_tree = etree.HTML(resume_data)
        resume_download_url = resume_tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
        print(resume_download_url)
        resume_rar_data = requests.get(url=resume_download_url,headers=headers).content
        resume_path = 'doc/' + resume_t
        with open(resume_path, 'wb') as fp:
            fp.write(resume_rar_data)
            print(resume_t, '下载成功!')'''

      



















