# use this to calculate monthly earnings
import math
import random

def monthlyEarnings(perQuestion, monthly, subscribers, nonSubscribers, categories, turnout = '', totalPayUse = 0, totalUse = 0, tutors = 0, successQuestions = 0):
    print()
    
    #determine stats
    if totalPayUse == 0:
        if turnout == 'good':
            for i in range(int(nonSubscribers)):
                totalPayUse += random.randint(5,10)

            totalUse = 0
            for i in range(int(subscribers)):
                totalUse += random.randint(8,30)            
        elif turnout == 'bad':
            for i in range(int(nonSubscribers)):
                totalPayUse += random.randint(1,5)

            totalUse = 0
            for i in range(int(subscribers)):
                totalUse += random.randint(4,12)           
        elif turnout == 'normal':
            for i in range(int(nonSubscribers)):
                totalPayUse += random.randint(1,10)

            totalUse = 0
            for i in range(int(subscribers)):
                totalUse += random.randint(4,30)           
        tutors = (float((subscribers + nonSubscribers)) * 0.25) / categories
        successQuestions = float(totalPayUse + totalUse) * 0.95
    
    
    #generate prices
    costPerQuestion = (perQuestion * 0.971)
    monthly = ((monthly - 0.3) * 0.971)
    
    #determine revenue
    revenue = (subscribers * monthly) + ((totalPayUse * costPerQuestion) - (0.3 * nonSubscribers))
    
    #determine user authentication cost
    userAuth = 0.01 * (subscribers + nonSubscribers)
    
    #determine ec2 costs
    numInstances = 1
    totalUsers = subscribers + nonSubscribers
    numInstances += totalUsers // 500
    instanceCost = 48.46 * numInstances
    
    #determine storage cost
    storageCost = 0.18 * (successQuestions / 1000)
    
    #determine db reads
    totalQuestions = totalUse + totalPayUse
    tutorDocs = (tutors // 45000) + 1
    reads = (0.06 * ((totalQuestions * tutorDocs) / 100000))
    
    #determine total profit
    profit = revenue - userAuth - instanceCost - reads
    
    return [revenue, monthly, subscribers, costPerQuestion, totalPayUse, nonSubscribers, userAuth, instanceCost, numInstances, storageCost, reads, totalQuestions, tutors, profit]
print()
print('StuddyBuddy business model testing')
print()
fastOrDetailed = input('do you want the fast version or detailed version?: ')
costPerQuestion = float(input('cost per question?: $'))
monthlyCost = float(input('cost per month?: $'))
subscribers = float(input('enter number of paying subscribers: '))
nonSubscribers = float(input('enter number of non-subscribed users that used services: '))
categories = float(input('enter number of categories to search through: '))
profit = 0
if fastOrDetailed == 'fast':
    turnout = input('good, bad, or normal turnout? (use-wise?): ')
    if turnout == 'good':
        results = monthlyEarnings(costPerQuestion, monthlyCost, subscribers, nonSubscribers,
        categories, turnout = 'good')
        
        #print revenue
        print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question)')

        #print user authentication cost
        print('		- $' + str(results[6]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        print('		- $' + str(results[7]) + ' : amazon ec2 c6g.large cost (' + str(results[8]) + ') instances')

        #print storage cost
        print('		- $' + str(results[9]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('		- $' + str(results[10]) + ' : total cost of db reads (' + str(results[11]) + ' total questions * ' + str(results[12]) + ' average tutors per category)')

        #print total profit
        print()
        print('		= $' + str(results[13]))
    elif turnout == 'bad':
        results = monthlyEarnings(costPerQuestion, monthlyCost, subscribers, nonSubscribers,
        categories, turnout = 'bad')
        
        #print revenue
        print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question)')

        #print user authentication cost
        print('		- $' + str(results[6]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        print('		- $' + str(results[7]) + ' : amazon ec2 c6g.large cost (' + str(results[8]) + ') instances')

        #print storage cost
        print('		- $' + str(results[9]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('		- $' + str(results[10]) + ' : total cost of db reads')

        #print total profit
        print()
        print('		= $' + str(results[13]))
    elif turnout == 'normal':
        results = monthlyEarnings(costPerQuestion, monthlyCost, subscribers, nonSubscribers,
        categories, turnout = 'normal')
        
        #print revenue
        print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question)')

        #print user authentication cost
        print('		- $' + str(results[6]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        print('		- $' + str(results[7]) + ' : amazon ec2 c6g.large cost (' + str(results[8]) + ') instances')

        #print storage cost
        print('		- $' + str(results[9]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('		- $' + str(results[10]) + ' : total cost of db reads')

        #print total profit
        print()
        print('		= $' + str(results[13]))      
else:
    totalPayUse = float(input('enter the total number of questions non-subscribers asked: '))
    totalUse = float(input('enter the total number of questions asked: '))
    tutors = float(input('enter the number of tutors: '))
    successQuestions = float(input('enter total number of successful question and answers: '))
    #print revenue
    print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question)')
    
    #print user authentication cost
    print('		- $' + str(results[6]) + ' : user authentication cost(FireBase)')
    
    #print ec2 costs
    print('		- $' + str(results[7]) + ' : amazon ec2 c6g.large cost (' + str(results[8]) + ') instances')
    
    #print storage cost
    print('		- $' + str(results[9]) + ' : FireStore question & answer storage costs')
    
    #print db reads
    print('		- $' + str(results[10]) + ' : total cost of db reads')
    
    #print total profit
    print()
    print('		= $' + str(results[11]))   
    
print()
decision = input('see growth over months? (y/n): ')
if decision == 'y':
    while True:
        months = int(input('how many months?: '))
        subscriberGrowth = float(input('rate of subscriber growth (each month)?: '))
        nonSubscriberGrowth = float(input('rate of non-subscriber use growth (each month)?: '))
        tutorGrowth = float(input('rate of tutor growth (each month)?: '))
        
        
		
        totalProfit = 0
        avgProfitIncrease = 0
        for i in range(1, months+1):
            print('Month ' + str(i))
            lastMonth = monthlyEarnings(costPerQuestion, monthlyCost, (subscribers * math.pow(subscriberGrowth,i-1)), (nonSubscribers * math.pow(nonSubscriberGrowth,i-1)), turnout = 'normal')
            results = monthlyEarnings(costPerQuestion, monthlyCost, (subscribers * math.pow(subscriberGrowth,i)), (nonSubscribers * math.pow(nonSubscriberGrowth,i)), turnout = 'normal')
            
            #print revenue
            print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question)')
            
            #print user authentication cost
            print('		- $' + str(results[6]) + ' : user authentication cost(FireBase)')
            
            #print ec2 costs
            print('		- $' + str(results[7]) + ' : amazon ec2 c6g.large cost (' + str(results[8]) + ') instances')
            
            #print storage cost
            print('		- $' + str(results[9]) + ' : FireStore question & answer storage costs')
            
            #print db reads
            print('		- $' + str(results[10]) + ' : total cost of db reads')
            
            #print total profit
            print()
            print('		= $' + str(results[11]))              
            
            totalProfit += results[11]
            avgProfitIncrease += (results[11] / lastMonth[11])
        print()
        print('after ' + str(months) + ' months, total profits are: ' + str(totalProfit))
        avgProfitIncrease = avgProfitIncrease / months
        if avgProfitIncrease > 1:
            print('on average, the profit per month increased at a rate of: {:.2f}%.'.format(avgProfitIncrease * 100))
        elif avgProfitIncrease < 1:
            print('on average, the profit per month decreased at a rate of: {:.2f}%.'.format(100 - (avgProfitIncrease * 100)))
        else:
            print('on average, the profit per month stayed the same.')
        print('')
        goAgain = input('do you want to run the rates again?: ')
        if goAgain != 'yes':
            break
