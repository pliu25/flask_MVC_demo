import json
import os

class Fruit_Model:
    def __init__(self, DB_location):
        self.DB_location =  DB_location
        with open(DB_location, 'r') as file:
            self.data = json.load(file) #in-memory view of data (ie. RAM, temporary)

    def create_fruit(self, newFruit):
        print(f"DB request to create {newFruit}")
        self.data[newFruit["name"]] = newFruit["url"]

        #don't forget to write th echange to disk
        json_object = json.dumps(self.data, indent=4)
        with open(self.DB_location, "w") as outfile:
            outfile.write(json_object)
        
        return newFruit
    
    def get_all_fruit(self):
        print(f"DB request for all fruit")
        return self.data

    def get_single_fruit(self, fruit_name):
        print(f"DB request for fruit: {fruit_name}")
        if self.data[fruit_name]:
            return self.data[fruit_name]
        else:
            return {}