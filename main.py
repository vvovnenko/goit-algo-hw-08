import heapq


def calc_min_cost(cables: list):
    h = cables[:]
    heapq.heapify(h)

    print('heap = ', h)

    while len(h) > 1:
        cable_1 = heapq.heappop(h)
        cable_2 = heapq.heappop(h)
        print(f'connecting cables {cable_1} and {cable_2}')
        heapq.heappush(h, cable_1 + cable_2)
        print('heap = ', h)


    return h.pop()


print(calc_min_cost([1, 2, 4, 10]))
