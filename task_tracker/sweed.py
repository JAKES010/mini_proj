import sys 
import os
import json

if len(sys.argv) < 3 :
    sys.exit()

default_data = {"tasks" : []}
filename = "tsk_file.json"

if len(sys.argv) < 3 : 
    sys.exit("Too Few Arguments")

p_command = sys.argv[1]
tasks = sys.argv[2]

if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    with open(filename,"w") as file :
        json.dump(default_data,file)

data = {}
note = 0

if p_command == "Add" :
    with open(filename,"r") as file :
        data = json.load(file)

        for item in  data["tasks"] :
            if item["id"] > note:
                note = item["id"]
                print(note)

        info = {"id" : 1 , "description" : tasks}
        data["tasks"].append(info)
        with open(filename, "w") as file:
            json.dump(data,file)

        print(f"ADDED: {info}")