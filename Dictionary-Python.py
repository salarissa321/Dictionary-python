


#----------------------
#----Dictionary----
#----------------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are contains Key : Value
# [3] Dict Key Neet to Be Immutable => (String, Number, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is not Ordered You Access Its Element With Key
#-----------------------

# Ditionary 

user = {
    "name" : "Salar", 
    "age" : 36,
    "Country" : "Deutschalnd",
    # [1,2,3,4]: "Test" # TypeError: unhashable type: 'list'
    "Skills" : ["Html" , "Css" , "Js"] , 
    "rating" : 1.542, 
    "name" : "Issa" # {'name': 'Issa', 'age': 36, 'Counrty': 'Deutschalnd', 'Skills': ['Html', 'Css', 'Js'], 'rating': 1.542}
}


print(user) # {'name': 'Salar', 'age': 36, 'Counrty': 'Deutschalnd', 'Skills': ['Html', 'Css', 'Js'], 'rating': 1.542}
print(user["Country"]) # Deutschalnd
print(user.get("Country")) # Deutschalnd
print(user.keys()) # dict_keys(['name', 'age', 'Country', 'Skills', 'rating'])
print(user.values()) # dict_values(['Issa', 36, 'Deutschalnd', ['Html', 'Css', 'Js'], 1.542])


print("-" * 40) # ----------------------------------------


# Two Dimensional Dictionary


languages = {
    "one" : {
    "name" : "html" ,
    "progress" : "80%"
    },

    "two" :{
    "name" : "Css" ,
    "progress" : "90%"

    },
     "three" :{
    "name" : "Js" ,
    "progress": "90%"
     }
}

print(languages) # {'one': {'name': 'html', 'progress': '80%'}, 'two': {'name': 'Css', 'progress': '90%'}, 'three': {'name': 'Js', 'progress': '90%'}}
print(languages["one"]) # {'name': 'html', 'progress': '80%'}
print(languages["three"]) # {'name': 'Js', 'progress': '90%'}
print(languages["three"] ["name"]) # Js
print(languages["three"] ["progress"]) # 90%


# Ditionary Length


print(len(languages)) # 3
print(len(languages["two"])) # 2




# Create Dictionary for Variables

frameworkOne = {
    "name" : "Vujes" , 
    "progress" : "80%"

}

frameworkTwo = {
    "name" : "React" ,
    "progress" : "80%"
}

frameworkThree = {
    "name" : "Angular" ,
    "progress" : "80%"
}

allFramework = {
    "one" : frameworkOne,
    "two" : frameworkTwo ,
    "three" : frameworkThree 
}

print(allFramework) #{'one': {'name': 'Vujes', 'progress': '80%'}, 'two': {'name': 'React', 'progress': '80%'}, 'three': {'name': 'Angular', 'progress': '80%'}}


