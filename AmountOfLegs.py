
def Animals(chicken, cow, pig):
    chicken *= 2
    cow *= 4
    pig *= 4
    total_legs = chicken + cow + pig
    return total_legs
print("Total amount of legs in the farm is:",Animals(2, 3, 5))