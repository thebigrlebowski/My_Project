import requests
import sys

def start():
    user_selection = input("\nPress 1 to search by zip code or 2 to search by city name: ")

    if user_selection == str(1):
        selection1()
    elif user_selection == str(2):
        selection2()
    else:
        print("ERROR: Invalid Selection")
        restart()


def restart():
    restart = input("\nPress Y to restart or any other button to exit: ").lower()
    if restart == 'y':
        start()
    else:
        print("\nGoodbye\n")
        sys.exit()


def selection1():
    zip_code = input("Please enter Zip Code: ")

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code}&units=imperial&appid=e8d2ba9706d1d0532b51670a8f124e05")
    
    weather = response.json()

    try:
        wx_data(weather)
    except:
        print("ERROR: Zip code is not valid.")   
        restart() 

    
def selection2():
    city_name = input("Please enter city name: ")        

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=imperial&appid=e8d2ba9706d1d0532b51670a8f124e05")

    weather = response.json()
    
    try:
        wx_data(weather)
    except:
        print("ERROR: City name is not valid.")   
        restart() 


def wx_data(weather):
    location = weather['name']
    temp = weather['main']['temp']
    hightemp = weather['main']['temp_max']
    lowtemp = weather['main']['temp_min']
    wind_speed = weather['wind']['speed']
    pressure = weather['main']['pressure']
    latitude = weather['coord']['lat']
    longitude = weather['coord']['lon']
    humidity = weather['main']['humidity']
    description = weather['weather'][0]['description']

    print(f'\nThe current forecast for {location} is:')
    print(f'Current Temperature : {temp} degree fahrenheit')
    print(f'High Temperature : {hightemp} degree fahrenheit')
    print(f'Low Temperature : {lowtemp} degree fahrenheit')
    print(f'Wind Speed : {wind_speed} mph')
    print(f'Pressure : {pressure} hPa')
    print(f'Latitude : {latitude}')
    print(f'Longitude : {longitude}')
    print(f'Humidity : {humidity}%')
    print(f'Description : {description}')
    

print("\nWelcome to my forecast tool!")

start()

while True:
    restart()