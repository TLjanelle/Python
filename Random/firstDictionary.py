#Example
instructor = {
    "name": "Colt",
    "owns_dog" : True,
    "num_course" : 4,
    "favorite_language" : "Python",
    "is_hilrious" : False,
    44 : "my favorite number!"
}

#Another Way
another_dictionary = dict(key = 'value')
another_dictionary # { 'key':'value' }

#Access Indvidual Values
instructor["name"] #Colt
instructor["thing"] #KeyError

#Access All Values in a Dictionary
    #variable.values()......prints all values ex: "colt"
    for value in instructor.values():
        print(value) 
    
    #variable.keys()......prints all keys ex: "name"
    for key in instructor.keys():
        print(key)

    #variable.items().......prints key and value ex: name "colt"
    for key, value in instructor.items():
        print(key,value)

#Additional Methods
    #variable.clear()....clears all keys and values

    #variable.copy().....makes a copy of a dictionary
    d = dict(a=1,b=2,c=3)
    c = d.copy()
    c # {'a':1,'b':2,'c':3}
    c is d #false

    #{}.fromkeys.....creates key-value pairs from comma sperated values
    {}.fromkeys("a", "b" # {'a':'b'}
    {}.fromkeys(["email"], 'unknown') # {'email':'unknown'}
    {}.fromkeys("a", [1,2,3,4,5,]) # {'a': 1,2,3,4,5}

    #variable.get().....retrieves a key in an object and
    # return None instead of a KeyError if the key does 
    # not exist`

    #variable.pop()...takes a single arugment corresponding 
    #to a key and removes that key-value pair from the 
    # dictionary. Returns the value corresponding to the 
    # key that was removed
    d = dict(a=1,b=2,c=3)
    d.pop() #TypeError:pop expected at least 1 arguments, got 0
    d.pop('a') #1
    d # {'c':3, 'b':2}
    d.pop('e') #KeyError

    #variable.popitem().....will remove something at random

    #variable.update()...update keys and values in a 
    # dicitonary with another set of key value pairs
    first = dict(a=1,b=2,c=3,d=4,e=5)
    second = {}

    second.update(first)
    second #{'a':1,'b':2,'c':3,'d':4,'e':5}

        #let's overwrite an existing key
        Second{'a'} = "AMAZING"

        # if we update again
        second.update(first) #{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

        #the update overrides our values
        second #{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

