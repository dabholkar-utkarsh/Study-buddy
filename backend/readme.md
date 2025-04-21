# Backend API

This backend API is built using Flask and provides endpoints for processing PDF files and querying information from them using a vector store.

## Project Structure

- `app.py`: Initializes the Flask application and sets up routes.
- `routes.py`: Contains the route definitions and their logic.
- `utils.py`: Contains utility functions for processing PDFs and creating the FAISS store.
- `AI_Engineering.pdf`: Example PDF file for testing.

## Setup

1. **Install Dependencies**

   Make sure you have Python installed. Then, install the required packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY="your_openai_api_key"
   ```

3. **Run the Application**

   Start the Flask server:

   ```bash
   python app.py
   ```

   The server will run on `http://localhost:5000` by default.

## API Endpoints

### 1. Process PDF

- **Endpoint**: `/process-pdf`
- **Method**: POST
- **Description**: Upload a PDF file to process and create a FAISS vector store.
- **Request**:
  - Form-data with a key `file` containing the PDF file.

### 2. Process Pre-uploaded PDF

- **Endpoint**: `/process-preuploaded-pdf`
- **Method**: POST
- **Description**: Process a pre-uploaded PDF file (`AI_Engineering.pdf`) and create a FAISS vector store.

### 3. Ask Question

- **Endpoint**: `/ask`
- **Method**: POST
- **Description**: Query the processed PDF for information.
- **Request**:
  - JSON body with a key `question` containing the question to ask.

## Example Usage

1. **Process a PDF**

   ```bash
   curl -X POST -F "file=@path/to/your/file.pdf" http://localhost:5000/process-pdf
   ```

2. **Process Pre-uploaded PDF**

   ```bash
   curl -X POST http://localhost:5000/process-preuploaded-pdf
   ```

3. **Ask a Question**

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"question": "What are the key concepts in Chapter 1?"}' http://localhost:5000/ask
   ```

## Notes

- Ensure the `AI_Engineering.pdf` file is in the same directory as `app.py` for the pre-uploaded PDF endpoint.
- The server must be running to process requests.
