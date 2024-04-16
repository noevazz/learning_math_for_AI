# Algebra

## Recommended Books

- [The complete idiots guide to algebra](../books/the-complete-idiots-guide-to-algebra.pdf) By W. Michael Kelley https://igcsestudybank.weebly.com/uploads/5/2/0/3/52038731/the-complete-idiots-guide-to-algebra.pdf

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

## Equations with Multiple Variables

```
5x-4 = 0
```

If I tell you `solve the equation above for x` then you already know you need to isolate x to find its value.
This is pretty obvious because `x` is the only variable in the equation.

What if the equation has more that one variable:

```
3(w + 4x) -10 = 6x + 7

```

In this case you need to carefully read what you are asked for: `solve the equation for 'w'`, since the sentence is saying `for 'w'` then you have enough to solve the equation, you just need to isolate y in one side of the equation:

```
3(w + 4x) -10 = 6x + 7

first simplify:
3w + 12x -10 = 6x + 7

Now move things to the right:
    3w + 12x = 6x + 7 + 10
    3w + 12x = 6x + 17
          3w = 6x - 12x + 17
          3w = -6x + 17
           w = (-6x + 17)3
This can be reduced even more using fractions with the same denominator:
           w = (-6x)/3 + 17/3
           w = -2x + 17/3
```

There you go, you have solved the equation for `w`, the result may look a little weird but it is still valid.

## The Coordinate Plane

The coordinate plane, also known as the `Cartesian plane`, is a two-dimensional plane formed by two perpendicular number lines called the `x-axis` (the horizontal line) and the `y-axis` (the vertical line). These axes intersect at a point called the `origin`, usually denoted as `(0, 0)`.

Coordinates on the plane are written in the form `(x, y)`, where 'x' represents the horizontal position (along the x-axis) and 'y' represents the vertical position (along the y-axis). The x-coordinate tells you how far to move horizontally from the origin, while the y-coordinate tells you how far to move vertically from the origin.

`(x,y)`: These numbers are known as the `abscissa` (for x) and the `ordinate` (for y). So, what do they represent?

![cartesian-plane-3-robot_ver_1.jpg](../media/img/cartesian-plane-3-robot_ver_1.jpg)

The intersection of the two axes at the origin creates a cross shape, with four spaces of equal size around the axes. These spaces are called quadrants.

Learn more at: https://www.twinkl.com.mx/teaching-wiki/cartesian-plane

Could you tell me the coordinates (the values for x and y) to find the start?:

![Cartesian_Plane_star.PNG](../media/img/Cartesian_Plane_star.PNG)

Answer: the coordinates are `(2,4)`, this means 2 positive units in the x-axis and 4 positive units in the y-axis.

### Sketching Equations

Let's say we have this equation:

```
x+y = 9
```

If tell you to solve it for `x` then the answers is `x = 9-y` and if I tell you solve it for `y` then the answer is `y = 9-x`, but what if I told you I need both the values for `x` and `y` that makes the equation true (9), then we have infinite answers:

```
1+8 = 9
2+7 = 9
0+9 = 9
3.5+5.5 = 9
etc...
```

What if you put those values in the cartesian plane:

```
point 1: (1, 8)
point 2: (2, 7)
point 3: (9,0)
point 4: (3.5, 5.5)
```

Graph:

![x_plus_y_equals_9.png](../media/img/x_plus_y_equals_9.png)

The spot where the line intersects the x- or y-axis is called `intercept`. Using these spots are a practical way to draw the equation, therefore you only need to find (0,y) and (0,y):

```
Find y in (0,y):
  0=9-y ∴ y=9
Finally: (0,9) intersects in y

Find x in (x,0):
  x=9-0 ∴ x=9
Finally: (9,0) intersects in x
```

> `∴` means therefore in math.

You can see all dots make a perfect `straight line`, this line represent the infinite number of solutions for `x+y=9`, every single point on that line is a solution for the `linear equation`, it is called linear because it makes a straight line.

> Sketching an equations is useful to visualize the all the ordered pairs (x,y) that conforms the equation.

## Linear Equations

The standard form of a linear equation is:

```
Ax + By = C
```

> Sometimes the equation is written different but it keeps the same characteristics.

Where:

- `A` and `B` represent coefficients.
- `C` is a constant.

Characteristics of linear equations:

- Variables are raised to a power no higher than one.
- They make a straight line graph.

An example worth to review:

- `x = 5.5`, yes, it is a linear equation, it may help to see it in another form just to understand why: `1x + 0y = 5.5`, reduce the equation and you will find why it is still a linear equation, this is the graph:

  ![x_equals_5dot5.png](../media/img/x_equals_5dot5.png)
  
  Why the line is vertical this time?, answer: because all possible value for `y` are converted to 0 since the equation has `0y`, so in `(x,y)` the variable responsible to make the equation `5.5` will be `x` and `y` can have any value, in other words: `(5.5,y)` where `x` is fixed and `y` have infinite values therefore making a vertical line.

You can find online graphing calculators so you can visualize your equations, example: https://www.desmos.com/calculator

Another example:

```
-3x+y = 8
```

First let's solve the equation for `y`:

```
y = 3x +8
```

> When `y` is isolated is called the `slope-intercept` form.

Now it is easier to find some (x,y) pairs:

> You can take as many values for `x` as you want, at least two value are needed since you need to make a line.

|x-axis|y-axis|
|---|---|
|1|y=3(1)+8=11|
|2|y=3(2)+8=14|
|3|y=3(3)+8=17|
|4|y=3(4)+8=20|
|5|y=3(5)+8=23|

Now let't plot this points:

![minus_3_plus_y_equals_8.png](../media/img/minus_3_plus_y_equals_8.png)

> Image above was generated using https://www.desmos.com/calculator

Using this chart you can find other valid values like (-2,2)
.

## How To Find The Slope

The slope describes how slanty a line is.

![slope-equation.png](../media/img/slope-equation.png)

This is the slope formula, which states `Slope = Rise/Run`. When plotting a line on a graph, the `Rise` refers to the change in `y` that corresponds to a specific change in `x`. This change in `x` is called the `Run`.

In the image above the first spot is found at `(3,2)` where `3 is x₁` and `2 is y₁` and the second one is at `(7,5)` where `7 is x₂` and `5 is y₂`, let's find the slope of this line:

```
        5-2   3
slope = --- = -
        7-3   4
```

### What The Slope Tells You

- What does `3/4` means?: it means you can go up 3 units and right 4 units and you will be still in the line

- Positive slopes means the line rises up (negative slopes means the line fall)

- An slope equals to 0 means the line is horizontal.

- Undefined slopes (where x₂ and x₁ are the same therefore making a division by 0 in the equation) means the line is vertical.

- Slopes close to 0 mean that the line rise/falls slowly

- Slopes far from 0 mean that the line rise/falls quickly.

![types_of_slopes.png](../media/img/types_of_slopes.png)

## Absolute Value Graphs

Consider the following equation:

```
|x|-y = -9
```

Let's solve for `y`:

```
|x|+9 = y
```

Let's create a table for some spots:

|x-axis|y-axis|y-axis(simplified)|
|---|---|---|
|-3| &#124;-3&#124;+9 = y | 12|
|-2| &#124;-2&#124;+9 = y | 11|
|-1| &#124;-1&#124;+9 = y | 10|
|0| &#124;0&#124;+9 = y | 9|
|1| &#124;1&#124;+9 = y | 10|
|2| &#124;1&#124;+9 = y | 11|
|3| &#124;1&#124;+9 = y | 12|

You can see we can take all [Real](foundations.md#classifying-number-sets) numbers (all negatives and all positives), but the result for `y` is always a positive number.

Let's plot this spots:

![abs_x_abs_plus_9_equals_y.png](../media/img/abs_x_abs_plus_9_equals_y.png)

As you can see by the chart, equations with absolute expressions generate a V-shape chart.

>💡 The sharp point is called `vertex`

**Is the absolute value function a linear function?**, have fun and try to find the answer: https://math.stackexchange.com/questions/88669/is-the-absolute-value-function-a-linear-function

It does not have a constant slope. Therefore, it is not a linear function, but you can have some fun discussing with others about this.

### More About Absolute Value Graphs

In the image below you can see how operations affect an absolute value graph:

![More_About_Absolute_Value_Graphs.png](../media/img/More_About_Absolute_Value_Graphs.png)

- Red line `|x| = y` shows a basic graph, calculate the slope taking two spots: `(5/2)/(5-2) = 1`, which means (and also is visible) the slope is at 45 degrees.

- Blue line `-|x|-2 = y` shows and inverted graph in the x-axis because the abs term is being multiplied by `-1` and it is move `2` units down in the y-axis because `-2` is being subtracted.

- Green line `3|x|+1 = y` shows a thin graph because is being multiplied by `3`, which means the line will rise quickly, and finally is moved `1` unit up in the y-axis because `+1` is being added.

- Purple line `|(1/4)|x|-5 = y` shows a thick graph because the absolute term is being divided by `4` and it is moved `5` units down in the y-axis because `-5` is being subtracted.

## Point-Slope Form

So far we have seen the `standard form` of a linear equation:

```
Ax + By = C
```

Where:

- `A`, `B` and `C` are constants (numbers).
- `x` is the value for the x-axis
- `y` the value for the y-axis.

> Other author use different letters but it is the same.

> TIP: if you have an equation that uses the standard form you can find the slope using this formula: `Ax + By = C  ∴  m=A/B`, this is because you have to send `Ax` to the right side and the dived by `B` to isolate `y`.

And we have seen the `slope-intercept` form:

```
y = mx +b

Example:
-3x+y = 8  👈 standard equation
y = 3x +8  👈 slope-intercept equation
```

Where:
- `m` is the slope
- `b` is the intercept in the y-axis


But now we are going to see another way to represent linear equations, the `point-slope` form:

```
y-y₁ = m(x-x₁)
```

Where:

- `m` is the slope
- `y` is the y coordinate of any point
- `y₁` is the y coordinate of an known point.
- `x` is the x coordinate of any point
- `x₁` is the x coordinate of an known point.

Let's see a practical example:

Having the equation `x=y` transform the equation into its point-slope form:

![x_equals_y.png](../media/img/x_equals_y.png)

- Find the slope: `m=(y₂-y₁)/(x₂-x₁)`, from the image I will pick these spots `(5,5)` and `(1.5, 1.5)`, then the slope is `m=(5-1.5)/(5-1.5) =1`, so the slope is `m=1`.
- Now let's add that slope to the formula: `y-y₁ = 1(x-x₁)`, and there you go, now you have created the point-slope form of the equation `|x|=y`..

What if I want to have a point-slop formula of a linear equation that rise twice as fast than `|x|=y`?, then you only need to modify the slope: `y-y₁ = 2(x-x₁)`, let's use this last form and see the graph:

![x_equals_y__and__2_times_abs_x_equals_y.png](../media/img/x_equals_y__and__2_times_x_equals_y.png)

You can see the the line rises 2 times faster, e.g. for 5 in x we have 10 in y.

Now, let's go further, I will give you one spot and the corresponding slope of the line, then I want you to give me the point-slope form and finally the general equation:

Spot: (5,10)\
Slope: 2

```
  y-y₁ = m(x-x₁)
  
  y-10 = 2(x-5)   👈 Point-slope form
  
  y-10 = 2x-10
  y = 2x          👈 standard equation
```

Guess what, you have found the same exercise we saw earlier (the green line):

![x_equals_y__and__2_times_x_equals_y.png](../media/img/x_equals_y__and__2_times_x_equals_y.png)

💡 So you can find the standard equation if you have the slope and any point of the line using the point-slope formula.

## From Point A To Point B

Using the slope formula, find the linear equation giving two points:

```
Point A: (3,2)

Point B: (6, 4)
```

Procedure:

```
    y₂-y₁
m = -----
    x₂-x₁

    4-2     2
m = ---  =  -
    6-3     3
```

since we have two points and the slope, we can use the `point-slope` formula:


```
y-y₁ = m(x-x₁)

I will use this point: (3,2), now let's replace the slope and the point:
y-2 = (2/3)(x-3)
```

Now we can reduce and move things around to get the `slope-intercept` form:

```
y-2 = (2/3)(x-3)

Reduced:

y-2 = (2/3)(x-3)
y-2 = (2/3)x - (2/3)3
y-2 = (2/3)x - (6/3)
y-2 = (2/3)x - 2
  y = (2/3)x - 2 + 2
  y = (2/3)x +0     👈 intercept in y-axis is in 0
```

Let's use a graphical calculator:

![2_over_3_equals_x.png](../media/img/2_over_3_equals_x.png)

There you go.

## Parallel And Perpendicular Lines

![Parallel-and-Perpendicular-Lines.png](../media/img/Parallel-and-Perpendicular-Lines.png)

Examples:

![parallel-perpendicular-examples.png](../media/img/parallel-perpendicular-examples.png)


> For perpendicular lines: `m₁*m₂ = -1`, in other words: the result of the product of both slope is `-1`.

## Linear Inequalities

An inequality is a statement that shows the relationship between two quantities.

Expressing that one quantity is `greater than`, `less than`, or not equal to the other.

![inequality_symbols.jpeg](../media/img/inequality_symbols.jpeg)

> Note: the symbol `≠` (not equal to) is not really helpful to describe why something is not equal, instead `>, <, ≥, ≤` are preferred because they explay why the quantities are unequal.

For example

- `x > 5` means that the value of `x` is greater than `5`
- `y ≤ 10` means that the value of `y` is less than or equal to `10`.
- `10 ≥ 6` means `10` is either greater or equal to `6` which is true.
- `10 ≥ 10` means `10` is either greater or equal to `10` which is true (kinda obvious).

You may be tested to say if an statement is `true` or `false`:

- `10 ≥ 5000`, this is `false`, `10` is not greater or equal than `5000`

**IMPORTANT**: an equation has one unique solution but inequalities have a `range` of solutions, e.g. `x > 5` here there are a lot of numbers for `x` that satisfy this statement.

### Negative Number

Large negative numbers are considered the smallest quantities, for example, all these statements are true:

- `-6000 < 50`
- `-6000 < 1`
- `-6000 < 0`
- `-6000 < -3`
- `-6000 < -5999`

### Solving Inequalities

Solving inequalities involves finding all the values that makes the statement true.

Example:

`2x > 10`, answer: all values greater than 5 make the statement true.

How I found the answer?, isolating the variable:

```
  2x > 10

Divide by 2 in both sides:
2x/2 > 10/2

Reduce:
  x > 5
```

Let's see the graph for `2x > 10`:

![2_x_greater_than_10.png](../media/img/2_x_greater_than_10.png)

> Note there is a vertical dotted line in 5, this means 5 is not included as part of the answer, but if the problem uses `≥` or `≤` the line will be solid because the value will be part of the solution, e.g. `2x ≥ 10`.

> You can use https://www.desmos.com/calculator to generate this graph.

Sometimes a number line is preferred since the y-axis is not needed:

![2_x_greater_than_10_line.png](../media/img/2_x_greater_than_10_line.png)

When using number a `filled circle` usually indicates that the endpoint is included in the solution set, in the image above an `open circle` means `5` is not included in the solution set, in other words, `5` is not a valid option, only values greater than `5`.

> Image above was generated using https://quickmath.com/webMathematica3/quickmath/graphs/inequalities/basic.jsp#c=solve&v1=2x%253E10

![important.gif](../media/img/important.gif)

**IMPORTANT**: If you ever need to **multiply** or **divide** by a **negative** number you MUST **reverse** the inequality sign.

Example:

```
   -3x > 12

Divide by -3 AND REVERSE THE SIGN:
-3x/-3 < 12/-3

Reduce
     x < -4
```

Test the result:

> Use eny number less than `-4` (tip: `-4` is not an option because it is not less than `-4`, it is equal)

```
   -3x > 12
-3(-5) > 12
    15 > 12
```

Reversing the sign of an inequality is called the inequality `mood swing.`

### Compound Inequalities

Compound inequalities are statements that express two inequalities:

```
-2 < x ≤ 10
```

Statement above is read as "-2 is less than x, which is greater than 10"

![minus_2_is_less_than_x_which_is_greater_or_equal_than_10.png](../media/img/minus_2_is_less_than_x_which_is_greater_or_equal_than_10.png)

> To remember: `≥` and `≤` signs are inclusive, so you will see a filled circle.

> Image above was generated here: https://quickmath.com/webMathematica3/quickmath/graphs/inequalities/basic.jsp#c=solve&v1=-2%253Cx%255Cle10

#### Solving Compound Inequalities

Compound inequalities have three parts, in order to isolate a variable you have to apply an operation in al three parts:

```
   -16   <     2x + 4    <   24

Subtract -4:
-16 -4   <   2x + 4 -4   <   24 -4

Reduce
   -20   <      2x       <   20
  
Divide by 2:
  -20/2  <      2x/2     <   20/2

Reduce
    -10  <        x      <   10   ANSWER
```

![minus_10_less_than_x_which_is_less_than_10.png](../media/img/minus_10_less_than_x_which_is_less_than_10.png)

> https://quickmath.com/webMathematica3/quickmath/graphs/inequalities/basic.jsp#c=solve&v1=-16%253C2x%2B4%253C24

![important.gif](../media/img/important.gif)

**IMPORTANT**: If you ever need to **multiply** or **divide** by a **negative** number you **MUST reverse BOTH** signs.

### Inequalities With Absolute Values

Inequalities with absolute values are solve differently if the sentence has a `greater than` or `less than` sign:

When the inequality has the symbol `less than` (<), what we are looking for is to find the range of values of x that make the statement true:

```
|x-3| < 10
```

In this example we can provide negative numbers tha satisfy the statement, e.g. `-6`, or positive numbers e.g. `10`, but if we provide a large negative number the absolute operation will change it into a large positive number, same if we provide a large positive number, so there's only one range between negative and positive numbers that satisfy the statement, therefore inequalities with `less than` sign needs to find that range.

Solve it for `x`:

```
Rewrite the statement as a compound inequality, change the sign in the left of the statement:
-10 < x-3 < 10

Now solve the compound inequality:
-10 < x-3 < 10
-10+3 < x < 10+3
-7 < x < 13
```

The solution is the resulting compound inequality:

![minus_7_less_than_x_which_is_less_than_13.png](../media/img/minus_7_less_than_x_which_is_less_than_13.png)

> See graph above at https://quickmath.com/webMathematica3/quickmath/graphs/inequalities/basic.jsp#c=solve&v1=%257Cx-3%257C%253C10

When the inequality has the symbol `greater than` (>), there are typically parts of the number line for x that are discarded, so we use `or` to indicate that the solution can be in one part or another of the number line:

> The result will be two inequalities joined with an `or`, in other words: a number needs to satisfy inequality 1 `or` inequality 2. This is because there's a section in the negative numbers that satisfy the inequality, there's also a section in the positive numbers tha satisfy the statement, but there's a section between them that does NOT satisfy the statement, so that's why we need two inequalities, one to satisfy the negative section and the other to satisfy the positive section, and the part in the middle that does not satisfy the statement is not added as part of the result.

```
|2x + 3| > 5

Create two inequalities and solve them:
2x + 3 > 5                                 -(2x + 3) > 5
    2x > 5 -3                                 -2x -3 > 5
    2x > 2                                       -2x > 5 + 3
  2x/2 > 2/2                                     -2x > 8
     x > 1        I REVERSED THE SIGN HERE👉  -2x/-2 < 8/-2
                                                   x < -4

Now combine the answers with and OR:

x > 1 or x < -4
```

Let's see the graph:

![x_less_than_minus_4_OR_x_greater_than_1.png](../media/img/x_less_than_minus_4_OR_x_greater_than_1.png)

> See graph above at https://quickmath.com/webMathematica3/quickmath/graphs/inequalities/basic.jsp#c=solve&v1=%257C2x%2B3%257C%253E5

You can see by the graph tha using an `or` is required since there's a section in the number line that we want to exclude, this part are numbers that does NOT make the expression greater than the value.

## Inequalities With Two Variables

```
2x – 3y < 12
```

Imagine the less than sign is an equal sign and solve it as if it was an equation:

```
2x – 3y = 12
2x = +3y +12
2x -12 = 3y
(2x -12)/3 = y
(2/3)x -4 = y    This is the slope-intercept form
```

Now let's plot this equation:

![](../media/img/2_over_3_x_minus_4_equals_y.png)

You can see the line splits the coordinate plane in two regions, you can select any point from these regions and see which one satisfy the inequality, (0,0) seems to be the easier point for the region on the top:

```
    2x – 3y < 12
2(0) – 3(0) < 12
          0 < 12
```

There you go, any point in the top region satisfy the statement, you can shade this region to make it more clear:

![2_x_minus_3_y_less_than_12.png](../media/img/2_x_minus_3_y_less_than_12.png)

## Systems Of Equations

A system of equations is a collection of two or more equations.

### The Substitution Method

There are a few ways to solve systems of equations, the `substitution method` can be used to solve any system, let's see this method with a practical example:

Toretto is chasing an assassin. 🚗💨

- The assassin is going at A `150 km/h`, or `2.5 km/min`
- Toretto is going at `180 km/h`, or`3 km/h` and started to run `5 min later`.

**How long will it take Toretto to catch up with the assassin?**

Equation the assassin:

```
m = 2.5
point = (0,0)

Using point-slope form:
y-y₁ = m(x-x₁)
y-0 = 2.5(x-0)
y = 2.5x
```

Equation for Toretto:

```
m = 3
point = (5,0)    5 in x-axis because it started 5 minutes later

Using point-slope form:
y-y₁ = m(x-x₁)
y-0 = 3(x-5)
y = 3x-15
```

System of equations are usually written with a left brace:

![systems_of_equations_toretto_left_brace.png](../media/img/systems_of_equations_toretto_left_brace.png)

> Image above was generated using latex at http://www.tlhiv.org/ltxpreview/

Let's see the graph for this system of equations:

![systems_of_equations_toretto.png](../media/img/systems_of_equations_toretto.png)

> Red line is Toretto and blue line is the assassin.

> TIP: if the equations never cross then there is no solution. Check the slope and also check if they overlap, if both have the same slope and overlap then there are infinite solutions, if the slope is the same but they do not overlap then there is not solution.

The substitution method is about solving one equation and then plug the result into the other equation, let's take `3x-15 = y` and substitute `y` with the other equation `2.5x`:

```
  3x-15 = 2.5x
Reduce:
      3x = 2.5x +15
3x -2.5x = +15
    0.5x = 15
       x = 15/0.5
       x = 30
```

Answer: Toretto is going to catch up to the assassin in `30` minutes.

If you want to know the green spot in the chart then:

```
   3x-15 = y
3(30)-15 = y
   90-15 = y
      75 = y
```

So there you have it: `(30, 75)` is the solution for the system of equations.


Example 2:

```
  ,- 
 _|   2x -5y = 20
  |   x -y = 40
  `- 
```

Using the standard form is an easier way to see how we plug one equation into another:

We just need to see which equation is easier to solve for `y`, in this case `x-y = 40` is easier to solve so let's do it:

```
x -y = 40
  -y = 40 -x
   y = -40 +x
```

Now let's plug the **result** into the other equation:

```
2x -5y = 20
2x -5(-40 +x) = 20
```

And now resolve for `x`:

```
2x -5(-40 +x) = 20
  2x +200 -5x = 20
       2x -5x = 20 -200
       2x -5x = -180
          -3x = -180
       -3x/-3 = -180/-3
            x = 60
```

`60` is the value for the x-axis, now let's use any equation to find the value for `y`:

```
y = -40 +x
y = -40 +60
y = 20
```

SOLUTION for the system: `(60, 20)`


### The Elimination Method

The elimination method involves adding or subtracting equations in order to eliminate one of the variables, making it easier to solve for the remaining variables.

Let's solve the same system of the previous section but this time using the elimination method:

```
  ,- 
 _|   2x -5y = 20
  |   x -y = 40
  `- 
```

Let's multiply the second equation by 5:

```
  ,- 
 _|   2x -5y = 20
  |   5(x -y) = 5(40)
  `- 
```

Reduce:

```
  ,- 
 _|   2x -5y = 20
  |   5x -5y = 200
  `- 
```

Now we can subtract:

```
2x -5y - (5x -5y) = 20 - 200
2x -5y - 5x +5y = -180
2x - 5x = -180
-3x = -180
-3x/-3 = -180/-3
x = 60
```

There you go.

You can take a different approach and `add` instead of subtract:

```
  ,- 
 _|   2x -5y = 20
  |   x -y = 40
  `- 
```

Let's multiply the second equation by `-2`:

```
  ,- 
 _|   2x -5y = 20
  |   -2(x -y) = -2(40)
  `- 
```

Reduce:

```
  ,- 
 _|   2x -5y = 20
  |  -2x +2y = -80
  `- 
```

Now let's sum the equations:

```
     2x -5y = 20
 +  -2x +2y = -80
    --------------
        -3y = -60
      =   y =  20
```

To find `x` just plug the value of `y` in any equation:

```
x -y = 40
x -20 = 40
x = 40 + 20
x = 60
```

You can add or subtract equation depending on your approach.

## Systems With No Solutions

Let's say you have to parallel equations without overlapping each other:

```
  ,- 
 _|   2x -3y = 20
  |   6x -9y = 30
  `- 
```

You can convert those equations into its slope-intercept form (by isolating `y`) and there you can easily find the slope by seeing the coefficient of `x`, a trick to find the slope is `m=A/B` for `Ax + By = C`.

In this system of equations the slope is `1/2` for both equations, and also the equations do not overlap.

If you try to use the elimination method you will end up with no variables:

```
  Multiply by 3:
  ,- 
 _|   3(2x -3y) = 20
  |   6x -9y = 30
  `- 
  Reduce:
  ,- 
 _|   6x -9y = 20
  |   6x -9y = 30
  `- 
```

If you subtract you will delete all variables, this is just another sign that the system of equations does not have a solution.

## Systems Of Inequalities

![systems_of_inequalities.png](../media/img/systems_of_inequalities.png)

Systems of inequalities are threated pretty much the same as in section [Linear Inequalities](#linear-inequalities), you just need to graph both inequalities and the answer will be the overlap between the inequalities.

## Tensors

Tensors are the most common data structure used in Machine Learning.

A popular Python library to work with tensors is called `Tensorflow`. https://www.tensorflow.org

### What Is A Tensor

In simple words, tensors are arrays of numbers.

Tensors are classified depending on the amount of dimensions.

![shape_of_tensor.jpg](../media/img/shape_of_tensor.jpg)

> When we have more than two indices to refer to a specific element in a data structures (or mathematical, structure) we stop treating them with special names like scalars, vectors, matrices etc. Instead we address them with a more generalized language, tensors.

Let's see an example of each one using Python:

```
scalar = 4

vector = [1, 2, 3]

matrix = [
  [1, 2, 3]
  [4, 5, 6],
  [7, 8, 9]
]

threeTensor = [
  [[1, 2], [3, 4]],
  [[5, 6], [7, 8]]
]
```

## Matrix

![the_matrix_has_you.webp](../media/img/the_matrix_has_you.webp)

A matrix is a collection of `elements` arranged in `rows` and `columns`.

The `order` of a matrix describes how many rows and columns a matrix have, e.g. a matrix of order 3x5 (three by five) has 3 rows and 5 columns.

Matrix are typically displayed surrounded by big brackets:

![example_matrix_3_by_5.png](../media/img/example_matrix_3_by_5.png)

> This image was generated at http://www.tlhiv.org/ltxpreview/ with this file [example_matrix_3_by_5.tex](../scripts/latex/example_matrix_3_by_5.tex)

Image above shows:

- The matrix ***A***, you can use any letter to named a matrix.
- In algebra the letter used to represent a matrix **is typically in bold, uppercase and italic** so it can be distinguished from other types of variables.
- The position of each element is identified with a subscript where the first number is the row, and the second is the column.
- Typically, the same letter used to represent the entire matrix is used to represent a specific element but in lowercase.
- Instead of `x` and `y`, as in the cartesian plane, we use `i` and `j` when talking about matrices.

When talking about a matrix of unkown order this `m by n` is used:

![m_by_n_matrix.png](../media/img/m_by_n_matrix.png)

> This image was generated at http://www.tlhiv.org/ltxpreview/ with this file [m_by_n_matrix.tex](../scripts/latex/m_by_n_matrix.tex)

💡 When a matrix has the same number of rows and column is called `square matrix`.

When you want to refer to a specific element in the matrix you need to use the subscript e.g. `a₂,₁`.

Matrices are typically composed of elements that belong to a common field, such as real numbers, complex numbers, or integers. Mixing different types of numbers within a single matrix isn't inherently invalid, but it may not always make sense depending on the context of the problem you're working on.

Anyways, math teachers like to create this type of scenarios to test your abilities:

![matrix_with_mixed_real_numbers.png](../media/img/matrix_with_mixed_real_numbers.png)

> This image was generated at http://www.tlhiv.org/ltxpreview/ with this file [matrix_with_mixed_real_numbers.tex](../scripts/latex/matrix_with_mixed_real_numbers.tex)

### Matrix Operations

#### Multiplication By A Scalar

`Scalars` are numbers that scale or stretch other mathematical objects without changing their direction. Scalars are NOT elements within a matrix, they are just real numbers.

When you multiply a matrix by a scalar, you simply multiply each element of the matrix by that scalar. If `A` is a matrix and `k` is a scalar, the result of multiplying `A` by `k` is denoted as `kA`.

![matrix_miltiplied_by_scalar.png](../media/img/matrix_multiplied_by_scalar.png)

> This image was generated at http://www.tlhiv.org/ltxpreview/ with this file [matrix_multiplied_by_scalar.tex](../scripts/latex/matrix_multiplied_by_scalar.tex)

#### Adding And Subtracting Matrices

IMPORTANT: **ONLY** if you have two matrices of the same order you can add or subtract them.


- Addition:

  ![add_matrices.png](../media/img/add_matrices.png)

  > This image was generated at http://www.tlhiv.org/ltxpreview/ with this file [add_matrices.tex](../scripts/latex/add_matrices.tex)

- Subtraction:

  ![subtract_matrices.png](../media/img/subtract_matrices.png)

  > This image was generated at http://www.tlhiv.org/ltxpreview/ with this file [subtract_matrices.tex](../scripts/latex/subtract_matrices.tex)

#### Matrix Multiplication

**IMPORTANT**: There is a big rule for multiplying matrices and tha is the number of columns in the first matrix should be the same as te number of rows in the second matrix, in other words:

![rule_for_matrix_multiplication.png](../media/img/rule_for_matrix_multiplication.png)

Example:

![matrix_multiplication.gif](../media/img/matrix_multiplication.gif)

![matrix_multiplication.png](../media/img/matrix_multiplication.png)

#### Hadamard Product

In mathematics, the Hadamard product (also known as the element-wise product, entrywise product[1]: ch. 5  or Schur product[2]) is a binary operation that takes in two matrices of the same dimensions and returns a matrix of the multiplied corresponding elements.

This operation can be thought as a "naive matrix multiplication" and is different from the matrix product. 

The Hadamard product A ⊙ B (sometimes A ∘ B)

![hadamard_product.png](../media/img/hadamard_product.png)

### Determinants

A determinant is a real number found in every `squared` matrix.

It is used to solve systems of linear equations.

- Find the determinant of a 2x2 matrix:

  Having this system of linear equations:

  ```
  2x+3y = 11
  4x−y = 5
  ```

  We can represent the system in a matrix:

  ```
  | 2   3 |
  | 4  -1 |
  ```

  > Determinant syntax usually uses a straight line instead of brackets.

  Now let's use this method to find the determinant:

  ![determinants_2x2.jpg](../media/img/determinants_2x2.jpg)

  ```
      | 2   3 |
  A = | 4  -1 |

  det(A) = (2*-1) - (3*4) = -2 - 12 = -14
  ```
- Find the determinant of a 3x3 matrix:

  ![determinants_3x3.jpg](../media/img/determinants_3x3.jpg)

### Cramer's Rule

The cramer's rule uses determinants to solve systems of linear equations.

![cramersrulenotes.jpg](../media/img/cramersrulenotes.jpg)

- In the image above `a`, `b`, `e`, `c`, `d` and `f` are constants.

- Basically you need to find the determinant in the numerator and divide the result by the determinant in the denominator.

### Vectors

A vector is a mathematical object that represents a quantity with both `magnitude` and `  `.

A vector may look like a 1xN matrix:

![vectors.png](../media/img/vectors.png)


> A `unit vector` is a vector with magnitude 1. 

Vector can represent 2 dimensional object:

```
[x, y]
```

Three dimensional objects:

```
[x, y, z]
```

![xyz_plane.png](../media/img/xyz_plane.png)


Or N dimensional objects.

#### Dot Product

The dot product of two vectors is a scalar quantity obtained by multiplying corresponding components of the vectors and then summing up these products.

![dot_product.png](../media/img/dot_product.png)

## Polynomials

Polynomials are mathematical expressions made up of variables and constants by using arithmetic operations like addition, subtraction, and multiplication.

### Characteristics

- In polynomials, the exponents of each of the variables should be non-negative integers.
  ```
  2x^-2        This is NOT a polynomial
  √x = x^(1/2) This is NOT a polynomial
  ```
- A polynomial comprises constants and variables, but we cannot perform division operations by a variable in polynomials.
  ```
  1/(y+2)   This is NOT a polynomial
  ```

This is how a polynomial look:

![what-is-a-polynomial.png](../media/img/what-is-a-polynomial.png)

### Classification

- Classification based by number of terms:
  ![polynomial_classification_based_on_terms.png](../media/img/polynomial_classification_based_on_terms.png)
- Classification based by degree:
  ![polynomial_classification_based_on_degree.png](../media/img/polynomial_classification_based_on_degree.png)
  > Note the terms are ordered from left to right based in the degree.

It is common to use both classifications at the same time (**the degree is always mentioned first**):

```
2x³ + 5x    cubic monomial
```

### Operations With Polynomials

- Addition and subtraction: You can add terms of the same variable with the same exponent by adding the coefficient:
  ```
  3x² + 7x² = 10x²
  ```
  Another example:
  ```
  2x³y⁴ - 8x³y⁴ = -6x³y⁴
  ```
  The variable and the exponent are not touch.

-  Multiplying Polynomials:
  ```
  (3x²)*(5x⁴) = 15x⁶
  ```
  > Basically apply the distributive rule and exponential rules saw in the [foundations](foundations.md) unit.
  
  Another example:
  ```
  (2x² + x)*(3x⁴) = 6x⁶ + 3x⁵
  ```

  Another example:
  ```
  (x+2)*(x+2)
  = (x+2)²
  = x² + 2x + 2x + 4
  = x² + 4x + 4
  ```

- Division:
  Similar to multiplication but this time subtract the exponents and also divide the coefficients:
  ```
  (10x⁴)/(5x²) = 2x²
  ```
  > Note: division between monomials is straight forward, we will dig more on division between polynomials with more than one term later.

- LONG DIVISION

  Polynomial long division is like the long division you do with numbers but with polynomials.

  You start by asking, "How many times does THIS go into THAT"

  Example 1:
  ![LongDivisionofPolynomials_example_1.png](../media/img/LongDivisionofPolynomials_example_1.png)

  Example 2:
  ![LongDivisionofPolynomials_example_2.png](../media/img/LongDivisionofPolynomials_example_2.png)

  Since there was a reminder then we can add that as a part of the result at the end `reminder/divisor`

- Synthetic Division

Synthetic division is a method that facilitates the operations of polynomials over `linear binomials` e.g. `x-c` where `c` is a constant.

This method uses the coefficients in the polynomial, example:

![synthetic-division-cheat-sheet.jpg](../media/img/synthetic-division-cheat-sheet.jpg)

Important:

- Note the constant written in the "house" is the opposite value, in other words, the divisor is `x-5` so the value for the house needs to be `+5`
- The `known zero` refers to a value of `x` that makes the polynomial equation equal to zero, in this example `x-5` the value that makes the equation equal to zero is `+5`: `(+5)-5`.
- If the polynomial is missing a power you can add it: `0x^power`

## Factoring Polynomials

Just to remember: A factor is a number that divides evenly into a number and leaves behind no reminder, e.g. the factors of 10 are 10, 5, 2, and 1.

Factoring a polynomial means finding the smaller expressions that, when multiplied together, give you the original polynomial. 

Example:

Factor the polynomial of `6x²y³ - 12xy²`

1. Find the GCF of the coefficients, in this case the GCF of `6` and `12` is `6`.
2. Identify common variable powers. In this example both terms contains at least `one x` and at least `two y`.
3. Combine the results of #1 and #2:
  ```
  6x¹y²
  ```
  > This is the GCF for both terms. The `Greatest Common Factor (GCF) of a polynomial` is the largest monomial that divides evenly into each term.
4. Now take the original polynomial and divide EACH term **separately**  by #4:
  ```
  First term:
  (6x²y³) / 6x¹y²
  reduce:
  (6x²y³) / 6x¹y² = xy

  Second term:
  (-12xy²) / 6x¹y²
  reduce:
  (-12xy²) / 6x¹y²= -2x⁰y⁰
  = -2(1)(1)
  = -2
  ```
5. The factored result is equal to the GCF found in #3 multiplying #4:
  ```
  (6x¹y²)*(xy-2)

  or just: 6xy²*(xy-2)
  ```

## Factoring By Grouping

This technique is used when just SOME terms in a polynomial have a GCF.

Basically you will group the terms that have a GCF, then factor those groups individually.

Example:

Factor `2x³ -4x² -3x¹ +6`.

- You can see none of the coefficients have a UNIQUE common factor but we can group the terms that have a common factor:

  ```
  (2x³ -4x²) + (-3x¹ +6)
  ```

- Now find the GCF:
  - GCF for `(2x³ -4x²)` is `2x²`

- Then divide the term by that GCF:
  ```
  (2x³ -4x²) / 2x²  =  x - 2

  ∴ (2x³ -4x²) =  (2x²) * (x - 2)
  ```
- Now rewrite the polynomial:
  ```
  2x³ -4x² -3x¹ +6   =   (2x²) * (x - 2) + (-3x +6)
  You can factor the second term:
  2x³ -4x² -3x¹ +6   =   (2x²) * (x - 2) -3(x -2)
  ```
- Now `(x-2)` can be factorized:
  ```
  (2x²) * (x - 2)  -3(x -2)


  Divide by (x-2):

  (2x²) * (x - 2)  -3(x -2)
  ---------------  --------
      (x -2)        (x -2)

  =  (2x²) -3

  Multiply result by the GCF:

  (x - 2) * (2x²-3)     This is equal to the original polynomial
  ```


## Time-Saving Patterns

These are some patterns that help you factorize faster:

- `Perfect square`: it is the result of multiplying something by itself, example
  ```
  (2x)*(2x) = 4x²
  ```
  > In the example above the perfect square is `4x²`.

- `Perfect cube`:
  ```
  (3x)*(3x)*(3x) = 27x³
  ```

- `Perfect binomial square`: A perfect square binomial is a trinomial that when factored gives you the square of a binomial, example:
  ```
  4x² +8x +4 = (2x+2)²
  ```
  Test the result:
  ```
  (2x+2)*(2x+2) = 4x² +4x +4x +4
  ```
  The result of (Ax + C)² is always:
  1. first term to the power of 2
  2. 2 times the product of both terms
  3. second term to the power of 2

- `Difference of perfect square`: here is a rule for this case:
  ```
  (a²-b²) = (a+b)(a-b)
  ```
  > IMPORTANT: this rule does **NOT** apply to `(a²+b²)`, the sum of perfect squares cannot be factor as easy as the difference.
  
  Example:
  ```
  x²-4 = (x+2)(x-2)
  ```
  > Note: in `x²-4` the second term `4` is the same as `2²`

  ```
  (x+2)(x-2) = x²  -2x  +2x  -4
                    ☝️  ☝️
                    ⛔  ⛔
  ```
  Another example: `5x² -125`

  We need to rewrite this binomial because `5` does NOT have a square root:

  ```
  5x² -125 = 5(x² -25)
  ```
  Now we can apply the rule:
  ```
  a² = x²
  a  = x

  b² = -25
  b  = -5

  5(x² -25) = 5[(x-5)(x+5)]
  ```
- `Difference of perfect cubes`:
  ```
  (a³ -b³) = (a-b)(a² +ab + b²)
  ```
  Example: `(8x³ -27)`\
  First find `a` and `b`:
  ```
  a = (8x³)^(1/3)
    = 2x
  
  b = (27)^(1/3)
    = 3
  ```
  Now rewrite it:
  ```
  (2x-3) [(2x)² + (3)2x + 3²]
  reduce:
  (2x-3) (4x² + 6x + 9)
  ```
- `Sum of perfect cubes`:
  ```
  (a³ + b³) = (a+b)(a² -ab + b²)
  ```
  Example: `16x³ -2y³`

  This example is a little bit tricky, because there's no cube root of 16:
  ```python
  # python
  >>> 16**(1/3)
  2.5198420997897464
  ```
  So let's start by factoring the greatest common factor:
  ```
  16x³ -2y³ = 2(8x³ -y³)
  ```
  Guess what, `8` has a cube root: `8^(1/3) = 2`
  ```
  2(8x³ -y³) = 2(apply the rule here)
  2(8x³ -y³) = 2[(2x + y)((2x)² - 2xy + y²)]
  Reduce:
  2(8x³ -y³) = 2[(2x + y)(4x² - 2xy + y²)]
  ```

superscript: ⁰¹²³⁴⁵⁶⁷⁸⁹
subscript: ₀₁₂₃₄₅₆₇₈₉