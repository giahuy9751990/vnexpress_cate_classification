import json
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import re
import pandas as pd
import numpy as np
import streamlit as st




def crawl_a_site(url):
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		'Accept-Encoding': 'none',
		'Accept-Language': 'en-US,en;q=0.8',
		'Connection': 'keep-alive'}
	req = urllib.request.Request(url, headers=hdr)
	page = urlopen(req).read()
	bs = BeautifulSoup(page,"lxml")
	return bs
def crawl_name_of_goverment_2020():
    url = "https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_B%C3%AD_th%C6%B0_t%E1%BB%89nh_th%C3%A0nh_Vi%E1%BB%87t_Nam_nhi%E1%BB%87m_k%E1%BB%B3_2020-2025"
    bs = crawl_a_site(url)
    tbody = bs.find("tbody")
    # crawl tinh
    tinh = tbody.select("tr td:nth-of-type(1) a")
    tinh_list  = []
    for i in tinh:
        tinh_list.append(i.string)
        
    # Ho ten
    hoten = tbody.select("tr td:nth-of-type(2) a")
    hoten_list  = []
    for i in hoten:
        hoten_list.append(i.string)
        
        
    # Ho ten
    namsinh = tbody.select("tr td:nth-of-type(3)")
    namsinh_list  = []
    for i in namsinh:
        namsinh_list.append(i.string)

    # nguyen quan
    nguyenquan= tbody.select("tr td:nth-of-type(4) a")
    nguyenquan_list  = []
    for i in nguyenquan:
        nguyenquan_list.append(i.string)
        
    # nhiem ki
    nhiemki= tbody.select("tr td:nth-of-type(5)")
    nhiemki_list  = []
    for i in nhiemki:
        nhiemki_list.append(i)
        
    df = pd.DataFrame(list(zip(tinh_list,hoten_list,namsinh_list,nguyenquan_list,nhiemki_list)),columns =['Tinh', 'HoTen','namsinh','nguyenquan','nhiemki'])
    return df

page = st.sidebar.selectbox("Choose a page",['Crawl_Ten_Bi_Thu','Crawl_Vnexpress'])
if page == 'Crawl_Ten_Bi_Thu':
    if st.button("Crawl_Ten_Bi_Thu"):
        df = crawl_name_of_goverment_2020()
        print(df)
        df.to_csv("Ten_Bi_Thu_Tinh_Nam_2021_2026.csv",index=None)