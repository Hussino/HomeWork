# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 12:15:35 2023

@author: pc
"""


# Hussein Ali Al-Shami - 21_16_0112

word = "book"

attempt = []
counter =0
for i in range(4):
        while counter != 3:
            temp = input("Enter letter!\n")
            if temp == word[i]:
                attempt.append(temp)
                print("Letter number "+str(i+1)+" is correct! Next Letter!\n")
                break
            else:
                print("Wrong answer! try again!\n")
                counter +=1
        if counter == 3:
            print("Better luck next time!\n")
            break
        
    