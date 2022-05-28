from curses import ACS_GEQUAL
import traceback
from unicodedata import name


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score
        
    def change_name(cls, change_name, change_age, add_track, get_score):
        cls.change_name = change_name
        cls.change_age = change_age
        cls.add_track = add_track
        cls.get_score = get_score
    


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
