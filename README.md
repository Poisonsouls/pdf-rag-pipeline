# PDF RAG Pipeline

A Retrieval Augmented Generation (RAG) data pipeline built with Python. This project extracts text from a PDF, cleans and chunks the content, generates embeddings using Sentence Transformers, stores them in ChromaDB, and performs semantic search over the document.

## Features

- Extract text from PDF files using PyMuPDF
- Clean and preprocess raw text
- Split text into manageable chunks
- Generate embeddings with Sentence Transformers
- Store embeddings in a local ChromaDB vector database
- Perform semantic search using natural language queries


## Technologies Used

- Python 3.12
- PyMuPDF
- Sentence Transformers
- ChromaDB
- UV

## Installation

Clone the repository:

```bash
git clone https://github.com/Poisonsouls/pdf-rag-pipeline.git
cd pdf-rag-pipeline
```

Install dependencies:

```bash
uv sync
```

Or install packages manually:

```bash
uv add pymupdf
uv add sentence-transformers
uv add chromadb
```

## Usage

### 1. Build the Vector Database

Run the indexing pipeline to:

- Extract text from the PDF
- Clean the text
- Split it into chunks
- Generate embeddings
- Store everything in ChromaDB

```bash
uv run python src/index.py
```

### 2. Ask Questions

Run the query script:

```bash
uv run python src/query.py
```

Example:

```text
Ask a question:
What is the maximum LTV ratio?
```

Example output:

```text
Result 1:
The maximum LTV ratios permitted are...
```

## Pipeline

```text
1-PDF
2-Extract Text
3-Clean Text
4-Chunk Text
5-Generate Embeddings
6-Store in ChromaDB
7-Semantic Search
```



