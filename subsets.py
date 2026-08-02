def sorted_subset_sums(numbers: set):
    # Put your iterator/generator here. 
    import heapq

    numbers = sorted(numbers)

    yield 0

    if len(numbers) == 0:
        return

    heap = [(numbers[0], 0)]

    while heap:
        total, i = heapq.heappop(heap)
        yield total

        if i + 1 < len(numbers):
            heapq.heappush(heap, (total + numbers[i + 1], i + 1))
            heapq.heappush(heap, (total - numbers[i] + numbers[i + 1], i + 1))

if __name__ == '__main__':
    # from itertools import takewhile, islice
    # for i in eval(input()):
    #     print(i, end=", ")
    pass
