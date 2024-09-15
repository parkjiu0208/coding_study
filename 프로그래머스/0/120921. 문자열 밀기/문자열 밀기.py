def solution (A, B):
    if A == B: 
        return 0

    N = len(A)
    for i in range(1, N):
        is_equal = True
        for j in range(N): 
            if A[j] != B[(i+j) % N]:
                is_equal = False
                break 
        if is_equal:
            return i
    return -1