"""
x, y           float - кординати
АВ, BC, CD, DA float - вектори
"""
x_1 = float(input("x_1 = "))
y_1 = float(input("y_1 = "))
x_2 = float(input("x_2 = "))
y_2 = float(input("y_2 = "))
x_3 = float(input("x_3 = "))
y_3 = float(input("y_3 = "))
x_4 = float(input("x_4 = "))
y_4 = float(input("y_4 = "))
xx_1 = x_1 - x_2
yy_1 = y_1 - y_2
xx_2 = x_2 - x_3
yy_2 = y_2 - y_3
xx_3 = x_3 - x_4
yy_3 = y_3 - y_4
xx_4 = x_4 - x_1
yy_4 = y_4 - y_1
print("AB = ({0}, {1}) BC = ({2}, {3}) CD = ({4}, {5})"
      " DA = ({6}, {7}) ".format(xx_1, yy_1, xx_2, yy_2, xx_3, yy_3, xx_4, yy_4))
if xx_3 != 0 and yy_3 != 0 and xx_1/xx_3 == yy_1/yy_3:
    print("Це трапеція!")
elif xx_3 != 0 and yy_3 != 0 and  xx_4 != 0 and yy_4 != 0 and xx_1/xx_3 == yy_1/yy_3 and xx_2/xx_4 == yy_2/yy_4:
    print("Це рівнобічна трапеція!")
else:
    print("Це не трапеція!")
