def cnt_non_zeros(a):
    cnt = 0
    for i in range(0, len(a)):
        if a[i] != 0:
            cnt += 1
    return cnt
