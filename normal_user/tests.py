from django.test import TestCase

# Create your tests here.
a = ["ab d", "dd"]
ac = ["ab d", "dd","1565"]

b= "1"

if b in ac:
    print("in")
else:
    print("out")