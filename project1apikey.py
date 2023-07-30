import requests
def kelvin_to_celsius_convertor (temp):
    data=temp-273.15    #response get in kelvin to convert celsius 
    fn="{:.2f}".format(data)
    return fn
def ftech_weatherdata_using_apikey():
    api_key = "94f636d1fdc1a2f551f9e94613cb3767"
    print("----------------------------------------------------------")
    cityName=input("Please enter valid city Name:")
    params={'q':cityName,'appid':api_key}
    url='http://api.openweathermap.org/data/2.5/weather'
    weatherdata= requests.get(url,params=params)
#print(weatherdata)
    if (weatherdata.status_code==200):
        temp=weatherdata.json()
        temprature=temp["main"]["temp"]
        print("Result :-")
        print("          The temprature of city",cityName,"is",kelvin_to_celsius_convertor(temprature),"°C")  
        print("-----------------------------------------------------------------")
   
    else:
        print("Server error!",weatherdata.status_code)


ftech_weatherdata_using_apikey()
         
    
           
    
    
    
           


 




  