# Intercollegiate Programming Competition 2021 Blue Track Problem 7
# Less or More

def main():
    numsAsString = input("Enter count, integers separated by a space: ").split()
    nums = [int(x) for x in numsAsString[1:]]
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                count += 1
                break
    print(count)


main()