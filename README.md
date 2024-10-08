# AI Web Scraper

Welcome to the AI Web Scraper, a simple web-based application built using **Streamlit** that allows you to scrape web pages, clean the content, and extract specific information using AI-driven parsing. This project makes use of **Selenium** for web scraping, **BeautifulSoup** for HTML content extraction and cleaning, and **Ollama LLM** for parsing the cleaned content based on user input.

## Features

- Scrape content from a website URL
- Extract and clean body content
- Break down DOM content into manageable chunks
- Use AI to extract specific information based on user-defined prompts

## How It Works

1. **Input a URL**: The user provides a website URL to scrape.
2. **Scrape the Website**: Selenium is used to load and retrieve the page source.
3. **Extract Body Content**: BeautifulSoup is used to extract and clean the body content of the page.
4. **Parse Content**: The user can specify a description of what information they want to extract, and the system will use **Ollama LLM** to parse the content based on the user-provided prompt.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- Selenium WebDriver (Chrome)
- BeautifulSoup4
- Ollama LLM
- Langchain Core Prompts

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-web-scraper.git
