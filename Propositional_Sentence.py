#@title Propositional Sentence Classifier
# ---
# ##### 1. Run the application and input a Propositional Sentence in the text box
# ##### 2. System breaks down the variables from the sentence and calculate the number of possible sentences to make based on the number of variables and replaces all the operators using replace_operators()
# ##### 3. The function find_truth_values() is used to do a recursive loop and find all the truth values
# ##### 4. All the truth values checked to see if they are Tautology, Contingency or Contradiction 
# ##### 5. Show the final classifier of the given propositional sentence. 
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
# REPLACE OPERATORS function
# ---
# The function "replace_operators" replaces all the proposition in the given statement 
def replace_operators(string,variables_count):
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
    # Get the maximum length of the row count in binary
    max_num=len(str(bin(variables_count-1)[2:]))
    # Create an array for propositional_sentences
    propositional_sentences=[]
    # Loop through the number of rows for the given variables of Propositional Sentence
    for i in range(variables_count):
        propositional=string
        # Create a binary number for the current row. Pad the leading zeroes, for 1 pad two zeroes to make 001, for 10, pad one zero to make 010 etc. 101 needs to padding
        current_bin_num = bin(i)[2:].zfill(max_num)
        # Loop through all the numbers of binary number for example 101.
        for row in range(0, len(current_bin_num)):
            # Make 1 into True and 0 into False and replace the statement
            propositional=propositional.replace(variables[row], "True" if current_bin_num[row] == '1' else 'False')    #Define the variables with True and False in propositional sentence
        # Add the statement with the turth values in the propositional_sentences array
        propositional_sentences.append(change_negetion(propositional))
    return propositional_sentences
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
        #print(char)
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
                #print(logical)  
                # Find the truth value using eval
                value = eval(logical)
                # Replace part of the statement with the value found using replace function
                statement = statement.replace(logical,str(value))  
                #print(statement)
        # If the operator has parentheses "( True )" then remove the parentheses and replace the statement
        elif statement_split_words[i-1] == '(' and statement_split_words[i+1] == ')':
            logical = "( "+statement_split_words[i]+" )"
            statement = statement.replace(logical,statement_split_words[i]) 
            #print(statement) 
    # If the length of the statement is greater than 10 then recall "find_truth_values" again. Keep doing recursion until the length of the statement is less than 11               
    if (len(statement)>10):
        statement=find_truth_values(statement)
    else:
        statement
    # Finally return the statement 
    return statement
# ---    
# Input propositional sentence
try:
    try:
        fname='q2_in.txt'
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
            # Split strings with tab propositional sentence
            problemT = (problem.split("\t"))    
            # Split strings with comma propositional sentence 
            variables =  (problemT[0].split(","))
            # Calculate the maximum number of rows needed in the truth table, 2 variables => 4 rows, 3 variables => 8 rows and so on
            variables_row_count = 2 ** len(variables)
            # Call the "replace_operators" to create all the possible truth statements for the given variables and replace the operators
            sentence = replace_operators(problemT[1],variables_row_count)
            # Declare a count_all variable to sum up all the values of the truth statement
            count_all=0
            # Loop through all the sentences to check if it is True or False as 1 and 0
            for classify in list(sentence):
                #print(classify)
                result=find_truth_values(classify)
                if result=='~( False )':
                    # If the Value is True then add 1 to the count_all variable
                    count_all+=1
                if result=='~( True )':
                    # If the Value is False then add 0 to the count_all variable
                    count_all+=0
                if result=='True':
                    count_all+=1
                if result=='False':
                    count_all+=0
            # If the count_all is same as variables_row_count then all statements are True therefore it is Tautology
            if count_all == variables_row_count:
                #print ('Tautology')
                file_output+='Tautology\n'
            # If the count_all is 0 then all statements are False therefore it is Contingency
            elif count_all == 0:
                #print ('Contingency')
                file_output+='Contradiction\n'
            # Otherwise if it has both True and False it is Contradiction
            else:
                #print ('Contradiction')
                file_output+='Contingency\n'
        except:
            #print('Failed to find true value')
            file_output+='FAIL\n'
    print('Please check the file q2_out.txt for output')
    with open('q2_out.txt', 'w') as f:
        print(file_output, file=f)
except:
    print('Program failed to execute')