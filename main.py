file = open('abc.txt', 'r')#open file for reading
string = file.read()#reading the opened file

def word_split(input_string):#function which will take string as input and will give result
    results= []#empty array to store the final result
    temporary_variable= ""#container to hold the temporary values until they are appended in the resultslist
    lines = input_string.split("\n")  #when reading from a file we use this to get an array of all the lines in that file
    is_comment = False  #its false value will treat it as code and process it

    separators = [';', ',', '\n', ':', '.', '[', ']', '{', '}', '(', ')', '+', '-', '*', '/', '//', '%', '**', '=', '+=', '-=', '*=', '/=', '//=', '%=', '**=', '==', '!=', '>', '<', '>=', '<=', 'not', 'and', 'or', '~', '&', '|', '^', '<<', '>>', 'is', 'is not', 'in', 'not in']
    #list of all separators
    for line in lines: #we use loop on the lines of file that we had split
        #to take each line at a time and process it to fulfil our requirements
        if line.startswith("#"):
            is_comment = True
            #this condition will treat the line as if it is a comment and will not process it
            #resulting in an empty array
        else:
            is_comment = False
            #otherwise it will be shifted to false to continue the processing
        if is_comment:
            continue  #skip lines within a comment block

        for char in line:
            #this loop will take each character from a line at a time and process it to fulfil our requirements
            if char != ' ':#if char is not equal to space (first condition)
                if char in separators:#and character is in separators list  (second condition)
                    if temporary_variable!= "":#and if our temporary variable is empty (third condition)
                        results.append(temporary_variable)#it will add our temporary variable's value to the resultsarray 
                        temporary_variable= ""#it will again empty the temporary variable for next iteration
                    results.append(char)#this line will add the separator to the results array
                else:
                    #otherwise if character is not in separators list (second condition)
                    #it will simply add the character to our temporary variable
                    temporary_variable+= char
            else:#otherwise character is equals to space (first condition)
                if temporary_variable!= "": #and temporary variable is not empty 
                    results.append(temporary_variable)#it will append the temporary variable to results array
                    temporary_variable= ""#it will again empty the temporary variable for next iteration

        if temporary_variable!= "":#if temporary variable is not empty
            #this condition will arise in the case char != space and char is not in separators list
            results.append(temporary_variable)#it will add the temporary_variableto results array 
            temporary_variable= ""#it will again empty the temporary variable for next iteration

    return results #this will return the results 


output = word_split(string) #here i have made a variable to store the return value of my function
print(output)#at last i can print my output to see the result
