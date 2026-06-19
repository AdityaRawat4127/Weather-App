import requests 
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

base_url="https://api.openweathermap.org/data/2.5/weather"

apikey=" " # ENTER YOUR API KEY HERE

def get_weather():
    place=entry1.get()

    params={
        'q':place,
        'appid':apikey,
        'units':'metric'
        }
    r=requests.get(base_url, params=params)
    data=r.json()
    #print(data)
    if data.get("cod") != 200:
        messagebox.showerror("Error", "City not found!")
        return
    
    temp=data['weather'][0]['id']
    sky=data['weather'][0]['description']
    humidity=data['main']['humidity']
    

    output_label.config(
        text=f"Place: {place}\n"
             f"Temperature: {temp}°C\n"
             f"Sky: {sky}%\n"
             f"Humidity: {humidity}%"
    )


weather=tk.Tk()
weather.title("Weather App")
weather.geometry("400x400")
weather.iconbitmap("main_icon.ico")
weather.configure(bg="#87CEEB")
weather.minsize(700,500)

"""image=Image.open("weather_icon.png")
photo=ImageTk.PhotoImage(image)
"""
output_label=tk.Label(weather,text='',bg="#87CEEB",font=("verdana",12,"italic","bold"))
output_label.pack(pady=10)

text_label1=tk.Label(weather, text="Type State Name", bg="#87CEEB",font=("verdana",12,"italic","bold"))
text_label1.pack(pady=10)

entry1=tk.Entry(weather, width=30)
entry1.pack(pady=8, ipady=3)


text_button=tk.Button(weather, text='GO',bg="white",font=('verdana',12,'bold'), command=get_weather )
text_button.pack(pady=10)

weather.mainloop()
