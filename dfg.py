import streamlit as st
import openai


openai.api_type = "open_ai"
openai.api_base = "http://localhost:1234/v1"  # Use the correct base URL for your API
openai.api_key = "NULL"  # Replace with your actual API key or authorization method


def chat_with_gpt(prompt):
    system_instruction = {
        "role": "system",
        "content": "You are a menstrual healthcare assistant. Provide information and advice only related to menstrual health. You should not respond to topics outside this topic.you must not provide any answers to prompts containing mathematical, numerical calculations and current affairs"
    }

    response = openai.ChatCompletion.create(
        model="mistral", 
        messages=[
            system_instruction,
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message['content'].strip()


st.markdown( """
    <style>
    .stApp{
     background-image: url('https://img-cdn.pixlr.com/image-generator/history/66a1e7dcd0c1ae69a309dc1e/be0b3552-fcec-4595-b486-32983997a431/preview.webp');
        background-size: 100%;
        background-position: center;
        background-repeat: no-repeat;
    }
    
    </style>
""",
unsafe_allow_html = True
)


st.title(':red[HerCare]')                                          #
st.title( 'Your Menstrual Healthcare Assistant')

st.write("Ask me anything related to menstrual healthcare!")

user_input = st.text_input("User:")

if user_input:
    response = chat_with_gpt(user_input)
    st.write(f"Chatbot: {response}")

st.write("Note: This chatbot provides information and advice related to menstrual healthcare. For medical advice, please consult a healthcare professional.")



st.audio(r"c:\Users\VISHWANATHA\Downloads\mini.mp3", format="audio/mpeg", loop=True)