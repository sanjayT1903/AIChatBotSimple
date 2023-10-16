from transformers import MarkupLMFeatureExtractor, MarkupLMProcessor
from bs4.element import Comment
from bs4 import BeautifulSoup

"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as palm
def aiHelper(inputer):
    palm.configure(api_key="AIzaSyCHHmecpNDam9V3qPC52FbcBgHkhLnSOeA")
    
    defaults = {
    'model': 'models/text-bison-001',
    'temperature': 0.7,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
    'max_output_tokens': 1024,
    'stop_sequences': [],
    'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":4},{"category":"HARM_CATEGORY_TOXICITY","threshold":4},{"category":"HARM_CATEGORY_VIOLENCE","threshold":4},{"category":"HARM_CATEGORY_SEXUAL","threshold":4},{"category":"HARM_CATEGORY_MEDICAL","threshold":4},{"category":"HARM_CATEGORY_DANGEROUS","threshold":4}],
    }
    input = inputer
    prompt = f"""input: Out of 1-10 where 10 is the most inappropriate statement 1 being least - @turtleseal Next time I got a post abt the Swim Team I’ll add it
    sanjay_thasma
    @turtleseal U think I can post the infamous chair photo
    sanjay_thasma
    Ahhhhhhh
    Gay
    Group A messed up
    lol alex looks gay
    output: 9 - The term gay in this context can be seen as highly offensive
    input: Out of 1-10 where 10 is the most inappropriate statement 1 being least - @turtleseal Next time I got a post abt the Swim Team I’ll add it
    sanjay_thasma
    Eating poop tastes so good
    You are weird
    output: 5- Eating poop is an inappropriate for talking but not necessarily horrible
        input: I would love to see you shirtless
        output: 5 - It is normal to want to see someone shirtless but it is a bit inappropriate to say out loud and can make people uncomfortable
    input: I hate black people
    output: 10 - Hate speech is not tolerated
    input: sanjay_thasma
    Ahhhhhhh
    Gay
    Group A messed up
    lol alex looks gay
    output: 8- Gay is a derogatory term and is offensive to a lot of people
    input: I love eating muffins
    output: 1 - There is nothing wrong with this statement
    input: {input}
    output:"""

    response = palm.generate_text(
    **defaults,
    prompt=prompt
    )
    print(response.result)
    return response.result

page_name_1 = "post_comments_1.html"

with open(page_name_1) as f:
    single_html_string = f.read()

# The provided HTML string
html_segment = single_html_string

# Parse the HTML segment using BeautifulSoup
soup = BeautifulSoup(html_segment, 'html.parser')

# Find all the elements with class "_2pin _a6_q" (or use other suitable class)
elements = soup.find_all('td', class_='_2pin _a6_q')

# Extract the comment values and store them in an array
comment_values = []
for element in elements:
    comment = element.find('div').text
    comment_values.append(comment)
i = 0
string = ""
bad_values = []

my_list = ["gay", "terrorism"] #need to add more



# Print the comment values in an array
for value in comment_values:
    if value.find("PM") != -1 or value.find("AM") != -1:
        if i ==1:
            i=0
            bad_values.append(string + " -> " + value)
            #print(value)
    else:
        #print(value)
        holder =""
        if any(value.lower() in item for item in my_list):
            holder2 = aiHelper(value)
            #print(str(holder) )
            charVal2 = str(holder2)[0]
            #print(charVal)
            intVal2 = int(charVal2)
            #print(intVal)
            if intVal2>=6:
                string = value
                i = 1
        elif value.count(" ") >0: #change gay wth array of derogatory words
            holder = aiHelper(value)
            #print(str(holder) )
            charVal = str(holder)[0]
            #print(charVal)
            intVal = int(charVal)
            if charVal==1 and  str(holder)[0] == 0:
                intVal = 10
            #print(intVal)
            if intVal>=6:
                string = value
                i = 1
        
print("---------------------------------------" + "\n")
for element in bad_values:
    print(element)
