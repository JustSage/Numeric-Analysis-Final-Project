## About

This is some simple code for calculating an approximation of a double integral using the Gauss-Legendre method.

## Requirements

The Numpy library, install via command line:

  `python -m pip install numpy`
  
The Sympy library, install via command line:

  `python -m pip install sympy`

## How to use

To start the code, either run main.py from the command line using python, or open a project in your IDE of choice and run from it.
The input requested is as follows:

1. The function written in python syntax, as you would in actual python code. When using functions from the math library, use them as is without the `math.` before the function name.
2. The lower bound of the y axis to integrate in
3. The upper bound of the y axis to integrate in
4. The lower bound of the x axis to integrate in
5. The upper bound of the x axis to integrate in
6. The number of points to use in the method.

After all of the input is given, you will receive the approximation of the integral.

## Credits

Ben Lambert (youtube channel [here](https://www.youtube.com/user/SpartacanUsuals)), for a clear and concise explanation of how to use the method [here](https://www.youtube.com/watch?v=Hu6yqs0R7GA).
