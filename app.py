import os
from flask import Flask, request, render_template, redirect, url_for, jsonify
from pdf_handler import extract_text_from_pdf, generate_questions, compare_question_and_answer

app = Flask(__name__)

# constants
text = ""
generated_question = ""
user_prompt = ""

#functions
# Function to show the pop-up message with a given message
def show_popup(message):
    messagebox.showinfo("Popup", message)

@app.route('/')
def index():
    return render_template('index.html')

# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    global text
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']

    # condition to check if empty before upload
    if file.filename == '':
        return '''
        <script>
            window.onload = function() {
                alert('No file selected. Please choose a file to upload.');
            };
            setTimeout(function() {
                window.location.href = '/';
            }, 1000); // Redirect after 1 second
        </script>
        '''
    
    # condition to check if file is a PDF
    if file and file.filename.endswith('.pdf'):
        upload_folder = './uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        # saving the pdf file in uploads folder
        pdf_path = os.path.join(upload_folder, file.filename)
        file.save(pdf_path)

        # extract the text
        text += extract_text_from_pdf(pdf_path)
        return redirect('/')
    else:
        return '''
        <script>
            window.onload = function() {
                alert('Please upload a PDF file.');
            };
            setTimeout(function() {
                window.location.href = '/';
            }, 1000);
        </script>
        '''

@app.route('/get_text', methods=['GET'])
def get_text():
    global generated_question
    global text
    generated_question = generate_questions(text)
    return generated_question


@app.route('/get_prompt', methods=['POST'])
def get_prompt():
    data = request.get_json()
    user_prompt = data['prompt']
    global generated_question
    comparison = compare_question_and_answer(generated_question, user_prompt)
    return jsonify({'comparison': comparison})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
