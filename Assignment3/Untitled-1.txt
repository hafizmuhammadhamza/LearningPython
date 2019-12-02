   Assignment#4
 //Q#1 charging dofferent prizes
prompt = "How old are you?"
prompt +="\nEnter 'quit' when you are finished."

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    
    if age<3:
        print("your ticket is free!")
    elif age<13:
         print("your ticket is $10")
    else:
         print("your ticket is $15")

//Q#2 making dictionary
cities = {
  "karachi":{
      "country":"pakistan",
       "population":"190 million",
       "nearby area":"haidrabad",
       },  
  "Madina":{
        "country":"saudia",
        "population":"190 million",
         "nearby area":"Makkah",
       },  
   "islamabad":{
        "country":"pakistan",
         "population":"190 million",
         "nearby area":"pindi",
       } 
      }
for city_info in cities.items():
    country = city_info["country"].title()
    population = city_info["population"] 
    area = city_info["nearby area"].title()
    
    print("\n"+ city.title() +"is in" + country +"." )
    print("it has population of about" + str(population)+ ".")
    print(" The " + area + " area are nearby.") 

//Q#3 fav book
def fav_book(title):
    print (title + " is one of my favorite book")
fav_book("Islamiat")
output:
Islamiat is one of my favorite book

//Q4 making person dictionary for add and del dictionary
person = {
'first_name':'Hamza',
'last_name':'Abid'
 'age':23
 'city':'karachi',
},

for key value in person.items():
    print(key value':',value)
person['Qualification'] = 'inter mediate'
person['Qualification'] = 'Bs-cs'

person = {
 'first_name':'Hamza',
  'last_name':'Abid'
   'age':23,
    'city':'karachi',
 };
 
for key value in person.items():
    print(key value':',value)
person['Qualification'] = 'inter mediate'
person['Qualification'] = 'Bs-cs'