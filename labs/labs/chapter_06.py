# labs/chapter_06.py

# 6.1 part 1
x = 10
for row in range(1,10):
    for column in range(row):
        print (x,end=" ")
        x += 1
 
    # Print a blank line
    # to move to the next row
    print()
    
    
# 6.2 part 2
# Step 1: Claculate rows and columns
n = 0
while True:
    n = int(input("Enter n (n > 1): "))
    if n > 1:
        break
    else:
        continue

rows = n
columns = n * 2

# Step 2: Draw the first row
for i in range(columns):
    print("o", end = "")

for i in range (rows - 2):
    print("\n", end = "")
    # Step 3.1: The first character
    print("o", end = "")

    # Step 3.2: The blank spaces
    for j in range (columns - 2):
        print(" ", end = "")
        
    # Step 3.3: The last character
    print("o", end = "")

# Step 4: Draw the last row
print("\n", end = "")
for i in range(columns):
    print("o", end = "")
