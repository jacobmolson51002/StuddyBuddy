import SBBusinessModel as sb
import tax as t

months = int(input('how many months?: '))
quickOrManual = input('quick version or manual version?: ')
costPerQuestion = 0.0
costPerAnswer = 0.0
subscriberPercent = 0.0
userPercent = 0.0
tutorPercent = 0.0
categoryPercent = 0.0
schoolPercent = 0.0
if quickOrManual != 'manual':
    costPerQuestion = float(input('cost per question?: $'))
    costPerAnswer = float(input('cost per answer?: $'))
    subscriberPercent = float(input('enter percent of monthly users for subscribers: '))
    userPercent = 1 - subscriberPercent
    tutorPercent = float(input('enter percent of monthly users for tutors: '))
    categoryPercent = float(input('enter percent of monthly users for categories: '))
    schoolPercent = float(input('enter percent of monthly categories for schools: '))
taxableIncome = 0.0
amountOfSavedTax = 0.0
yearlyPayedTax = 0.0
totalProfit = 0.0
quarterlyIncome = 0.0
for i in range(1,months+1):
    print()
    income = 0.0
    savedTax = 0.0
    profit = 0.0
    if quickOrManual == 'manual':
        income, savedTax, profit = sb.main()
        quarterlyIncome += income
    else:
        totalUsers = float(input('enter total users for month #'+str(i)+': '))
        nonSubscribers = userPercent * totalUsers
        subscribers = subscriberPercent * totalUsers
        tutors = tutorPercent * totalUsers
        categories = categoryPercent * totalUsers
        schools = schoolPercent * categories
        income, savedTax, profit = sb.main(taxNums=True, costPerQuestion=costPerQuestion, costPerAnswer=costPerAnswer, nonSubscribers=nonSubscribers, subscribers=subscribers, tutors=tutors, categories=categories, schools=schools)
        quarterlyIncome += income
    print('profit: $' + str(profit))
    taxableIncome += income
    amountOfSavedTax += savedTax
    totalProfit += profit
    if i % 3 == 0:
        print()
        print('Quarter #' + str(i / 3))
        #quarterlyTax = t.getTaxes(taxableIncome * (12 / i), entity='business') / 4
        quarterlyTax = t.getTaxes(quarterlyIncome * 4, entity='business') / 4
        print('quarterly tax: $' + str(quarterlyTax))
        print('saved tax: $' + str(amountOfSavedTax))
        print('profit: $' + str(totalProfit))
        if amountOfSavedTax >= quarterlyTax:
            print('good job, you saved enough this quarter!')
        else:
            print('you did not save enough this quarter')
        yearlyPayedTax += amountOfSavedTax
        amountOfSavedTax = 0.0
        quarterlyIncome = 0.0
    if i % 12 == 0:
        print()
        taxesOwed = t.getTaxes(taxableIncome, entity='business')
        print('taxable income for this year: $' + str(taxableIncome))
        print('taxes owed at the end of the year: ' + str(taxesOwed))
        print('sum of quarterly taxes payed: ' + str(yearlyPayedTax))
        if yearlyPayedTax >= taxesOwed:
            print('good job! You saved enough this year!')
        else:
            print('oops, you owe $' + str(taxesOwed - yearlyPayedTax) + ' to the IRS this year...')
        print()
        print('also, StuddyBuddy made $'+str(totalProfit)+' of profit this year!')
if months != 12:
    print()
    taxesOwed = t.getTaxes(taxableIncome * (12 / months), entity='business') / (12 / months)
    print('taxable income for these '+str(months)+' months: $' + str(taxableIncome))
    print('taxes owed at the end of the year: ' + str(taxesOwed))
    if yearlyPayedTax > 0:
        yearlyPayedTax += amountOfSavedTax
        print('sum of saved taxes: $' + str(yearlyPayedTax))
        if yearlyPayedTax >= taxesOwed:
            print('good job! You saved enough this period!')
        else:
            print('oops, you owe $' + str(taxesOwed - yearlyPayedTax) + ' to the IRS this period...')
    else:
        print('sum of saved taxes: $' + str(amountOfSavedTax))
        if amountOfSavedTax >= taxesOwed:
            print('good job! You saved enough this period!')
        else:
            print('oops, you owe $' + str(taxesOwed - amountOfSavedTax) + ' to the IRS this period...')
    print()
    print('also, StuddyBuddy made $'+str(totalProfit)+' of profit this period!')
