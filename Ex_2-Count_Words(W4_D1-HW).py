from collections import Counter

def count_words(a_text):
    count_dict = {}

    a_text = a_text.lower()
    a_split = a_text.split()
    x = 'a'

    for x in a_split:
        for d in a_split:
            d = Counter(a_split)
        count_dict[x] = d[x]
    print(count_dict)
   

count_words('In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found')