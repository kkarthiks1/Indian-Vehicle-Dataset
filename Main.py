# install latest labelbox version (3.0 or above)
#pip3 install labelbox[data]

import labelbox
import pandas as pd

# Labelbox API key
LB_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJjanMwMGF2Nm04eTNhMGIyOTVqcTg3N3JwIiwib3JnYW5pemF0aW9uSWQiOiJjanMwMGF2NjU0a3liMGE2MnJlazk3a3Y3IiwiYXBpS2V5SWQiOiJjbDRhMXRlbzM3Ym02MDg3c2Y1Z3kwNXJzIiwic2VjcmV0IjoiOGM0MDJiN2M0N2RmMTdhM2FmZDZiNjRjZjU5NTg4ZTciLCJpYXQiOjE2NTQ5NjIyODgsImV4cCI6MjI4NjExNDI4OH0.QLnIYJavrsWMMnxNCAm5FMLzoe6CbAkZg1T32W9_SJY"

# Creation of Labelbox client
lb = labelbox.Client(api_key=LB_API_KEY)

# The project ID
project = lb.get_project('cl42s0e4904c5072k76lm3xd8')

#Read the JSON file (From Data Folder)
data=pd.read_json("/data/data.json")

#Display Heads
data.info()

# Iterating through the json
# list - To display the Raw images link
for i in data['Labeled Data']:
    print(i)

# Iterating through the json
# list - The Anotated images link
for i in data['Label']:
    print(i)

import json