# labs/chapter_9.py

def min3(a,b,c):
    if a <= b and a <= c:
        result = a
        return result
    elif b <= a and b <= c:
        result = b
        return result
    elif c <= a and c <= b:
        result = c
        return result
    
print(min3(4, 7, 5))
print(min3(4, 5, 5))
print(min3(4, 4, 4))
print(min3(-2, -6, -100))
print(min3("Z", "B", "A"))


# ----------------------------------------------------
height = 0
width = 0
def box(height,width):
    for i in range(height):
        print('')
        for n in range(width):
            print("*", end ="")
box(7,5)  # Print a box 7 high, 5 across
print()   # Blank line
box(3,2)  # Print a box 3 high, 2 across
print()   # Blank line
box(3,10) # Print a box 3 high, 10 across

# ----------------------------------------------------
my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

def find(my_list,key):
    index = 0
    for i in range(len(my_list)):
        if key == my_list[i]:
            index = i
            print(f"FOUND {key} at position {index}")

find(my_list, 12)
find(my_list, 91)
find(my_list, 80)
