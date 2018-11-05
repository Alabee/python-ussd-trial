from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
# Create your views here.

@csrf_exempt
@api_view(['POST'])
def index(request):
	text = request.POST['text']
	phoneNumber = request.POST['phoneNumber']
	#Considering text contains the responses given by the user as a string separated by asterisk e.g "1*500" or "2*Jane"
	#We use the asterisk to separate the responses and store them in an array
	if len(text) > 1:
		user_responses = text.split('*')
		user_option = user_responses[1]
	#level 1
	if text == "":
		response = "CON Welcome to Femijirani\nPlease select an option to proceed\n1. Donate\n2. Apply for sanitary towels"
	
	#level 2	
	elif text == "1":
		response = "CON Please enter amount to donate"

	elif text == "2":
		response = "CON Please enter the following details\nFirst name"
	
	#level 3
	elif user_option == "1" and user_responses.index(user_option) == 1:
		response = "CON Please enter M-Pesa pin"

	elif user_option == "2" and user_responses.index(user_option) == 1:
		response = "CON Second name"

	else:
		response = "END Thank you!"


	#request.content_type = text/plain
	#request.method = GET
	#request.get_host() = e3602885.ngrok.io
	#get_port() = 8000
	#get_full_path() = /
	#api_post = request.method 

	#getting values from POST request from Africs's talking API
	

		

	f = open("guru99.txt","a+")
	f.write(str(text) + "\n")
	#f.write(str(user_responses) + "\n")
	f.write(str(phoneNumber) + "\n\n")

	return HttpResponse(response, content_type="text/plain")