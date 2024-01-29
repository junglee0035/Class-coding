def sumList(nums):
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

def main():
    print(sumList([2,4,6,8]))
    print(sumList([10,20,30,40]))
    print(sumList([5,10,15,20]))

main()