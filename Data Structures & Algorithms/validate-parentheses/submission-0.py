class Solution:
    def isValid(self, s: str) -> bool:
        
        #given a string of (),{},[]
        #for example:"{()}"

        #valid:
        # +) if we got ( then we must have this ) (make sure the close have to be after the open)
        # +) have to be in correct order, {[}] is invalid


        #IDEAS:
        #we have a string "{()}"
        #we want to check that ) have ( and } have { => we delete } first and find if there is any { to delete as well 
        #=> we use stack since it will remove from top (we can use the end) and we use hashmap to check if it has a pair or no (check at the top)

        #we gonna an array to hold the parenthecies , if empty=> true, else is false
        stack=[]

        #we then create a hashmap to create a pair of closing paran and open paren
        closeToOpen ={'}' : '{', ')' : '(', ']' : '['}

        #we want to find the closing paren, delete it and tryna delete its other opening pair
        #add those opening to the stack and remove it when looping through its correspond closing
        for char in s:
            if( char in closeToOpen):
                if stack and stack[-1] == closeToOpen[char]:  # check if the first paren match the last paren and the stack is not empty
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(char)
        
        if not stack: # if the stack =[]
            return True
        else:
            return False


        
        