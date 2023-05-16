li = []


def printTheArray(arr, n):
    s = ""
    for i in range(0, n):
        # print(arr[i], end = " ")
        s = s + str(arr[i])
    li.append(s)
    print()


# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
    if i == n:
        printTheArray(arr, n)
        return
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)


if __name__ == "__main__":

    n = 5
    arr = [None] * n
    # Print all binary strings
    generateAllBinaryStrings(n, arr, 0)
    count = 0
    count1 = 0
    for day in li:
        if "0000" in day:
            count1 += 0
        elif day[-1] == '0':
            count += 1
            count1 += 1
        else:
            count += 1
    print(str(count1) + "\\" + str(count))