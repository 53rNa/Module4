# Домашнее задание по уроку "Пространство имен"
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()    #Вызов функцию inner_function внутри функции test_function
test_function()
inner_function() #Вызов функциюи inner_function вне функции test_function вызывает ошибку
