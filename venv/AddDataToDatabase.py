
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : ""
})

ref = db.reference('Students')

data = {
    "100519733061":
        {
            "name": "Mir Mayasir",
            "branch": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "class1": 0,
            "class2": 0,
            "class3": 0,
            "c":1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "100519733045":
        {
            "name": "Ayush Raina",
            "branch": "CSE",
            "starting_year": 2019,
            "total_attendance": 0,
            "standing": "B",
            "year": 4,
            "class1": 0,
            "class2": 0,
            "class3": 0,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "111111111111":
        {
            "name": "Dr Shayamla",
            "branch": "HOD CSE DEPT",
            "starting_year": 2020,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "class1": 0,
            "class2": 0,
            "class3": 0,
            "c": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)