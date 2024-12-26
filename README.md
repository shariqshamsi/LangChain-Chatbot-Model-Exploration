# LangChain-Chatbot-Model-Exploration
This repository contains two implementations of Q&A chatbots leveraging the **LangChain framework** to integrate and experiment with different language models:  
1. **OpenAI GPT Chatbot**  
2. **Gemma-based Chatbot**  

Both implementations provide an interactive, user-friendly interface powered by **Streamlit** to explore and compare the capabilities of these language models.  

---

## Core Features  

### 1. **Dual Chatbot Integration**  
- **OpenAI GPT Chatbot:**  
  Utilizes GPT models (`gpt-4`, `gpt-3.5-turbo`) for high-quality, detailed responses.  
- **Gemma Chatbot:**  
  Integrates the `gemma2:2b` model for efficient, lightweight answers.  

### 2. **Dynamic Parameter Customization**  
- Adjust **temperature** to control the creativity of the responses.  
- Configure **max tokens** to limit the response length.  
- Select from multiple models to tailor chatbot behavior.

### 3. **LangSmith Tracing**  
- Activities and operations are traced using **LangSmith**, enabling detailed insights into how the prompts and models are working during runtime.

### 4. **Modular Prompting with LangChain**  
- Uses `ChatPromptTemplate` for creating flexible, reusable prompts.  
- Implements LangChain pipelines for chaining prompts, models, and parsers seamlessly.  

### 5. **Interactive Streamlit UI**  
- A simple interface to input questions, select models, and fine-tune parameters.  
- Sidebar customization for API keys and model settings.  

### 6. **Privacy-Conscious Setup**  
- `.env` file is excluded from the repository to protect sensitive API keys. Users must create their own `.env` file locally with the necessary credentials.  

---

## Installation  

### 1. Clone the Repository  
```bash
git clone https://github.com/yourusername/LangChain-Chatbot-Model-Exploration.git
cd LangChain-Chatbot-Model-Exploration
