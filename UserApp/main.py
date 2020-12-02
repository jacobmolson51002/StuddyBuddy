#main script for user-side
from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials, firestore, storage, auth
import random
from urllib.parse import quote
import time
import os.path
import pyrebase

cred = credentials.Certificate('static/ServiceAccountKey.json')

firebase_admin.initialize_app(cred, {
    'storageBucket': 'gs://studdybuddy-5021a.appspot.com/.appspot.com'
})
db = firestore.client()
#defaultApp = firebase_admin.initialize_app(cred)
#set up storage bucket to get txt files
'''
bucket = storage.bucket()

db = firestore.client()
answers = db.collection('answeredquestions').document('math')
answer = answers.get()
#print('Math Answer: {}'.format(answer.to_dict()))'''
config = {
    'apiKey': 'AIzaSyCSNJDwjQ7_TOHluDbrETq6zZroEA-x3N8',
	'authDomain': 'studdybuddy-5021a.firebaseapp.com',
	'databaseURL': 'https://studdybuddy-5021a.firebaseio.com',
	'projectId': 'studdybuddy-5021a',
	'storageBucket': 'studdybuddy-5021a.appspot.com'
}
firebase = pyrebase.initialize_app(config)
files = firebase.storage()
#db = firebase.database()
#auth = firebase.auth()



def login(request):
	email = request.POST.get('email')
	password = request.POST.get('password')
	try:
		user = auth.get_user_by_email(email)
		print(user.uid)
		if user.password == password:
			return HttpResponse('User logged in')
		else:
			return HttpResponse('Password incorrect')
			
	except Exception as e:
		print('ERROR: ' + str(e))
		if 'No user record found for the provided email' in str(e):
			#return HttpResponse("We couldn't find that email")
			return HttpResponse('Invalid email')
		else:
			return HttpResponse('')
	


def hello(request):
    #admin = auth.sign_in_with_email_and_password('jacobmolson51002@gmail.com', 'Qweruiop1535!')
    #getSchools = db.child("basicusers").get()
    
    '''
    getTestQuery = db.collection('missouri s&t').document('calculus 1')
    testQuery = getTestQuery.get()
    print(testQuery.to_dict())
    getSchools = db.collection('generalInfo').document('schools')
    schools = getSchools.get()
    schools = schools.to_dict()
    content = {
        'schools': schools
    }
    print(content)'''
    return render(request, 'UserApp/index.html')
	
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

def isLineOnlySpaces(line):
	answer = True
	for letter in line:
		if letter != ' ':
			answer = False
			break
	return answer
	
def search(request):
    question = request.POST.get('question')
    schoolFilter = request.POST.get('school').lower()
    classFilter = request.POST.get('class').lower()
    categoryFilter = request.POST.get('category').lower()
    
    question = safeSearch(question)
    question = question.lower()
    question = question.replace('\n', ' ')
    question = question.replace('?', '')
    question = question.replace('.', '')
    question = question.replace(',', '')
    question = question.replace(';', '')
    while True:
        if question.find('  ') != -1:
            question = question.replace('  ', ' ')
        else:
            break
    print(question);
    
    questionID = generateQuestionKey(question)
    
    print(questionID)
    response = ''
    
    '''answer = db.collection('math').document(questionID)
    answer = answer.get()
    if answer.exists:
        answer = answer.to_dict()
        answer = answer['answer']
        filePath = 'static/answers/' + answer
		
        answer = open('')
    else:
        answer = 'We did not find the answer.'
    return HttpResponse(answer)'''
    
    filePath = 'answers/' + questionID + '.txt'
    fileName = questionID + '.txt'
    files.child(filePath).download('', fileName)
    if os.path.isfile(fileName):
        response = questionID
    else:
        response = 'not found'
    
    '''if os.path.isfile(fileName):
        file = open(fileName, 'r')
        for line in file:
            if isLineOnlySpaces(line) == False:
                answer += line + '<p>'
            else:
                answer += '<p>'
        file.close()
        os.remove(fileName)'''
    return HttpResponse(response)

def getDocInfo(questionID):
    question = []
    answer = []
    currentlyOnQuestion = True
    file = open(questionID + '.txt', 'r')
    for line in file:
        if currentlyOnQuestion == True:
            print(type(questionID))
            print(type(line))
            print()
            if line.strip() == questionID.strip():
                print('worked')
                currentlyOnQuestion = False
            else:
                question.append(line)
        else:
            answer.append(line)
    file.close()
    return {'question': question, 'answer': answer}

def question(request, questionID):
    '''
    if subscriber logged in:
        if file exists:
            get file 
            display question and answer
        else:
            download file
            get file
            display question and answer
    elif basicuser logged in:
        if file exists:
            get file
            display question
            prompt user for payment to see answer
            once they pay, display answer
        else:
            download file
            display question
            prompt user for payment to see answer
            once they pay, display answer
    else:
        if file exists:
            get file
            display question
            prompt user for payment to see answer
            once they pay, display answer
        else:
            download file
            display question
            prompt user for payment to see answer
            once they pay, display answer
    
    
    '''
    if os.path.isfile(questionID + '.txt'):
        doc = getDocInfo(questionID)
    else:
        filePath = 'answers/' + questionID + '.txt'
        fileName = questionID + '.txt'
        files.child(filePath).download('', fileName)
        doc = getDocInfo(questionID)
    os.remove(questionID + '.txt')
    return render(request, 'UserApp/answer.html', doc)

def generateQuestionKey(text):
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
	return id