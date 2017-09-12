a=dir(123)
print a
def is_(x):
	return x[0] != '_'

b=filter(is_,dir(123))
print b