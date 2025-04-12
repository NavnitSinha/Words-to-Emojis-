#Example Few-Shot Prompt Use-Case (Emoji Conversion):

#header files
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import os
from api import api

os.environ["GOOGLE_API_KEY"] = api

llm = ChatGoogleGenerativeAI(
    model = "gemini-1.5-pro-latest",
    temperature = 0.6
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a pro at converting sentences into emojis. Go ahead and convert the following sentence into emojis."),
    ("human", "I love pizza and ice cream"),
    ("ai", "🍕❤️🍦"),
    ("human", "It’s raining and I forgot my umbrella"),
    ("ai", "🌧️😩☔"),
    ("human", "I’m going on a vacation to the beach"),
    ("ai", "🏖️✈️😎"),
    ("human", "{user_input}")
])

chain = prompt | llm

u_input = input("Let's covert your texts into Emojis. Enter what you want to convert into Emojis and I will do it for you: ")

response = chain.invoke({"user_input": u_input})
print("Here's your Output!\n")
print(response.content)