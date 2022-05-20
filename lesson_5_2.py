# (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.

def odd_nums(num):
    return (num for num in range(1, num + 1) if num % 2 == 1)

odd_to_15 = odd_nums(15)
print(*odd_to_15)