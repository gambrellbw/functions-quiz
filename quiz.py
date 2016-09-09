
def has_teen(a,b,c):
	if a >= 13 and a <= 19:
		return True
	if b >= 13 and b <= 19:
		return True
	if c >= 13 and c <= 19:
		return True
	else:
		return False

print has_teen(13,4,21)#Should return True
print has_teen(17,15,16)#Should return True
print has_teen(4,4,12)#Should return False
print has_teen(3,4,5)#Should return False

def not_string(str):
	if str[:3] == "not":
		 return str + "not"
	else:
		return "not" + str

print not_string("notBill")# Should return not Bill not
print not_string("Bill")# Should return not Bill

def icy_hot(a,b):
	   if a > 100 and b >= 100:
		  return False
	   if a <= 0 and b <= 0:
		  return False
	   if a < 0 or b > 100:
		    return True
	   if b < 0 or a > 100:
 		    return True
	   else:
			 return False
print icy_hot(21,151)# Should return True
print icy_hot(-21,70)# Should return True
print icy_hot(21,50)# Should return False

def closer_to(t,a,b):
	u = abs(t-a)
	e = abs(t-b)

	if a == b:
		return 0
	if a == t:
		return a
	if b == t:
		return b
	if e < u:
		return b
	if u < e:
		return a

print closer_to(21,20,9)#Should return 20
print closer_to(7,20,9)#Should return 9
print closer_to(21,9,9)#Should return 0
print closer_to(17,16,8)#Should return 16

def two_as_one(a,b,c):
	if a + b == c or a + c == b or b + c == a:
		return True
	else:
		return False

print two_as_one(1,2,3)#Should return True
print two_as_one(5,6,11)#Should return True
print two_as_one(2,2,3)#Should return False
print two_as_one(3,2,3)#Should return False

#def pig_latinify(str):

#print pig_latinify("cool")
#print pig_latinify("apple")
