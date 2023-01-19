from django.shortcuts import render
import json
import urllib.request

def kelvin_to_celcius(kelvin_string):
    kelvin = float(kelvin_string)
    celcius = kelvin - 273.15
    return str(celcius)

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=785dc38ec650d4e116bc3e70bcd2ee02').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": kelvin_to_celcius(str(json_data['main']['temp']))+' degree celcius',
            "pressure": str(json_data['main']['pressure']),
            "humidity":str(json_data['main']['humidity']), 
        }

    else:
        city = ''
        data = {}
    return render(request,'index.html',{'city':city,'data':data})


# Create your views here.
