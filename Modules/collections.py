# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 09:32:26 2018

"""
#named tuple - readable and elegant
#default dict - nested data dict 
#counter - find common thing
#deque - improve performance

from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve
import os
import pandas as pd

user= ('roland', 'coder')
f'{user[0]} is a {user[1]}'

# Named tuple
User = namedtuple('User', 'name role')

user = User(name = 'Roland', role = 'Coder')
print(user.name)
print(user.role)

print(f'{user.name} is a {user.role}')

# Defaultdict holds lists 
users = {'bob' : 'coder'}
users['bob']
users['julian'] # Keyerror
users.get('bob')

challenges_done = [('mike', 20), ('julian',30), ('bob', 50),
                   ('mike', 21), ('julian',3), ('bob', 8)] 

print(challenges_done)

#Using a dictionary
challenges = {}
for name, challenge in challenges_done:
    challenges[name].append(challenge)

#Using defaultdicts
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
challenges

words = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

""".split()
words[:5]

common_words = {}
for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] +=1
    
for k, v in sorted(common_words.items(),
                   key = lambda x:x[1], 
                   reverse = True)[:5]:
    print(k, v)
    
# As compared to counter    
Counter(words).most_common(4)    

# Deques and moving things around - Better performance than lists
lst = list(range(1000000))
deq = deque(range(1000000))

def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)
        
#%timeit insert_and_delete(lst)
    
        














































#base_folder = os.path.dirname(__file__)
#test = os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')
#
#read_file = pd.read_table(test)
