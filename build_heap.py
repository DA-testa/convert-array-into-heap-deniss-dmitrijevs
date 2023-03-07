# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)

    n = len(data)

    #sift_down each non-leaf node from the lowest most-right one
    #not including -1
    for i in range(n // 2, -1, -1):
        sift_down(i, data, swaps)

    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    r_child = 2 * i + 2
    l_child = 2 * i + 1

    incorrect_child_candidate = 0

    if l_child < len(data):
        #pick best fitting child (smallest in min-heap) to swap with parent
        if r_child >= n or not correct_parent_to_child_relation(data[r_child], data[l_child]):
            incorrect_child_candidate = l_child
        else:
            incorrect_child_candidate = r_child

        if not correct_parent_to_child_relation(data[i], data[incorrect_child_candidate]):
            swaps.append([i, incorrect_child_candidate])
            data[i], data[incorrect_child_candidate] = data[incorrect_child_candidate], data[i]
            #check if subtree of swapped child is in correct relation
            sift_down(incorrect_child_candidate, data, swaps)
        


def correct_parent_to_child_relation(parent, child):
    if parent <= child:
        return True
    else:
        return False

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    input_type = input()
    if 'I' in input_type:
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif 'F' in input_type:
        file_name = str(input())
        path = "tests/" + file_name
        if not "a" in path:
            with open(path, 'r') as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
    else:
        exit()
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    if not 'F' in input_type:
        for i, j in swaps:
            print(i, j)


if __name__ == "__main__":
    main()
