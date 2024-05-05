def print_params(a=1, b="mon", c=True):
    print("print_params = ", a, b, c)
    print("print_params = ", a, b)
    print("print_params = ", a)
    print("print_params = ", b, c)
    print("print_params = ", )


#print_params(b=25)
#print_params(c=[1,2,3])
values_list = [1, "anot", False]
values_dict = {"a": 15, "b": "not" , "c": 50}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = (30, "hot")
print_params(*values_list_2)