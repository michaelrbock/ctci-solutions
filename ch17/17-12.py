def pairs_that_sum(lst, val):
    nums = {}
    pairs = []
    for n in lst:
        if n not in nums:
            nums[n] = True
        if (val - n) in nums:
            pairs.append((n, val - n))
    return pairs