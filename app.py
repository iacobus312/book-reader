from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Load the homepage HTML

# Route to serve the PDF
@app.route('/pdf/<filename>')
def display_pdf(filename):
    return send_from_directory('files', filename, mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
