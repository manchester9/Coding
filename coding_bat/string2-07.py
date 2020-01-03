# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:39:18 2019
"""

#########################
## String 2 ##############
#########################
"S7.1" ["""How is return different?"""]
#Given a string, return a string where for every char in the original, there are two chars.
#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'

#def double_char(str):
#    for elm in str:
#        return elm*2
#    for i in range(len(str)):
#        print(str[i]*2, end = '')

def double_char(str):
	char = ""
	for ch in str:
		char = char + (ch*2)
	return char

double_char('Height-Rose')

"S7.2"
#Return the number of times that the string "code" appears anywhere in the given string, 
#except we'll accept any letter for the 'd', so "cope" and "cooe" count.
#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2
def count_code(str):
    if 'code' in str:
        return 
    
def count_code(str):
	count = 0
	for i in range(len(str)):
		'''if str[i:i+2] == 'co':
			if str[i+3:i+4] == 'e':
				count += 1'''
		if str[i:i+2] == 'co' and str[i+3:i+4] == 'e':
			count += 1
	return count

count_code('cozexxcope') 

"S7.3"
#Return the number of times that the string "hi" appears anywhere in the given string.
#count_hi('abc hi ho') → 1
#count_hi('ABChi hi') → 2
#count_hi('hihi') → 2
def count_hi(str):
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == 'hi':
      count += 1
  return count

print(
count_hi('abc hi ho'),
count_hi('ABChi hi'),
count_hi('hihi')
)


"S7.4"
#Given two strings, return True if either of the strings appears at the very end of the other 
#string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
#Note: s.lower() returns the lowercase version of a string.
#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True
#end_other('abc', 'abXabc') → True
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return (b.endswith(a) or a.endswith(b))
#   return a[-(len(b)):] == b or a == b[-(len(a)):] 

print(
end_other('Hiabc', 'abc'),
end_other('AbC', 'HiaBc'),
end_other('abc', 'abXabc')
)


"S7.5"
#Return True if the string "cat" and "dog" appear the same number of times in the given string.
#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True
def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for i in range(len(str)-2):
    if str[i:i+3] == 'dog':
      count_dog += 1
    if str[i:i+3] == 'cat':
      count_cat += 1
   
  return count_cat == count_dog

print(
cat_dog('catdog'),
cat_dog('catcat'),
cat_dog('1cat1cadodog')
)


"S7.6"
#Return True if the given string contains an appearance of "xyz" where the xyz is not directly 
#preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
#xyz_there('abcxyz') → True
#xyz_there('abc.xyz') → False
#xyz_there('xyz.abc') → True

def xyz_there(str):
  for i in range(len(str)):
    if str[i] != '.' and str[i+1:i+4] == 'xyz':
      return True
  if str[0:3] == 'xyz':
    return True
  return False

print(
xyz_there('abcxyz'),
xyz_there('abc.xyz'),
xyz_there('xyz.abc')
)