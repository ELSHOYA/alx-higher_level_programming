#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_len = len(my_list)
    if idx < 0 or  idx > len(my_list)-1:
        return my_list.copy()
    else:
        my_list.copy()[idx] = element
        return my_list.copy()
