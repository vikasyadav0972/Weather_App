from tkinter import *
from tkinter import ttk
import requests
import json

def data_get():
    city=city_name.get()

    #API_key = ""
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid= your api").json()
    print(data)

    w_lable1.config(text=data["weather"][0]["main"])
    wb_lable1.config(text=data["weather"][0]["description"])
    temp_lable1.config(text=(int(data["main"]["temp"]-273.15)))
    per_lable1.config(text=data["main"]["pressure"])
        
win=Tk()
win.title("Real time Weather")
win.config(bg="lightblue")
win.geometry("500x570")

name_lable=Label(win,text="Weather App",font=("bold",40))  
name_lable.place(x=25,y=50, height=50,width=450)

city_name=StringVar()
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com=ttk.Combobox(win,text="Weather App",font=("bold",20),values=list_name,textvar=city_name)

com.place(x=25,y=120, height=50,width=450)

w_lable=Label(win,text="Weather climate",font=(10))  
w_lable.place(x=25,y=260, height=50,width=210)

w_lable1=Label(win,text=" ",font=(10))  
w_lable1.place(x=250,y=260, height=50,width=210)


wb_lable=Label(win,text="Weather Descrition",font=(10))  
wb_lable.place(x=25,y=330, height=50,width=210)

wb_lable1=Label(win,text=" ",font=(10))  
wb_lable1.place(x=250,y=330, height=50,width=210)

temp_lable=Label(win,text="Temperature",font=(10))  
temp_lable.place(x=25,y=400, height=50,width=210)

temp_lable1=Label(win,text=" ",font=(10))  
temp_lable1.place(x=250,y=400, height=50,width=210)

per_lable=Label(win,text="Pressure",font=(10))  
per_lable.place(x=25,y=470, height=50,width=210)

per_lable1=Label(win,text=" ",font=(10))  
per_lable1.place(x=250,y=470, height=50,width=210)

button=Button(win,text="Enter",font=("bold",20),command=data_get)
button.place(x=200,y=190, height=50,width=100)

win.mainloop()