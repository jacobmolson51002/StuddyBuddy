# use this to calculate monthly earnings
import math

def monthlyEarnings(subscribers, nonSubscribers, totalPayUse, totalUse, tutors, successQuestions):
	print()
	revenue = (subscribers * 5) + (totalPayUse * 0.18)
	print('Total Revenue: ' + str(revenue))
	userAuth = 0.01 * (subscribers + nonSubscribers)
	print('		- $' + str(userAuth) + ' : user authentication cost(FireBase)')
	numInstances = 1
	totalUsers = subscribers + nonSubscribers
	numInstances += totalUsers // 500
	instanceCost = 48.46 * numInstances
	print('		- $' + str(instanceCost) + ' : amazon ec2 c6g.large cost (' + str(numInstances) + ') instances')
	storageCost = 0.18 * (successQuestions // 1000)
	print('		- $' + str(storageCost) + ' : FireStore question & answer storage costs')
	reads = 0.06 * ((totalUse * 10) // 100000)
	print('		- $' + str(reads) + ' : total cost of db reads')
	profit = revenue - userAuth - instanceCost - reads
	print()
	print('		= $' + str(profit))
	return profit
	
print('StuddyBuddy business model testing')
print('Service costs: $0.50/question or $5/month for unlimted questions')
print()
subscribers = int(input('enter number of paying subscribers: '))
nonSubscribers = int(input('enter number of non-subscribed users that used services: '))
totalPayUse = int(input('enter the total number of questions non-subscribers asked: '))
totalUse = int(input('enter the total number of questions asked: '))
tutors = int(input('enter the numnber of tutors: '))
successQuestions = int(input('enter total number of successful question and answers: '))
profit = monthlyEarnings(subscribers, nonSubscribers, totalPayUse, totalUse, tutors, successQuestions)
print()
decision = input('see growth over months? (y/n): ')
if decision == 'y':
	while True:
		months = int(input('how many months?: '))
		subscriberGrowth = float(input('rate of subscriber growth (each month)?: '))
		nonSubscriberGrowth = float(input('rate of non-subscriber use growth (each month)?: '))
		tutorGrowth = float(input('rate of tutor growth (each month)?: '))
		totalPayUseGrowth = float(input('rate of growth for non-subscriber questions (each month)?: '))
		totalUseGrowth = float(input('rate of growth for total questions asked (each month)?: '))
		successQuestionsGrowth = float(input('rate of growth for total number of successful questions (each month)?: '))
		
		totalProfit = 0
		avgProfitIncrease = 0
		for i in range(1, months+1):
			print('Month ' + str(i))
			lastMonth = monthlyEarnings((subscribers * math.pow(subscriberGrowth,i-1)), (nonSubscribers * math.pow(nonSubscriberGrowth,i-1)), (totalPayUse * math.pow(totalPayUseGrowth,i-1)), (totalUse * math.pow(totalUseGrowth,i-1)), (tutors * math.pow(tutorGrowth,i-1)), (successQuestions * math.pow(successQuestionsGrowth,i-1)))
			thisMonth = monthlyEarnings((subscribers * math.pow(subscriberGrowth,i)), (nonSubscribers * math.pow(nonSubscriberGrowth,i)), (totalPayUse * math.pow(totalPayUseGrowth,i)), (totalUse * math.pow(totalUseGrowth,i)), (tutors * math.pow(tutorGrowth,i)), (successQuestions * math.pow(successQuestionsGrowth,i)))
			totalProfit += thisMonth
			avgProfitIncrease += (thisMonth / lastMonth)
		print()
		print('after ' + str(months) + ' months, total profits are:')
		print('		$' + str(totalProfit), end='')
		totalProfitGrowth = totalProfit / profit
		if totalProfitGrowth > 1:
			print(', which is a {:.2f}% increase from the first month.'.format((totalProfitGrowth * 100) - 100))
		elif totalProfitGrowth < 1:
			print(', which is a {:.2f}% decrease from the first month.'.format(100 - (totalProfitGrowth * 100)))
		else:
			print(', which is the same as your first month\'s profit.')
		avgProfitIncrease = avgProfitIncrease / months
		if avgProfitIncrease > 1:
			print('on average, the profit per month increased at a rate of: {:.2f}%.'.format((avgProfitIncrease * 100) - 100))
		elif avgProfitIncrease < 1:
			print('on average, the profit per month decreased at a rate of: {:.2f}%.'.format(100 - (avgProfitIncrease * 100)))
		else:
			print('on average, the profit per month stayed the same.')
		print('')
		print('with those growth rates, total profit after  ')
		goAgain = input('do you want to run the rates again?: ')
		if goAgain == 'no':
			break
