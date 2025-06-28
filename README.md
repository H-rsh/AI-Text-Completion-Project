# AI-Powered Text Completion App Project Overview

This is a command-line Python application that uses Cohere's Generative AI API to generate text completions based on user prompts. It simulates how real-world AI-driven assistants work, showcasing prompt handling, parameter tuning, and exception handling in a terminal-based environment.

This AI-Powered Text Completion App allows users to:

- Enter a prompt and receive an AI-generated response in real-time.
- Experiment with creative, instructional, and informational queries.
- Run multiple prompt requests in a single session.
- Safely store and load API keys using environment variables.
- Handle errors gracefully (invalid API keys, empty input, API exceptions).
- Modify generation behavior with temperature and token length parameters.

---

## How to Run the Script

1. **Clone the repository** or copy the script locally:
      ```bash
   git clone https://github.com/H-rsh/AI-Text-Completion-Project.git
   cd Text_Completion_App
3. Ensure Python and pip are installed on your system.
4. Create and store your Cohere API key in a .env file: 
    api_key=your_actual_cohere_api_key_here
5. Install the required libraries:
    pip install cohere
    pip install cohere python-dotenv
6. Run the script:
    python Text_Completion_App.py
7. Follow the prompts in the terminal to generate AI responses.

---

### Python Concepts Used
This project demonstrates core Python programming principles:

- Environment configuration using dotenv
- API usage and exception handling
- Loops, conditional logic, and modular functions
- String formatting and user input handling
- External library integration with cohere and os

---

### Dependencies
- Python 3.7+
- Cohere Python SDK
- python-dotenv
