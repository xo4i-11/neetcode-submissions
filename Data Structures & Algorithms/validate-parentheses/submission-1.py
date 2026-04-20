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
        pair={'}' : '{', ']' : '[', ')' : '('}

        for c in s:
            if c not in pair:
                stack.append(c)
            else:
                stack.pop()
        
        if len(stack)==0:
            return True
        return False


        


#ideas:
# we see that the first and the last char must be the right pair
# we gonna use a stack to store the seen element => stack=[]

# first, we gonna store the correct pair of parenthis:
# => hashmap={'}' : '{', ']' : '[', ')' : '('}
# next, we gonna loop through the string to check if the closing bracket if in string or not:
# if not => append to the end stack 
#if yes => remove from the end of the stack -> pop (LIFO RULES)

#if the stack still have elem => false
#if it is empty => correct

#[(,[,{]
        stack=[]
        pair={'}' : '{', ']' : '[', ')' : '('}

        for c in s:
            if c not in pair:
                stack.append(c)
            else:
                stack.pop()
        
        if len(stack)==0:
            return True
        return False
        






















































        


        