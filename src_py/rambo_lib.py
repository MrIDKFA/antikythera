import shutil
import os
import sqlite3
import csv


def it_data_copy():
    src_folder = "T:\\Specialni\\Porady\\ZTP\\"
    dst_folder= 'D:\\OneDrive\\FAST\\Ecovacs\\data\\'

    files = ["sk_ztp_NEW.CSV", "all_ztp.CSV"]

    for filename in os.listdir(src_folder):
        if filename in files:
            src_file = os.path.join(src_folder, filename)
            dst_file = os.path.join(dst_folder, filename)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dst_file)

def terminy_data_copy():
    src_folder= "T:\\Produkty\\Bila dovoz\\SENCOR\\skladovka\\data\\"
    dst_folder= 'D:\\OneDrive\\FAST\\Ecovacs\\data\\'

    files = ["Terminy_dovozu.csv"]

    for filename in os.listdir(src_folder):
        if filename in files:
            src_file = os.path.join(src_folder, filename)
            dst_file = os.path.join(dst_folder, filename)
            if os.path.isfile(src_file):
                shutil.copy(src_file, dst_file)

def update_sklad():
    conn = sqlite3.connect("antikythera.db")
    cursor = conn.cursor
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS sklad (
	    line_id integer PRIMARY KEY AUTOINCREMENT,
	    sapItem text,
	    skladNum integer,
	    KS integer,
	    ATP integer
    ) 
