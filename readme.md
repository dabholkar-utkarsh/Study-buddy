# 📚 Study Buddy – Your AI-Powered Study Companion

**Study Buddy** is a smart web portal designed to help users learn and explore content from books, YouTube videos, or any other uploaded material using ChatGPT. Users can ask questions via voice or text and get answers the same way. The app also offers a searchable library of all uploaded resources, making studying interactive, personalized, and fun.

---

## ✨ Features

- **🔐 Authentication**  
  Secure login/signup system for users to manage their content and sessions.

- **🎯 Landing Page**  
  Beautiful and intuitive landing page introducing the Study Buddy features.

- **📤 Upload Content**  
  Upload:
  - PDF books  
  - YouTube video links  
  - Other textual resources  
  These are automatically parsed and stored.

- **📖 Content Parsing and Storage**  
  - Uploaded books are chunked intelligently (based on semantic breaks).
  - Chunks are embedded using vector embeddings.
  - Stored in a **Vector Database** for semantic search and retrieval.

- **💬 ChatGPT Interface**  
  - Text and voice input supported.
  - Ask questions related to the uploaded content.
  - See the referenced section from the book/video when a question is answered.

- **🗣 Voice and Text Output**  
  Get answers in both text and **AI-generated voice**.

- **📚 Personal Library**  
  Users can access all uploaded and parsed content in a searchable, filterable format.

---

## 🛠️ Tech Stack

- **Frontend:** React / Angular / Next.js (customizable)
- **Backend:** FastAPI / Node.js
- **Vector DB:** Pinecone / Chroma / FAISS
- **LLM:** OpenAI GPT-4 / GPT-3.5
- **Speech:** Web Speech API / ElevenLabs / Whisper (for speech-to-text and vice-versa)
- **Authentication:** Firebase Auth / OAuth

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/study-buddy.git
cd study-buddy

# Setup frontend
cd frontend
npm install
npm start

# Setup backend
cd ../backend
pip install -r requirements.txt
uvicorn main:app --reload
