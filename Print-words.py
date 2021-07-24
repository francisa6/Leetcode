

def change_i(input, ind):
    # while (ind < len_word):
    for i in char_list:
        
        input[ind] = i
        ind +=  1 
        if ind == len(input)  :
            print(input, i, ind)
            ind = 0
            continue 
        else:
            input = change_i(input, ind )
            
    return input


len_word = 3
input = ['a'] * len_word
char_list = ['a', 'b', 'c']
ind = 0


change_i(input, ind)


l = 'a'
var = 'b'

def test(l, var):
    l = l + var
    if len(l) == 3:
        return print(l)
    l = test(l, var)
    