def sorted_subset_sums(numbers: set):
    import heapq

    numbers = sorted(numbers)
    heap = [(0, -1)]
    seen = {(0, -1)}

    while heap:
        total, i = heapq.heappop(heap)
        yield total

        j = i + 1
        if j < len(numbers):
            option1 = (total + numbers[j], j)
            if option1 not in seen:
                seen.add(option1)
                heapq.heappush(heap, option1)

            if i >= 0:
                option2 = (total - numbers[i] + numbers[j], j)
                if option2 not in seen:
                    seen.add(option2)
                    heapq.heappush(heap, option2)

if __name__ == '__main__':
    # from itertools import takewhile, islice
    # for i in eval(input()):
    #     print(i, end=", ")
    pass
