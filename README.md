# Collatz Conjecture Testing & Visualization

## About 

This codebase is a playground built around the Collatz Conjecture (otherwise known as the 3x+1 problem). The application allows a user to input a number from the command line and see the resulting output of the Collatz calculation. The current version of this application is developed in pure Python. 

## The Collatz Conjecture

The steps for the observing this conjecture are as follows: 

- For any positive, non-zero integer, if the value is even, perform a n/2 calculation, if odd, perform a 3n+1 calculation, where n is the integer
- For the result for the above calcualtion, continue using the two calculations in the same manner
- Eventually, the results will enter a 4-2-1 loop to infininty

The 4-2-1 loop that is observed happens for all known tested numbers for the conjecture. It can be seen in this application by viewing the final three numbers in the series. For more information on the Collatz Conjecture, please click [here](https://en.wikipedia.org/wiki/Collatz_conjecture).

## Running this Application

- Clone the repository to your local machine (or download the ZIP)
- Create a virutual environment; Optionally: Install the dependencies in the `requirements.txt` file to use the .ipynb notebook
- Run the Python script: `python3 collatz.py`
- Enter a number and hit `enter` to see the results

## License

This project repository is classified under the MIT license. Any and all code contained in the repository is open sourse and free to use. Please view the LICENSE document for more information.
