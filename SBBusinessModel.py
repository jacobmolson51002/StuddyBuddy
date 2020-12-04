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
    
    
    subscriberRevenue = 0.0
    userRevenue = 0.0
    tutorMoney = 0.0
    totalAnswerViews = 0.0
    averageQuestionCost = []
    averageAnswerCost = []
    subscriberModels = []
    if totalPayUse == 0:
        if turnout == 'good':
            for i in range(int(nonSubscribers)):
                totalPayUse += random.randint(3,6)

            for i in range(int(subscribers)):
                x = random.randint(0,len(models) - 1)
                questions = random.randint(0,models[x][1])
                subscriberRevenue += ((models[x][0] - (questions * 0.1) - 0.3) * 0.971)
                totalUse += questions           

                #totalUse += random.randint(8,30)            
        elif turnout == 'bad':
            for i in range(int(nonSubscribers)):
                totalPayUse += random.randint(1,3)

            for i in range(int(subscribers)):
                x = random.randint(0,len(models) - 1)
                questions = random.randint(0,models[x][1])
                subscriberRevenue += ((models[x][0] - (questions * 0.1) - 0.3) * 0.971)
                totalUse += questions           

                #totalUse += random.randint(4,12)           
        elif turnout == 'normal':
            for i in range(int(nonSubscribers)):
                questionsAsked = random.randint(1,7)
                answersViewed = 0
                if subscribers > 500:
                    answersViewed = random.randint(1,12)
                revenue = 0.0
                questionCost = 0.0
                avgQCost = 0.0
                for i in range(questionsAsked):
                    cost = random.uniform(0.10,0.30)
                    questionCost += cost
                    revenue += (0.3 + perQuestion)
                    averageQuestionCost.append((cost + 0.3 + perQuestion) * 1.029)
                for i in range(answersViewed):
                    cost = random.uniform(0.05,0.15)
                    questionCost += cost
                    revenue += (0.3 + perAnswer)
                    averageAnswerCost.append((cost + 0.3 + perAnswer) * 1.029)
                userRevenue += revenue
                tutorMoney += questionCost
                totalPayUse += questionsAsked
                totalAnswerViews += answersViewed

            for i in range(int(subscribers)):
                x = random.randint(0,len(models) - 1)
                if models[x][1] != 0:
                    questionsAsked = random.randint(0, (models[x][1] + 7))
                    questionCost = 0
                    for i in range(questionsAsked):
                        questionCost += random.uniform(.10, .30)
                    #questions = random.randint(0,models[x][1])
                    subscriberRevenue += ((models[x][0] + (abs(models[x][1] - questionsAsked) * 0.1) - 0.3) * 0.971)
                    totalUse += questionsAsked
                    tutorMoney += questionCost
                else:
                    questionsAsked = random.randint(0, 50)
                    questionCost = 0
                    for i in range(questionsAsked):
                        questionCost += random.uniform(0.10, 0.30)
                    subscriberRevenue += ((models[x][0] + (questionsAsked * 0.10)) - 0.3) * 0.971
                    totalUse += questionsAsked
                    tutorMoney += questionCost
            
                #totalUse += random.randint(4,30)           
        successQuestions = float(totalPayUse + totalUse) * 0.95
    
    
    #generate prices
    #costPerQuestion = (perQuestion * 0.971)
    #monthly = ((monthly - 0.3) * 0.971)
    
    #determine revenue
    #revenue = subscriberRevenue + ((totalPayUse * costPerQuestion) - (0.3 * nonSubscribers))
    stripeFee = 0.3 * nonSubscribers
    revenue = (userRevenue - stripeFee) + subscriberRevenue
    
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
    leftOver = revenue - userAuth - reads
    
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
    
    
    questionMax = 0.0
    questionMin = 1.0
    totalCostPerQuestion = 0.0
    for num in averageQuestionCost:
        if num > questionMax:
            questionMax = num
    for num in averageQuestionCost:
        if num < questionMin:
            questionMin = num
    for num in averageQuestionCost:
        totalCostPerQuestion += num

    answerMax = 0.0
    answerMin = 1.0
    totalCostPerAnswer = 0.0
    for num in averageAnswerCost:
        if num > answerMax:
            answerMax = num
    for num in averageAnswerCost:
        if num < answerMin:
            answerMin = num
    for num in averageAnswerCost:
        totalCostPerAnswer += num
        
    
    
    averageQuestionCost = totalCostPerQuestion / len(averageQuestionCost)
    if len(averageAnswerCost) > 0:
        averageAnswerCost = totalCostPerAnswer / len(averageAnswerCost)
    else:
        averageAnswerCost = 0
    
    
    return [revenue, subscriberRevenue, userRevenue, stripeFee, nonSubscribers, userAuth, storageCost, reads, totalQuestions, tutors, ads, taxes, tutorMoney, profit, averageQuestionCost, questionMax, questionMin, averageAnswerCost, answerMax, answerMin, totalUse, totalPayUse, totalAnswerViews]
print()
print('StuddyBuddy business model testing')
print()
print('sample price models:    5 10 15, 7 20 25, 10 30 40, 15 50 70')
print()
#fastOrDetailed = input('do you want the fast version or detailed version?: ')
costPerQuestion = float(input('cost per question?: $'))
costPerAnswer = float(input('cost per answer?: $'))
monthlyCost = input('monthly pricing models(price, # questions, # answers, separate by commas): ')
nonSubscribers = float(input('enter number of non-subscribed users that used services: '))
subscribers = float(input('enter number of paying subscribers: '))
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
        print('     + $'+str(results[1])+' (subscriber revenue) ('+str(results[20])+' total subscriber questions)')
        print('     + $'+str(results[2])+' (userRevenue) ('+str(results[21])+' total user questions, '+str(results[22])+' total user answers viewed)')
        print('     - $'+str(results[3])+' (Stripe fee)')
        print('Total Expenses: $'+str(results[0] - results[13]))
        
        #print revenue
        #print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question) + $' + str(results[12] * 2) + ' (tutor fee)')

        #print user authentication cost
        print('     - $' + str(results[5]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        #print('     - $' + str(results[6]) + ' : amazon ec2 c6g.large cost (' + str(results[7]) + ') instances')

        #print storage cost
        print('     - $' + str(results[6]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('     - $' + str(results[7]) + ' : total cost of db reads (' + str(results[8]) + ' total questions * ' + str(results[9]) + ' average tutors per category)')
        
        #print tutor payout
        #print('     - $' + str(results[13]) + ' : tutor payout')
        
        #print ad money if any
        if results[10] > 0.0:
            print('     - $' + str(results[10]) + ' : ad money for next month')
        
        #print taxes
        print('     - $' + str(results[11]) + ' : monthly taxes')

        #print total profit
        print()
        print('     = $' + str(results[13]))
        print('On average, each tutor made: $' + str(results[12] / results[9]))
        print('On average, each question costs: $' + str(results[14]) + ', most expensive question: ' + str(results[15]) + ', cheapest question: ' + str(results[16]))
        print('On average, each question costs: $' + str(results[17]) + ', most expensive question: ' + str(results[18]) + ', cheapest question: ' + str(results[19]))
    elif turnout == 'bad':
        results = monthlyEarnings(costPerQuestion, costPerAnswer, monthlyCost, subscribers, nonSubscribers, tutors,
        categories, turnout = 'bad')
        
        #print revenue
        print('Total Revenue: $' + str(results[0]))
        print('     + $'+str(results[1])+' (subscriber revenue) ('+str(results[20])+' total subscriber questions)')
        print('     + $'+str(results[2])+' (userRevenue) ('+str(results[21])+' total user questions, '+str(results[22])+' total user answers viewed)')
        print('     - $'+str(results[3])+' (Stripe fee)')
        print('Total Expenses: $'+str(results[0] - results[13]))
        
        #print revenue
        #print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question) + $' + str(results[12] * 2) + ' (tutor fee)')

        #print user authentication cost
        print('     - $' + str(results[5]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        #print('     - $' + str(results[6]) + ' : amazon ec2 c6g.large cost (' + str(results[7]) + ') instances')

        #print storage cost
        print('     - $' + str(results[6]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('     - $' + str(results[7]) + ' : total cost of db reads (' + str(results[8]) + ' total questions * ' + str(results[9]) + ' average tutors per category)')
        
        #print tutor payout
        #print('     - $' + str(results[13]) + ' : tutor payout')
        
        #print ad money if any
        if results[10] > 0.0:
            print('     - $' + str(results[10]) + ' : ad money for next month')
        
        #print taxes
        print('     - $' + str(results[11]) + ' : monthly taxes')

        #print total profit
        print()
        print('     = $' + str(results[13]))
        print('On average, each tutor made: $' + str(results[12] / results[9]))
        print('On average, each question costs: $' + str(results[14]) + ', most expensive question: ' + str(results[15]) + ', cheapest question: ' + str(results[16]))
        print('On average, each question costs: $' + str(results[17]) + ', most expensive question: ' + str(results[18]) + ', cheapest question: ' + str(results[19]))
    elif turnout == 'normal':
        results = monthlyEarnings(costPerQuestion, costPerAnswer, monthlyCost, subscribers, nonSubscribers, tutors,
        categories, turnout = 'normal')
        
        #print revenue
        print('Total Revenue: $' + str(results[0]))
        print('     + $'+str(results[1])+' (subscriber revenue) ('+str(results[20])+' total subscriber questions)')
        print('     + $'+str(results[2])+' (userRevenue) ('+str(results[21])+' total user questions, '+str(results[22])+' total user answers viewed)')
        print('     - $'+str(results[3])+' (Stripe fee)')
        print('Total Expenses: $'+str(results[0] - results[13]))
        
        #print revenue
        #print('Total Revenue: ' + str(results[0]) + '  --  ($' + str(results[1]) + ' * ' + str(results[2]) + ' users) + ($' + str(results[3]) + ' * ' + str(results[4]) + ' non-subscriber questions) - $' + str(0.3 * results[5]) + ' stripe fee per question) + $' + str(results[12] * 2) + ' (tutor fee)')

        #print user authentication cost
        print('     - $' + str(results[5]) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        #print('     - $' + str(results[6]) + ' : amazon ec2 c6g.large cost (' + str(results[7]) + ') instances')

        #print storage cost
        print('     - $' + str(results[6]) + ' : FireStore question & answer storage costs')

        #print db reads
        print('     - $' + str(results[7]) + ' : total cost of db reads (' + str(results[8]) + ' total questions * ' + str(results[9]) + ' average tutors per category)')
        
        #print tutor payout
        #print('     - $' + str(results[13]) + ' : tutor payout')
        
        #print ad money if any
        if results[10] > 0.0:
            print('     - $' + str(results[10]) + ' : ad money for next month')
        
        #print taxes
        print('     - $' + str(results[11]) + ' : monthly taxes')

        #print total profit
        print()
        print('     = $' + str(results[13]))
        print('On average, each tutor made: $' + str(results[12] / results[9]))
        print('On average, each question costs: $' + str(results[14]) + ', most expensive question: ' + str(results[15]) + ', cheapest question: ' + str(results[16]))
        print('On average, each question costs: $' + str(results[17]) + ', most expensive question: ' + str(results[18]) + ', cheapest question: ' + str(results[19]))
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
            print('On average, each tutor made: $' + str((results[10] / results[11]) * 0.1))
            
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
