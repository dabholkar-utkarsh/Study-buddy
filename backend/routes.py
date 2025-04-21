from flask import request, jsonify
from utils import process_pdf, split_documents, create_faiss_store, make_qa_chain
import os
from werkzeug.utils import secure_filename

def setup_routes(app):
    @app.route('/process-pdf', methods=['POST'])
    def process_pdf_endpoint():
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'File must be a PDF'}), 400
        
        try:
            # Save the uploaded file
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            
            # Process the PDF
            docs = process_pdf(file_path)
            chunks = split_documents(docs)
            create_faiss_store(chunks)
            
            # Clean up the uploaded file
            os.remove(file_path)
            
            return jsonify({'message': 'PDF processed successfully'}), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/process-preuploaded-pdf', methods=['POST'])
    def process_preuploaded_pdf():
        try:
            # Process the pre-uploaded PDF
            file_path = "AI_Engineering.pdf"
            if not os.path.exists(file_path):
                return jsonify({'error': 'PDF file not found'}), 404
            
            # Process the PDF
            docs = process_pdf(file_path)
            chunks = split_documents(docs)
            create_faiss_store(chunks)
            
            return jsonify({'message': 'PDF processed successfully'}), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/ask', methods=['POST'])
    def ask_question():
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({'error': 'No question provided'}), 400
        
        try:
            qa = make_qa_chain()
            result = qa(data['question'])
            
            response = {
                'answer': result['result'],
                'sources': [
                    {
                        'source': doc.metadata.get('source', 'Unknown'),
                        'page': doc.metadata.get('page', 'Unknown')
                    }
                    for doc in result['source_documents']
                ]
            }
            
            return jsonify(response), 200
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500 