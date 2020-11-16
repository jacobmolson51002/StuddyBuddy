#main script for user-side
from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials, firestore
import random
from urllib.parse import quote

cred = credentials.Certificate('static/ServiceAccountKey.json')
defaultApp = firebase_admin.initialize_app(cred)

db = firestore.client()
answers = db.collection('answeredquestions').document('math')
answer = answers.get()
#print('Math Answer: {}'.format(answer.to_dict()))

def hello(request):
	return render(request, 'UserApp/index.html')
	
def searchQuestion(request):
	question = request.POST.get('question')
	newLine = question[7]
	print('this is at index 7: \n')
	print(question);
	questionID = generateQuestionKey(question)
	print(questionID)
	answer = db.collection('math').document(questionID)
	answer = answer.get()
	if answer.exists:
		answer = answer.to_dict()
		answer = answer['answer']
	else:
		answer = 'We did not find the answer.'
	return HttpResponse(answer)
		
	
def generateQuestionKey(text):
	uniqueNum = 0
	id = ''
	keyChars = ['q','w','a','s','z','x','e','r','d','f','c','t','y','g','h','v','b','u','j','n','i','k','m','o','p','l','Q','A','Z','W','S','X','E','D','C','R','F','V','T','G','B','Y','H','N','U','J','M','I','K','O','L','P','5','6','1','2','8','0','9','3','4','7','#','!','@','-','_']
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
			id += keyChars[random.randint(0,len(keyChars))]
		else:
			numToAdd = 0
			for letter in listOfWords[i]:
				for i in range(128):
					if letter == chr(i):
						numToAdd += i
			random.seed(numToAdd + uniqueNum)
			id += keyChars[random.randint(0,len(keyChars))]
	return id