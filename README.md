# AI Blog Generator

## Overview
The AI Blog Generator is a Streamlit-based web application that creates structured blog posts using Google's Gemini AI model. It enhances blog quality by conducting automated research through Wikipedia and DuckDuckGo search.

## Features
- Generate well-structured blog posts on any topic.
- Specify a **main focus** for the blog.
- Automated research using Wikipedia and DuckDuckGo.
- Uses **Google Gemini AI** for content generation.
- Simple **Streamlit UI** for easy usage.

## Installation
### Prerequisites
- Python 3.8+
- Google API Key

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-blog-generator.git
   cd ai-blog-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add API keys (in app.py):
   ```ini
   GOOGLE_API_KEY=your_api_key_here
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage
1. Enter a **blog topic** in the text input.
2. Provide a **main focus** (e.g., "AI in Healthcare").
3. Click **"Generate Blog"** and wait for the AI to generate content.

## Project Structure
```
├── app.py              # Main Streamlit application
├── requirements.txt    # Required dependencies
├── README.md           # Documentation
```

## License
This project is licensed under the MIT License.

