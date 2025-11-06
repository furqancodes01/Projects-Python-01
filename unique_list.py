def unique_nums(*args):
    nums = set(args)
    return list(nums)
print("Enter number seperated by spaces: ")
nums = input("")

number = [int(n) for n in nums.split()]

unique = unique_nums(*number)
print("\n Unique Numbers")
print(unique)
