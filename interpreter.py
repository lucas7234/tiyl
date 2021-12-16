import re

#Variable Dictionaries
variable = {}

#Regular Expressions
variablenamep = re.compile("[A-Za-z]+\s")
variablevaluep = re.compile("\s[A-Za-z]+[.]")
printvarp = re.compile("[(][A-Za-z]+[)]")
printstringp = re.compile("[A-Za-z]*[(][A-Za-z]+[)][A-Za-z]*")

while True:
    command = input(">>> ")
    if 'is' in command or 'IS' in command:
        varname = variablenamep.findall(command)[0][0:len(variablenamep.findall(command)[0])-2] - 1]
        varvalue = variable.findall(command)[0][1:len(variable.findall(command)[0]-1)
        variable[varname] = varvalue
    elif '(' is in command and ')' is in command:
        vartoprint = printvarp.findall(command)[0][1:len(printvarp.findall(command)[0])-2]
        printstring = printvarp.sub(variable.get(vartoprint, 0), command)
        print(printstring)
    else: print(command)
    print()
