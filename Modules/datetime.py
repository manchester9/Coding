# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:20:06 2018

"""

from datetime import datetime
from datetime import date
from datetime import timedelta

today = datetime.today()
type(today)
today_date = date.today()
type(today_date)

today_date.month
today_date.day
today_date.year

t = timedelta(days = 4, hours = 10)
print(t.days)
print(t.seconds/60/60)

eta = timedelta(hours = 6)
today = datetime.today()

print(str(today + eta))

# Creating an application
import sys
import time
import datetime

print("Time in seconds since the epoch: %s" %time.time())
print("Current date and time: " , datetime.datetime.now())
print("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

print("Current year: ", datetime.date.today().strftime("%Y"))
print("Month of year: ", datetime.date.today().strftime("%B"))
print("Week number of the year: ", datetime.date.today().strftime("%W"))
print("Weekday of the week: ", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))



