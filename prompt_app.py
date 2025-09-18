import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Load environment variables from .env file
load_dotenv()

st.title("Simple Chat Prompt Interface")

@st.cache_resource
def get_chat():
    """Create and return the chat chain with history"""
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.environ.get("GEMINI_API_KEY"),
        temperature=0.2,
        transport="rest"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a concise, polite assistant. Use prior turns for continuity."),
        MessagesPlaceholder("history"),
        ("human", "{question}")
    ])

    chain = prompt | llm | StrOutputParser()
    history = ChatMessageHistory()

    def get_session_history():
        return history
    
    chat = RunnableWithMessageHistory(
        chain,
        get_session_history=get_session_history,
        input_messages_key="question",
        history_messages_key="history",
    )
    return chat

# Initialize session state for history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from LLM
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                chat = get_chat()
                response = chat.invoke({"question": prompt})
                st.markdown(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()