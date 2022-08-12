import math

#this function receives a string line as a parameter,
#splittes it into two parts, and returns that two parts
def get_nums(line):
    temp = line.split()
    return (str(temp[0]), str(temp[1]), str(temp[2]))


#this function returns true if the given string 
#is a real number
def is_float(str):
    try: 
        float(str)
    except ValueError: 
        return False
    return True

#this function solves the ax+b=0 linear equation, where str1=a, str2=b
#and returns the answer as a string
def linear(str1, str2):
    if (not is_float(str1) or not is_float(str2)):
        return 'mistake'
    else:
        a = float(str1)
        b = float(str2)
        if (a == 0 and b == 0):
            return "R"
        elif (b != 0 and a == 0):
            return "no solution"
        elif (b == 0):
            return "0"
        else:
            d = float("{0:.3f}".format(- b / a))
            if (d.is_integer()):
                d = int(d)
            return str(d)

#this function solves the quadratic equation ax^2+bx+c=0, where a, b, and c are given as 
#str1, str2, str3.  Answer is written in the <answer> string
def quadr(str1, str2, str3):
    if(not is_float(str1) or not is_float(str2) or not is_float(str3)):
        return "mistake"
    else:
        a = float(str1)
        if(a == 0):
            return linear(str2, str3)
        else:
            b = float(str2)
            c = float(str3)
            d = b * b - 4 * a * c; #discriminant
            if(d == 0):
                temp = float("{0:.3f}".format(- b / ( 2 * a )))
                if (temp.is_integer()):
                    temp = int(temp)
                return str(temp)
            elif (d < 0):
                return "no solution"
            else:
                s1 = "{0:.3f}".format((- b + math.sqrt(d)) / (2 * a));
                s2 = "{0:.3f}".format((-b - math.sqrt(d)) / (2 * a));
                s1 = float(s1)
                s2 = float (s2)
                if(s1.is_integer()):
                    s1 = int(s1)
                if(s2.is_integer()):
                    s2 = int(s2)  
                if(s2 > s1):    
                	return str(s1) + ' ' + str(s2)
                else:
                	return str(s2) + ' ' + str(s1)


