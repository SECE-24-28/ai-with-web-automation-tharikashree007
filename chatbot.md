# GPT-OSS-120B Interactive Chatbot

A simple AI-powered chatbot built using Python and the Groq API. This project uses the GPT-OSS-120B Large Language Model to generate intelligent responses in real time through a terminal-based interface.

---

## Features

- Interactive command-line chatbot
- Real-time AI-generated responses
- Powered by GPT-OSS-120B
- Simple and lightweight implementation
- Easy to customize and extend
- Continuous conversation support

---

## Tech Stack

- Python 3.x
- Groq API
- GPT-OSS-120B Model

---

## Prerequisites

Before running the project, ensure you have:

- Python 3.8 or higher
- A Groq API Key
- Internet connection

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/gpt-oss-chatbot.git
cd gpt-oss-chatbot
```

### Install Dependencies

```bash
pip install groq
```

---

## Project Structure

```text
gpt-oss-chatbot/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

---

## Configuration

Replace the API key in the code:

```python
client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)
```

You can obtain your API key from the Groq Console.

---

## Usage

Run the chatbot:

```bash
python chatbot.py
```

---

## Source Code

```python
from groq import Groq

client = Groq(
    api_key="YOUR_GROQ_API_KEY"
)

print("GPT-OSS-120B Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_completion_tokens=1024
    )

    print("\nAI:", response.choices[0].message.content)
    print()
```

---

## Example

### Input

```text
You: What is Artificial Intelligence?
```

### Output

```text
AI: Artificial Intelligence (AI) is the simulation of human intelligence in machines that can learn, reason, and make decisions.
```

---

## Applications

- Personal AI Assistant
- Educational Chatbot
- Research Assistant
- Customer Support Bot
- Content Generation
- Coding Assistant

---

## Future Improvements

- GUI using Tkinter
- Web Interface using Flask or Streamlit
- Voice Input and Output
- Conversation History
- Database Integration
- Multi-language Support

---

## Learning Outcomes

This project helps understand:

- API Integration
- Large Language Models (LLMs)
- Conversational AI
- Python Development
- Prompt Engineering

---

