


import streamlit as st
from langgraph.graph import StateGraph, START, END
from together import Together
from typing import TypedDict, Annotated
from dotenv import load_dotenv
import time
import os
import operator
import re

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment variable
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")

# Initialize the Together client if the API key is available
client = Together(api_key=TOGETHER_API_KEY) if TOGETHER_API_KEY else None

# Define the UPSCState class
class UPSCState(TypedDict):
    essay: str
    language_feedback: str
    analysis_feedback: str
    clarity_feedback: str
    overall_feedback: str
    individual_scores: Annotated[list[int], operator.add]
    avg_score: float

# Function to safely extract score from feedback
def extract_score(feedback: str):
    # Use regex to find a score in the feedback
    match = re.search(r'\b([0-9]|10)\b', feedback)
    if match:
        return int(match.group(0))
    else:
        return 0  # Default score if no score is found

# Functions to evaluate different aspects of the essay

def evaluate_language(state: UPSCState):
    prompt = f'Evaluate the language quality of the following essay and provide a feedback and assign a score out of 10 \n {state["essay"]}'
    
    if client is not None:
        response = client.chat.completions.create(
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500,
        )
        feedback = response.choices[0].message.content.strip()
        score = extract_score(feedback)  # Extract score safely
    else:
        feedback = "API key is missing or invalid."
        score = 0

    return {'language_feedback': feedback, 'individual_scores': [score]}

def evaluate_analysis(state: UPSCState):
    prompt = f'Evaluate the depth of analysis of the following essay and provide a feedback and assign a score out of 10 \n {state["essay"]}'
    
    if client is not None:
        response = client.chat.completions.create(
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500,
        )
        feedback = response.choices[0].message.content.strip()
        score = extract_score(feedback)  # Extract score safely
    else:
        feedback = "API key is missing or invalid."
        score = 0

    return {'analysis_feedback': feedback, 'individual_scores': [score]}

def evaluate_thought(state: UPSCState):
    prompt = f'Evaluate the clarity of thought of the following essay and provide a feedback and assign a score out of 10 \n {state["essay"]}'
    
    if client is not None:
        response = client.chat.completions.create(
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500,
        )
        feedback = response.choices[0].message.content.strip()
        score = extract_score(feedback)  # Extract score safely
    else:
        feedback = "API key is missing or invalid."
        score = 0

    return {'clarity_feedback': feedback, 'individual_scores': [score]}

def final_evaluation(state: UPSCState):
    prompt = f'Based on the following feedbacks create a summarized feedback \n language feedback - {state["language_feedback"]} \n depth of analysis feedback - {state["analysis_feedback"]} \n clarity of thought feedback - {state["clarity_feedback"]}'
    
    if client is not None:
        response = client.chat.completions.create(
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500,
        )
        overall_feedback = response.choices[0].message.content.strip()
    else:
        overall_feedback = "API key is missing or invalid."
    
    avg_score = sum(state['individual_scores']) / len(state['individual_scores'])

    return {'overall_feedback': overall_feedback, 'avg_score': avg_score}

# Set up the StateGraph
graph = StateGraph(UPSCState)

# Add nodes to the graph
graph.add_node('evaluate_language', evaluate_language)
graph.add_node('evaluate_analysis', evaluate_analysis)
graph.add_node('evaluate_thought', evaluate_thought)
graph.add_node('final_evaluation', final_evaluation)

# Add edges to the graph
graph.add_edge(START, 'evaluate_language')
graph.add_edge(START, 'evaluate_analysis')
graph.add_edge(START, 'evaluate_thought')
graph.add_edge('evaluate_language', 'final_evaluation')
graph.add_edge('evaluate_analysis', 'final_evaluation')
graph.add_edge('evaluate_thought', 'final_evaluation')
graph.add_edge('final_evaluation', END)

# Compile the workflow
workflow = graph.compile()

# Streamlit UI
st.title('UPSC Essay Evaluation Chatbot')

# Initialize session state for message history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Display conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# User input for the essay
user_input = st.chat_input('Type your essay here:')

if user_input:
    # Add user message to message history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Set up the state for the workflow and invoke it
    initial_state = {'essay': user_input}

    # Evaluate and stream feedback
    with st.chat_message('assistant'):
        feedback_placeholder = st.empty()  # Empty placeholder for streaming the feedback
        feedback_message = ''
        final_state = workflow.invoke(initial_state)

        # Simulate streaming the evaluation content
        for key, value in final_state.items():
            feedback_message += f"{key.capitalize()}: {value}\n"
            feedback_placeholder.text(feedback_message)
            time.sleep(0.1)  # Simulate delay

        st.session_state['message_history'].append({'role': 'assistant', 'content': feedback_message})
