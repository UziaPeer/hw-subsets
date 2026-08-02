import pytest
from subsets import sorted_subset_sums
from testcases import parse_testcases

testcases = parse_testcases("testcases.txt")

def run_testcase(input:str):
    from itertools import takewhile, islice
    output = ""
    for i in eval(input):
        output += f"{i}, "
    output = output[:-2]  # remove last comma
    return output

@pytest.mark.parametrize("testcase", testcases, ids=[testcase["name"] for testcase in testcases])
def test_cases(testcase):
    actual_output = run_testcase(testcase["input"])
    assert actual_output == testcase["output"], f"Expected {testcase['output']}, got {actual_output}"


def test_new_cases():
    from itertools import islice, takewhile

    assert list(sorted_subset_sums([1, 2, 4])) == [0, 1, 2, 3, 4, 5, 6, 7]

    assert list(sorted_subset_sums([1, 2, 3])) == [0, 1, 2, 3, 3, 4, 5, 6]

    assert list(sorted_subset_sums([2, 3, 4])) == [0, 2, 3, 4, 5, 6, 7, 9]

    assert list(islice(sorted_subset_sums(range(100)), 5)) == [0, 0, 1, 1, 2]

    assert list(takewhile(lambda x: x <= 6, sorted_subset_sums(range(1, 100)))) == [
        0, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6
    ]

    assert list(sorted_subset_sums([])) == [0]

    assert list(sorted_subset_sums([5])) == [0, 5]
