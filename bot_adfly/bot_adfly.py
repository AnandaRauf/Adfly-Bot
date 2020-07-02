import os,random,sys,time
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

print("Bot Adfly Open Source\n")
print("Vesri 1.0\n")

def Menubot(): #Syntax ini untuk buat menu selain def memakai syntax class juga bisa, untuk berfungsi membuat class di satu file tanpa buat file baru untuk membuat class baru ^-^ yang lain juga begitu.
    print("Pilih menu bot :")
    print
    print("1. Start")
    print("2. Keluar")
def Start():
    browser = webdriver.Chrome('webdriver/chromedriver.exe') #pemanggilan webdriver chrome
    bukafilelisturl = open('listurl.txt') #pemanggilan file
    bacafile = bukafilelisturl.readlines() #readlines untuk membaca file yang terdapat text
    targeturl1 = bacafile[0] #membaca tulisan di baris pertama 0 = 1,  1 = 2 , 2 = 3 dan seterusnya , dikarenakan angka 0 itu pertama 1 itu kedua ^-^
    #Loop Syntax disini misal while targeturl1() 100 mengulang sebanyak 100 kali ini:
    browser.get(targeturl1)
def Keluar():
    exit()
    print("Kamu keluar Bot")
    print("Selamat datang di Adfly Bot ^-^\n")
Menubot() #pemanggilan menu pilihan bot ^-^
pilih = int(input("Masukan nomor pilihan menu :")) #variable syntax untuk memilih pilihan dalam menu bot ^-^.
if pilih == 1: #logika percabangan tanpa else ^-^ nested if ini kalau enggak salah :D.
    Start()
elif pilih == 2 :
    Keluar()

    
    #Okay sampai disini, sampai  jumpa di tutorial berikutnya see you ^-^ .
    #Jangan lupa share, komen, dan subscribe channel Youtube : Tech Education Indonesia 
    #Jangan lupa saling follow github : AnandaRauf github saya ^-^.

