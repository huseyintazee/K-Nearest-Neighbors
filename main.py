import math
age = [25,35,45,20,35,52,23,40,60,48,33]
loan = [40000,60000,80000,20000,120000,18000,95000,62000,100000,220000,150000]
standardAge = []
standardLoan = []
minAge = min(age)
minLoan = min(loan)
maxAge = max(age)
maxLoan = max(loan)
isStandardized = input('Standardizasyon yapılsın mı ? (Evet: 1 ,Hayır: 2) ')
if isStandardized == '1':
    for age in age:
        standardedAge = (age-minAge)/(maxAge-minAge)
        standardAge.append(standardedAge)
    for loan in loan:
        standardedLoan = (loan-minLoan)/(maxLoan-minLoan)
        standardLoan.append(standardedLoan)
    preAge = int(input('Age: '))
    preLoan = int(input('Loan: '))
    preStanderdedAge = (preAge-minAge)/(maxAge-minAge)
    preStandardedLoan = (preLoan - minLoan)/(maxLoan-minLoan)
    distanceFunctionsName = input('Distance Functions (Euclidean = 1,Manhattan = 2): ')
    if distanceFunctionsName == '1':
        for age in standardAge:
            for loan in standardLoan:
                distance = math.sqrt(pow(preStanderdedAge-age,2)+pow(preStandardedLoan-loan,2))
                print("Distance: " + str(distance))

    else:
        print("Lütfen doğru bir uzaklık hesaplama fonksiyonu seciniz...")
if isStandardized == '2':
    preAge = int(input('Age: '))
    preLoan = int(input('Loan: '))
    distanceFunctionsName = input('Distance Functions (Euclidean = 1,Manhattan = 2): ')
    if distanceFunctionsName == '1':
        for age in age:
            for loan in loan:
                distance = math.sqrt(pow(preAge - age, 2) + pow(preLoan - loan, 2))
                print("Distance: " + str(distance))

    else:
        print("Lütfen doğru bir uzaklık hesaplama fonksiyonu seciniz...")