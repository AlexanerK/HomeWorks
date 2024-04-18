immutable_var = (1, 2, 3, "hell", True)
print(immutable_var)
immutable_var [0] = 5  #кортеж нельзя изменить потомучто так задумано, это аксиома
mutable_list = [1, 2, 3, 4,"hell"]
mutable_list[0]= 5
print(mutable_list)
