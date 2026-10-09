# Multi-Agent AI Research System

A small AI research assistant that helps turn a topic into a structured
report. It uses an LLM to support the research workflow, searches the
web for relevant information, and then drafts and reviews the result
before showing it in a Streamlit app.

I built this project to explore how AI agents and tools can work
together on a research task, rather than relying on one prompt to do
everything.

## What it does

-   **Web search:** looks for relevant information using Tavily.
-   **Page scraping:** fetches page content so the system can use
    information beyond search-result snippets.
-   **Report writing:** turns the collected material into a readable
    report.
-   **Review step:** runs a critic pass to identify issues in the draft.
-   **Streamlit interface:** provides a simple UI for entering a
    research topic and viewing the output.

The quality of the final report depends on the sources found and how
well the model uses them. Generated content should be checked against
the original sources before being used as factual research.

## Tech stack

-   Python
-   LangChain agents and chains
-   Groq for model inference
-   Tavily for web search
-   Streamlit for the UI
-   `uv` for Python dependency and environment management

## How the workflow works

1.  Enter a research topic in the Streamlit app.
2.  The research workflow uses web-search and page-scraping tools to
    gather information.
3.  The writer creates a draft from the available material.
4.  A critic step reviews the draft.
5.  The app displays the generated report and review output.

This is a learning project, so the workflow and its checks can be
improved further. The critic step should not be treated as a guarantee
that every claim is correct.

## Getting started

### 1. Clone the repository

``` bash
git clone https://github.com/Prakharyadav64/Multi-Agent-AI-Research-System.git
cd Multi-Agent-AI-Research-System
```

### 2. Install `uv`

If you don't already have `uv`, install it by following the instructions
at <https://docs.astral.sh/uv/>.

### 3. Install dependencies

``` bash
uv sync
```

If you prefer to use pip, the repository also includes a
`requirements.txt` file:

``` bash
pip install -r requirements.txt
```

### 4. Add API keys

Create a `.env` file in the project root and add the API keys used by
the application:

``` env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get the keys from the relevant providers: - Groq:
<https://console.groq.com/> - Tavily: <https://tavily.com/>

Keep your `.env` file private. Do not commit API keys to GitHub.

### 5. Run the app

From the project root, run:

``` bash
uv run streamlit run app.py
```

Streamlit will print a local URL in the terminal. Open that URL in your
browser.

## Project structure

``` text
Multi-Agent-AI-Research-System/
├── app.py                         # Streamlit user interface
├── agents.py                      # Agent and writing/review logic
├── tools.py                       # Web search and page-scraping tools
├── pipeline.py                    # Research workflow
├── requirements.txt               # pip dependencies
├── pyproject.toml                 # Project and dependency configuration
├── uv.lock                        # Locked dependency versions
├── .python-version                # Python version selection
└── src/
    └── multi_agent_reseach_system/
        └── __init__.py
```

## Current limitations

-   Search results and scraped pages can be incomplete, outdated, or
    unavailable.
-   The model may misunderstand sources or generate unsupported claims.
-   A critic pass can catch some problems, but it cannot guarantee
    factual accuracy.
-   API access and model availability depend on the providers and their
    current limits.

For important work, open the original links and verify the claims
yourself.

## Possible improvements

-   Include source links alongside the claims they support.
-   Add clearer error handling for failed searches and unavailable
    pages.
-   Evaluate report quality with a repeatable set of research questions.
-   Add tests for the tools and pipeline.
-   Improve the review step so it checks claims against the retrieved
    sources.

## Author

**Prakhar Yadav**

GitHub: <https://github.com/Prakharyadav64>

------------------------------------------------------------------------

Built as a hands-on project to learn about tool-using AI agents and
research workflows.
