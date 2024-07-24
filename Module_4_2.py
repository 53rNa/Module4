# Домашнее задание по уроку "Пространство имен"
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    return inner_function
call_innf = test_function()
call_innf()
