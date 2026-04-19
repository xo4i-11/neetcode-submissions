class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i in range(len(temperatures)):

            while len(stack)!=0 and temperatures[stack[-1]] < temperatures[i]:
                latest_day = stack.pop()
                days_num = i - latest_day
                res[latest_day]=days_num

            stack.append(i) #when the stack is empty => just add it in stack without comparing anything
        
        return res


        


    #IDEAS:
    # given an array of int: temperature
    # temperatures[i] represent themp on ith day
    # array: result where result[i] is the number of day after such that the temp become warmer

    # Create an arraylist with [0]*len(temperatures) to represent the result
    # We gonna use a stack to track the index of the element that is waiting to have a warmer day coming after

    #we gonna loop through every elem inside the temperatures array:
    # while it have not not met the warmer day => keep adding to the stack
    #if it reach the day that have a warmer temperature compare to THE LATEST DAY => we gonna add the day to the correct position in result list

    #example:  temperatures = [30,38,30,36,35,40,28]
    # i=0
    #   res= [0,0,0,0,0,0,0]
    #   stack=[0]

    #i=1
    # res=[1,0,0,0,0,0,0]
    # stack=[1]

    #i=2
    #res=[1,0,0,0,0,0,0]
    #stack=[1,2]

    #i=3
    #res=[1,0,1,0,0,0,0]
    #stack=[1,3]

    #i=4
    #res=[1,0,1,0,0,0,0]
    #stack=[1,3,4]

    #i=5
    #res=[1,4,1,2,1,0,0]
    #stack=[5]

    #i=6
    #res=[1,4,1,2,1,0,0]
    #stack=[5,6]



    







































