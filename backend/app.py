from flask import Flask
from dotenv import load_dotenv
import os
from routes import setup_routes

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size

# Create uploads directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Setup routes
setup_routes(app)

if __name__ == '__main__':
    app.run(debug=True) 