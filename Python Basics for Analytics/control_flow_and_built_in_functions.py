def age_check(age):

    if age > 40:  # if age greater than 40, print "Older than 40"
        print("Older than 40")
    elif age > 30 and age <= 40: # if age greater than 30 and less than or equal to 40, print "Between 30 and 40"
        print("Between 30 and 40")
    else:  # if neither of the previous conditions are met, print "Other"
        print("Other")

print(age_check(41))

names = ['tyler', 'karen', 'jill']   # list containing names

for i, name in enumerate(names):     # iterating over names
    print("Index: {0}".format(i))    # printing index number
    print("Value: {0}".format(name)) # print the value at the index

numbers_gt_5 = [x for x in range(1,15) if x > 5]  # loop over the range and only keep the value if greater than 5
print(numbers_gt_5)

nums_plus_one = [x + 1 for x in range(5)]
print(nums_plus_one)

my_list = [2, 10, 1, -5, 22]
my_list.sort()  # sorting the list

print(my_list)

my_list = [2, 10, 1, -5, 22]

# Sorted reversely on basis of absolute value
my_list_sorted_abs = sorted(my_list, key=abs, reverse=True)

print(my_list_sorted_abs)

list_1 = [1, 2, 3]  # create your first list
list_2 = ['x', 'y', 'z']  # create your second list

print(list(zip(list_1, list_2)))  #combine and print

pairs = [('x', 1), ('y', 2), ('z', 3)]  # a list of tuples
letters, numbers = zip(*pairs)  # break into two lists

print(letters)  # print the first values of the tuples
print(numbers)  # print the second values of the tuples

