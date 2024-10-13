def sorting(s_list):
    n = len(s_list)
    for i in range(n):
        min_el = i
        for j in range(i + 1, n):
            if s_list[j] < s_list[min_el]:
                min_el = j
        s_list[i], s_list[min_el] = s_list[min_el], s_list[i]
    return s_list

test_short = [4, 2, 7, 1, 9]
test_long = [15, 8, 1, 22, 5, 17, 3, 9, 12, 2]
print("Original short list:", test_short)
sorting(test_short)
print("Sorted short list:", test_short)

print("\nOriginal long list:", test_long)
sorting(test_long)
print("Sorted long list:", test_long)