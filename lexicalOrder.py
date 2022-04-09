class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def f(curr_num):
            # if 'curr_num'+'0' <= n then add zero to end
            curr_str = str(curr_num)
            n0 = int(curr_str + '0')
            if n0 <= n:
                return n0
            # elif remove all consecutive 9s from back and add 1. Unless it's empty then it's done
            elif curr_str[-1] == '9':
                while curr_str:
                    if int(curr_str[-j]) % 10 == 9:
                        curr_num = curr_num % 10
                        curr_str = str(curr_num)
                    else: 
                        return curr_num
                    j+=1
            # elif curr_num + 1   <= n 
            elif curr_num + 1 <=n:
                return curr_num + 1
            # else curr_num + 1 > n then remove last digit and add 1
            elif curr_num + 1 > n:
                return int(curr_str[:-1]) + 1
            else:
                return -1
            
        
        curr_num = 1
        for i in range(n):   
            yield curr_num
            curr_num = f(curr_num)
            