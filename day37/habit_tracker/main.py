"""
USAGE - The code is using the requests library to interact with the Pixela API, 
        which is a service for tracking various data over time. The code defines 
        six functions that allow a user to create a new account, create a new 
        graph to track a certain type of data, add data points (called pixels) 
        to the graph, and delete the graph if desired. The code uses the requests.post() 
        and requests.delete() methods to send HTTP requests to the Pixela API, 
        passing in the necessary parameters to create, modify, or delete the 
        specified user account and graph.

AUTHOR - https://github.com/Ahendrix9624/
"""

import requests
import os
from datetime import datetime

USERNAME = "drewman"
TOKEN = os.environ.get("PIXELA_API_KEY")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph2"

headers = {
        "X-USER-TOKEN": TOKEN
}

###################### Create User ##########################
def create_user():

    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)
    
# create_user()

###################### Create Graph ##########################
def create_graph():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

    graph_config = {
        "id": GRAPH_ID,
        "name": "Pill Tracker",
        "unit": "Pill's taken",
        "type": "int",
        "color": "ajisai"
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

# create_graph()

###################### Delete Graphs ##########################
def delete_graphs():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

    response = requests.delete(url=graph_endpoint, headers=headers)
    print(response.text)

# delete_graphs()

###################### Add Pixels ##########################
def add_pixels():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

    today = datetime.now()
    graph_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "1" # Can add an input to be prompted in the terminal
    }

    response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)

# add_pixels()

###################### Update Pixels ##########################
def update_pixels():
    #Change today variable to the date you want to update
    # today = datetime(year=2023, month=3, day=22)
    today = datetime.now()
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    today = datetime.now()
    graph_params = {
        "quantity": input("How many Pill's have you taken today? ")
    }
    response = requests.put(url=graph_endpoint, json=graph_params, headers=headers)
    print(response.text)

update_pixels()

###################### Delete Pixels ##########################
def delete_pixels():
    #Change today variable to the date you want to update
    today = datetime(year=2023, month=3, day=21)
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
    
    response = requests.delete(url=graph_endpoint, headers=headers)
    print(response.text)

# delete_pixels()