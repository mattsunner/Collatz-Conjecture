"""
Collatz Conjecture Script


Author: Matthew Sunner, 2022
"""


class Collatz():
    def __init__(self, input):
        self.input = input

    def odd_func(self, n):
        result = 3*n+1

        return result

    def even_func(self, n):
        result = n // 2
        
        return result


    def conjecture(self):
        n = self.input
        while n > 1:
            if (n % 2):
                n = self.odd_func(n)
                print(n)
            else:
                n = self.even_func(n)
                print(n)


def main():
    guess = int(input('Please Enter a Positive Number: '))

    c = Collatz(guess)
    c.conjecture()


if __name__ == '__main__':
    main()
