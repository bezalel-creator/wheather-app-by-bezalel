import sys
import requests
import tkinter as tk
from tkinter import ttk


import ttkbootstrap as tb  

class wheatherapp:
    def __init__(self,window):
        self.window = window
        self.window.title("weather app")
        self.window.style = tb.Style("cyborg")
        self.window.geometry('400x650')
        self.window.minsize(300 , 500)
        self.searching_label= ttk.Label(window,font=("Helvetica", 30), text="search a city weather")
        self.get_city_button= ttk.Button(window,text="get city weather", command= lambda: (self.get_weather()))
        self.searching_entry= ttk.Entry(window,font=("Helvetica", 30))
        self.dgrees_label = ttk.Label(window ,text="")
        self.emogi_label = ttk.Label(window, text="")
        self.description_label= ttk.Label(window,text="")

        #layout
        self.searching_label.pack()
        self.searching_entry.pack(pady=50)
        self.get_city_button.pack(ipadx=150)
        self.dgrees_label.pack()
        self.emogi_label.pack()
        self.description_label.pack()

        
    def get_weather(self):
        api_key = "8e62e406f9f01ccf6af2e2c04853c103"
        city = self.searching_entry.get()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        try:    
            response= requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.dysplay_whether(data)
        except requests.exceptions.HTTPError as http_error:
                match response.status_code:
                    case 400:
                        print("bad requst\n pleas check your input")
                    case 401:
                        print("unouthouraized\n invalid api key")
                    case 403:
                        print("forbidden\n acces is denied")
                    case 404:
                        print("not found \n city not found")
                        self.display_error()
                    case 500:
                        print("internal server error\n please try again later")
                    case 502:
                        print("bad getway\n invalid response from the server")
                    case 503:
                        print("service unavalible\n server is down")
                    case 504:
                        print("getway timeout\n response from the server")
                    case _:
                        print(f"HTTPError acourd\n{http_error}")
                        
        except requests.exceptions.ConnectionError as e:
            print("conection error\n check your internet conection")
            self.conection_error()

        except requests.exceptions.Timeout as e:
            print("timeout error\n the reqqiest time out")
        except requests.exceptions.TooManyRedirects as e:
            print("to many redirect\n check the url")                        
        except requests.exceptions.RequestException as request_error:
                print(f"request error\n{request_error}")
    
    def dysplay_whether(self, data):
        print(data)
        print("its working")

        temperture_k= data["main"]["temp"]
        temperture_c = temperture_k - 273.15
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.whether_id_func(weather_id)


        self.description_label.config(font=("Helvetica", 30), text=f"{weather_description}")
        print(f"its{temperture_c} dgrees")
        self.dgrees_label.config(font=("Helvetica", 40), text=f" its {temperture_c:.0f} dgrees")
        emoji = self.whether_id_func(weather_id)
        self.emogi_label.config(font=("Helvetica", 50),text=emoji)
    
    def display_error(self):
                      
                      self.dgrees_label.config(font=("Helvetica", 30), text="not found: \n city not found")
                      self.emogi_label.config(text="")
                      self.description_label.config(text="")
    
    def conection_error(self):
        self.dgrees_label.config(font=("Helvetica", 15), text="      conection error:\n check your internet conection")
    
    def whether_id_func(self, weather_id):
         
         if 200 <= weather_id <= 232:
              return "🌧️" 
        
         elif 300 <= weather_id <= 321:
              return "🌧️" 
        
         elif 500 <= weather_id <= 531:
              return "🌧️" 
        
         elif 600 <= weather_id <= 622:
              return "❄️" 
        
         elif 701 <= weather_id <= 741:
              return "🌤️" 
        
         elif 701 <= weather_id <= 741:
              return "🌫️" 
         
         elif weather_id == 762:
              return "🔥" 

        
         elif weather_id == 771:
              return "💨"

         elif weather_id == 781:
              return "🌪️" 

         elif weather_id == 800:
              return "☀️"
         elif 801 <= weather_id <= 804:
              return "☁️"
         else: 
              return "" 
          




            

if __name__ == "__main__":
    window = tk.Tk()
    app = wheatherapp(window) 
    window.mainloop() 
