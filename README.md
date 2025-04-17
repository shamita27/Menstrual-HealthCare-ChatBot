
# HerCare  — Your Menstrual Healthcare Assistant

**HerCare** is a Streamlit-based AI chatbot designed to provide helpful, informative, and empathetic responses related to menstrual health. It leverages large language models (LLMs) through OpenAI and local LLMs via CTransformers.

---

## 🚀 Features

- 💬 Natural language conversation interface
- 🤖 Uses either OpenAI or Mistral models
- 🎨 Custom background UI with Streamlit
- 🎵 Background audio support
- 🔒 Provides safe, focused advice only on menstrual health

---

## 📂 Project Structure

- `app.py`: Core OpenAI-based chatbot script
- `app2.py`: Streamlit UI with LangChain + CTransformers integration
- `dfg.py`: Streamlit app using OpenAI with strict instructions for menstrual health
- `audio_checkig.py`: Embeds audio into the Streamlit app

---

## ⚙️ Installation & Setup

1. **Clone this repo:**
   ```bash
   git clone https://github.com/yourusername/hercare-chatbot.git
   cd hercare-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the app (choose one):**
   ```bash
   streamlit run app2.py    # for Mistral (local model)
   streamlit run dfg.py     # for OpenAI model with strict filter
   ```

---

## 📌 Requirements

- Python 3.8+
- Streamlit
- `openai` Python package
- `langchain`
- `ctransformers` (for local LLMs)

Optional:
- A `mistral-7b-instruct` model file (for `app2.py`)
- MP3 audio file in the correct path

---

## 🔐 Notes

- The assistant **does not respond** to non-health topics, math, or current events.
- Ensure your local OpenAI-compatible API is up and running at `http://localhost:1234/v1`.

---

## 📸 Screenshot

![HerCare Screenshot](https://img-cdn.pixlr.com/image-generator/history/66a1e7dcd0c1ae69a309dc1e/be0b3552-fcec-4595-b486-32983997a431/preview.webp)

---

## 🙏 Disclaimer

> HerCare is an AI-powered information assistant and **not a replacement for medical professionals**. Always consult your doctor for medical advice.

---

## 🧑‍💻 Author

**Vishwanatha**  
Made with ❤️ to help users get informed menstrual healthcare advice using modern AI tools.
