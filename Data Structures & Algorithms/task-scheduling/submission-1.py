class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) == 0 :
            return 0
        
        # 1. count fequency of every task
        hashmap = {}
        for task in tasks:
            if task in hashmap:
                hashmap[task] +=1
            else:
                hashmap[task] = 1

        # 2. Find maximum frequency
        max_frequency = max(hashmap.values())

        # 3. count how many task have max frequency
        max_frequency_task_count = 0

        for val in hashmap.values():
            if val == max_frequency:
                max_frequency_task_count +=1
        

        # 4. Build the skeleton/gaps
        #
        # Example:
        # A A A, n = 2
        #
        # A _ _ A _ _ A
        #
        # Each gap has n + 1 positions including the
        # task at the beginning of the gap.
        
        skeletons = (max_frequency-1)*(n+1) + max_frequency_task_count 
        return max(len(tasks), skeletons)











"""
problem:
    - tasks: array of CPU tasks
    - tasks[i]: upper char from A->Z
    - n: int 

    - tasks maybe completed in any order 
    - idential tasks must be separated by at least n CPU cycles
    - return min num of cycle 

idea:
    1. Count frequency of every task
    2. Find maximum frequency
    3. Put the most frequent task into a skeleton
    4. Create gaps of size n
    5. Fill gaps with other tasks
    6. If gaps remain → idle
    7. If all gaps are filled → answer = number of tasks

"""