
def migratoryBirds(arr):
    # Write your code here
    ar = list(set(arr))
    ar.sort(reverse=True)

    counter = 0
    cn_big = 0
    nm_big = 0
    cn_num = 0

    for i in ar:
        counter = arr.count(i)
        cn_num = i

        if counter>=cn_big:
            cn_big = counter
            nm_big = i

    return nm_big



arr = list(map(int, input("type an array:").rstrip().split()))

print(migratoryBirds(arr))

