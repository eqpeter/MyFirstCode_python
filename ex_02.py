﻿########################################################################
# Python x AI Agent
# List & OOP 串列與物件導向
#
# [作業]
# 財務報表輸入系統
# 請以物件導向方式改寫先前作業 (ex_13)
#
# 規劃：撰寫程式制定新的類別：
#   Income，年度銷貨收入紀錄：
#     1)屬性：'年度', '營業額', '利潤' 等等
#     2)物件方法：
#       a)字串(報表印出)表現方式
#       b)以獲利率比較大小(__lt__)
#     3)類別方法：
#       a)以獲利率排序報表並填入名次(欄位).
#       b)印出整份報表 (以年度排序)
#      
#   函數：
#     1)協助使用者輸入相關數值資料並存檔
#     2)儲存檔案
#     3)載入檔案
#
# 問題：請建立實體執行以下操作
#   輸入：
#     從檔案載入並印出先前所輸入的報表，
#     要求使用者輸入 '年度', '營業額', '利潤' 數值
#     1)必須輸入3個數值，數值間以逗號隔開
#     2)按 'Q' 或 'q' 離開
#     3)如果有新增資料，在離開系統前自動儲存報表。
#   輸出：
#     1)請增加「獲利率」一欄(自動計算)，
#     2)請增加「排名(獲利率)」一欄(自動計算)，
#     3)印出這份報表。
#       - 其中營業額與利潤要加上千分位符號；
#       - 獲利率要採百分比表示，精確度到小數點後2位。
#
#
#   年度        營業額       利潤      獲利率     排名
# ======================================================
#    108      1550000	    47895
#    109      2000000	   104600
#    110      2234000	   122200
# ======================================================
#
# (提示)：使用 os.path.isfile(path) 測試檔案是否存在？
########################################################################

import csv
from os.path import isfile

class Income:
    """代表一筆資料 (年度銷貨收入紀錄)"""
    all = []

    def __init__(self, year, sales, profit):
        """初始化一筆(年度)資料，並附加入報表串列"""


    def __repr__(self) -> str:
        """傳回描述每筆(列)資料的字串"""


    def __str__(self):
        """傳回列印時每筆(列)資料的字串(已排版)"""


    def __lt__(self, other):
        """以獲利率比較大小"""


    @classmethod
    def sort_rate(cls):
        """以 獲利率 排序報表並填入 名次(欄位)."""

        
    @classmethod
    def report(cls):
        """印出整份財務報表"""
    

def save_to_csv(CSV_FILENAME):
    """儲存報表至指定檔案名稱"""


def load_csv(CSV_FILENAME):
    """載入檔案，恢復報表資料"""


def entry(CSV_FILENAME):
    """要求輸入營業數據，以建立年度資料物件並存檔
    :param str CSV_FILENAME: file path
    """ 


if __name__ == '__main__':
    filename = input('\nEnter the department code: ') + '.csv'
    file_updated = True

    load_csv(filename)

    print('\nCurrent Report:')  # debug
    Income.report()

    entry(filename)

    print('\nUpdated Report:')  # debug
    Income.report()

    print("Peter")


