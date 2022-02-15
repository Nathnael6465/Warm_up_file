def findMax(list):
    max = list[0]

    for i in range(1, len(list)):
        'return the max please'
        if list[i] > 0:
            max = list[i]
    return max
if __name__ == '__main__':
    print(findMax([1,3,4,2,12,4,23,4,23,4,134,123,324]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
