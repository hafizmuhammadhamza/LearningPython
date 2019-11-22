# to print poem in seprate line , using one print function
myPoem_1 = "Twinkle Twinkle little, star,";
myPoem_2 =  "          How i wonder what you are up above the world so high";
myPoem_3 = "Twinkle Twinkle little, star,";
myPoem_4 =  "          How i wonder what you are up above the world so high";
print(myPoem_1 + "\n" +myPoem_2+ "\n" +myPoem_3+ "\n" +myPoem_4);

# to show date and time now
from datetime import datetime

today = datetime.now()
print("Today's date:", today)

# REverse name
fName= input("Enter your First name:")
lName= input("Enter your second name:")
print ("Hello  " + lName + " " + fName)
# oUT put:
Enter your First name:Hamza
Enter your second name:Abid
Hello  Abid Hamza

# python versio:
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
 
 output:
 Python version
3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
Version info.
sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0)


#ASSIGNMENT 2
#Input user for even or odd number
num = int(input("Enter your number"));
val= num %2
if val >0 :
    print("This is odd number")
else:
    print("This is even number")

    #for getting length list
    len_list=['Karachi','Islamabad','Lahore','Quetta','Pishawar']
     print(len(len_list))
      5

  #  for marks and graade 
 print("Enter marks obtained in 5 subjects: ");
mark1 = input();
if mark1 == 'x':
    exit();
else:
    mark1 = int(mark1);
    mark2 = int(input());
    mark3 = int(input());
    mark4 = int(input());
    mark5 = int(input());
    sum = mark1 + mark2 + mark3 + mark4 + mark5;
    average = sum/5;
    if(average>=91 and average<=100):
    print("Your Grade is A+");
    elif(average>=81 and average<=90):
    print("Your Grade is A");
    elif(average>=71 and average<=80):
    print("Your Grade is B+");
    elif(average>=61 and average<=70):
    print("Your Grade is B");
    elif(average>=51 and average<=60):
    print("Your Grade is C+");
    elif(average>=41 and average<=50):
    print("Your Grade is C");
    elif(average>=0 and average<=40):
    print("Your Grade is F");
    else:
    print("Strange Grade..!!");

## to get largest num from list

List = [10, 20, 4, 45, 99]
print(max(List))
99