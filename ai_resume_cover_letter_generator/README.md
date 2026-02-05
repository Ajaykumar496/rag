# AI Resume & Cover Letter Generator

Built by **Ajaykumar**

An AI-powered tool that generates professional, ATS-friendly resumes and personalized cover letters using OpenAI GPT-4o. Built with Streamlit for an easy-to-use web interface with PDF export support.

## Features

- **Resume Generation** — Creates well-structured, ATS-friendly resumes from your details
- **Cover Letter Generation** — Writes personalized cover letters tailored to specific job descriptions
- **Multiple Tones** — Choose between Professional, Friendly, Confident, or Formal tone
- **PDF Export** — Download your resume or cover letter as a clean PDF
- **Text Export** — Download as plain text for easy editing
- **Real-time Generation** — Powered by GPT-4o for high-quality output

## Tech Stack

| Technology | Purpose |
|---|---|
| [OpenAI GPT-4o](https://openai.com/) | AI text generation |
| [Streamlit](https://streamlit.io/) | Web interface |
| [fpdf2](https://github.com/py-pdf/fpdf2) | PDF generation |
| Python 3.9+ | Backend |

## Getting Started

### Prerequisites

- Python 3.9+
- OpenAI API key

### Installation

1. **Clone the repo**:

   ```bash
   git clone https://github.com/Ajaykumar496/rag.git
   cd rag/ai_resume_cover_letter_generator
   ```

2. **Install dependencies**:

   ```bash
   pip install -e .
   ```

   Or with uv:

   ```bash
   uv sync
   ```

3. **Run the app**:

   ```bash
   streamlit run main.py
   ```

4. **Enter your OpenAI API key** in the sidebar when the app opens.

## How to Use

### Generating a Resume

1. Enter your OpenAI API key in the sidebar
2. Select **Resume** mode
3. Fill in your details — name, contact info, skills, experience, education, projects
4. Pick a tone (Professional, Friendly, Confident, Formal)
5. Click **Generate**
6. Download as PDF or Text

### Generating a Cover Letter

1. Enter your OpenAI API key in the sidebar
2. Select **Cover Letter** mode
3. Fill in your details
4. Enter the **company name**, **job title**, and paste the **job description**
5. Click **Generate**
6. Download as PDF or Text

## Project Structure

```
ai_resume_cover_letter_generator/
├── main.py                    # Streamlit app (UI and orchestration)
├── resume_generator.py        # Resume generation with OpenAI
├── cover_letter_generator.py  # Cover letter generation with OpenAI
├── pdf_export.py              # Markdown-to-PDF conversion
├── pyproject.toml             # Project config and dependencies
├── .env.example               # Example environment variables
├── .gitignore
└── README.md
```

## Configuration

You can pass your API key through the sidebar UI. Alternatively, set it as an environment variable:

```bash
export OPENAI_API_KEY=your_key_here
```

The app uses `gpt-4o` by default. You can change the model in `resume_generator.py` and `cover_letter_generator.py`.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## License

MIT License
