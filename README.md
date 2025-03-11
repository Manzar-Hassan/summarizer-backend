# 🎯 Briefly Backend

A FastAPI-powered backend service that processes meeting transcripts using Groq's LLM API to generate intelligent summaries.

## 🌟 Features

- 🔄 WebVTT file processing
- 🤖 AI-powered meeting analysis
- 🔍 Intelligent text extraction
- 🚀 Fast response times
- 🔒 CORS support
- 🌐 RESTful API endpoints

## 🛠 Tech Stack

- **Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **AI Integration**: Groq API
- **HTTP Client**: HTTPX
- **Environment**: Python-dotenv

## 🚀 Getting Started

1. **Clone the repository**
```bash
git clone <repository-url>
cd briefly-backend
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
```

5. **Run the server**
```bash
uvicorn app.main:app --reload
```

Server will be running at [http://localhost:8000](http://localhost:8000)

## 📁 Project Structure

```
briefly-backend/
├── app/
│   └── main.py        # Main application file
├── requirements.txt   # Python dependencies
└── .env              # Environment variables
```

## 🔌 API Endpoints

### GET /
- Health check endpoint
- Returns: `{"message": "Groq API Backend is running"}`

### POST /analyze-meeting
- Accepts: `.vtt` file
- Returns: Meeting summary and analysis
- Content-Type: `multipart/form-data`

## 🔧 Configuration

The application uses the following environment variables:
- `GROQ_API_KEY`: Your Groq API authentication key

## 📦 Dependencies

Core dependencies include:
- fastapi: 0.109.0
- uvicorn: 0.27.0
- python-dotenv: 1.0.0
- groq: 0.4.2
- python-multipart: 0.0.6

## 🔒 Security

- CORS middleware configured
- Environment variables for sensitive data
- Input validation for file uploads

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.