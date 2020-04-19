# -*- coding:UTF-8 -*-

from src.core.main.common.downloadTools import downloadCore
from bs4 import BeautifulSoup
import time

url_map_info=[
    {"classify":"水果","url_site":"https://www.cnhnb.com/purchase/sgzw-0-0-0-0-page_num","start_index":"1","end_index":"833"},
    {"classify":"蔬菜","url_site":"https://www.cnhnb.com/purchase/sczw-0-0-0-0-page_num","start_index":"1","end_index":"833"},
    {"classify":"蛋肉","url_site":"https://www.cnhnb.com/purchase/qcrd-0-0-0-0-page_num","start_index":"1","end_index":"833"},
    {"classify":"农副","url_site":"https://www.cnhnb.com/purchase/nfjg-0-0-0-0-page_num","start_index":"1","end_index":"281"},
    {"classify":"粮食","url_site":"https://www.cnhnb.com/purchase/lymm-0-0-0-0-page_num","start_index":"1","end_index":"536"}
]

def save_to_local_file(pd_list):
    for pd_dict in pd_list:
        with open('/home/guimingbao/Data/spider/farmerProduct/20200419.txt','a') as rr_pip:
            rr_pip.write(str(pd_dict))
            rr_pip.write("\n")
    time.sleep(1)

for single_classify in url_map_info:

    classify_info = single_classify.get("classify")
    url_site_info = single_classify.get("url_site")
    start_index_info = single_classify.get("start_index")
    end_index_info = single_classify.get("end_index")

    print("产品类别 : "+classify_info+" , 网址 : "+url_site_info+" , 索引结束页 : "+end_index_info)

    for page_num in range(int(start_index_info),int(end_index_info)+1):
        pd_list = []
        single_url = url_site_info.replace('page_num',str(page_num))
        html_content = downloadCore(single_url)
        soup = BeautifulSoup(html_content, "html.parser")
        # soup.find("p").text + "|" + soup.find("source").attrs['src']
        for cell in soup.find_all(name='div',class_='purchase-cell'):

            cell = str(cell).replace('\n','')
            child_cell = BeautifulSoup(cell, "html.parser")
            p_product = child_cell.find(name='div',attrs={"class":"cateName"}).text.strip()
            p_number = child_cell.find(name='div',attrs={"class":"qty"}).text.replace(' ','')
            p_area = child_cell.find(name='div',attrs={"class":"scopeFullName"}).text.replace(' ','')
            p_person = child_cell.find(name='div',attrs={"class":"linkName"}).text.replace(' ','')
            #print("\t\t采购品种 : "+str(p_product)+" , 采购数量 : "+str(p_number)+" , 期望货源地 : "+str(p_area)+" , 发布人 : "+str(p_person))
            pd_dict = {"p_classify":classify_info,"page_num":page_num,"p_product":p_product,"p_number":p_number,"p_area":p_area,"p_person":p_person}
            pd_list.append(pd_dict)
        save_to_local_file(pd_list)
