def minimal(l):
    enum = l[0]
    for i in l:
        if i < enum:
            enum = i
    return enum

nums1 = [2, 5, 79, 98]
min1 = minimal(nums1)

nums2 = [55, 54, 8, 7]
min2 = minimal(nums2)

if min1 < min2:
    print(min1)
else:
    print(min2)