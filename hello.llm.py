import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq



load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API KEY NOT FOUND")


client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-20b"

role = "user"
prompt = "Do You know padho with pratyush"

message={
    "role": role,
    "content": prompt
}


messages = [message]  #list of messages

response = client.chat.completions.create(model = model, messages = messages)

answer = response.choices[0].message.content
print(answer)



# Notes of Day 1


# LLM Call and Understanding Response 

# 1) .venv (Virtual Environment)
 
 
#     Firstly We take example of to understand the virtual Environment How it works 


#     ek person ek din gta 5 khel rha hai ab gta 5 ke liye driver 2.0 ki j4rurat jisse voh gta 5 khel skta toh usne driver 2.0 install kiya or kehla 
#     kuch din baad usko gta 6 khelne ka maan hua toh but gta 6 khelne ke liye usne fir khelna start kiya but uske laptop me jo driver 2.0 tha usse voh gta 6 kyoki uske
#     liye driver 4.0 update krdiya pure laptop jisse gta 6 chal padi but fir baad me jb voh gta 5 khelne gya toh gta 5 aad gyi voh chali kyoki UserWarning
#     pure laptop ka driver 4.0 update krdiya 
    
#     toh uske liye venv (Virtual environment aaya)
    
#     ab virtual  environment me kya hai ek har system ke liye ek class bnegi gta 5 ke liye ek alg class bnali driver 2.0 install krdiya na ki laptop ka us class ka version install krdiya 
#     or gta 6 ke liye ek alg class bnadi or usme driver 4.0 install krdiya means har class ya room ke liye ek venv activate jisse us class ya room ka effect dusri class ke version 
#     par na pade this is the process of venv
    
#     jiske liye one thing to activate venv in every class  ->  ./venv/scripts/activate
    
    
#     Now we start the How LLM Call works and after we review the code properly
    
#     Firstly Take a step then one by one discuss
    
#     1) API Key 
       
#        Client(me) -> server(Groq)  (Open chatgpt like pages and ask me anything)
       
       
#     2) Model -> To ensure that model name is exact  (For ex: "openai/gpt-oss-20b")

#     3) Message -> 

#             1) role
#             2) content 
            
#     Now role have another three part 
#             1) User 
#             2) Assistant
#             3) System
    
#     Role

# Now Role means to describle the role menas us chatgpt ke model ko phele role btana  ki kya role 

# For example i want to know about the age of virat kohli so  shuruat me mene chatgpt ko btaya Who is virat kohli then mene usse pucha what is his age then voh 
# cheej kka response uske role rrelated dega agr mai sidha puch leta ki what is his role so voh bta nhi pta uska aage se response hona tha ki kiski age puch rhe ho so phele role btayo ki kis related hai 


# Now after Assistant ko uske response Dega

# System-> now system par baat kr lete hai 

# system meanns ki maine usko system role diya kis behaviour ke sath tune jwab dena hai for ex mera aaj interview hai toh mujhe one line answer de har question this is the system role , bada choda anwwer mat de 
# this is the system role

# Now at the end 

# We discuss Response 
#     Response have 2 part 
    
#     1) Choices 
#     2) Usages
    
#     Choices means for example jab hum kabhi bhi kuch puchta hai chatgpt se tab voh  kabhi kabhi 3 4 response de deta fir user us us hissab se answer select kr leta hia 
    
#     so choices menas array of answer ki main choice[0] select kruga
    
#     2) usage 
    
#     Usage means to debited the token from every prommpt and some have limit  and but some have limitless it depennds on the  model
    
