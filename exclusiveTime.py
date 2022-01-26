import re
from typing import List

class SolutionOld:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ongoing_stack = []
        res = [0]*n
        
        for i in range(len(logs[:-1])):
            curr_fun, curr_start_ind, curr_time = re.split(':', logs[i])            
            next_fun, next_start_ind, next_time = re.split(':', logs[i+1])
            
            curr_fun = int(curr_fun)
            curr_time = int(curr_time)
            next_fun = int(next_fun)
            next_time = int(next_time)

            if curr_start_ind == "start":
                ongoing_stack.append(curr_fun)
            else:
                ongoing_stack.pop()

            time_interval = next_time - curr_time
            
            if curr_start_ind == "start" and next_start_ind == "end":
                time_interval +=1  
            elif curr_start_ind == "end" and next_start_ind == "start":
                time_interval -=1
            
            if ongoing_stack:
                active_fn = ongoing_stack[-1]
                res[active_fn] += time_interval
            
        return res

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ongoing_stack = []
        res = [0]*n
        prev_time = 0
        
        for log in logs:
            curr_fun, curr_start_ind, curr_time = log.split(':')            
            curr_fun = int(curr_fun)
            curr_time = int(curr_time)
            
            if curr_start_ind == "start":
                if ongoing_stack:
                    res[ongoing_stack[-1]] += curr_time - prev_time
                ongoing_stack.append(curr_fun)
                prev_time = curr_time
            else:
                res[ongoing_stack.pop()] += curr_time - prev_time + 1
                prev_time = curr_time + 1
            
        return res

n = 3
logs = ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]

print(Solution().exclusiveTime(n, logs))
