x = float(input('x = '))
y = float(input('y = '))
if x > 0 and y > 0:
    print("Перша чверть")
elif x < 0 and y > 0:
    print("Друга чверть")
elif x < 0 and y < 0:
    print("Третя чверть")
elif x > 0 and y < 0:
    print("Четверта чверть")
else:
    print("Жодна чверть")

