from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
import unicodedata
import emoji
import random
from bs4 import BeautifulSoup
from PIL import Image
import cv2
import glob
import os.path
import csv


def main(filename,output_filename):
    with open(filename) as fp:
        lst = list(csv.reader(fp))

    URL="https://disclosure.edinet-fsa.go.jp/E01EW/BLMainController.jsp?uji.bean=ee.bean.parent.EECommonSearchBean&uji.verb=W0EZA230CXP001007BLogic&TID=W1E63010&PID=W0EZ0001&SESSIONKEY=&lgKbn=2&dflg=0&iflg=0"#askFMのURL
    print("---Chromeを起動---")
    driver = webdriver.Chrome()
    for i in range(len(lst)):
    #for i in range(3):
    #for i in range(351,400):
        contents = []
        d0 = np.array(lst)[i,0]
        d1 = np.array(lst)[i,1]
        d2 = np.array(lst)[i,2]

        COMPANY = np.array(lst)[i,3]

        if COMPANY == "":
            info = [d0,d1,d2,COMPANY,"","","","",""]
            pass
        else:
            if "･" in COMPANY:
                COMPANY = COMPANY.replace("･","・")
            else:
                pass

            info = [d0,d1,d2,COMPANY]

            try:

                driver.get(URL)
                #mul_t #社名埋め込み
                #COMPANY = "厳選ジャパン"
                #COMPANY = "企業価値成長小型株ファンド"
                driver.find_element_by_css_selector("#mul_t").send_keys(COMPANY)

                #sch #検索
                driver.find_element_by_css_selector("#sch").click()
                driver.find_element_by_css_selector("#control_object_class1 > div > div:nth-child(6) > div.panel-item.panel.panel-up > div > p.open-close").click()
                time.sleep(1)#開く
                #control_object_class1 > div > div:nth-child(6) > div.panel-target.panel-closed > div > table > tbody > tr:nth-child(2) > td.search_value.table_border_1.table_cellpadding_1 > div > select
                driver.find_element_by_css_selector("#control_object_class1 > div > div:nth-child(6) > div.panel-target.panel-closed > div > table > tbody > tr:nth-child(2) > td.search_value.table_border_1.table_cellpadding_1 > div > select").click()
                time.sleep(1)#全期間指定
                #control_object_class1 > div > div:nth-child(6) > div.panel-target.panel-closed > div > table > tbody > tr:nth-child(2) > td.search_value.table_border_1.table_cellpadding_1 > div > select > option:nth-child(7)
                driver.find_element_by_css_selector("#control_object_class1 > div > div:nth-child(6) > div.panel-target.panel-closed > div > table > tbody > tr:nth-child(2) > td.search_value.table_border_1.table_cellpadding_1 > div > select > option:nth-child(7)").click()
                time.sleep(1)#検索
                driver.find_element_by_css_selector("#sch").click()


                #control_object_class1 > div > div.result > table > tbody > tr:nth-child(2) > td:nth-child(3) > div

                #control_object_class1 > div > div.result > table > tbody > tr:nth-child(3) > td:nth-child(3) > div

                #control_object_class1 > div > div.result > table > tbody > tr:nth-child(11) > td:nth-child(3)


                text = driver.find_element_by_css_selector("#control_object_class1 > div > div.result > table > tbody > tr:nth-child(2) > td:nth-child(3) > div")
                info[2] = text.text


                
                #1
                time.sleep(1)#一つ目クリック
                driver.find_element_by_css_selector("#control_object_class1 > div > div.result > table > tbody > tr:nth-child(2) > td:nth-child(6) > div > a > img").click()
                #別ウィンドウ立ち上げ待ち
                time.sleep(5)#検索
                # ウィンドウハンドルを取得する(list型配列)
                handle_array = driver.window_handles
                # それぞれのウィンドウハンドルを表示する  #print(handle_array[0])  #print(handle_array[1])
                driver.switch_to.window(handle_array[1])

                now = driver.current_url
                info.append(now)
                driver.close()
                driver.switch_to.window(handle_array[0])
                
                #2
                time.sleep(1)#2つ目クリック
                driver.find_element_by_css_selector("#control_object_class1 > div > div.result > table > tbody > tr:nth-child(4) > td:nth-child(6) > div > a > img").click()
                #別ウィンドウ立ち上げ待ち
                time.sleep(5)#検索
                # ウィンドウハンドルを取得する(list型配列)
                handle_array = driver.window_handles
                # それぞれのウィンドウハンドルを表示する  #print(handle_array[0])  #print(handle_array[1])
                driver.switch_to.window(handle_array[1])

                now2 = driver.current_url
                info.append(now2)
                driver.close()
                driver.switch_to.window(handle_array[0])
                time.sleep(1)
                #3
                time.sleep(1)#つ目クリック
                driver.find_element_by_css_selector("#control_object_class1 > div > div.result > table > tbody > tr:nth-child(6) > td:nth-child(6) > div > a > img").click()
                #別ウィンドウ立ち上げ待ち
                time.sleep(5)#検索
                # ウィンドウハンドルを取得する(list型配列)
                handle_array = driver.window_handles
                # それぞれのウィンドウハンドルを表示する  #print(handle_array[0])  #print(handle_array[1])
                driver.switch_to.window(handle_array[1])

                now3 = driver.current_url
                info.append(now3)
                driver.close()
                driver.switch_to.window(handle_array[0])
                time.sleep(1)

                #4
                time.sleep(1)#つ目クリック
                driver.find_element_by_css_selector("#control_object_class1 > div > div.result > table > tbody > tr:nth-child(8) > td:nth-child(6) > div > a > img").click()
                #別ウィンドウ立ち上げ待ち
                time.sleep(5)#検索
                # ウィンドウハンドルを取得する(list型配列)
                handle_array = driver.window_handles
                # それぞれのウィンドウハンドルを表示する  #print(handle_array[0])  #print(handle_array[1])
                driver.switch_to.window(handle_array[1])

                now4 = driver.current_url
                info.append(now4)
                driver.close()
                driver.switch_to.window(handle_array[0])
                time.sleep(1)

                #5
                time.sleep(1)#つ目クリック
                driver.find_element_by_css_selector("#control_object_class1 > div > div.result > table > tbody > tr:nth-child(10) > td:nth-child(6) > div > a > img").click()
                #別ウィンドウ立ち上げ待ち
                time.sleep(5)#検索
                # ウィンドウハンドルを取得する(list型配列)
                handle_array = driver.window_handles
                # それぞれのウィンドウハンドルを表示する  #print(handle_array[0])  #print(handle_array[1])
                driver.switch_to.window(handle_array[1])

                now5 = driver.current_url
                info.append(now5)
                driver.close()
                driver.switch_to.window(handle_array[0])
            
            except:
                try:
                    driver.close()
                    time.sleep(2)
                except:
                    pass

                try:
                    driver.close()
                    time.sleep(2)
                    driver = webdriver.Chrome()
                except:
                    driver = webdriver.Chrome()

            contents.append(info)


            with open(output_filename, 'a') as f:
                writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
                #writer.writerow(list)     # list（1次元配列）の場合
                writer.writerows(contents) # 2次元配列も書き込める
            
    driver.close()

if __name__ == "__main__":
    filename = 'edinet_data_final.csv'
    output_filename = 'yu-kasho-ken.csv'
    main(filename,output_filename)

