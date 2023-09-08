import requests
import tkinter as tk

API_KEY = "6576149e93fbdc6c4c633229adf525db"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


class WeatherSearcher:
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("300x300")

        self.label = tk.Label(self.root, text="Weather Searcher", font=('Arial', 18))
        self.label.pack(padx=5, pady=5)

        labelDir = tk.Label(self.root, text="Enter a city", font=('Arial', 16))
        labelDir.pack()

        self.cityname = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.cityname, font=('Arial', 16))
        self.entry.pack()

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Celcius", font=('Arial', 16), variable=self.check_state)
        self.check.pack()

        self.cityname = self.entry.get()
        self.button = tk.Button(self.root, text="Search", font=('Arial', 18), command=self.search)
        
        self.button.pack(pady=5)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))

        self.textbox.configure(state="disabled")
        self.textbox.pack(padx=5)

        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=5, pady=5)


        self.root.mainloop()
    
    def search(self):

        self.textbox.configure(state="normal")
        self.textbox.delete('1.0', tk.END)
        self.textbox.configure(state="disabled")

        city = self.entry.get()
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
        response = requests.get(request_url)

        self.textbox.configure(state="normal")
        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temp = round(data['main']['temp'] - 273.15, 1)


            print_city = str(city).capitalize()
            print_weather = str(weather).capitalize()

            
            if self.check_state.get() == 0:
                temp = round((temp * 9.5 / 5.0) + 32.0, 1)
                self.textbox.insert('1.0',
                                 "City: " + print_city + "\n"
                                 "Weather: " + print_weather + "\n"
                                 "Temp: " + str(temp) + "F"
                                   +"\n")
            else:
                self.textbox.insert('1.0',
                                 "City: " + print_city + "\n"
                                 "Weather: " + print_weather + "\n"
                                 "Temp: " + str(temp) + "C"
                                   +"\n")
        else:
            self.textbox.insert('1.0', "The city name is invalid!")
        self.textbox.configure(state="disabled")
    
    def clear(self):
        self.entry.delete(0, tk.END)
        self.textbox.configure(state="normal")
        self.textbox.delete('1.0', tk.END)
        self.textbox.configure(state="disabled")

        
WeatherSearcher()


