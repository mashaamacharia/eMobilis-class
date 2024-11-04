from flask import Flask, request, jsonify, render_template
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from PyPDF2 import PdfReader

app = Flask(__name__)

# Step 1: Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

pdf_path = '3 - Computer Software.pdf'  # Replace with the path to your PDF file
pdf_text = extract_text_from_pdf(pdf_path)
print("PDF text extracted successfully")

# Step 2: Set Up GPT-J
print("Loading GPT-J model and tokenizer...")
try:
    tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")
    model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-j-6B")
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
    print("GPT-J model loaded successfully")
except Exception as e:
    print("Error loading GPT-J model:", str(e))

def generate_response(prompt):
    context_window_size = 1000  # Adjust based on GPT-J token limit and desired context size
    prompt_with_context = prompt + "\n\nContext: " + pdf_text[-context_window_size:]  # Use the last part of the context
    responses = generator(prompt_with_context, max_new_tokens=50, num_return_sequences=1, truncation=True)
    return responses[0]['generated_text']

# Step 3: Create Flask App
@app.route('/')
def index():
    return render_template('ui.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
