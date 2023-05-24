'''
如何使用Python取得歷史股價，簡介yfinance、ffn、FinMind
https://havocfuture.tw/blog/python-stock-history
'''

'''
這是專門取得台灣股市資料
'''
import pandas_datareader.data as pdr
import yfinance as yf
import os
from datetime import datetime
import pandas as pd

def get_stock_data(stockid, year='all'):
    '''
    @param stockid是股票代碼
    @param year 是年份
    '''
    yf.pdr_override()
    stockid_str = f'{stockid}.TW'   
    current = os.path.abspath("./")
    current_date = datetime.now()    
    filename = f"{stockid_str}_{current_date.year}_{current_date.month}_{current_date.day}.csv"
    csv_file_path = os.path.join(current,'data',filename)

    if not os.path.exists(csv_file_path):
        stock_dataFrame = pdr.get_data_yahoo(stockid_str)
        stock_dataFrame.to_csv(csv_file_path)
    stock_dataFrame = pd.read_csv(csv_file_path)
    #print(stock_dataFrame)
    #stock_dataFrame1 = stock_dataFrame.reset_index()
    #stock_dataFrame1['Date'] = stock_dataFrame1['Date'].map(lambda x:f'{x.year}-{x.month}-{x.day}')
    if year == 'all':
        return stock_dataFrame
    else:
        startYear = f'{year}-1-1'
        stopYear = f'{year}-12-31'        
        stock_dataFrame['Date'] = pd.to_datetime(stock_dataFrame['Date'])     
        mask = (stock_dataFrame['Date'] >= startYear) & (stock_dataFrame['Date'] <= stopYear)
        year_stock_data = stock_dataFrame.loc[mask]
        #stock_list = year_stock_data.to_numpy().tolist()
    return year_stock_data

import sqlite3
from sqlite3 import Error
def get_stockid():
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    def select_all_tasks(conn):
        sql ="SELECT  code,name FROM codeSearch"
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows

    current = os.path.abspath("./")
    filename = "code.db"
    db_file_path = os.path.join(current,'data',filename)
    con = create_connection(db_file_path)
    rows = select_all_tasks(con)
    con.close()
    return rows