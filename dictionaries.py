"""my_variable = {
    "key1": value1,
    "key2: value2,
    ...
}
"""

# Creating a dictionary
student = {
    "name": "John",
    "age": 68,
    "major": "Computer Science"
}
print(student)

new_student = {
    "name": "Pam",
    "age": 31,
    "name": "Angela" # if you use the same key twice, the last value will overwrite the previous one.
}

print(new_student)

# Accessing items
print(student["name"]) # accessing by key
print(student["age"])
print(student["major"])

# Adding new items
student["graduation_year"] = 2025
print(student)

# Changing values
student["age"] = 20
print(student)

# Removing items
student.pop("major") # Removes by key
print(student)

del student["name"] # Removes specific key
print(student)

print(len(student)) # Number of key-value pairs

# Clearing dictionaries
student.clear()
print(student)

students_group = {
    "student_one":{
        "name": "bruce",
        "age": 20
    },
    "student_two": {
        "name": "peter",
        "age": 89
    }
}
print(students_group)
print(students_group["student_one"]["name"])
print(students_group["student_two"]["name"])

"""

--------------------------------------------
Mini-Challenge: Song Metadata
--------------------------------------------
Create a dictionary called song with keys: "title", "artist", "duration".
Print the "title" value.
Add a new key "album".
Update "duration" to a new value.
Remove "album".
Print the dictionary length.

Add a print after every step
"""

song= {
    "title": "Bodies",
    "artist": "StaticX",
    "duration": 5
    
}
print(song["title"])
song["album"] = "Wisconsin Death Trip"
print(song)

song["duration"] = 6
print(song)

song.pop("album")
print(song)
print(len(song))

# -------- Assignment #2 --------