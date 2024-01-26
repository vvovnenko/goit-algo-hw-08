import heapq


def calc_min_cost(cables: list):
    cost = 0
    h = cables[:]
    heapq.heapify(h)

    print('heap = ', h)

    while len(h) > 1:
        cable_1 = heapq.heappop(h)
        cable_2 = heapq.heappop(h)
        connection_cost = cable_1 + cable_2
        print(f'connecting cables {cable_1} and {cable_2} with cost {connection_cost}')
        cost += connection_cost
        heapq.heappush(h, connection_cost)
        print('heap = ', h)

    return cost


print(calc_min_cost([1, 2, 4, 10]))
