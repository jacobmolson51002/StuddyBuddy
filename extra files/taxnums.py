import SBBusinessModel as sb
import tax as t

months = int(input('how many months?: '))
taxableIncome = 0.0
amountOfSavedTax = 0.0
yearlyPayedTax = 0.0
totalProfit = 0.0
for i in range(1,months+1):
    print()
    income, savedTax, profit = sb.main()
    taxableIncome += income
    amountOfSavedTax += savedTax
    totalProfit += profit
    if i % 3 == 0 and i % 12 != 0:
        print()
        print('Quarter #' + str(i / 3))
        quarterlyTax = t.getTaxes(taxableIncome * (12 / i), entity='business') / 4
        print('quarterly tax: ' + str(quarterlyTax))
        print('saved tax: ' + str(amountOfSavedTax))
        if amountOfSavedTax >= quarterlyTax:
            print('good job, you saved enough this quarter!')
        else:
            print('you did not save enough this quarter')
        yearlyPayedTax += amountOfSavedTax
        amountOfSavedTax = 0.0
    if i % 12 == 0:
        taxesOwed = t.getTaxes(taxableIncome, entity='business')
        print('taxes owed at the end of the year: ' + str(taxesOwed))
        print('sum of quarterly taxes payed: ' + str(yearlyPayedTax))
        if yearlyPayedTax >= taxesOwed:
            print('good job! You saved enough this year!')
        else:
            print('oops, you owe $' + str(taxesOwed - yearlyPayedTax) + ' to the IRS this year...')
        print()
        print('also, StuddyBuddy made $'+str(totalProfit)+' of profit this year!')
