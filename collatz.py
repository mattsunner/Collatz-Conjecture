"""
Collatz Conjecture Script


Author: Matthew Sunner, 2022
"""

import plotly.express as px
import pandas as pd

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

    def visualize_conjecture(self):
        n = self.input
        results = []
        while n > 1:
            if (n % 2):
                n = self.odd_func(n)
                results.append(results)
            else:
                n = self.even_func(n)
                results.append(results)
        
        # Create a Dataframe From the Results
        print(results)
        df = pd.DataFrame(results)
        print(df)

        # Create Plot & Display Results

        x = range(1,len(results)+1)
        y = results

        #fig = px.line(df, x=df.index, y=df['Result'])

        #fig.show()


def main():
    guess = int(input('Please Enter a Positive Number: '))

    c = Collatz(guess)
    c.visualize_conjecture()


if __name__ == '__main__':
    main()
