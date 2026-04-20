class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # given an array: "position" where position[i] is the position of ith car
        # given an array:  "speed" where speed[i] is the speed of ith car
        # destination: "target"

        # a car cannot pass the car ahead, can only catch up with the same speed
        # "car fleet" is a non-empty set of cars driving at the same positon and speed
        # if a car catch up with the car fleet at the destination => that car is a part of the fleet
        # return the number of different car fleets that arrive at destination 


        #Thinking:
        # we can find if the car intersect each other by finding the time they reach the destination.
        # if the car behind reach the destination within fewer hours than the car in front of => they must intersect 
        # else: they would not


        #Approach:
        # we gonna create a list of cars, each car means key, value pair of positon and speed
        # we gonna sort them backward so that we can find how much time that the closest car reach the destnation 

        # create a stack to store the fleet
        # if the closest car reach the dest fater than the prev => add it to the stack to represent a fleet 
        # else if it is slower => remove the faster car (since faster car will merge with slower one) and keep compare to the prev


        cars=[]

        for i in range(len(position)):
            car = [position[i],speed[i]]
            cars.append(car)
        
        car.sort (reverse=True) #sort desending by position

        stack=[]

        for car in cars:
            position = car[0]
            speed = car[1]
            time = (target-position)/speed
            stack.append(time)

            while len(stack)>=2 and stack[-1]<= stack[-2]:
                stack.pop()
        
        return len(stack)



