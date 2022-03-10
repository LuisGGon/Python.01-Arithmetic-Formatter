def arithmetic_arranger(problems, operate = False):
    
    errors  = ['Error: Too many problems.', 
               'Error: Operator must be \'+\' or \'-\'.', 
               'Error: Numbers cannot be more than four digits.',
               'Error: Numbers must only contain digits.']
    
    splitted = splitted_list(problems)
    
    check = checker(splitted)
    if check != -1:
        return errors[check]
   
    normal = normalize(splitted)
    
    up_string = ''
    low_string = ''
    dash_string = ''
    sol_string = ''
    
    count = 0
    while count < len(normal)-1:
        up_string = up_string + normal[count][0] + ' '*4
        low_string = low_string + normal[count][1] + normal[count][2] + ' '*4
        dash_string = dash_string + normal[count][3] + ' '*4
        sol_string = sol_string + normal[count][4] + ' '*4
        count = count + 1
        
    up_string = up_string + normal[-1][0]
    low_string = low_string + normal[-1][1] + normal[-1][2]
    dash_string = dash_string + normal[-1][3]
    sol_string = sol_string + normal[-1][4]

    if operate == False:
        arranged_problems= up_string + '\n' + low_string + '\n' + dash_string
    else:
        arranged_problems= up_string + '\n' + low_string + '\n' + dash_string + '\n' + sol_string
    
    return arranged_problems

def splitted_list(problems):

    splitted = []
    
    for oper in problems:
        splitted.append(oper.split(' '))
        
    return splitted

def add_space(string, n):
    count = 0
    while count < n:
        string = ' '+string
        count = count+1
    return string

def normalize(splitted):
    
    res = []
    
    for k in range(len(splitted)):
        
        maxi = max(len(splitted[k][0]),len(splitted[k][2]))
        
        
        temp = 0
        if splitted[k][1] == '+':
            temp = int(splitted[k][0]) + int(splitted[k][2])
        else:
            temp = int(splitted[k][0]) - int(splitted[k][2])
        
        temp = str(temp)
        temp = add_space(temp, maxi+2-len(temp))
        res.append(temp)

        splitted[k][0] = add_space(splitted[k][0], maxi-len(splitted[k][0]))
        splitted[k][2] = add_space(splitted[k][2], maxi-len(splitted[k][2]))
        splitted[k][1] = splitted[k][1]+' '
        splitted[k][0] = '  '+splitted[k][0]
        splitted[k].append('-'*(maxi+2))
        splitted[k].append(res[k])    
    
    return splitted

def checker(splitted):

    if len(splitted)>5:
        return 0
      
    for element in splitted:
        if element[1] != '+' and element[1] !='-':
            return 1
        if len(element[0])>4 or len(element[2])>4:
            return 2
    for element in splitted:
        try:
            int(element[0])
            int(element[2])
        except:
            return 3
    return -1