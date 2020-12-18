import math
import random

def getTaxes(money, entity='tutor'):
    taxes = 0.0
    taxBrackets = [
        [.1, 9875],
        [.12, 40125],
        [.22, 85525],
        [.24, 163300],
        [.32, 207350],
        [.35, 518400],
        [.37, 1000000000000000000000]
    ]
    for i in range(len(taxBrackets)):
        if money > taxBrackets[i][1]:
            if i == 0:
                taxes += taxBrackets[i][0] * taxBrackets[i][1]
            else:
                taxes += taxBrackets[i][0] * (taxBrackets[i][1] - taxBrackets[i-1][1])
        else:
            if i == 0:
                taxes += taxBrackets[i][0] * money
                break
            else:
                taxes += taxBrackets[i][0] * (money - taxBrackets[i - 1][1])
                break
    if entity == 'business':
        selfEmploymentTax = 0.0
        if (money * .9235) > 137700:
            selfEmploymentTax += 137700 * 0.124
            selfEmploymentTax += (money * .9235) * .029
        else:
            selfEmploymentTax += (money * .9235) * .153
        taxes += selfEmploymentTax

    return taxes

def main(taxNums=False, costPerQuestion=0.0, costPerAnswer=0.0, nonSubscribers=0.0, subscribers=0.0, tutors=0.0, categories=0.0, schools=0.0):
    #get info
    if taxNums == False:
        costPerQuestion = float(input('cost per question?: $'))
        costPerAnswer = float(input('cost per answer?: $'))
        nonSubscribers = float(input('enter number of non-subscribed users that used services: '))
        subscribers = float(input('enter number of paying subscribers: '))
        tutors = float(input('enter nu  mber of tutors: '))
        categories = float(input('enter number of categories to search through: '))
        schools = float(input('enter average number of categories per school: '))
    schools = categories / schools
    profit = 0


    #calculate stuff


    subscriberRevenue = 0.0
    userRevenue = 0.0
    tutorMoney = 0.0
    totalPayUse = 0.0
    totalUse = 0.0
    totalAnswerViews = 0.0
    for i in range(int(nonSubscribers)):
        questionsAsked = random.randint(1,7)
        answersViewed = 0
        if subscribers > 500:
            answersViewed = random.randint(1,12)
        revenue = 0.0
        questionCost = 0.0
        avgQCost = 0.0
        for i in range(questionsAsked):
            cost = random.uniform(.01,0.10)
            questionCost += cost
            revenue += (costPerQuestion * 0.971) - cost
        for i in range(answersViewed):
            cost = random.uniform(0.01,0.05)
            questionCost += cost
            revenue += (costPerQuestion * 0.971) - cost
        userRevenue += revenue
        tutorMoney += questionCost
        totalPayUse += questionsAsked
        totalAnswerViews += answersViewed

    for i in range(int(subscribers)):
        models = [[2.5, 10, 20], [4, 20, 30], [7, 30, 40], [10, 0, 0]]
        x = random.randint(0,len(models) - 1)
        '''
        weight = random.randint(1,5)
        x = 0
        models = []
        if weight == 1:
            x == 10
            models = [x,0]
        else:
            x = random.uniform(1.50, 9.99)
            questions = int((x / 9.99) * 70)
            models = [x,questions]
        '''
        if models[x][1] != 0:
            questionsAsked = random.randint(0, (models[x][1] + 7))
            questionCost = 0
            questionsOver = 0
            if questionsAsked > models[x][1]:
                questionsOver = models[x][1] - questionsAsked
            for i in range(int(questionsOver)):
                cost = random.uniform(.01, .10)
                questionCost += cost
                subscriberRevenue += (costPerQuestion * 0.971) - cost
            #questions = random.randint(0,models[x][1])

            subscriberRevenue += ((models[x][0] * 0.971) - 0.3)
            totalUse += questionsAsked
            tutorMoney += questionCost
        else:
            questionsAsked = random.randint(0, 500)
            totalUse += questionsAsked
            subscriberRevenue += ((models[x][0] * 0.971) - 0.3)


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
    storageCost = 0.18 * ((totalUse + totalPayUse) / 1000)

    #determine db reads
    totalQuestions = totalUse + totalPayUse
    tutorDocs = (tutors // 225) + 1
    reads = (0.06 * ((totalQuestions * tutorDocs) / 100000))

    #determine algolia search fee
    algoliaFee = totalQuestions / 1000

    #determine money left over after expenses
    leftOver = revenue - userAuth - reads - algoliaFee

    #determine tutor payout
    #tutorPayouts = leftOver * 0.2
    #leftOver -= tutorPayouts


    #determine tutor payout amount
    tutorCash = leftOver * 0.10
    leftOver -= tutorCash

    #determine ad money
    ads = 0.0
    if ((leftOver * 0.8) * 0.50) > 500:
        ads = leftOver * 0.2
        leftOver -= ads


    #determine taxes
    #taxes = getTaxes(leftOver, 'month')
    '''print(getTaxes(leftOver * 12) / 12)
    print(getTaxes(leftOver * 12) / 4)'''
    taxes = (getTaxes(leftOver * 12, entity='business') / 12) * 1.1

    yearlyTaxable = leftOver


    #determine total profit
    profit = leftOver - taxes

    if taxNums == False:
        print('Total Revenue: $' + str(revenue))
        print('     + $'+str(subscriberRevenue)+' (subscriber revenue) ('+str(totalUse)+' total subscriber questions)')
        print('     + $'+str(userRevenue)+' (userRevenue) ('+str(totalPayUse)+' total user questions, '+str(totalAnswerViews)+' total user answers viewed)')
        print('     - $'+str(stripeFee)+' (Stripe fee)')
        print('Total Expenses: $'+str(revenue - profit))

        #print user authentication cost
        print('     - $' + str(userAuth) + ' : user authentication cost(FireBase)')

        #print ec2 costs
        #print('     - $' + str(results[6]) + ' : amazon ec2 c6g.large cost (' + str(results[7]) + ') instances')

        #print storage cost
        print('     - $' + str(storageCost) + ' : FireStore question & answer storage costs')

        #print db reads
        print('     - $' + str(reads) + ' : total cost of db reads (' + str(totalQuestions) + ' total questions * ' + str(tutorDocs) + ' average tutors per category)')

        #print tutor payout
        #print('     - $' + str(results[13]) + ' : tutor payout')

        #print algolia fee
        print('     - $'+str(algoliaFee)+' : algolia search fee ('+str(totalQuestions / 1000)+' total questions asked / 1000)')

        #print ad money if any
        if ads > 0.0:
            print('     - $' + str(ads) + ' : ad money for next month')

        #print taxes
        print('     - $' + str(taxes) + ' : monthly taxes')

        proportionalNum = (8 * schools * tutorCash) / ((tutorCash * schools) + (8 * tutorCash))
        winningTutorCash = tutorCash * (proportionalNum / schools)
        winningTutorCash = winningTutorCash - getTaxes(winningTutorCash)
        avgCashPerSchoolWinner = (tutorCash - winningTutorCash) / schools
        avgCashPerSchoolWinner = avgCashPerSchoolWinner - getTaxes(avgCashPerSchoolWinner)
        print('     - $' + str(tutorCash)+' (tutor payout, winner: $'+str(winningTutorCash)+', school winners average: $'+str(avgCashPerSchoolWinner)+')')
        print()
        print('     = $' + str(profit))
        print(yearlyTaxable)
        print('     at this rate, tax at the end of the year is: $'+str(getTaxes((yearlyTaxable * 12), entity='business') / 4))

    return yearlyTaxable, taxes, profit


if __name__ == "__main__":
    main()
