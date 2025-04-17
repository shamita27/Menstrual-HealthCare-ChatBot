import streamlit as st
from app import chat_with_gpt
from langchain.llms import CTransformers

# Set the page configuration
st.set_page_config(
    layout='centered', page_icon='😆'
)

# Set background and styles
page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("imageURL");
    background-size: 100% 100%;
    }

    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }

    [data-testid="stBottomBlockContainer"] {
    background-color: rgba(0, 0, 0, 0);
    }

    .st-emotion-cache-uhkwx6.ea3mdgi6 {
        background-color: rgba(0, 0, 0, 0);
    }
    </style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Set the title of the app
st.title(':orange[HerCare]')

# Load the language model
@st.cache_resource
def load():
    #model_path = 'Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q5_0.gguf'
    model_path = 'Mistral-7B-Instruct-v0.1-GGUF\mistral-7b-instruct-v0.1.Q5_0.gguf'
    llm = CTransformers(
        model=model_path,
        model_type='mistral',
        config={
           'max_new_tokens': 1024,
                'temperature': 0.8,
                'top_p': 0.95,
                'top_k': 40,
                'repetition_penalty': 1.1,
        }
    )
    return llm

# Generate response based on the input and model instruction
def generate(x):
    model_instruction = (
        "You are a helpful menstrual healthcare assistant. "
        "Please provide information and advice related to menstrual health. "
        "Do not respond as 'User' or pretend to be 'User'."
    )
    prompt = f"{model_instruction} user: {x}\n assistant_response:"
    model = load()
    output = model(prompt)
    return output

# User input field
x = st.text_input('Hello, I am your menstrual health assistant. How can I help you today?')

# Generate response on button press
if st.button("Ask"):
    if x:
        y = generate(x)
        st.write(y)
    else:
        st.write("Please enter a question or statement related to menstrual health.")
else:
    st.write("Goodbye")