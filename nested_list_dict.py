# nested dictionary : dictionary within another dictionary.
'''Syntax : data = {
                     key1 : {dict},
                     key2 : {dict},
                     key3 : [list]
                     }'''
'''student_data = {
    "Ram":{"roll_no":10,"age":12,"course":"java"},
    "Syam":{"roll_no":11,"age":13,"course":"c++"},
}
print(student_data)
print(student_data["Ram"])
print(student_data["Ram"]["age"])
student_data["Ram"]["phone_no"] =123434
print(student_data["Ram"])
print()
#delete the phone_no of ram. if you want to delete the data from dict then use "del" and if you want to return deleted data
                             # dict then use "pop()" function
#del student_data["Ram"]["phone_no"]
print(student_data["Ram"].pop("phone_no"))'''
print()

# NESTING A LIST INTO A DICTIONARY
'''travel_data = {
    "Gujrat":["Dwarika","Somnath","Statue of Liberty"],
    "Rajasthan":["Jaipur","Udaipur","Jaisalmer"]
}
print(travel_data)
for place in travel_data:
    print(place)
    print(travel_data[place])
    print(travel_data[place][-1])'''
print()

#NESTING OF DICTIONARY IN LIST OF DICTIONARY
'''student_data = [
    {"Name":"Ram",
     "roll_no":10,
     "age":12,
     "course":"java"
     },
    {"Name":"Syam",
     "roll_no":11,
     "age":13,
     "course":"c++"}
]
print(student_data)
print(student_data[0])
print(student_data[1])
student_data[0]["phone_no"] =1233423
print(student_data[0])
print(student_data[0]["phone_no"])'''
print()

# EXERCISE BSD ON DICT add a dict into list
student_data = [
    {"Name":"Ram",
     "roll_no":10,
     "age":12,
     "course":"java"
     },
    {"Name":"Syam",
     "roll_no":11,
     "age":13,
     "course":"c++"}
]
def add_new_student(name,rollno,course):
    new_student = {}
    new_student["Name"] =name
    new_student['roll_no']  = rollno
    new_student["course"]= course
    student_data.append(new_student)
add_new_student("Aniket",26,"ME")
print(student_data)