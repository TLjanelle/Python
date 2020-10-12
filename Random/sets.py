#sets cannot have duplicates
s = set({1,2,3,4,5,5,5})

#creating a new set
s = set({1,4,5})

#creates a set with the same values as above
s = {1,4,5}

4 in s #True

8 in s #false

#Accessing All Values in a set
numbers = {1,2,3,4}

for number in numbers:
    print(number) #1 #2 #3 #4

#Common Use: cities, 
cities = ["Los Angeles", "Boulder", "Kyoto", "Florence", "Santiago", "Los Angeles", "Shanghai"]
print(list(set(cities))

#.add().....Adds an element to a set unless the element is already in the set
s = set([1,2,3])

s.add(4)

s #{1,2,3,4,}

#doesn't work second time

s.add(4)

s #{1,2,3,4}

#.remove()....removes a value form the set - returns a KeyError if the value is not found

set1 = {1,2,3,4,5,6,}

set1.remove(3)

print(set1) #{1,2,4,5,6}

#if you need to avoid KeyErrors use .discard()

#.copy()....makes a copy of the set just like lists

#.clear()...deletes everything

#Set Math.....intersection, symmetric_difference, union Ex:

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

#To generate a set with all unique students
math_students | biology_students

#To generate a set with students in both course
math_students & biology_students

#Set Comprehension
{x**2 for x in range(10)} #{0,1,64,4,36,9,16,49,81,25}

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5