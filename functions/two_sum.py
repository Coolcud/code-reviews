def twoSum(list, target):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[j] == target - list[i]:
                return [list[i], list[j]]
