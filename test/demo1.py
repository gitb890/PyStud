target = 9
array = [2,13,-2,6,7]


def ArraytoNUm():
    for i in range(len(array)):
        for j in range(i+1,i):
            if array[i] + array[j] == target:
                print(i,j)