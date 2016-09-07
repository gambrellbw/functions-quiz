
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
	 if str[:1] == "not":
		  return str + "not"
	   else:
		   return "not" + str
 print not_string("not Bill")# Should return not Bill not
 print not_string(" Bill")# Should return not Bill

  
