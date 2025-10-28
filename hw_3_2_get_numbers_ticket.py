import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not all(isinstance(x, int) for x in [min_num, max_num, quantity]):
        print("Помилка: усі параметри мають бути цілими числами.")
        return []
    
    if min_num < 1 or max_num > 1000:
        print("Помилка: значення мають бути в межах від 1 до 1000.")
        return []
    
    if min_num > max_num:
        print("Помилка: мінімум не може бути більшим за максимум.")
        return []
    
    if quantity < 1 or quantity > (max_num - min_num + 1):
        print("Помилка: кількість чисел має бути у межах діапазону.")
        return []
    
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    numbers = sorted(numbers)

    if numbers:
        return numbers


lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
