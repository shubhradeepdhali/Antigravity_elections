# ElectIQ - Your Intelligent Election Assistant 🗳️

ElectIQ is a stunning, interactive web application that leverages the power of the Google Gemini AI to educate users on global election processes. With an emphasis on neutrality and clear explanations, this tool helps demystify political systems, voter registration, campaign finance, and more.

## ✨ Features

- **Rich, Interactive UI:** A premium deep navy and gold aesthetic built from scratch using HTML and vanilla CSS. Features a dynamic typing indicator and smooth UI transitions.
- **Global Context:** Supports election information for multiple regions including the United States, United Kingdom, India, and the European Union.
- **Smart Prompts:** "Quick Chips" and starter prompt cards allow for immediate engagement with common questions like gerrymandering or ranked-choice voting.
- **Google Gemini Integration:** A lightweight Flask backend processes questions through the blazing-fast `gemini-2.5-flash` model, seamlessly parsing structured HTML responses right into the chat.
- **Fully Responsive:** Beautifully designed sidebar layout that works smoothly across different screens.

## 🛠️ Technology Stack

- **Frontend:** Vanilla HTML5, CSS3, JavaScript (Fetch API)
- **Backend:** Python 3, Flask, Flask-CORS
- **AI Integration:** Google Generative AI (`google-generativeai` SDK)

---

## 🎯 Hackathon Information

### 🏢 Chosen Vertical
**Civic Tech & Education** - This project aims to empower citizens by making complex electoral systems, voting procedures, and political nuances accessible and easy to understand globally.

### 🧠 Approach and Logic
The goal was to create an intelligent system that feels like a premium conversational agent rather than a generic search engine. To achieve this, the logic was divided into three core pillars:
1. **Unbiased Tone System Prompting:** The Gemini AI is strictly instructed via a backend system prompt to act neutrally and avoid political bias, ensuring all information is purely educational.
2. **Context-Aware Formatting:** Instead of returning plain text or markdown, the AI is prompted to return pre-formatted semantic HTML (using custom CSS classes for tags, timelines, and info-cards).
3. **Seamless UX:** A carefully crafted frontend interface intercepts the backend HTML payloads and injects them directly into the DOM with smooth animations, giving users a highly polished, app-like experience.

### ⚙️ How the Solution Works
1. The user selects a country context (US, UK, India, EU) and types a question or clicks a Quick Prompt chip in the `electiq.html` interface.
2. The frontend JavaScript triggers an asynchronous `fetch` POST request to the Flask server (`backend.py`) carrying the user's query and regional context.
3. The Flask server combines the query with a rigid System Prompt designed to enforce HTML structure, educational neutrality, and visual formatting rules.
4. The backend securely queries the **Google Gemini 2.5 Flash** model via the Generative AI SDK.
5. The generated HTML response is returned to the frontend, where it is dynamically appended to the chat interface alongside an animated typing indicator.

### 🤔 Assumptions Made
- Users will access the app using a modern web browser that supports the Fetch API and CSS variables.
- Information requests are generally inquisitive and educational, rather than seeking real-time polling data or highly subjective political opinions.
- The Gemini model will consistently adhere to the structural HTML constraints defined in the system prompt.
- The app is deployed in an environment (like Google Cloud Run) that automatically injects the `$PORT` environment variable for the web server to bind to.

---

## 🚀 Getting Started

To run ElectIQ locally on your machine, follow these simple steps:

### 1. Prerequisites
Make sure you have Python installed on your system.

### 2. Install Dependencies
Navigate to the project directory in your terminal and install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Set Up Your API Key
You will need a Google Gemini API Key.
1. Create a file named `.env` in the root directory of the project.
2. Add your API key to the file like this:
```env
GEMINI_API_KEY=your_actual_api_key_here
```
*(Note: Do not wrap your API key in quotes. The `.gitignore` file is already set up to ensure this file is never pushed to GitHub).*

### 4. Start the Backend Server
Run the Flask backend server:
```bash
python backend.py
```
The server will start on `http://localhost:5000` and listen for incoming chat requests.

### 5. Launch the App
Since the frontend uses basic web technologies, you don't need a build step! Simply open the `electiq.html` file in any modern web browser (Chrome, Edge, Firefox, Safari).

Select a country, type a question (or click a quick chip), and start learning!

---

## 👨‍💻 Author

Crafted with precision by **Shubhradeep Dhali**
