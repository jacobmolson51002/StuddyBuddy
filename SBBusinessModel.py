# use this to calculate monthly earnings
import math
import random

def monthlyEarnings(perQuestion, perAnswer, monthly, subscribers, nonSubscribers, tutors, categories, turnout = '', totalPayUse = 0, totalUse = 0, successQuestions = 0):
    print()

    #determine stats
    pricingModels = monthly.split(',')
    models = []
    for price in pricingModels:
        model = price.split()
        currentModel = [float(i) for i in model]
        models.append(currentModel)
    print(models)
    
    
    subscriberRevenue = 0.0
    subscriberModels = []
    if totalPayUse == 0:
        if turnout == 'good':
            for i in range(int(nonSubscribers)):
                totalPayUse += random.randint(5,10)

            for i in range(int(subscribers)):
                x = random.randint(0,len(models) - 1)
                questions = random.randint(0,models[x][1])
                subscriberRevenue += ((models[x][0] - (questions * 0.1) - 0.3) * 0.971)
                totalUse += questions           

                #totalUse += random.randint(8,30)            
        elif turnout == 'bad':
            for i in range(int(nonSubscribers)):
                totalPayUse += random.randint(1,5)

            for i in range(int(subscribers)):
                x = random.randint(0,len(models) - 1)
                questions = random.randint(0,models[x][1])
                subscriberRevenue += ((models[x][0] - (questions * 0.1) - 0.3) * 0.971)
                totalUse += questions           

                #totalUse += random.randint(4,12)           
        elif turnout == 'normal':
            for i in range(int(nonSubscribers)):
                totalPayUse += random.randint(1,10)

            for i in range(int(subscribers)):
                x = random.randint(0,len(models) - 1)
                questions = random.randint(0,models[x][1])
                subscriberRevenue += ((models[x][0] - (questions * 0.1) - 0.3) * 0.971)
                totalUse += questions
            
            
                #totalUse += random.randint(4,30)           
        successQuestions = float(totalPayUse + totalUse) * 0.95
    
    
    #generate prices
    costPerQuestion = (perQuestion * 0.971) - 0.1
    #monthly = ((monthly - 0.3) * 0.971)
    
    #determine revenue
    revenue = subscriberRevenue + ((totalPayUse * costPerQuestion) - (0.3 * nonSubscribers))
    
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
    tutorDocs = (tutors // 225) + 1
    reads = (0.06 * ((totalQuestions * tutorDocs) / 100000))
    
    #determine money left over after expenses
    leftOver = revenue - userAuth - instanceCost - reads
    
    #determine tutor payout
    #tutorPayouts = leftOver * 0.2
    #leftOver -= tutorPayouts
    
    
    #determine ad money
    ads = 0.0
    if ((leftOver * 0.7) * 0.75) > 500:
        ads = leftOver * 0.3
        leftOver -= ads
    
    #determine taxes
    taxes = leftOver * 0.25
    
    #determine total profit
    profit = leftOver - taxes
    
    
    return [revenue, subscriberRevenue, costPerQuestion, totalPayUse, nonSubscribers, userAuth, instanceCost, numInstances, storageCost, reads, totalQuestions, tutors, ads, taxes, profit]
print()
print('StuddyBuddy business model testing')
print()
#fastOrDetailed = input('do you want the fast version or detailed version?: ')
costPerQuestion = float(input('cost per question?: $'))
costPerAnswer = float(input('cost per answer?: $'))
monthlyCost = input('monthly pricing models(price, # questions, # answers, separate by commas): ')
subscribers = float(input('enter number of paying subscribers: '))
nonSubscribers = float(input('enter number of non-subscribed users that used services: '))
tutors = float(input('enter number of tutors: '))
categories = float(input('enter number of categories to search through: '))
profit = 0
if True:
    turnout = input('good, bad, or normal turnout? (use-wise?): ')
    if turnout == 'good':
        results = monthlyEarnings(costPerQuestion, costPerAnswer, monthlyCost, subscribers, nonSubscribers, tutors,
        categories, turnout = 'good')
        
        
        #print revenue
        print('Total Revenue: $' + str(results[0]))
        print('     + $'+str(results[1])+' (subscriber revenue)')
        print('     + $'+str(results[2] * results[3])+' ($'+str(results[2])+' per question * '+str(results[3])+' users)')
        print('Total Expenses: $'+str(results[0] - results[14]))
        
        #print revenue
        #print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question) + $' + str(results[12] * 2) + ' (tutor fee)')

        #print user authentication cost
        print('     - $' + str(results[5]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        print('     - $' + str(results[6]) + ' : amazon ec2 c6g.large cost (' + str(results[7]) + ') instances')

        #print storage cost
        print('     - $' + str(results[8]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('     - $' + str(results[9]) + ' : total cost of db reads (' + str(results[10]) + ' total questions * ' + str(results[11]) + ' average tutors per category)')
        
        #print tutor payout
        #print('     - $' + str(results[13]) + ' : tutor payout')
        
        #print ad money if any
        if results[12] > 0.0:
            print('     - $' + str(results[12]) + ' : ad money for next month')
        
        #print taxes
        print('     - $' + str(results[13]) + ' : monthly taxes')

        #print total profit
        print()
        print('     = $' + str(results[14]))
        print('On average, each tutor made: $' + str(results[10] / results[11]))
    elif turnout == 'bad':
        results = monthlyEarnings(costPerQuestion, costPerAnswer, monthlyCost, subscribers, nonSubscribers, tutors,
        categories, turnout = 'bad')
        
        #print revenue
        print('Total Revenue: $' + str(results[0]))
        print('     + $'+str(results[1])+' (subscriber revenue)')
        print('     + $'+str(results[2] * results[3])+' ($'+str(results[2])+' per question * '+str(results[3])+' users)')
        print('Total Expenses: $'+str(results[0] - results[14]))
        
        #print revenue
        #print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question) + $' + str(results[12] * 2) + ' (tutor fee)')

        #print user authentication cost
        print('     - $' + str(results[5]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        print('     - $' + str(results[6]) + ' : amazon ec2 c6g.large cost (' + str(results[7]) + ') instances')

        #print storage cost
        print('     - $' + str(results[8]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('     - $' + str(results[9]) + ' : total cost of db reads (' + str(results[10]) + ' total questions * ' + str(results[11]) + ' average tutors per category)')
        
        #print tutor payout
        #print('     - $' + str(results[13]) + ' : tutor payout')
        
        #print ad money if any
        if results[12] > 0.0:
            print('     - $' + str(results[12]) + ' : ad money for next month')
        
        #print taxes
        print('     - $' + str(results[13]) + ' : monthly taxes')

        #print total profit
        print()
        print('     = $' + str(results[14]))
        print('On average, each tutor made: $' + str(results[10] / results[11]))
    elif turnout == 'normal':
        results = monthlyEarnings(costPerQuestion, costPerAnswer, monthlyCost, subscribers, nonSubscribers, tutors,
        categories, turnout = 'normal')
        
        #print revenue
        print('Total Revenue: $' + str(results[0]))
        print('     + $'+str(results[1])+' (subscriber revenue)')
        print('     + $'+str(results[2] * results[3])+' ($'+str(results[2])+' per question * '+str(results[3])+' users)')
        print('Total Expenses: $'+str(results[0] - results[14]))
        
        #print revenue
        #print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question) + $' + str(results[12] * 2) + ' (tutor fee)')

        #print user authentication cost
        print('     - $' + str(results[5]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        print('     - $' + str(results[6]) + ' : amazon ec2 c6g.large cost (' + str(results[7]) + ') instances')

        #print storage cost
        print('     - $' + str(results[8]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('     - $' + str(results[9]) + ' : total cost of db reads (' + str(results[10]) + ' total questions * ' + str(results[11]) + ' average tutors per category)')
        
        #print tutor payout
        #print('     - $' + str(results[13]) + ' : tutor payout')
        
        #print ad money if any
        if results[12] > 0.0:
            print('     - $' + str(results[12]) + ' : ad money for next month')
        
        #print taxes
        print('     - $' + str(results[13]) + ' : monthly taxes')

        #print total profit
        print()
        print('     = $' + str(results[14]))
        print('On average, each tutor made: $' + str(results[10] / results[11]))
else:
    totalPayUse = float(input('enter the total number of questions non-subscribers asked: '))
    totalUse = float(input('enter the total number of questions asked: '))
    tutors = float(input('enter the number of tutors: '))
    successQuestions = float(input('enter total number of successful question and answers: '))
    #print revenue
    print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question)')
    
    #print user authentication cost
    print('     - $' + str(results[6]) + ' : user authentication cost(FireBase)')
    
    #print ec2 costs
    print('     - $' + str(results[7]) + ' : amazon ec2 c6g.large cost (' + str(results[8]) + ') instances')
    
    #print storage cost
    print('     - $' + str(results[9]) + ' : FireStore question & answer storage costs')
    
    #print db reads
    print('     - $' + str(results[10]) + ' : total cost of db reads (' + str(results[11]) + ' total questions * ' + str(results[12]) + ' average tutors per category)')
    
    #print tutor payout
    print('     - $' + str(results[13]) + ' : tutor payout')
        
    #print ad money if any
    if results[14] > 0.0:
        print('     - $' + str(results[14]) + ' : ad money for next month')
        
    #print taxes
    print('     - $' + str(results[15]) + ' : monthly taxes')

    #print total profit
    print()
    print('     = $' + str(results[16]))
    
print()
decision = input('see growth over months? (y/n): ')
if decision == 'y':
    while True:
        months = int(input('how many months?: '))
        subscriberGrowth = float(input('rate of subscriber growth (each month)?: '))
        nonSubscriberGrowth = float(input('rate of non-subscriber use growth (each month)?: '))
        tutorGrowth = float(input('rate of tutor growth (each month)?: '))
        categoryGrowth = float(input('rate of category growth (each month)?: '))
        
        
        
        totalProfit = 0
        avgProfitIncrease = 0
        for i in range(1, months+1):
            print('Month ' + str(i))
            lastMonth = monthlyEarnings(costPerQuestion, costPerAnswer, monthlyCost, (subscribers * math.pow(subscriberGrowth,i-1)), (nonSubscribers * math.pow(nonSubscriberGrowth,i-1)), (tutors * math.pow(tutors,i-1)), (categories * math.pow(categoryGrowth,i-1)), turnout = 'normal')
            results = monthlyEarnings(costPerQuestion, costPerAnswer, monthlyCost, (subscribers * math.pow(subscriberGrowth,i)), (nonSubscribers * math.pow(nonSubscriberGrowth,i)), (tutors * math.pow(tutors,i)), (categories * math.pow(categoryGrowth,i)), turnout = 'normal')
                
            #print revenue
            print('Total Revenue: $' + str(results[0]))
            print('     + $'+str(results[1])+' (subscriber revenue)')
            print('     + $'+str(results[2] * results[3])+' ($'+str(results[2])+' per question * '+str(results[3])+' users)')
            print('Total Expenses: $'+str(results[0] - results[14]))
            
            #print revenue
            #print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question) + $' + str(results[12] * 2) + ' (tutor fee)')

            #print user authentication cost
            print('     - $' + str(results[5]) + ' : user authentication cost(FireBase)')

            #print ec2 costs
            print('     - $' + str(results[6]) + ' : amazon ec2 c6g.large cost (' + str(results[7]) + ') instances')

            #print storage cost
            print('     - $' + str(results[8]) + ' : FireStore question & answer storage costs')

            #print db reads
            print('     - $' + str(results[9]) + ' : total cost of db reads (' + str(results[10]) + ' total questions * ' + str(results[11]) + ' average tutors per category)')
            
            #print tutor payout
            #print('     - $' + str(results[13]) + ' : tutor payout')
            
            #print ad money if any
            if results[12] > 0.0:
                print('     - $' + str(results[12]) + ' : ad money for next month')
            
            #print taxes
            print('     - $' + str(results[13]) + ' : monthly taxes')

            #print total profit
            print()
            print('     = $' + str(results[14]))   
            print('On average, each tutor made: $' + str(results[10] / results[11]))
            
            totalProfit += results[16]
            avgProfitIncrease += (results[16] / lastMonth[16])
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
