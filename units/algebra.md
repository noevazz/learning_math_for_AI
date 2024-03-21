# Algebra

## Recommended Books

- Calculus I By W. Michael Kelley

Tip: if you use firefox to open PDFs you can add this CSS style to invert the colors of the pdf:
```
.pdfViewer {
  filter: invert(1);
}
```

## What Is Algebra

Algebra is a branch of mathematics where letters and symbols represent numbers and quantities in equations and expressions

![algebra.jpg](../media/img/algebra.jpg)

## Equations and Inequalities

An **equation** in algebra is a mathematical statement that shows that two expressions are equal.

Example:

```
2w+5=11,
```

In this example `w` represents an unknown value.

Solving the equation implies finding the value of `w` so the equation remains true. For the example above the answer is `w=3`. You can confirm this result by substituting the result in the equation and check if the equality remains true:

```
2(3)+5=11
   6+5=11
    11=11
```

We have confirmed `3` is the right number that keeps the balance (equality).

Now, how do you find the value of `w`?, that's what we are going to study in this section.

### Solving An Equation

In orders to solve an equation you have to isolate the variable on one side of the equal sign so you can have the actual value on the other side.

You can play with the equation and add, subtract, divide, multiply, etc. values to the equation to isolate the variable, but you need to keep the balance at any point, that means if you want to subtract `-5` of one side, then you MUST do it in both side to keep the balance (equality):

```
2w+5 = 11

Let's subtract -5:
2w+5-5 = 11-5

Simplify:
2w = 6

Now let's remove that 2 by dividing by 2:
2w/2 = 6/2

Simplify:
w = 3

THE ANSWER IS 3 OH YEAH!!!
```

You can replace `3` in the original equation `2w+5 = 11` and see if the result is `11`, if true then `3` is in fact the right answer.

Sometimes adding an operation in both sides can be pretty obvious, some people like to save some lines by just writing the next expression that keeps the equation in balance:

```
2w+5 = 11

Let's subtract -5:
2w = 11-5      You can see I directly removed +5
Some people go further and directly reduce 11-5:

2w = 6

Finally divide by 2:
w = 3           This time I simplified 6/2 directly
```

You can do this as long as you keep your process readable, sometimes making things clears is better than writing less.

> To remember: that `2` attached to `2w` is called **coefficient** and it represents a multiplication, this time `2 times w`.

Another example:

In this exaple the variable is `k`:

```
                -k/6+4 = 28

Start by the easy tasks:
remove that +4:   -k/6 = 24   I subtracted -4
remove that 1/6:    -k = 144  I multiplied by 6 in both sides

Now finally multiply by -1 so k will be positive:
                     k = -144
```

> Note: in this example the coefficient attached to `k` was a fractional coefficient, `1/6` to be precised. `(1/6)*k` is the same as `k/6`.

Let's check if our result is right:

```
                -k/6+4 = 28
           -(-144)/6+4 = 28
               144/6+4 = 28
                  24+4 = 28
                    28 = 28

                  OH YEAH!!!!
```

Another example:

```
                x + 3 = 5 + 3
        In this case we can directly cancel +3:
                    x = 5
        Why? because it is the same as:
                x+3-3 = 5+3-3
````

So if you find the same `terms` in both sides then you can directly cancel them.

Another example:

```
–3x – 21 = –2x + 7
     -3x = -2x + 7 + 21
     -3x = -2x + 28
-3x + 2x = 28
      -x = 28
      x = -28
```

Test the result:

```
    –3x – 21 = –2x + 7
-3(-28) - 21 = -2(-28) + 7
     84 - 21 = 56 + 7
          63 = 63

         OH YEAH!!
```

### SymPy

SymPy is a Python library for symbolic math. 

Learn more at: https://www.sympy.org/en/index.html

In symbolic math, symbols are used to represent mathematical expressions.

You can find practical examples at: https://problemsolvingwithpython.com/10-Symbolic-Math/10.00-Introduction/

- Install sympy: `pip install sympy`

Let's solve the same equation we solve in the previous section:

```
    –3x – 21 = –2x + 7
```

Python code:

```python
from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define la equation
equation = Eq(-3*x - 21, -2*x + 7)

# Solve the equation
solution = solve(equation, x)

print(f"The solution for {equation} is {solution}")
```

> This code is also available at [solving_equations.py](../scripts/solving_equations.py).


Execution:

```
$ python3 solving_equations.py
The solution for Eq(-3*x - 21, 7 - 2*x) is [-28]
```

Just a note, in an IPython console session, or a regular Python session, it will use the Unicode pretty printer if the terminal supports Unicode:

```
$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from sympy import *
>>> x,y,z = symbols('x y z')
>>> init_printing()
>>> Integral(sqrt(1/x), x)
 ⌠
⎮     ___
⎮    ╱ 1
⎮   ╱  ─  dx
⎮ ╲╱   x
⌡
>>>
```

Learn more at https://docs.sympy.org/latest/tutorials/intro-tutorial/printing.html


### Absolute Value Equations

Steps:

1. Isolate the absolute expression.
2. Create two equations, both equations will look like the isolated version but without the bars, the second equation will change the value on the left for its opposite value.
3. Solve the equation, both equations are the answer for the original absolute equation.

Example:

```
20|3x-3| = 20

Dived by 20:
  |3x-3| = 1

Now create two equations:
3x-3 = 1    and   3x-3 = -1

Solve both equations:
3x-3 = 1    and   3x-3 = -1
  3x = 1+3          3x = -1+3
  3x = 4            3x = 2
   x = 4/3           x = 2/3
```

Solution using python here [absolute_equations.py](../scripts/absolute_equations.py).

Let's verify the answers:

```
For x = 4/3
            20|3x-3| = 20
        20|3(4/3)-3| = 20
        20|(12/3)-3| = 20
             20|4-3| = 20
               20|1| = 20
                  20 = 20

For x = 2/3
            20|3x-3| = 20
        20|3(2/3)-3| = 20
         20|(6/3)-3| = 20
             20|2-3| = 20
              20|-1| = 20
                  20 = 20
```




Systems of Linear Equations and Matrices
    Quadratic Equations and Functions
    Polynomials and Polynomial Functions
    Rational Expressions and Equations
    Exponential and Logarithmic Functions
    Radical Equations and Functions
    Conic Sections
    Sequences and Series
    Complex Numbers
    Matrices and Determinants
    Vectors
    Vector Spaces
    Linear Transformations
    Eigenvalues and Eigenvectors
    Polynomial Interpolation
    Factorization Techniques
    Group Theory
    Ring Theory
    Field Theory