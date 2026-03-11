
import random

def get_lucky_numbers(amount: int) -> tuple[int]:
    """
     return a tuple of random numbers as - the lucky numbers
     :param amount: amount of numbers
     :return: tuple of random numbers
     """
    rand_num = []
    for _ in range(amount):
        rand_num.append(random.randint(1, 100))
    return tuple(rand_num)

def input_until_lucky(lucky_numbers: tuple) -> int:
    """
      return amount of inputs entering hitting correct lucky number
      :param lucky_numbers:
      :return:
      """
    count: int = 0
    while True:
        try:
            guess_lucky: int = int(input('enter your guess: '))
            count += 1
            if guess_lucky in lucky_numbers:
                return count
        except ValueError as e :
            print('invalid input', e)


amount = int(input('chose the amount of lucky numbers: '))
lucky_numbers: tuple = get_lucky_numbers(amount)
print(lucky_numbers)
print(input_until_lucky(lucky_numbers))
print(lucky_numbers)


