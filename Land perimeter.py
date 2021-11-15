def land_perimeter(arr):
    arr.append("O"*len(arr[0]))
    per = 0
    for i in arr:
        temp = "O"
        i = i + 'O'
        for j in i:
            if j == temp:
                per = per
            if j != temp:
                per = per + 1
                temp = j
    for i in range(len(arr[0])):
        temp = "O"
        for j in range(len(arr)):
                  if arr[j][i] == temp:
                per = per
            if arr[j][i] != temp:
                per = per + 1
                temp = arr[j][i]
    return "Total land perimeter: " + str(per)

arr2 = ["XXXOOO",
        "OOOOOO",
        "OOOOOO",
        "OOOOOO",
        "OOOOOO",
        "OOOOOO",
        "OOOOOO",
        "OOOOOO",
        "OOOOOO",
        "OOOOOO"]

arr1 = ["OXOOOX",
        "OXOXOO",
        "XXOOOX",
        "OXXXOO",
        "OOXOOX",
        "OXOOOO",
        "OOXOOX",
        "OOXOOO",
        "OXOOOO",
        "OXOOXX"]
print(land_perimeter(arr1))

