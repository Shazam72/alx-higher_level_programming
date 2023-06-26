#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    _list = []
    for i in range(0, list_length):
        try:
            v = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            v = 0
        except ZeroDivisionError:
            print("division by 0")
            v = 0
        except IndexError:
            print("out of range")
            v = 0
        finally:
            _list.append(v)
    return (_list)
