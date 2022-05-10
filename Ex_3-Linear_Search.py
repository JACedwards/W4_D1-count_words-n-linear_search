#Time complexity of following is O(n)

def search(list, num):

    if num in list:
        return True
    else:
        return False

print(search([1,2,3,4,5], 6))