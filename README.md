# Thunderbird AI Assistant

This project creates an AI-powered assistant for Thunderbird that helps analyze emails and suggest responses using LangChain and OpenAI.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root with your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

3. Install the Thunderbird extension:
   - Open Thunderbird
   - Go to Tools > Add-ons
   - Click the gear icon and select "Install Add-on From File"
   - Navigate to the `thunderbird-extension` folder and select it
   - Restart Thunderbird

4. Start the Python backend:
```bash
python src/app.py
```

## Usage

1. Open an email in Thunderbird
2. Click the AI Assistant icon in the toolbar
3. Click "Analyze Email" to get:
   - Email summary
   - Suggested response points
   - Action items

## Features

- Email analysis using LangChain and OpenAI
- Automatic summary generation
- Response suggestions
- Action item extraction
- Easy-to-use interface integrated with Thunderbird

## Requirements

- Python 3.8+
- Thunderbird 78.0+
- OpenAI API key
- Internet connection for API access