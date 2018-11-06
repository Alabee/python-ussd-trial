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
	
	user_responses = text.split('*')

	#level 1
	if text == "":
		response = "CON Welcome to Femi-jirani\nPlease select an option to proceed\n1. Donate\n2. Apply for sanitary towels"
	
	#level 2	
	elif text == "1":
		response = "CON Please enter amount to donate"

	elif text == "2":
		response = "CON Please enter the following details\nFirst name"

	#level 3
	elif user_responses[1] != "" and len(user_responses) == 2:
		if user_responses[0] == "1":
			response = "CON Please enter M-Pesa pin"

		elif user_responses[0] == "2":
			response = "CON Last name"

	#level 4
	elif user_responses[2] != "" and len(user_responses) == 3:
		if user_responses[0] == "1":
			response = "END Thank you for your donation.\nIt counts."

		elif user_responses[0] == "2":
			response = "CON ID number/DOB(DD/MM/YY)"
	
	#level 5
	elif user_responses[3] != "" and len(user_responses) == 4:
		response = "CON Help us establish your location\nCounty"
	
	#level 6
	elif user_responses[4] != "" and len(user_responses) == 5:
		response = "CON Town"

	#level 7
	elif user_responses[5] != "" and len(user_responses) == 6:
		response = "CON Estate/Village"

	#level 8
	elif user_responses[6] != "" and len(user_responses) == 7:
		response = "CON Nearest landmark(Primary school/secondary school/hospital/local church"

	#level 9
	elif user_responses[7] != "" and len(user_responses) == 8:
		response = "END Your application has been received.\n Confirmation will be sent to you via text."

	else:
		response = "END Thank you for visiting Femi-jirani!"


	#request.content_type = text/plain
	#request.method = GET
	#request.get_host() = e3602885.ngrok.io
	#get_port() = 8000
	#get_full_path() = /
	#api_post = request.method 

	#getting values from POST request from Africs's talking API
	

		

	f = open("guru99.txt","a+")
	f.write(str(text) + "\n")
	f.write(str(user_responses) + "\n")
	f.write(str(phoneNumber) + "\n\n")
	f.close()

	return HttpResponse(response, content_type="text/plain")