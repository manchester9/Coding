# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 16:39:18 2019
"""

#########################
## String 1 #############
#########################
"S3.1"
#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
#hello_name('Bob') → 'Hello Bob!'
#hello_name('Alice') → 'Hello Alice!'
#hello_name('X') → 'Hello X!'
def hello_name(name):
    final = 'Hello ' + name + '!'
    return final

hello_name('Alice')

"S3.2"
#Given an "out" string length 4, such as "<<>>", and a word, return a new string where 
#the word is in the middle of the out string, e.g. "<<word>>".
#make_out_word('<<>>', 'Yay') → '<<Yay>>'
#make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
#make_out_word('[[]]', 'word') → '[[word]]'
def make_out_word(out, word):
	return out[:2] + word + out[2:]

print(
make_out_word('<<>>', 'Yay'),
make_out_word('<<>>', 'WooHoo'),
make_out_word('[[]]', 'word'))

"S3.3"
#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
#first_half('WooHoo') → 'Woo'
#first_half('HelloThere') → 'Hello'
#first_half('abcdef') → 'abc'
def first_half(str):
    # half = int(len(str)/2)
    # reduced = str[:int(len(str)/2)]
    # return reduced
    return str[:int(len(str)/2)]

first_half('HelloThere')


"S3.4"
#Given 2 strings, return their concatenation, except omit the first char of each. 
#The strings will be at least length 1.
#non_start('Hello', 'There') → 'ellohere'
#non_start('java', 'code') → 'avaode'
#non_start('shotl', 'java') → 'hotlava'








"S3.5"
#Given two strings, a and b, return the result of putting them together in 
#the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
#make_abba('Hi', 'Bye') → 'HiByeByeHi'
#make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
#make_abba('What', 'Up') → 'WhatUpUpWhat'






"S3.6"
#Given a string, return a new string made of 3 copies of the last 2 chars of the 
#original string. The string length will be at least 2.
#extra_end('Hello') → 'lololo'
#extra_end('ab') → 'ababab'
#extra_end('Hi') → 'HiHiHi'





"S3.7"
#Given a string, return a version without the first and last char, 
#so "Hello" yields "ell". The string length will be at least 2.
#without_end('Hello') → 'ell'
#without_end('java') → 'av'
#without_end('coding') → 'odin'


"S3.8"
#Given a string, return a "rotated left 2" version where the first 2 chars are 
#moved to the end. The string length will be at least 2.
#left2('Hello') → 'lloHe'
#left2('java') → 'vaja'
#left2('Hi') → 'Hi'


"S3.9"
#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
#In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag 
#and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
#make_tags('i', 'Yay') → '<i>Yay</i>'
#make_tags('i', 'Hello') → '<i>Hello</i>'
#make_tags('cite', 'Yay') → '<cite>Yay</cite>'



"S3.10"
#Given a string, return the string made of its first two chars, so the String 
#"Hello" yields "He". If the string is shorter than length 2, return whatever there is, 
#so "X" yields "X", and the empty string "" yields the empty string "".
#first_two('Hello') → 'He'
#first_two('abcdefg') → 'ab'
#first_two('ab') → 'ab'




"S3.11"
#Given 2 strings, a and b, return a string of the form short+long+short, with the 
#shorter string on the outside and the longer string on the inside. The strings will not be 
#the same length, but they may be empty (length 0).
#combo_string('Hello', 'hi') → 'hiHellohi'
#combo_string('hi', 'Hello') → 'hiHellohi'
#combo_string('aaa', 'b') → 'baaab'





















