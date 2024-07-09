# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
tem_list = data["temp"]
total = 0
for temperature in tem_list:
    total+= temperature
print(f"average temperature : {round(total/ len(tem_list))}")
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
temp_c = monday.temp[0]
temp_c = temp_c * 9/5 + 32
print(temp_c)