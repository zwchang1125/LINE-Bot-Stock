# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:42:45 2024

@author: User

下單動作
"""
import time
import pyautogui
from loguru import logger

def open_order_stock():
    pyautogui.moveTo(1785, 165)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.3)

def enter_stock_No(No:int):
    pyautogui.moveTo(1660, 290)
    pyautogui.click(clicks=1, button='left')
    pyautogui.typewrite(str(No), interval=0.01)
    time.sleep(0.3)
    pyautogui.press('enter')    
    time.sleep(0.1)

def select_whole_odd_shares(whole_odd:str):
    if whole_odd == '整股':
        pos = (1490, 375)
    elif whole_odd == '零股':
        pos = (1660, 375)
    else:
        print('Error')
        return
    pyautogui.moveTo(pos)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)

def select_stock_type(stock_type:str):
    if stock_type == '現股':
        pos = (1490, 445)
    elif stock_type == '融資':
        pos = (1660, 445)
    elif stock_type == '融券':
        pos = (1820, 445)
    else:
        print('Error')
        return        
    pyautogui.moveTo(pos)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)

def select_buy_sell_shares(whole_odd:str):
    if whole_odd == '買':
        pos = (1535, 575)
    elif whole_odd == '賣':
        pos = (1780, 575)
    else:
        print('Error')
        return
    pyautogui.moveTo(pos)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)

def enter_shares_counts(count:int):
    pyautogui.moveTo(1750, 645)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)
    pyautogui.press(['backspace', 'backspace'])
    pyautogui.typewrite(str(count))
    time.sleep(0.1)

def enter_order_price(price:int):
    pyautogui.moveTo(1760, 745)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)    
    pyautogui.press(['backspace' for _ in range(10)])
    pyautogui.typewrite(str(price))
    
def select_price_onsale(price_onsale:str, price:int=None):
    if price_onsale == '限價':
        enter_order_price(price)
    elif price_onsale == '市價':
        pyautogui.moveTo(1355, 745)
        pyautogui.click(clicks=1, button='left')
        time.sleep(0.01)
        pyautogui.moveTo(1325, 950)
        pyautogui.click(clicks=1, button='left')
    else:
        print('Error')
        return
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)    
    
def send_order():
    pyautogui.moveTo(1700, 800)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)   
    pyautogui.moveTo(1195, 530)
    pyautogui.click(clicks=1, button='left')
    pyautogui.moveTo(1260, 575)
    pyautogui.click(clicks=1, button='left')
    open_order_stock()

def refresh_stock_web():
    pyautogui.moveTo(100, 67)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    pyautogui.moveTo(1060, 650)
    pyautogui.click(clicks=1, button='left')
    time.sleep(5)
    pyautogui.moveTo(1160, 580)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)
    take_screenshot()
    
def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.jpg')
    
def query_order():
    pyautogui.moveTo(300, 170)
    pyautogui.click(clicks=1, button='left')
    pyautogui.moveTo(340, 315)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    pyautogui.moveTo(185, 170)
    pyautogui.click(clicks=1, button='left')
    pyautogui.moveTo(185, 400)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    take_screenshot()
    
def query_my_shares():
    pyautogui.moveTo(185, 170)
    pyautogui.click(clicks=1, button='left')
    pyautogui.moveTo(185, 400)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    pyautogui.moveTo(300, 170)
    pyautogui.click(clicks=1, button='left')
    pyautogui.moveTo(340, 315)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    take_screenshot()

def sort_by_status():
    pyautogui.moveTo(350, 290)
    pyautogui.click(clicks=1, button='left')
    take_screenshot()

def sotck_command_parsing(command_splt:list):
    try:        
        [_, stock_No, whole_odd, stock_type, buy_sell, count, price_onsale, price] = command_splt
        logger.info([stock_No, whole_odd, stock_type, buy_sell, count, price_onsale, price])
        open_order_stock()
        enter_stock_No(stock_No)
        select_whole_odd_shares(whole_odd)
        select_stock_type(stock_type)
        select_buy_sell_shares(buy_sell)
        enter_shares_counts(count)
        select_price_onsale(price_onsale, price)
        send_order()
        return True
    except:
        take_screenshot()
        return False
    

def delete_order(number:int):
    offset = (number-1)*50
    pyautogui.moveTo(70, 335+offset)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    pyautogui.moveTo(1190, 650)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    pyautogui.moveTo(1190, 695)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    pyautogui.moveTo(1265, 650)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.5)
    take_screenshot()

def query_stock_No(num:int):
    pyautogui.moveTo(1690, 220)
    pyautogui.click(clicks=1, button='left')
    time.sleep(0.1)
    pyautogui.typewrite(str(num))
    time.sleep(2)
    pyautogui.press(['enter'])
    time.sleep(0.5)
    take_screenshot()

def shut_down():
    pyautogui.moveTo(30, 1055)
    pyautogui.click(clicks=1, button='left')
    time.sleep(1)
    pyautogui.moveTo(30, 1000)
    pyautogui.click(clicks=1, button='left')
    time.sleep(1)
    pyautogui.moveTo(30, 895)
    pyautogui.click(clicks=2, button='left')

if __name__ == '__main__':
    shut_down()


    
       
       
       
       
       
       
       
       