class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []

        res = [0] * len(temperatures)
        stack = []


        for i in range(len(temperatures)):
            
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                latest_day = stack.pop()
                days = i - latest_day
                res[latest_day] = days

            stack.append(i)

        return res          









"""
problem: 
    - given a list of temperature
    - output: a list of number of days that temperature is higher than that day

idea:
1. Create a result list filled with zeros.
2. Use a stack to store pairs of (temperature, index) for days that haven't found a warmer day yet.
3. Iterate through the temperature list:
    - While the stack is not empty and the current temperature is warmer than the top of the stack:
        + Pop the top element.
        + Compute how many days passed and update the result.
    - Push the current day onto the stack.
    
4. Return the filled result list.

"""
        