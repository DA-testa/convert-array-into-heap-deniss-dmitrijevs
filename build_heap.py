# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)

    for i in range(n // 2 + 1, 0, -1):
        sift_down(i, data, swaps)

    print(data)
    return swaps

def sift_down(i, data, swaps):
    r_child = 2 * i + 2
    l_child = 2 * i + 1

    incorrect_child = 0

    if r_child < len(data):
        if not correct_parent_to_child_relation(data[i], data[r_child]):
            incorrect_child = r_child
            data[i], data[r_child] =  data[r_child], data[i]
            swaps.append([i, r_child])
            sift_down(i // 2, data, swaps)
    if l_child < len(data):
        if not correct_parent_to_child_relation(data[i], data[l_child]):
            incorrect_child = r_child
            data[i], data[l_child] =  data[l_child], data[i]
            swaps.append([i, l_child])
            sift_down(i // 2, data, swaps)


def correct_parent_to_child_relation(parent, child):
    if parent <= child:
        return True
    else:
        return False

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
