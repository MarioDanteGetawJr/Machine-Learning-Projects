import numpy as np
# program for Linear Regression

# define the data lists and their lengths
xVals = [1, 2, 3, 4, 5, 6]
#yVals = [10, 12, 15, 13, 21, 19] - main yVals
yVals = [10, 12, 15, 13, 21, 60]
m = len(xVals)
n = len(yVals)

# define a function to perform linear regression
def LinReg() :
    global xVals, yVals
    global m, n
    sumx = 0; sumy = 0; sumxy = 0; sumxx = 0
    global slope 
    global yInt 
    
    for index in range(n) :
        sumx += xVals[index]
        sumy += yVals[index]
        sumxy += xVals[index] * yVals[index]
        sumxx += xVals[index] * xVals[index]
    slope = (n * sumxy - sumx * sumy) / (n * sumxx - sumx * sumx) 
    yInt = (sumy * sumxx - sumx * sumxy) / (n * sumxx - sumx * sumx)
    print("------------------------------------------------\n")
    print ("the predicted slope is: %0.2f" % slope)
    print ("the predicted intercept is: %0.2f" % yInt)
    print ("")
    print ("linear model: y = %0.2fx + %0.2f" % (slope, yInt))
    print ("")
    # perform interpolation and extrapolation here
    # Interpolation (number within the range)
    xInterp = 0
    yInterp = 0


    # Request an interpolated x-value from the program user,
    # with these code statements
    msg = "please provide an x-value for interpolation "
    xInterp = float(input(msg))

    # Compute and display the interpolated y-value with
    # the lines of code
    yInterp = slope * xInterp + yInt
    print ("interpolation results: %0.2f" % yInterp)

    # Extrapolation (Outside the range)
    xExtrap = 0
    yExtrap = 0

    # Request an extrapolated x-value
    msgExtrap = "Please provide an x-value for extrapolation: "
    xExtrap = float(input(msgExtrap))

    # Compute and display the extrapolated y-value
    yExtrap = slope * xExtrap + yInt
    print("Extrapolation result: y = %0.2f" % yExtrap)

    # Correlation Coefficient = r
    r = np.corrcoef(xVals, yVals)[0, 1]
    print("The correlation coefficient is: %0.2f" % r)
    print("")

    # Coefficient of determination = r^2
    rSquared = r * r
    print("The coefficeint of determination is: %0.2f" % rSquared,"\n")
    
    # Strong or weak correlation?
    if ( r >= 0.80 and r <= 1.00) : 
        print("Analysis: strong postitive correlation\n")
    if ( r <= -0.80 and r >= -1.00) :
        print("Analysis: strong negative correlation\n")
    if ( r > -0.80 and r < 0.80) :
        print ("Analysis: weak correlation\n")
    
    print("------------------------------------------------\n")





# call the Linear Regression function
LinReg()

