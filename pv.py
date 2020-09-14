import math

r = int(input("Vad är radien på cirkeln du vill räkna ut arean av? "))


def Calc_circle_area(r):
    area = r**2 * math.pi
    return area
print(("Arean är: {} ").format(Calc_circle_area(r)))