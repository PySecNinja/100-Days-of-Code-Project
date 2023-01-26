import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()

print(data["temp"].mean())
print(data["temp"].max())

# Get Data in columns  
print(data["condition"])       #This is kind of like using a python dictionary
print(data.condition)          #This is like using object oriented programming

# Get data in the rows
print(data[data.day == "Monday"])
print((data[data.temp == data.temp.max()]))  

# Create dataframe from scratch 
data_dict = {
    "students": ["Ana", "James", "Drew"],
    "scores": [76, 56,65]
}

dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("new_data.csv")
print(dataframe)