
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import numpy as np
import unicodedata
import emoji
import random
from PIL import Image
import glob
import os.path
import csv
import time

import pyautogui as pg
from pykakasi import kakasi


def main(filename):

    kakasi = kakasi()
    kakasi.setMode('H', 'a')
    kakasi.setMode('K', 'a')
    kakasi.setMode('J', 'a')
    conv = kakasi.getConverter()

    year_list = ["H30","H29","H28","H27","H26"]
    #出来上がったファイルを読み込みます
    with open(filename) as fp:
        lst = list(csv.reader(fp))    
    driver = webdriver.Chrome()    
    for i in range(len(lst)):
    #for i in range(1):
        try:
            if np.array(lst)[i,4]!="":#PDFのURLが一つもなければパス
                name = np.array(lst)[i,0]#正式名称を読み込み変数nameに格納
                k = 0
                for url in np.array(lst)[i,4:len(lst[i])]:#URLの個数分繰り返す
                    driver.get(url)
                    if k==0:
                        time.sleep(6)
                    else:
                        time.sleep(2)
                    pdf_name = (name + str(year_list[k])+".pdf")#会社名＋H26～30＋.pdfで保存するファイル名を作る
                    print(pdf_name)
                    k+=1
                    fx=1259#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ウィンドウ上部の何もない部分を指定
                    fy=48
                    pg.click(fx, fy, 1, 0.5, 'left')
                    time.sleep(1)

                    fx=1000#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  ダウンロードボタンと同じ高さでX軸だけ何もない左の場所にずらし指定
                    fy=227
                    pg.click(fx, fy, 1, 0.5, 'left')
                    time.sleep(1)
                    #保存をクリック　　x=1341, y=227 yasuki pc >>>>>>>>>>>>>>>>>>>>>>>>>>>>> 保存座標
                    fx=1341
                    fy=227
                    pg.click(fx, fy, 1, 0.5, 'left')
                    time.sleep(2)
                    #保存するファイル名を入力　=　pdf_name
                    pdf_name = conv.do(pdf_name)
                    pg.typewrite(pdf_name, 0.01)
                    #保存
                    fx=916
                    fy=684
                    pg.click(fx, fy, 1, 0.5, 'left')

            else:
                pass
        except:
            pass
                        
if __name__ == "__main__":
    filename='yu-kasho-ken351~400.csv'
    main(filename)
