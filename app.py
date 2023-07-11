import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat



st.set_page_config(page_title="HugChat 1.0")
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# default startup message mode
# Generate empty lists for bot_response and user_input.
## bot_response stores AI generated responses
if 'bot_response' not in st.session_state:
    st.session_state['bot_response'] = ["I'm hugchat, How may I help you?"]

## user_input stores User's questions
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ['Hi!']



# Layout of input/response containers as a placeholder 
input_container = st.container()

colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

############
# User input
## Function for taking user provided prompt as input
############
def get_input():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

## Applying the user input box
with input_container:
    user_input = get_input()

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookie_path="cookies.json")
    print(f"--> call HugChat : {prompt}")
    response = chatbot.chat(prompt)
    print(f"<-- HugChat reply : {response}")
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.user_input.append(user_input)
        st.session_state.bot_response.append(response)
        
        
        
        
        
    if st.session_state['bot_response']:
        ctr = len(st.session_state['bot_response'])
        print(ctr)
        for i in range(len(st.session_state['bot_response'])):
            message(st.session_state['user_input'][i], is_user=True, key=str(i) + '_user')
            print(f"process user message : {i} ")
            message(st.session_state['bot_response'][i], key=str(i))
            print(f"process system message : {i} ")
        
