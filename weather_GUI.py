# author yahya stihi
# stihiyahy2016@gmail.com
#you need API key from https://openweathermap.org/
import tkinter as tk
import requests
from PIL import Image, ImageTk


root = tk.Tk()
root.title('yahya weather')

#7d3e88675b678961df9ba90435e7a5f6
#pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={your api key}

def format_response(weather):
    try:
        weather_icon.delete("all")
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = int(weather['main']['temp'])/10
        final_str = 'City: %s \nConditions: %s \nTemperture : %s °C' %(name, desc, temp)
    except:
        final_str = 'There was a problem while \nretrieving data'

    return final_str

def get_weather(city):
    if entry2.get() == '':
        weather_key = '7d3e88675b678961df9ba90435e7a5f6'
    else:
        weather_key = f'{entry2.get()}'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Celsius'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(frame2.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


canvas = tk.Canvas(root, height=400, width=500)
canvas.pack()

background_image = tk.PhotoImage(file='image.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#FF5733', bd=5)
frame.place(relx= 0.5, rely=0.05, relwidth=0.75, relheight=0.14, anchor='n')


entry = tk.Entry(frame, font=('bold',14))
entry.place(relx=0.01, rely=0.04, relwidth=0.70, relheight=0.9)


button = tk.Button(frame, text='Get Weather',font=('bold',12),command=lambda: get_weather(entry.get()))
button.place(relx=0.72, rely=0.05, relwidth=0.27, relheight=0.9)


frame2 = tk.Frame(root, bg='#FF5733', bd=10)
frame2.place(relx=0.5, rely=0.23, relwidth=0.75, relheight=0.60, anchor='n')

label = tk.Label(frame2, font=('bold', 14), anchor='nw', justify='left', bd=4 )
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(frame2, bd=0, highlightthickness=0)
weather_icon.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.40)

frame3 = tk.Frame(root, bg='green', bd=5)
frame3.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')

entry2 = tk.Entry(frame3, font=('bold', 11))
entry2.place(relx=0.25, rely=0, relwidth=0.75, relheight=1)

label2 = tk.Label(frame3,text='YOUR API >>', font=('bold', 10), justify='left', bd=1,bg='gray' )
label2.place(relwidth=0.24, relheight=1)

label3 = tk.Label(root,text='email: stihiyahya2016@gmail.com', font=('bold', 7), justify='left')
label3.place(relx=0.85, rely=0.96,anchor='n')


root.mainloop()