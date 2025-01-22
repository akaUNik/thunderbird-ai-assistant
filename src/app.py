import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LangChain
llm = OpenAI(temperature=0.7)
email_prompt = PromptTemplate(
    input_variables=["email_content"],
    template="""
    Analyze the following email content and provide a helpful response:
    
    Email Content:
    {email_content}
    
    Please provide:
    1. A summary of the email
    2. Suggested response points
    3. Any action items identified
    """
)

email_chain = LLMChain(llm=llm, prompt=email_prompt)

class EmailContent(BaseModel):
    subject: str
    body: str
    sender: str
    recipients: List[str]

class EmailResponse(BaseModel):
    analysis: str
    suggested_response: str
    action_items: List[str]

@app.post("/analyze-email", response_model=EmailResponse)
async def analyze_email(email: EmailContent):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    try:
        # Combine email content for analysis
        full_content = f"Subject: {email.subject}\nFrom: {email.sender}\nTo: {', '.join(email.recipients)}\n\n{email.body}"
        
        # Process with LangChain
        result = email_chain.run(email_content=full_content)
        
        # Parse the result (this is a simplified version)
        return EmailResponse(
            analysis=result.split("Suggested response points:")[0],
            suggested_response=result.split("Suggested response points:")[1].split("Action items:")[0],
            action_items=result.split("Action items:")[1].strip().split("\n")
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=54755)