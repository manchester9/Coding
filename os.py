# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:24:57 2018

@author: roland.ferrao
"""

#OS module - modify environment variable and move files around
import os
import datetime

print(dir(os)) # Attributes and methods within module

print(os.getcwd())
print(os.chdir('C:\\Users\\Roland.Ferrao\\Desktop\\'))
print(os.listdir())

'OS-Demo-2'
print(os.mkdir('OS-Demo-2'))
print(os.makekdirs('OS-Demo-2\\Sub-dir-1')) # Creating a sub-directory

print(os.rmdir('OS-Demo-2'))
print(os.removedirs('OS-demo-2'))


#Rename
os.rename('test.txt', 'demo.txt')

#Information on file
print(os.stat('demo.txt').st_size)
print(os.stat('demo.txt').st_mtime)
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


# Traversing directories - builds a three value tuple path - directories within path and files within path
for dirpath, dirname, filenames in os.walk('C:\\Users\\Roland.Ferrao\\Desktop\\'):
    print(dirpath)
    print(dirname)
    print(filenames)
    
#Joining files with the join method
print(os.environ.get('PATH'))
print(os.getenv())
'text.txt'

file_path = os.environ.get('PATH') + 'test.txt'
print(file_path)

print(os.path.join(os.environ.get('PATH'), 'test.txt'))

with open(file_path) as f:
    f.write()
    
print(os.path.basename('/tmp/test.txt')) #join, basename, dirname, split, exists, isdir, isfile, & splitext
print(dir(os.path))

# Reading and writing to files - file object - read, write, append, r+
f = open('test.txt' , 'r')
print(f.name)
print(f.mode)
f.close()


#Context manager - helps work with files within the block and closes automatically | Reading file contents - read, readline, readlines
with open('test.txt' , 'r') as f:
    for line in f:                # One line at a time so not a memory issue
        print(line, end = '')
        
    f_contents = f.readline()    
    print(f_contents, end = '')

print(f.read(100)) # I/O operation on a closed file - first 100 characters


# Reading large files
with open('test.txt' , 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    
    while len(f_contents) > 0:
        print(f_contents, end = '*')
        f_contents = f.read(size_to_read) 
        
    f.seek(0) # Sets position back to the begining of the file
    
# Working with multiple files
with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
            
            
            
# read and write bytes instead of text
with open('test.png', 'rb') as rf:
    with open('test_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
            
                
# Read files in chunk size
with open('test.png', 'rb') as rf:
    with open('test_copy.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    







































