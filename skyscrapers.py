def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']
    """
    with open(path) as f:
        content = f.readlines()

    lst = [obj[:-1] for obj in content if obj[-1] != '*']

    if lst[-1] != content[-1]:
        lst.append(content[-1])
    return lst
# print(read_input('semester2/lab1/check.txt'))

def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    if input_line[0] != "*":
        if str(pivot) == input_line[0]:
            return True
        return False
    if input_line[-1] != "*":
        if str(pivot) == input_line[-1]:
            return True
        return False
# print(left_to_right_check("412453*", 4))

def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    """
    
    lst = ["F" for item in board if "?" in item]
    
    if "F" in lst:
        return False
    return True
# print(check_not_finished_board(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    lst = []
    # board = [item.replace("*", "") for item in board]
    for obj in board:
        if str(len(obj)) not in obj:
            if obj[0] != "*":
                obj = obj[1:]
            if obj[-1] != "*":
                obj = obj[:-1]
        for el in obj:
            if obj.count(el) == 2 and el != "*":
                lst.append("f")
    if "f" in lst:
        return False
    return True
# print(check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))
            
def f_list(item):
    new_list = []
    lst = [item[1]]

    if int(lst[0]) == len(item[1:-1]):
        if int(item[0]) != 1:
            new_list = ["f"]
    else:
        for i in range(2, len(item) - 1):
            if int(item[i]) > int(item[i -1]):
                lst.append(item[i])

        for j in range(len(lst) - 1):
            k = j - 1
            while k < len(lst) - 1:
                k += 1
                if int(lst[k]) < int(lst[j]):
                    lst.pop(k)
                    # k += 1
                
        if len(lst) != int(item[0]):
            new_list.append("f")
    
    return new_list
# print(f_list('412453*'))

def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    lst = []
    
    for item in board: 
        
        if item[0] != "*" and item[-1] == "*":
            for el in f_list(item):
                lst.append(el)

        if item[0] == "*" and item[-1] != "*":
            item = item[::-1]
            for el in f_list(item):
                lst.append(el)    
        
        elif item[0] != "*" and item[-1] != "*":
            # l = f_list(item)
            for el in f_list(item):
                lst.append(el)
                
            item = item[::-1]
            # l1 = f_list(item)
            for el in f_list(item):
                lst.append(el)
    
    if "f" in lst:
        return False
    return True           
# print(check_horizontal_visibility(['2413251']))

def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    lst = []
    for i in range(len(board[0])):
        column = ''
        for item in board:
            column += item[i]
        lst.append(column)
    lst = lst[1:-1]
    # return lst
    if check_uniqueness_in_rows(lst) == True and \
        check_horizontal_visibility(lst) == True:
        return True
    return False
# print(check_columns(['***21**', '412453*', '423145*', '*543215', '*35214*', '*41532*', '*2*1***']))

def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    board = read_input(input_path)
    if check_not_finished_board(board) == True and\
        check_uniqueness_in_rows(board) == True and\
        check_horizontal_visibility(board) == True and\
        check_columns(board) == True:
        return True
    return False

if __name__ == "__main__":
    print(check_skyscrapers("semester2/lab1/check.txt"))