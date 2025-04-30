#inputstr=""

def parse_equation(inputstr):

    if inputstr.count('(')==inputstr.count(')'):
        #print("No. of open paranthesis is equal to close paranthesis")
        
        stack=[]
        #print("Length of input string",len(inputstr))
        final_result=[]

        for i in range(len(inputstr)-1):
            if inputstr[i]==')' and inputstr[i+1]==')':
                stack.pop()
            if inputstr[i]==',' or inputstr[i]==')' or inputstr[i]=='(':
                pass
            else:
                if inputstr[i+1]=='(':
                    stack.append(inputstr[i])
                elif inputstr[i+1]==',':
                    result=[]
                    #print(stack)
                    for ele in stack:
                        result.append(ele)
                    result.append(inputstr[i])
                    #print(result)
                    final_result.append(result)
                elif inputstr[i+1]==')':
                    result=[]
                    #print(stack)
                    for ele in stack:
                        result.append(ele)
                    result.append(inputstr[i])
                    #print(result)
                    stack.pop()
                    #print(stack.pop())
                    final_result.append(result)
        return final_result
        #print(inputstr,"-------",final_result)
    
    else:
        print("No. of open paranthesis is not equal to close paranthesis")

