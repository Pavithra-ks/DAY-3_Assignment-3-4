'''QUESTION - 
    def fun1(a,b=0, *args,**kwargs)
	?? 
fun1(?)	'''


def fun1(a,b=0, *args, **kwargs): # kwargs - keyword arguments
    print(a,b)
    print(args) # args store the positional arguments in a tuple 
    print(kwargs) # kwargs store the keyword arguments in a dictionary 
fun1(4,8,'Coding','Program',5.55,0.4, Name = 'Pavithra',Lang = 'Python')