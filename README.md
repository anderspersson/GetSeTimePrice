# GetSeTimePrice
GetSeTimePrice Get price for electricity in Sweden in day and hour

# Prerequisite
pip install requests

# Information
  GetSeTimePrice (C) 2023 Anders Persson
  __Tax and other fee is included read more about the API at__
  Using https://www.elprisetjustnu.se/elpris-api
        
## Areacodes
  SE1 = Luleå / Norra Sverige
  SE2 = Sundsvall / Norra Mellansverige
  SE3 = Stockholm / Södra Mellansverige
  SE4 = Malmö / Södra Sverige
 
# Use
When init the class, set year, month, day, area

# Example
price = GetSeTimePrice("2023","05","02","SE3")
price.process_and_print()

