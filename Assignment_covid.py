#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Please answer the questions below with 'yes' or 'no'.")
age = input("Are you a cigarette addict older than 75 years old? :").strip()
chronic = input("Do you have a severe chronic disease? :").strip()
immune = input("Is your immune system too weak? :").strip()
if age == "yes" :
    print("You are in danger")
elif chronic == "yes" :
    print("You are in danger")
elif immune == "yes" :
    print("You are in danger")
else:
    print("You are not in risky group")

