# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:39:18 2019
"""
#########################
## Warmup 1 #############
######################### 
def array123(nums):
  for i in range(len(nums)-2):
    if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
      return True
  return False


"S1.1"
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True
    
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
 # This can be shortened to: return(not weekday or vacation)
    
sleep_in(False, False)


"S1.2"
#Given an int n, return the absolute difference between n and 21, except return double 
#the absolute difference if n is over 21.
#diff21(19) → 2
#diff21(10) → 11
#diff21(21) → 0

def diff21(n):
    if n<21:
        return abs(n-21)
    else:
        return abs(2*(n-21))
    
diff21(21)
    
    
"S1.3"
#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes 
#the absolute value of a number.
#near_hundred(93) → True
#near_hundred(90) → True
#near_hundred(89) → False        
    
def near_hundred(n):
#    if (n -10) <= 200 or (n + 10) >= 200:
#        return True
#    if (n -10) <= 100 or (n + 10) >= 100: 
#        return True
#    else:
#        False
 
  if (n >= 90) and (n <= 110):
    return True
  if (n >= 190) and (n <= 210):
    return True
  else:
    return False
    
near_hundred(89)
 
    
"S1.4"
#Given a non-empty string and an int n, return a new string where the char at 
#index n has been removed. The value of n will be a valid index of a char in the 
#original string (i.e. n will be in the range 0..len(str)-1 inclusive).
#missing_char('kitten', 1) → 'ktten'
#missing_char('kitten', 0) → 'itten'
#missing_char('kitten', 4) → 'kittn'
    
def missing_char(str, n):
#    return str.replace(n, "")
    return str[0:n] + str[n+1:len(str)+1] 

missing_char('kitten',4)
 
    
"S1.5"
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if 
#each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. 
#Return True if we are in trouble.
#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False   
#
    
def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile):
        return True
    if not (a_smile or b_smile):
        return True
    else:
        return False
    
monkey_trouble(True, False)


"S1.6"
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
#We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
#Return True if we are in trouble.
#parrot_trouble(True, 6) → True
#parrot_trouble(True, 7) → False
#parrot_trouble(False, 6) → False    
    
def parrot_trouble(talking,hour):
    if (hour < 7 or hour > 20) and talking:
        return True
    else:
        return False
    
parrot_trouble(True, 7)


"S1.7"     """ [How to account for the last condition?] """
#Given 2 int values, return True if one is negative and one is positive. 
#Except if the parameter "negative" is True, then return True only if both are negative.
#pos_neg(1, -1, False) → True
#pos_neg(-1, 1, False) → True
#pos_neg(-4, -5, True) → True    
def pos_neg(int1, int2, negative):
    if int1 == abs(int1) or int2 != abs(int2):   
        return True
    if int2 == abs(int2) or int1 != abs(int1):
        return True
    else: 
        False

pos_neg(-1,-1,False)

"S1.8"
#Given a string, return a new string where the first and last chars have been exchanged.
#front_back('code') → 'eodc'
#front_back('a') → 'a'
#front_back('ab') → 'ba'    
def front_back(str):
#    new_str = str[len(str)-1] == str[0] 
#    return new_str
    if len(str) > 1:
        return str[len(str)-1] + str[1:len(str)-1] + str[0]
    else:
        return str

front_back('Roland')
    
    
"S1.9" 
#Given two int values, return their sum. Unless the two values are the same, 
#then return double their sum.
#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8   
def sum_double(a,b):
    if a != b:
        return a + b
    if a == b:
        return 2* (a + b)

sum_double(2,2)


"S1.10"    
#Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.
#makes10(9, 10) → True
#makes10(9, 9) → False
#makes10(1, 9) → True    
def makes10(a,b):
    if (a == 10) or (b == 10) or (a+b == 10):
        return True
    else:
        return False
makes10(9,9)


"S1.11"
#Given a string, return a new string where "not " has been added to the front. However, 
#if the string already begins with "not", return the string unchanged.
#not_string('candy') → 'not candy'
#not_string('x') → 'not x'
#not_string('not bad') → 'not bad'    
def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    else:
        return "not " + str
    
not_string('Difficult')


"S1.12"
#Given a string, we'll say that the front is the first 3 chars of the string. 
#If the string length is less than 3, the front is whatever is there. Return a new string 
#which is 3 copies of the front.
#front3('Java') → 'JavJavJav'
#front3('Chocolate') → 'ChoChoCho'
#front3('abc') → 'abcabcabc'        
def front3(str):
    if len(str) <= 3:
        return str
    else:
        return str[0:3]*3

front3('abcd')














