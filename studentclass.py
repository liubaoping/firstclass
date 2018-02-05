# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:52:47 2018

@author: l
"""
students=[]
class Student:
    def __init__(self,name,student_id=322):
        self.name=name
        self.student_id=student_id
        students.append(self)
    
    def __str__(self):
        return "student: %s" %self.name
    
    def __repr__(self):
        return "I am %s" %self.name
    
    def captalize_title(self):
        return self.name.title()
        
        
jack=Student("jack",213)
students
print(jack)