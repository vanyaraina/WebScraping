import pandas as pd

#list
# weather_data = { 
#     'date' : ['1 March 2024', '2 March 2024','3 March 2024','4 March 2024',],
#     'temperature' : [25, 24, 26, '21'],
#     'windspeed' : [6,7,8,9],
#     'event' : ['rain', 'sun', 'windy', 'rain']
# }

# df= pd.DataFrame(weather_data)
# print(df)

# df.to_csv('weather.csv', index = True, index_label = "id")



#tupple
# weather_data={
#     ('1/3/24', 32, 6, 'rain'),
#     ('2/3/24', 32, 7, 'sun'),
#     ('3/3/24', 32,8, 'rain'),
# }

# df = pd.DataFrame(data = weather_data, columns=['day', 'temp', 'wind', 'event'])
# print(df)


#listtodictionaries

weather_data = [
    {'day': '1/2/24', 'temp': 32, 'wind': 7, 'event':'rain'},
    {'day': '2/2/24', 'temp': 22, 'wind': 7, 'event':'sunny'},
    {'day': '3/2/24', 'temp': 35, 'wind': 8, 'event':'rain'},
]


df = pd.DataFrame(data = weather_data, columns=['day', 'temp', 'wind', 'event'])
print(df)