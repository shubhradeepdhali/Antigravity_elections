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
