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
def main():
    money = float(input('what money you wanna tax?: '))
    timeframe = input('yearly or quarterly?: ')
    if timeframe == 'yearly':
        print(getTaxes(money, entity='business'))
    elif timeframe == 'quarterly':
        print((getTaxes(money, entity='business') / 4))
    else:
        print((getTaxes(money, entity='business') / 12))
if __name__ == "__main__":
    main()
