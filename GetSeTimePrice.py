#pip install requests
import requests
import json
from datetime import datetime

class GetSeTimePrice:
    year = ""
    month = ""
    day = ""
    priceclass = ""

    status_code = {
        200: "Everything went okay, and the result has been returned (if any).",
        301: "The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.",
        400: "The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.",
        401: "The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.",
        403: "The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.",
        404: "The resource you tried to access wasn’t found on the server.",
        503: "The server is not ready to handle the request."
    }

    def __init__(self,year,month,day,priceclass):
        if int(year) in range(1980,2401):
            self.year = year
        else:
            print("Error year between 1980 - today")
            exit(-1)
            
        if month in "01,02,03,04,05,06,07,08,09,10,11,12":
            self.month = month
        else:
            print("Error month between 01 - 12")
            exit(-1)

        if int(day) in range(1,32):
            self.day = day
        else:
            print("Error day between 01 - 31")
            exit(-1)
        if priceclass in "SE1,SE2,SE3,SE4":
            self.priceclass = priceclass
        else:
            print("Error priceclass in SE1,SE2,SE3 or SE4")
            exit(-1)

    def help(self):
        print("""
        GetSeTimePrice (C) 2023 Anders Persson
        Using https://www.elprisetjustnu.se/elpris-api
        
        SE1 = Luleå / Norra Sverige
        SE2 = Sundsvall / Norra Mellansverige
        SE3 = Stockholm / Södra Mellansverige
        SE4 = Malmö / Södra Sverige
 
        When init the class, set year, month, day, area
        Example

        price = GetSeTimePrice("2023","05","02","SE3")
        price.process_and_print()
        """)
 
    def get_error_message(self,code):
        if code in self.status_code:
            return self.status_code[code]
        return ""

    def make_url(self):
        self.url = f"https://www.elprisetjustnu.se/api/v1/prices/{self.year}/{self.month}-{self.day}_{self.priceclass}.json"

    def get_response(self):
        """ get url respose ok(200) || Error +  exit"""
        response = requests.get(self.url) 
        if(response.status_code != 200):
            print(f"Error {response.status_code} {self.get_error_message(response.status_code)}")
            exit(-1)
        self.response = response

    def print_result(self):
        """ Print Result """
        data = self.response.json()
        print("-" * 20)
        print(f"{self.year}-{self.month}-{self.day} {self.priceclass}")
        print("-" * 20)

        for d in data:
          start = datetime.fromisoformat(d["time_start"]).hour
          pris = d["SEK_per_kWh"]
          print(f"{start:2} = {pris:.2f} kr / kWh")

    def process_and_print(self):
        self.make_url()
        self.get_response()
        self.print_result()
    
# main part here
price = GetSeTimePrice("2023","05","02","SE3")
price.help()
price.process_and_print()


