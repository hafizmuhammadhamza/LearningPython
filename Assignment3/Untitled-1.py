Assignment#3
## calculator
val1 = input("Enter first value")
val2 = input("Enter 2nd value")
operator = input("Enter operator")
val1 = int(val1)
val2 = int(val2)
if operator == '+' :
    val = val1+val2
    print(val,"answer")
elif operator == '-':
    val = val1-val2
    print(val,"answer")
elif operator =='/' :
    val = val1 / val2
    print(val,"answer")
elif operator =='*' :
    val = val1 * val2
    print(val,"answer")
    elif operator =='**' :
    val = val1 ** val2
        print(val,"answer")
else:
      print("entetr correct value")
 output:
Enter first value2
Enter 2nd value5
Enter operator**
32 answe

 ## For adding key value in dictionary

 customer_detail={
"First name":"Hamza",
"Last name":"Abid",
"Email" : "Hamzaabid4075@gmail.com"
}
for customer_inf in customer_detail.keys():
    print(customer_inf,"keys")
    output:
First name keys
Last name keys
Email keys
​
##For sum all numeric values
val = {"A":24,"B":20,"c":20,"D":19}
total= sum(vl.values())
print(total)
output:
83

## To chek if given key already exist in dictonary
list = {1: 2, 2:20, 3 :4, 5 :30, 6 :50, 7 :70}
def a_keypresent(n):
    if n in list:
        print("key is present in the dictionary")
    else:
        print("key is not present in dictionary")
a_keypresent(3)
a_keypresent(4)
output:
key is present in the dictionary
key is not present in dictionary

## python program to chk if there is any numeric values in this list using for loop
num_list = [2,4,8,10,12,14,15,16,17,19]
user_input = int(input("Enter the number"))
if user_input in num_list :
     print(f'{user_input}exist in this list!')
else:
      print(f'{user_input}does not exist in this list!')

    ## duplicate values from list
list = [1,2,3,2,4,6,9,6,10]
length_of_list = len(list)
duplicate_values =[]
for i in range(length_of_list):
k = i+1
 for j in range(k,length_of_list):
if list[i] == list[j]and list[i]not in duplicate_values:
duplicate_values.append(list[i])
 print(duplicate_values)