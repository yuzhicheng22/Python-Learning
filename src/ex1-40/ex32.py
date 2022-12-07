the_counter = [1, 2, 3, 4, 5]
for number in the_counter:
    print(f"This is count {number}")

change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for i in change:
    print(f"I got {i}")

temp = []
for i in range(0, 6):
    temp.append(i)

print(temp)



def loop(n, add):
    i = 0
    while i < n:
        print(i)
        i += add

loop(10, 2)
