def test(params):
    if params <= 0:
        return print("Ошибка,задано отрицательное число")
    if params == 1:
        return params
    else:
        return params * test(params - 1)


print(test(13))
