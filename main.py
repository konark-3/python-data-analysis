import pandas
import csv

with open("weather_data.csv") as file:
    weather_data = csv.reader(file)

    next(weather_data)

    temp_list = []

    for data in weather_data:
        temp = data[1]
        temp_int = int(temp)
        temp_list.append(temp_int)

    print(temp_list)

data = pandas.read_csv('weather_data.csv')

temp = data['temp']

dict_data = data.to_dict()
list_temp = temp.to_list()


print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']

celsius = monday.temp

fahrenheit = (celsius*1.8)+32

print(celsius)

print(fahrenheit)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240620.csv")

gray = data[data["Primary Fur Color"] == 'Gray']
cinnamon = data[data["Primary Fur Color"] == 'Cinnamon']
black = data[data["Primary Fur Color"] == 'Black']

gray_count = gray["Primary Fur Color"].count()
cinnamon_count = cinnamon["Primary Fur Color"].count()
black_count = black["Primary Fur Color"].count()

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray_count, cinnamon_count, black_count]
}

new_data = pandas.DataFrame(data_dict)

print(new_data)

new_data.to_csv("NewData.csv")
