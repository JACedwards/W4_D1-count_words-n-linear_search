#Time complexity of following is O(1)

def linear_search(list, num):

    if num in list:
        return True
    else:
        return False

print(linear_search([1,2,3,4,5], 6))