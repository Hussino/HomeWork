# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:54:23 2023

@author: pc
"""

# Hussein Ali Al-Shami - 21_16_0112

from random import randint

class contact:
    def __init__(self, name, number, email):
        self.ID = randint(1,1000)
        self.name = name
        self.number = number
        self.email = email
        
Contacts = []
contact1 = contact("Hussein" ,"777777777", "hussienalshami@gmail.com")
Contacts.append(contact1)
    
def AddContact():
    name = input("Type the name of the contact!\n")
    number = input("Type the phone number of the contact!\n")
    email = input("Type the email address of the contact!\n")
    contactAdd = contact(name, number, email)
    
    for i in range(len(Contacts)):
        if Contacts[i].email == email:
            print("Email is already in use!\n")
            return 0
        else:
            Contacts.append(contactAdd)
            print("Contact Added!\n")
            return 0

def ViewContacts():
    for i in range(len(Contacts)):
        print("Contact " + str((i+1)) + "\n")
        print("Name: " + Contacts[i].name + "  ")
        print("Number: " + Contacts[i].number + "  ")
        print("Email: " + Contacts[i].email + "  \n")

def DeleteContact():
    email = input("Enter the name of the contact you want to delete\n")
    for i in range(len(Contacts)):
        if email == Contacts[i].email:
            Contacts.pop(i)
            print("Contact Deleted.\n")
            return 0
    print("Contact not found!\n")
            


            
ViewContacts()

AddContact()

ViewContacts()

DeleteContact()

ViewContacts()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
