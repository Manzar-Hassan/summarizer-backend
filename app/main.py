from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import groq
import httpx
import re

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

http_client = httpx.Client(
    base_url="https://api.groq.com",
    follow_redirects=True,
)

groq_client = groq.Groq(
    api_key=os.getenv("GROQ_API_KEY"),
    http_client=http_client
)

def clean_webvtt(text):
    lines = text.split('\n')

    cleaned_text = []

    for line in lines:
        if '<v ' in line:
            speech = re.findall(r'<v.*?>(.*?)</v>', line)
            if speech:
                cleaned_text.append(speech[0])

    return ' '.join(cleaned_text)


@app.get("/")
async def root():
    return {"message": "Groq API Backend is running"}

@app.post("/analyze-meeting")
async def analyze_meeting(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith('.vtt'):
            raise HTTPException(status_code=400, detail="File must be a .vtt file")

        content = await file.read()
        meeting_transcription = clean_webvtt(content.decode('utf-8'))

        system_prompt = """You are a meeting analyzer. Extract and summarize the key points from the given meeting transcription.
            Focus on:
                1. Main decisions made
                2. Action items and their owners
                3. Important deadlines or dates
                4. Project updates
                5. Next steps

                Format the response in a clear, structured way."""

        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": meeting_transcription
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.4,  # Lower temperature for more focused summaries
            max_tokens=1024
        )

        return {
            "analysis": chat_completion
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
