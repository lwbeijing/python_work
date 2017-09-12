def fn (self,name='world'):
	print ('hello %s'%name)

h=type('Hello',(object,),dict(hello=fn))

q=h()
q.hello()
print(type(h))
print(type(q))

