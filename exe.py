import random

def get_lucky_numbers(amount: int) -> tuple[int]:
    rand_num = []
    for _ in range(amount):
        rand_num.append(random.randint(1, 100))
    return tuple(rand_num)



def input_until_lucky(lucky_numbers: tuple) -> int:
    try:
        count: int = 0
        while True:
            guess_lucky: int = int(input('enter your guess: '))
            count += 1
            if guess_lucky in lucky_numbers:
                return count
    except:
        input_until_lucky(lucky_numbers)
        return count


amount = int(input('chose the amount of lucky numbers: '))
lucky_numbers: tuple = get_lucky_numbers(amount)
print('the lucky numbers are -->', lucky_numbers)
print(input_until_lucky(lucky_numbers))
print('the lucky numbers are -->', lucky_numbers)


