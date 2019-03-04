import pyautogui as pg
import time
import pyperclip as pc
import datetime
import random

#予期せぬ挙動が起きたときはマウスを左上いっぱいにもってくととまる
pg.FAILSAFE = True

    #はじめの60回はスクロールして次のファンドへ
for i in range(60):
    fx=770
    fy=179
    #meigarasentaku
    pg.click(fx, fy, 1, 0.5, 'left')
    time.sleep(2)
    #メニュー最小化
    pg.click(682, 113, 1, 0.5, 'left')
    time.sleep(1)


    #fund名を取得
    pg.mouseDown(8, 110, button='left')
    pg.mouseUp(572, 110, button='left')
    pg.hotkey('ctrl', 'c')
    fund_name = pc.paste()
    fund_name=fund_name.replace("/","-")
    #fund_name=fund_name.replace("","^")

    #レポート一覧へ
    pg.click(510, 150, 1, 0.5, 'left')

    time.sleep(1)
    x=94
    indices =[[x,299],[x,320],[x,344],
            [x,367],[x,388],[x,409],
            [x,430],[x,455],[x,477],
            [x,498],[x,519],[x,544],
            [x,565],[x,588],[x,609],
            [x,630],[x,654],[x,675]]
    #indices = [[x,299]]

    for index in indices:
        x=index[0]
        y=index[1]

        #日付コピー
        pg.mouseDown(580, y, button='left')
        pg.mouseUp(634, y, button='left')
        pg.hotkey('ctrl', 'c')


        #レポートを開く
        pg.click(x, y, 1, 0.5, 'left')

        time.sleep(4)
        #window最大化
        pg.hotkey('win', 'up')
        #save_button
        pg.click(739, 65, 1, 0.5, 'left')
        time.sleep(1)

        pg.typewrite(fund_name)
        pg.press('_')
        #/はファイル名にいれられないので削除
        pg.hotkey('ctrl', 'v')
        pg.press('left')
        pg.press('left')
        pg.press('backspace')
        pg.press('-')
        pg.press('right')
        pg.press('right')
        #randomっぽい数字。名前かぶり防止
        """
        ran = random.random()*10
        ran=(int(ran))%10
        pg.press(str(ran))
        """
        pg.typewrite('.pdf', 0.5)
        #pg.press('_')]

        """
        pg.typewrite(timestr)
        pg.typewrite('.pdf', 0.5)
        """
        pg.typewrite(['enter'])

        #window最小化
        pg.hotkey('win', 'down')
        time.sleep(1)
        pg.hotkey('win', 'down')

        """
        #何もないとこをクリックしてアクティブにする
        pg.click(1323, 177, 1, 0.5, 'left')
        pg.click(720, 179, 1, 0.5, 'left')
        #scroll
        pg.scroll(-17, 94, 299)
        time.sleep(2)
        """

#次の24回は座標を下げてファンド選択
for k in range(24):
    fx=795
    fy=179+17*k
    #meigarasentaku
    pg.click(fx, fy, 1, 0.5, 'left')
    time.sleep(2)
    #メニュー最小化
    pg.click(682, 113, 1, 0.5, 'left')
    time.sleep(1)

    #fund名を取得
    pg.mouseDown(8, 110, button='left')
    pg.mouseUp(572, 110, button='left')
    pg.hotkey('ctrl', 'c')
    fund_name = pc.paste()
    fund_name=fund_name.replace("/","-")
    #fund_name=fund_name.replace("","^")

    #レポート一覧へ
    pg.click(510, 150, 1, 0.5, 'left')

    time.sleep(1)
    x=94
    indices =[[x,299],[x,320],[x,344],
                [x,367],[x,388],[x,409],
                [x,430],[x,455],[x,477],
                [x,498],[x,519],[x,544],
                [x,565],[x,588],[x,609],
                [x,630],[x,654],[x,675]]
    for index in indices:
        x=index[0]
        y=index[1]

        now = datetime.datetime.now() # 現在の日時を取得

        #日付コピー
        pg.mouseDown(580, y, button='left')
        pg.mouseUp(634, y, button='left')
        pg.hotkey('ctrl', 'c')


        #レポートを開く
        pg.click(x, y, 1, 0.5, 'left')

        time.sleep(4)
        #window最大化
        pg.hotkey('win', 'up')
        #save_button
        pg.click(739, 65, 1, 0.5, 'left')
        time.sleep(1)

        pg.typewrite(fund_name)
        pg.press('_')
        #/はファイル名にいれられないので削除
        pg.hotkey('ctrl', 'v')
        pg.press('left')
        pg.press('left')
        pg.press('backspace')
        pg.press('-')
        pg.press('right')
        pg.press('right')
        #randomっぽい数字。名前かぶり防止
        """
        ran = random.random()*10
        ran=(int(ran))%10
        pg.press(str(ran))
        """
        pg.typewrite('.pdf', 0.5)
        #pg.press('_')]

        """
        pg.typewrite(timestr)
        pg.typewrite('.pdf', 0.5)
        """
        pg.typewrite(['enter'])

        #window最小化
        pg.hotkey('win', 'down')
        time.sleep(1)
        pg.hotkey('win', 'down')

"""
        #何もないとこをクリックしてアクティブにする
        pg.click(1323, 177, 1, 0.5, 'left')
        pg.click(720, 179, 1, 0.5, 'left')
        #scroll
        pg.scroll(-17, 94, 299)
        time.sleep(2)
"""
