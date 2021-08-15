# import libraries
import random
import time
import matplotlib.pyplot as plt


def check_sort(lst):
    """
    Function that performs counting sort
    Precondition:     The list is not sorted
    Arguments:        lst = input list
    Time complexity:  O(N) where N is the length of input list
    Space complexity: O(N) where N is length of input list
    Aux space complexity: None
    Return: True (if sorted) or False
    """

    for s in range(0, len(lst) - 1):
        if lst[s] <= lst[s + 1]:
            continue
        else:
            return False
    return True


def counting_sort(n_list, b, col):
    """
    Function that performs counting sort
    Precondition:     The list is not sorted
    Arguments:        num_list = The list that is the be sorted
                      b = the base used to perform the sort by which
                          each element is placed into boxes (count_array)
    Time complexity:  Best case = O[N+M] where N is the length of list and M is length of count_array
                      Worst case = O(N+M) where N is the length of list and M is length of count_array
    Space complexity: O(N + M) where N is length of input list and M is the length of count array
    Aux space complexity: O(M) where M is the length of count array
    Return: output = sorted num_list
    """
    # step 1: Go through each number in n_list and use
    #         formula: number//base**col % base. The result
    #         is the index of the bucket in which to place the number
    # step 2: After going through the list of numbers, we have a list
    #         of lists which we have to flatten to the output list.

    # Declare and Initialize variables
    output = []
    count_array = []
    for _ in range(b):
        count_array.append([])

    # This code block puts each number in num_list into an
    # appropriate bucket
    for i in range(0, len(n_list)):
        bucket_num = n_list[i] // b**col % b
        count_array[bucket_num].append(n_list[i])

    # This code block goes through the count array and
    # appends the number in each bucket to the output list
    for j in range(len(count_array)):
        if count_array[j] == []:
            continue
        else:
            for number in count_array[j]:
                output.append(number)

    return output


def radix_sort(num_list, b):
    """
    Function that performs radix sort
    Precondition:       The list is not sorted
    Arguments:          num_list = The list that is to be sorted
                        b = the base used to perform the sort by which
                            each element is placed into boxes
    Time complexity:    Best case O(1)
                        Worst case O((N+B)*M) where N is the length of the list
                                                    B is the base
                                                    M is the length of maximum number
    Space complexity:   O(N + B) where N is length of input list and B is the base
    Aux space complexity: O(B) where B is the base
    Return: sorted num_list
    """
    # step 1: Find maximum number in list
    # step 2: Find the value of col which will be plugged into the mathematical
    #         equation that the function depends on
    # step 3: Do counting sort for length col with plugged value starting from 0.

    # Test cases
    if num_list == []:
        print("List is empty")
        return num_list
    elif check_sort(num_list):
        return num_list

    # Declare and Initialize variables
    n_list = num_list
    max_num = n_list[0]
    temp_list = []
    temp = 0

    # Code block from Counting Sort live coding session by Ian
    # Find maximum number in list
    for item in n_list:
        if item > max_num:
            max_num = item

    # Find the number of place values (col) that the number
    # will occupy in base b. This will help in the operation
    # of counting sort.
    for i in range(0, 100):
        c = max_num // b ** i % b
        temp_list.append(c)
    while temp_list[-1] == 0:  # remove trailing 0 to get max col
        temp_list.pop()
    col = len(temp_list)

    while temp < col:
        n_list = counting_sort(n_list, b, temp)
        temp += 1

    return n_list


def time_radix_sort():
    """
    Function that times a radix sort
    Return: list of tuples (base, time (s))
    """

    # Declare and initialize variables
    num_list = [random.randint(1, (2**64) - 1) for _ in range(100)]
    output = []

    base_list = [2, 5, 8, 11, 12, 25, 50]
    for v in range(10000, 100001, 2500):
        base_list.append(v)

    # Find time for each base and append (base, time) into output list
    for base in base_list:
        # time the function only for the radix sort
        start = time.time()
        radix_sort(num_list, base)
        end = time.time()
        time_taken = end - start
        output.append((base, time_taken))

    return output


def rotate_word(word, p):
    """
    Function that rotates a word based on input p
    Precondition:       The word has not been rotated
    Arguments:          word = the input that is to be rotated
                        p = the number of times the word is rotated
    Time complexity:    Best case O(1)
                        Worst case O(M) where M is length of word
    Space complexity:   O(M) where M is length of word
    Aux space complexity: O(M) where M is length of word
    Return: rotated word
    """

    # Declare and initialize variables
    word = list(word)
    length = len(word)
    new_word = []

    # reducing to p < length
    if p > 0:
        while p - length > 0:
            p = p - length
    else:
        while p + length < 0:
            p = p + length
        p = p + length  # turn negative to positive

    # appending appropriate letters to list new_word
    for i in range(p, length):
        new_word.append(word[i])
    for i in range(p):
        new_word.append(word[i])

    return ''.join(new_word)  # converting list new_word to string


def task3_group(lst):
    """
    Function that sorts string into group according to the length of the word
    Precondition:       No groups exist
    Arguments:          lst = input list consisting of words
    Time complexity:    Best  O(N) where N is the length of lst
                        Worst O(N) where N is the length of lst
    Space complexity:   O(N) where N is the length of lst
    Aux space complexity: O(N) where N is the length of lst
    Return: group_array = List consisting of grouped words according to length
    """

    string_list = lst.copy()

    # attaching length with the word and forming a tuple from them
    for i in range(len(string_list)):
        string_list[i] = (string_list[i], len(string_list[i]))

    # finding maximum length
    max_len = string_list[0][1]
    for word_l in string_list:
        if word_l[1] > max_len:
            max_len = word_l[1]

    # intialising group array
    group_array = []
    for _ in range(max_len + 1):
        group_array.append([])

    # putting words in array with length as the index
    for word_l in string_list:
        group_array[word_l[1]].append(word_l[0])

    return group_array


def find_rotations(string_list, p):
    """
    Function which rotates all words in a list and checks if present in the the list
    Arguments:          string_list = The list of words that the rotated words are checked against
                        p = the number of rotations done on the word
    Time complexity:    Best case O(1)
                        Worst case O(NM) where N is the length of input list
                                         where M is the length of the word
    Space complexity:   O(NM) where N is the length of input list
                              where M is the length of the word
    Aux space complexity: O(N) where N is the length of input list
    Return: list of orginal strings whose rotated forms are in the orginal list
    """
    # step 1: get the words in the input list grouped together
    # step 2: generate the list with the words rotated according to p
    # step 3: check whether rotated word is in the original list,
    #         append to output list if it is

    s_list = string_list.copy()
    groups = task3_group(s_list)
    rotated_list = []
    output = []

    if p == 0:
        return s_list

    for i in range(len(s_list)):
        rotated_list.append(rotate_word(s_list[i], p))

    for rotated_word in rotated_list:
        if rotated_word in groups[len(rotated_word)]:
            output.append(rotate_word(rotated_word, -p))

    return output


if __name__ == "__main__":

    # Driver for the test cases

    def test_radix_sort():
        print("TESTING RADIX SORT")
        for _ in range(10):
            num_list = [random.randint(1, (2 ** 64) - 1) for _ in range(50)]
            base = random.randint(2, 1000000)
            sort = radix_sort(num_list, base)

            if check_sort(sort):
                print("PASS")
            else:
                print("FAIL")
                return
        print("PASS ALL")

    def task2_plot():
        # Function to generate the scatter plot for Task 2
        # A graph which shows the effect of base on the time
        # for radix sort
        x = []
        y = []
        list_base_time_tuple = time_radix_sort()

        # Get data from tuple to appropriate list
        for l in range(len(list_base_time_tuple)):
            x.append(list_base_time_tuple[l][0])
            y.append(list_base_time_tuple[l][1])

        plt.scatter(x, y)
        plt.xlabel('Base')
        plt.ylabel('Time')
        plt.show()

    def test_find_rotations():
        print("TESTING FIND ROTATIONS")
        result = [['aaa', 'cab'], ['aaa', 'abc', 'wxyz', 'yzwx'], ['aaa', 'abc', 'cab', 'acb'],
                  ['aaa', 'cab', 'wxyz', 'yzwx'], ['aaa', 'abc'], ['aaa', 'abc', 'cab', 'acb', 'wxyz', 'yzwx'],
                  ['aaa', 'cab'], ['aaa', 'abc', 'wxyz', 'yzwx'], ['aaa', 'abc', 'cab', 'acb'],
                  ['aaa', 'cab', 'wxyz', 'yzwx'], ['aaa', 'abc']]

        lst = ["aaa", "abc", "cab", "acb", "wxyz", "yzwx"]

        for i in range(-5, 6):
            if find_rotations(lst, i) == result[i + 5]:
                print("PASS")
            else:
                print("FAIL")
                break
        print("PASS ALL")

    # test_radix_sort()
    # task2_plot()
    # test_find_rotations()
