class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Create a list of car
        cars = []

        for i in range(len(position)):
            car = (position[i], speed[i])
            cars.append(car)
        
        # sort descending by position
        cars.sort(reverse = True)
        
        # 2. use a stack 
        # The stack stores fleet arrival times
        stack = []
        for car in cars:
            position = car[0]
            speed = car[1]
            time = (target-position) / speed 
            stack.append(time)
        
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack) 
        






"""
problem:
    - car cannot pass another car head
    - if a car catch up with the fleet, the car will be considered as a part of the fleet 
    - return # of different car fleet

idea:
    TLDR: + CREATE A LIST TO STORE THE CAR (CAR = [POSTITION, SPEED])
          + CREATE A STACK TO STORE THE FLEET
        
    
    1. create a list of car (car = (position, speed)), then sort descending by position
    2. stack idea: 
        - the stack stores: Arrival times of fleets.
        - When processing a new car: current_time <= top_time -> current car catch the fleet -> do nothing
        - Otherwise: current_time > top_time -> cannot catch -> push a new fleet 
    

"""