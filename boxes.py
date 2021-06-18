import math

items = int(input("Enter the number of items: "))
packing_fit = int(input("Enter the number of items per box: "))

boxes = items/packing_fit
boxes = math.ceil(boxes)
remainder = items % packing_fit

print(f"For {items} items, packing {packing_fit} items in each box, you will need {boxes} boxes. There will be {remainder} items in the final(unfilled) box.")