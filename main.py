import os, socket, time, requests
from bs4 import BeautifulSoup
import tkinter as tk

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("www.google.com", 80))
    s.close()
    print("Çevrimiçi")
except Exception:
    print("Çevrimdışı")
    time.sleep(2)
    exit()

if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")

url = "https://kur.doviz.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
data = soup.find("span", {"data-socket-key":"gram-altin"}).text
data2 = soup.find("span", {"data-socket-key":"EUR"}).text
data3 = soup.find("span", {"data-socket-key":"USD"}).text
data4 = soup.find("span", {"data-socket-key":"GBP"}).text
data5 = soup.find("span", {"data-socket-key":"XU100"}).text
data6 = soup.find("span", {"data-socket-key":"bitcoin"}).text

window = tk.Tk()
window.geometry("300x275")
window.title("Borsa")
if os.name == "nt":
    window.iconbitmap(".\simge.ico")
elif os.name == "posix":
    window.iconbitmap("./simge.xbm")


label = tk.Label(window, text="BORSA", font="25")
label.pack()

gramaltin = tk.Label(window, text="Gram Altın", font="15")
gramaltin.pack()
gramaltin.place(x=30,y=25)
goldvalue = tk.Label(window, text=data, font="15")
goldvalue.pack()
goldvalue.place(x=30,y=45)

euro = tk.Label(window, text="Euro", font="15")
euro.pack()
euro.place(x=30,y=75)
eurovalue = tk.Label(window, text=data2, font="15")
eurovalue.pack()
eurovalue.place(x=30,y=95)

bist = tk.Label(window, text="Bist100", font="15")
bist.pack()
bist.place(x=30,y=125)
bistvalue = tk.Label(window, text=data5, font="15")
bistvalue.pack()
bistvalue.place(x=30,y=145)




dolar = tk.Label(window, text="Dolar", font="15")
dolar.pack()
dolar.place(x=200,y=25)
dolarvalue = tk.Label(window, text=data3, font="15")
dolarvalue.pack()
dolarvalue.place(x=200,y=45)

sterlin = tk.Label(window, text="Sterlin", font="15")
sterlin.pack()
sterlin.place(x=200,y=75)
sterlinvalue = tk.Label(window, text=data2, font="15")
sterlinvalue.pack()
sterlinvalue.place(x=200,y=95)


bitcoin = tk.Label(window, text="Bitcoin", font="15")
bitcoin.pack()
bitcoin.place(x=200,y=125)
bitcoinvalue = tk.Label(window, text=data6, font="15")
bitcoinvalue.pack()
bitcoinvalue.place(x=200,y=145)



window.mainloop()