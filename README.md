#description of the main program
this program finds the solution of the ax^2+bx+c=0 equation, where a, b and c numbers are written in the input file like this:
 num1 num2 num3
 num1 num2 num3
 ...
after the execution the answers will be store in the output file like this:
 answer1
 answer2
 ... 

# quadr_test.py (testing file) description
This project performs the following operations for every line in the input file:
1)reads three input values from the input file,which are the <a>,  <b> and <c> in 'ax^2+bx+c=0' equation, 
2)writes the solution in the output file, 
3)compares the result value with the corresponding value in the golden file
4)writes the appropriate message in the result file 

If the current values of the input file aren't real numbers, the answer is "mistake"
If the solution is (-inf, +inf), the answer is 'R'
if there is no solution the answer is "no solution"
if there are 2 solutions the answers are written from the small to the large
in my golden_file all the double numbers' precisions are set to 3 
(for excample if the result of the computation is 3.876543, the answer will be 3.876)

#files
 in this directory there are following files
* input.txt __ it is the file where our input values are written
* golden.txt __ it is the file where our correct answers are written
* quadr_functions.py __here is the function that solves the quadratic equation and there are some other related functions
* quadr_test.py __ this file contains the operations of reading from the input file, 
  solving and writing in the output and result files (testing)
* main.py __ this file contains the program which solves our main problem (without testing)

the files that will be generated are 
*output.txt__here result-values are written
*result.txt__here test results are written(test passed or not)
*__pycache__(this directory is generated because I import the functions from a file into another)


#to run the main program type in command line
 python3 main.py
to clean the generated files type 
 rm output.txt
 rm -r __pycache__


#to run the test type in command line
 python3 quadr_test.py
to clean the generated files type 
 rm output.txt result.txt
 rm -r __pycache__
