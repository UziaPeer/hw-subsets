def sorted_subset_sums(numbers: set):
    import heapq

    numbers = sorted(numbers)

    heap = [(0, 0)]

    while heap:
        total, i = heapq.heappop(heap)
        yield total

        if i < len(numbers):
            heapq.heappush(heap, (total + numbers[i], i + 1))
            heapq.heappush(heap, (total, i + 1))

if __name__ == '__main__':
    # from itertools import takewhile, islice
    # for i in eval(input()):
    #     print(i, end=", ")
    pass
