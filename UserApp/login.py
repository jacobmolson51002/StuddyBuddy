#login script for user-side
from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials, firestore, storage
import random
from urllib.parse import quote
import time
import os.path
import pyrebase

	