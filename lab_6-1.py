"""
Create a Python file named lab_6-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***


Create a array that contains the numbers 1 to 5 store it as a variable called my_arr.
Write a statement using the indexing operator that prints the number 3 in my_arr.
Write a statement that prints the length of my_arr.
Write a statement that repeats my_arr 3 times.
Write a statement that converts "string" to an array.


"""
# Author: Nicholas Yepes 11/7/23

#a array that contains number 1-5 and it is stored as my_arr.
my_arr = [1, 2, 3, 4, 5]

# '3' will be printed because the array's third element has an index of 2.
print(my_arr[2])  

#This will output the array's length, which is 5.
print(len(my_arr))  

#this will print [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
my_arr_repeated = my_arr * 3
print(my_arr_repeated) 

# This will print the array ['s', 't', 'r', 'i', 'n', 'g'].
string_to_array = list("string")
print(string_to_array)  
