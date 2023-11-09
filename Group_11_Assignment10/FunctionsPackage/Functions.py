# functions.py
# Name: Dylan Moore/ Max Smith
# email: moore4dl@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/8/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: use an API and connect to it via the web 
# Citations: Stack Overflow

import json
import requests #web requests

def get_starship_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        starship_data = json.loads(response.content)
        return starship_data
    else:
        return None