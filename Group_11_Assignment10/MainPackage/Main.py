# main.py
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
from FunctionsPackage.Functions import *

if __name__ == "__main__": 
    
    response = requests.get('https://swapi.dev/api/people/1/')
    #Person #1 is Luke Skywalker
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    #   loads the data
    
    print("These are the ships Luke Skywalker used in Star Wars: ")
    for starship_url in parsed_json['starships']:
        starship_info = get_starship_info(starship_url)
        if starship_info:
            print("Name:", starship_info['name'])
            print("Model:", starship_info['model'])
            print("Manufacturer:", starship_info['manufacturer'])
            #to add a line between ships, extra line is printed
            print() 
        