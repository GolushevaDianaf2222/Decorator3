import datetime 
 
 
def decorator(function): 
    def wrapper(*args, **kwargs): 
        return_value = function(*args, **kwargs) 
        print(f'Время запуска - {datetime.datetime.now()}') 
        print(f'Количество товаров -', *args) 
        print(f'Сумма доставки - {return_value}$') 
        return return_value 
 
    return wrapper 
 
@decorator 
def func(amount): 
    return round(2.95 * amount - 2.95 + 10.95, 2) 
 
 
func(int(input()))

 

