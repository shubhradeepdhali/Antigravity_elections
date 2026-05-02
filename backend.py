import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables (API key)
load_dotenv()

app = Flask(__name__)
# Enable CORS so the HTML file can talk to this backend
CORS(app)

# Configure the Gemini API
# Make sure to set GEMINI_API_KEY in your environment variables or a .env file
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Use the gemini-2.5-flash model 
model = genai.GenerativeModel('gemini-2.5-flash')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    
    if not data or 'message' not in data:
        return jsonify({'error': 'Missing message content'}), 400
        
    user_message = data['message']
    country_context = data.get('country', 'us')
    
    # System prompt to guide Gemini to act as an election assistant
    # and return HTML formatted responses matching our UI design
    system_prompt = f"""
    You are ElectIQ, an intelligent, neutral, and educational guide to understanding elections worldwide.
    The user is asking a question primarily in the context of: {country_context.upper()} elections.
    
    Format your response entirely in HTML using the following structure and CSS classes. Do NOT wrap the response in markdown blocks like ```html.
    
    1. Start with an <h3> tag. Inside the h3, start with a span containing a tag (e.g. <span class="tag tag-blue">Concept</span>, tag-green for Global, tag-orange for Timeline), followed by the title of your response.
    2. Use standard <p>, <ul>, <ol>, and <li> tags for text.
    3. If providing a timeline or sequence of events, use this structure:
       <div class="timeline">
           <div class="timeline-item">
               <div class="timeline-date">Date or Phase Name</div>
               <div><strong>Title.</strong> Description goes here.</div>
           </div>
           <!-- add more timeline-items as needed -->
       </div>
    4. For important callouts or fun facts, use:
       <div class="info-card">
           <strong>Bold Heading:</strong> Text goes here.
       </div>
       
    Keep responses concise, neutral, and highly educational. Avoid political bias.
    """
    
    full_prompt = f"{system_prompt}\n\nUser Question: {user_message}"
    
    try:
        # Generate response from Gemini
        response = model.generate_content(full_prompt)
        
        # Strip potential markdown formatting that Gemini might add around HTML
        clean_html = response.text.replace('```html', '').replace('```', '').strip()
        
        return jsonify({'response': clean_html})
        
    except Exception as e:
        available_models = []
        try:
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    available_models.append(m.name)
        except Exception:
            pass
            
        print(f"Error calling Gemini: {e}")
        error_msg = f'Gemini API Error: {str(e)}'
        if available_models:
            error_msg += f"<br><br><b>Available Models for your key:</b> {', '.join(available_models)}"
            
        return jsonify({
            'error': error_msg
        }), 500

if __name__ == '__main__':
    # Run the server on port 5000
    print("ElectIQ Backend running on http://localhost:5000")
    print("Make sure you have set the GEMINI_API_KEY environment variable!")
    app.run(debug=True, port=5000)
