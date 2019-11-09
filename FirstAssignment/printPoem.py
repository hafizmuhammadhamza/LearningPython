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
