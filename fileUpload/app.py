# Import necessary libraries
from io import BytesIO
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy

# Create a Flask web application
app = Flask(__name__)

# Configure the SQLAlchemy database settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'  # Use SQLite as the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a SQLAlchemy model for file uploads
class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each uploaded file
    filename = db.Column(db.String(10))  # Store the filename
    data = db.Column(db.LargeBinary)  # Store the binary data of the file

# Define a route for the homepage, which handles file uploads and displays a form
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']  # Get the uploaded file from the request
        if file:
            # Create an Upload object and store it in the database
            upload = Upload(filename=file.filename, data=file.read())
            db.session.add(upload)
            db.session.commit()
            return f'Uploaded: {file.filename}'  # Confirmation message
    return render_template('index.html')  # Render the HTML template for file upload

# Define a route for downloading files based on their upload_id
@app.route('/download/<upload_id>')
def download_file(upload_id):
    uploaded_file = Upload.query.get(upload_id)  # Retrieve the uploaded file by its ID
    if uploaded_file:
        # Send the file as a response with appropriate headers for download
        return send_file(BytesIO(uploaded_file.data), download_name=uploaded_file.filename, as_attachment=True)
    return "File not found"  # Return an error message if the file is not found

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True,port='5001')  # Run the Flask application in debug mode
