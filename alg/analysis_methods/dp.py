def get_lengths_leq_than(prices, limit_len):
    if limit_len > 0:
        return [(length, v) for length, v in prices if length <= limit_len]
    else:
        return []


def get_solution_top_bottom(length, optimals, prices, solution):
    if length <= 0:
        return 0
    if optimals[length] > 0:
        return optimals[length]
    else:
        options = get_lengths_leq_than(prices, length)
        max_price = 0
        max_length = 0
        for lng, price in options:
            remain = length - lng
            t = price + get_solution_top_bottom(remain, optimals,
                                                prices, solution)
            if t >= max_price:
                max_price = t
                max_length = lng
        optimals[length] = max_price
        solution[length] = max_length
        return max_price


def get_solution_bottom_top(length, optimals, prices, solution):
    for i in range(1, length + 1):
        options = get_lengths_leq_than(prices, i)
        max = 0
        max_len = 0
        for ln, price in options:
            remain = i - ln
            t = price + optimals[remain]
            if t > max:
                max = t
                max_len = ln
        optimals[i] = max
        solution[i] = max_len
    return optimals[length]
        

def get_optimal_solution(total, prices):
    optimals = [0 for i in range(total+1)]
    solution = optimals[:]
    summed = get_solution_bottom_top(total, optimals, prices, solution)
    slt = []
    i = total
    while i > 0:
        chosen = solution[i]
        slt.append(chosen)
        i -= chosen
    return summed, slt


if __name__ == "__main__":
    total = 30
    prices = [(1, 1), (3, 3), (4, 6), (5, 4)]
    ttl, optimals = get_optimal_solution(total, prices)
    print(optimals)
    print(ttl)
