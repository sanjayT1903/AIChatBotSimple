#Github Simplified Example


#THIS IS A SIMPLIFIED SYSTEM OF USING AI RESPONSES IN WHATAPP THAT CAN BE FREE FOR THE USER USING MAKER SUITE AND GREEN API.
#RECIEVE -> PROCESS -> DELETE -> FINISH  (THE METHODOLOGY OF THIS DESIGN)
#THIS DESIGN IS PURPOSFULLY LIMITED FOR EASIER USE OF USERS
#THIS IS PART PF A LARGER PROJECT TO KEEP AI PROJECT PRACTICE AND PROJEC CREATION INEXPENSIVE FOR AMUTEUR CODERS.
import os
import requests
from whatsapp_api_client_python.API import GreenApi 
from whatsapp_api_client_python import API
import json
from datetime import datetime
#BARD Calibration
import google.generativeai as palm


"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm
palm.configure(api_key="YOUR API KEY") #to use Makersuite, go to the waitlist and then get your key



def sending(message): #sending messages to a number of your choice using green API
    url = "https://api.green-api.com/waInstance{{7103849646}}/sendMessage/{{d9dac21fbc99470594388d556a0a5103ddedc1cc8db347a4a2}}"

    payload = "{\r\n\t\"chatId\": \"a phone number@c.us\",\r\n\t\"message\": \"I use Green-API to send this message to you!\"\r\n}"
    headers = {
    'Content-Type': 'application/json'
    }
    
    response = greenAPI.sending.sendMessage("a phone number @c.us", message)
    greenAPI.receiving.deleteNotification(2)
    print(response.data)
    exit()

#counter =0
def aiChat(m):
  greenAPI.receiving.deleteNotification(1)
  defaults = { #Settings for our ai
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
} #Context and examples for AI
  context = "Take the users input as some sort of achievement they have done, then send out advice on how to make that achievement into a larger project to help their resume. The advice should come out in a bullet point list."
  examples = [
   [
    "I just made a Animal Shelter Club",
    "Great to hear, here are three things to do to make this club go further\n\n1- Make donation stands and events where money can be collected. Make sure to place this on some sort of website as a from of validating your results.\n\n2- Partner with real animal shelters and train your club members on proper ways to deal with Animals that have trauma.\n\n3- Create a network of other Animal Shelter clubs in different areas around you that follow your principals.\n\nThose are just some ways to improve your idea for your resume."
   ],
   [
    "I just created an AI chatbot",
    "That's great! Here are some ways to make your AI chatbot into a larger project to help your resume:\n\n1. **Document your process.** Write a blog post or article about how you created the chatbot, what challenges you faced, and how you overcame them. This will show potential employers that you have the skills and knowledge to develop complex software projects.\n2. **Share your chatbot with others.** Post it on GitHub or another code repository, and let people know how they can use it. This will help you build a reputation as a developer who creates useful and innovative software.\n3. **Use your chatbot to solve a real-world problem.** For example, you could create a chatbot that helps people find information about a particular topic, or that provides customer service for a company. This will show potential employers that you can use your skills to create software that has a positive impact on the world.\n4. **Continue to develop your chatbot.** Add new features, improve the user experience, and make it more robust. This will show potential employers that you are passionate about your work and that you are always looking for ways to improve your skills.\n\nI hope these tips help you make your AI chatbot into a larger project that will help your resume."
   ]
 ]
  messages = []
  messages.append(m)
  response = palm.chat(
    **defaults,
   context=context,
    examples=examples,
    messages=messages
  )
  print(response.last) # Response of the AI to your most recent request
  sending(response.last)
  exit()
    



holder = ""



greenAPI = API.GreenApi(
    "GREENCHATCODE", "GREENAPIKEY"
    )

def mainTrail(): #Escentailly the main method of this program Recieve - process then end the program.
   
   
   print(greenAPI.receiving.receiveNotification())
  
   greenAPI.webhooks.startReceivingNotifications(onIncomingMessageReceived)
   
   exit()


def onIncomingMessageReceived(typeWebhook, body): #RECIEVE THE INITIAL WEBHOOK
 #print(body)
   
 
 #DIFFERE TYPES OF WEBHOOKS EXIST
 if typeWebhook == 'incomingMessageReceived':
  
  if body['messageData']['typeMessage'] == 'textMessage':

    
   # greenAPI.serviceMethods.deleteMessage("12149981139@c.us",idData)
    print(body['messageData'])

    messageData = body['messageData']["textMessageData"]['textMessage'] #PARSING FOR MESSAGE IN THE WEBHOOK
    message = json.dumps(messageData, ensure_ascii=False)
    messageFinal = message.replace('"','')
    holder = messageFinal
    print(messageFinal)
    greenAPI.receiving.deleteNotification(1)
    
    aiChat(messageFinal)
    
    



if __name__ == "__main__":
   #print("hello")
    mainTrail()

#print(response.text.encode('utf8'))
     




