import json
students ={
    "226070":{
        "gender": "male",
        "name": "Mark",
        "age": "18"
    },
    "226071":{
        "gender": "male",
        "name": "john",
        "age": "20"
    }
}

file = open("student13.json","w")

json.dump(students,file,indent=6)