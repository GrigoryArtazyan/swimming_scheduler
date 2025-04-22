import streamlit as st
import json
import ast  # To safely parse Python dictionaries from text
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate, 
    AIMessagePromptTemplate, 
    ChatPromptTemplate
)

# Set up the Streamlit UI
st.title(":woman-swimming: Swimming Training Planner")
st.write("Chatbot with Ollama & Langchain")
st.write("Ask me anything about swimming training, and I'll provide you with the best advice based on the knowledge base.")
st.write("Stay on track with your swimming goals! This AI-driven planner helps structure your training schedule, balancing endurance, technique, and strength for optimal progress. Stay motivated, disciplined, and efficient on your journey to success.")


# Load knowledge base from Python file
def load_knowledge():
    with open("source_information_on_training.py", "r", encoding="utf-8") as file:
        content = file.read()
        try:
            knowledge_base = ast.literal_eval(content)  # Convert string to dictionary
        except Exception as e:
            knowledge_base = {"error": f"Could not parse file: {str(e)}"}
    return knowledge_base

knowledge_base = load_knowledge()  # Load the data

# Initialize the LLM model
model = ChatOllama(model="llama3:8b", base_url="http://localhost:11434/")

# Define system message
system_message = SystemMessagePromptTemplate.from_template(
    "You are a helpful AI Assistant. You provide answers based on a training knowledge base."
)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

# User input form
with st.form("chat-form"):
    text = st.text_area("Enter your question here.")
    submit = st.form_submit_button("Submit")

# Function to find the best match in the knowledge base
def retrieve_answer(query):
    for key, value in knowledge_base.items():
        if query.lower() in key.lower():
            return value
    return "I could not find relevant information in the training database."

# Function to generate response
def generate_response(chat_history, user_query):
    # Try retrieving answer from knowledge base first
    knowledge_response = retrieve_answer(user_query)

    # If relevant information is found, use it in the response
    chat_template = ChatPromptTemplate.from_messages(chat_history + [
        HumanMessagePromptTemplate.from_template(f"Use the following information to answer: {knowledge_response}")
    ])
    
    chain = chat_template | model | StrOutputParser()
    response = chain.invoke("")
    
    return response

# Function to retrieve chat history
def get_history():
    chat_history = [system_message]
    for chat in st.session_state['chat_history']:
        user_prompt = HumanMessagePromptTemplate.from_template(chat['user'])
        ai_message = AIMessagePromptTemplate.from_template(chat['assistant'])
        chat_history.extend([user_prompt, ai_message])
    return chat_history

# Handle chat submission
if submit and text:
    with st.spinner("Generating response..."):
        user_prompt = HumanMessagePromptTemplate.from_template(text)
        chat_history = get_history()  # Retrieve past messages
        chat_history.append(user_prompt)  # Add new user input

        response = generate_response(chat_history, text)  # Get AI response

        # Update chat history
        st.session_state['chat_history'].append({'user': text, 'assistant': response})

# Display chat history
st.write("## Chat History")
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**🧑‍💻 User:** {chat['user']}")
    st.write(f"**🤖 Assistant:** {chat['assistant']}")
    st.write("---")
