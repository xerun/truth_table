#Automation of Truth Assignment
# ---
# ##### 1. Run the application and input a Propositional Sentence in the text box
# ##### 2. System breaks down the variables from the sentence and replaces all the operators using replace_operators()
# ##### 3. The function find_truth_values() is used to do a recursive loop and find all the truth values
# ##### 4. Show the final truth value of the sentence.
# ---
# REPLACE OPERATORS function
# ---
# The function "replace_operators" replaces all the proposition in the given statement 
def replace_operators(string):
    for vrV in range(0, len(variableValues)):
        # Define the variables with True and False in propositional sentence
        string = string.replace(variables[vrV], "True" if variableValues[vrV] == 'T' else 'False')   
        
    # replace TRUE with True in propositional sentence
    string = string.replace("TRUE", "True")   
    # replace FLASE with False in propositional sentence 
    string = string.replace("FALSE", "False") 
    # replace AND proposition with & in propositional sentence   
    string = string.replace("AND", "&")    
    # replace THEN(implies) with <= proposition with & in propositional sentence    
    string = string.replace("THEN", "<=")  
    # replace EQ(<->) with == proposition with & in propositional sentence  
    string = string.replace("EQ", "==")   
    # replace OR with | proposition with & in propositional sentence     
    string = string.replace("OR", "|")        
    # replace -(NOT) with ~ proposition with & in propositional sentence
    string = string.replace("- ", "~")        
    return string
# ---
# CHANGE NEGETION function
# ---
# After the final value is found, this function will check if contains any negation, if it does then it will flip it into True or False.
def change_negetion(statement):
    # Split all the words and store in an array
    statement_split_words = statement.split() 
    #print(statement_split_words)
    # Loop through the array and replaces the negation with True or False
    for words in list(statement_split_words):           
        statement = statement.replace('~True','False')
        statement = statement.replace('~False','True')    
    # Return the final statement
    return statement
# ---
# FIND TRUTH VALUES function
# ---
def find_truth_values(statement):
    # Store all the operators in an array
    operators = {
        '&',
        '|',
        '<=',
        '==',
        }
    # Split all the words and store in an array
    statement_split_words = statement.split()
    # Loop through the array word by word
    for i, char in enumerate(list(statement_split_words)):
        # Check if the word matches the operators, if it does then go inside the if condition
        if char in operators:   
            # Store the operator in a variable
            logical_expression = statement_split_words[i]
            #print(logical_expression)
            # Find the left and right truth value of the operator
            truth_value_1, truth_value_2 = (statement_split_words[i-1]), (statement_split_words[i+1])
            # Go inside the if condition only if there is True or False in the values, do not go inside if it has parentheses before or after the operator
            if (truth_value_1 == 'True' or truth_value_1 == 'False') and (truth_value_2 == 'True' or truth_value_2 == 'False'):
                # If there are parentheses before and after the truth values then add it with the values for example: "( True and False)" else just combine the truth values with the operator and store in logical variable
                if statement_split_words[i-2] == '(' and statement_split_words[i+2] == ')':
                    logical = "( "+truth_value_1+" "+logical_expression+" "+truth_value_2+" )"
                else:
                    logical = truth_value_1+" "+logical_expression+" "+truth_value_2 
                # Find the truth value using eval
                value = eval(logical)
                # Replace part of the statement with the value found using replace function
                statement = statement.replace(logical,str(value))                
    # If the length of the statement is greater than 5 then recall "find_truth_values" again. Keep doing recursion until the length of the statement is less than 6  
    if (len(statement)>5):
        statement=find_truth_values(statement)
    else:
        statement
    # Finally return the statement    
    return statement
# ---    
# Input propositional sentence
try:
    try:
        fname='q1_in.txt'
        with open(fname) as f:
            content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content] 
        #print(content)
    except IOError:
        print ("Could not read file:", fname)

    file_output=''
    for problem in list(content): 
        try:
            #problem =input()  
            # Split strings with tab propositional sentence
            problemT = (problem.split("\t"))   
            # Split strings with comma propositional sentence 
            variables =  (problemT[0].split(","))   
            # Split strings with comma propositional sentence
            variableValues = (problemT[1].split(","))    
            # Call the "replace_operators" to change all the operators
            statement=replace_operators(problemT[2])
            # Call the negation function then find the truth value of the statement
            result = find_truth_values(change_negetion(statement))
            # Show the output as TRUE if the result is True else show FALSE
            if(result=='True'):
                # if the sentence is true then return True
                #print ('TRUE') 
                file_output+='TRUE\n'
            else:
                # else return False
                #print ('FALSE') 
                file_output+='FALSE\n' 
        except:
            #print('Failed to find true value')
            file_output+='FAIL\n'
    print('Please check the file q1_out.txt for output') 
    with open('q1_out.txt', 'w') as f:
        print(file_output, file=f)
except:
    print('Program failed to execute')