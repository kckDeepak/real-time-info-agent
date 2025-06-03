# Real Time Info using AI Agent

An AI-powered agent built with LangChain and LangGraph, leveraging the Gemini 2.0 Flash model and Tavily search API for real-time information retrieval. Query weather updates (e.g., Hyderabad’s forecast), current events, or general facts (e.g., India’s Prime Minister) with a secure and extensible setup. Ideal for developers exploring AI-driven search applications.

## Features
- **Real-Time Search**: Fetches up-to-date information using the Tavily search API (e.g., weather in Hyderabad or current political leaders).
- **Gemini 2.0 Flash**: Utilizes Google’s Gemini 2.0 Flash model for fast and efficient natural language processing.
- **LangChain & LangGraph**: Employs LangChain for tool integration and LangGraph for robust agent workflows with memory persistence.
- **Secure API Key Management**: Uses environment variables via `.env` files to protect sensitive API keys.
- **Extensible Design**: Easily adaptable for additional queries, tools, or AI models.

## Prerequisites
- Python 3.13 or higher
- A valid [Tavily API key](https://tavily.com) (free tier offers 1000 searches/month)
- A valid [Google Gemini API key](https://aistudio.google.com/app/apikey)
- Git installed for cloning the repository

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kckDeepak/real-time-info-agent.git
   cd real-time-info-agent
   ```

2. **Install Dependencies**:
   Create a virtual environment (optional but recommended) and install required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configure API Keys**:
   Create a `.env` file in the project root with your API keys:
   ```env
   TAVILY_API_KEY=your-tavily-api-key
   GOOGLE_API_KEY=your-gemini-api-key
   ```
   Replace `your-tavily-api-key` and `your-gemini-api-key` with your actual keys.

4. **Run the Script**:
   Execute the main script to start the agent:
   ```bash
   python main.py
   ```

## Requirements
The `requirements.txt` file includes:
```
langchain-google-genai
langchain_community
langgraph
python-dotenv
```
Install them with:
```bash
pip install langchain-google-genai langchain_community langgraph python-dotenv
```

## Example Usage
The agent can handle queries like:
- **Weather Queries**: "What is the weather in Hyderabad"
  - Example Output: Retrieves real-time weather data for Hyderabad, Telangana, India (e.g., partly cloudy, 23°C–35°C with a chance of thunderstorms).
- **General Knowledge**: "Who is the current Prime Minister of India"
  - Example Output: Fetches the latest information, such as Narendra Modi (as of June 2024).
- **Greetings**: "Hi"
  - Example Output: Responds with a simple greeting to initiate the conversation.

Run the script (`main.py`) to test these queries. The agent uses Tavily for real-time search and Gemini 2.0 Flash for processing responses.

## Project Structure
```
real-time-info-agent/
├── main.py           # Main script with the AI agent logic
├── .env             # Environment variables (API keys, not tracked)
├── .gitignore       # Excludes .env, __pycache__, etc.
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## How It Works
- **LangChain**: Integrates the Gemini 2.0 Flash model and Tavily search tool for query processing.
- **LangGraph**: Manages the agent’s workflow with memory persistence using `MemorySaver` for conversation continuity.
- **Tavily Search**: Performs real-time web searches to fetch up-to-date information (e.g., weather or current events).
- **Gemini 2.0 Flash**: Processes queries and generates human-like responses based on search results.
- **Secure Configuration**: API keys are loaded from a `.env` file, excluded from version control via `.gitignore`.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, open an issue on GitHub or contact [kckDeepak](https://github.com/kckDeepak).