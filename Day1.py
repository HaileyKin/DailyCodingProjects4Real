# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

given_list = [10, 15, 3, 7]

def does_add(giv_list, k , current = 0):
    curr_list = giv_list[current]
    for i in range(current+1, (len(giv_list))):
        test_add = curr_list + giv_list[i]
        if test_add == k:
            return True
    current += 1
    if current <= (len(giv_list)-1):
        return does_add(giv_list, k, current)
    elif current == len(giv_list):
        return False

def main():
    k = 17
    run = does_add(given_list, k)
    if run == True:
        print("Two numbers add up to", k)
    else:
        print("Two numbers do not add up to", k)

main()