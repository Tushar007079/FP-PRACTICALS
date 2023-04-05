size = int(input('Enter number of elements: '))
num = [int(x)
       for x in input(f'Enter {size} space  separated numbers: ').split()]
print('Entered List: ', num)
for i in range(size):
    for j in range(0, size-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print('Sorted List: ', num)
