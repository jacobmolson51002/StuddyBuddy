import random
	
def safeSearch(text):
    newText = ''
    for letter in text:
        if letter == '\'':
            newText += '\''
        else:
            newText += letter
    if newText[0] != ' ':
        newText = ' ' + newText
    if newText[-1] != ' ':
        newText += ' '
    return newText

    
    
while True:
    text = input('what do you want to turn into key?: ')
    text = safeSearch(text)
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.replace('?', '')
    text = text.replace('.', '')
    text = text.replace(',', '')    
    text = text.replace(';', '')
    while True:
        if text.find('  ') != -1:
            text = text.replace('  ', ' ')
        else:
            break
    print(text)
    if text != 'quit':
        uniqueNum = 0
        id = ''
        keyChars = ['q','w','a','s','z','x','e','r','d','f','c','t','y','g','h','v','b','u','j','n','i','k','m','o','p','l','Q','A','Z','W','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','M','I','K','O','L','P','5','6','1','2','8','0','9','3','4','7','-']
        for letter in text:
            for i in range(128):
                if letter == chr(i):
                    uniqueNum += i
        listOfWords = text.split()
        r = 0
        if len(listOfWords) >= 15:
            r = 15
        else:
            r = len(listOfWords)
            for i in range(15 - (15 % r)):
                keyNum = 0
                if (uniqueNum + i) <= len(keyChars):
                    id += keyChars[(len(keyChars) % (uniqueNum + i))]
                else:
                    id += keyChars[((uniqueNum + i) % len(keyChars))]
        for i in range(r):
            if i % 2 == 0:
                numToAdd = 1
                for letter in listOfWords[i]:
                    for i in range(128):
                        if letter == chr(i) and i != 0:
                            numToAdd *= i
                random.seed(numToAdd + uniqueNum)
                id += keyChars[random.randint(0,len(keyChars) - 1)]
            else:
                numToAdd = 0
                for letter in listOfWords[i]:
                    for i in range(128):
                        if letter == chr(i):
                            numToAdd += i
                random.seed(numToAdd + uniqueNum)
                id += keyChars[random.randint(0,len(keyChars) - 1)]
        print(id)
    else:
        break