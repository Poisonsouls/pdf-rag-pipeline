# PDF RAG Pipeline

A Retrieval Augmented Generation (RAG) data pipeline built with Python. This project extracts text from a PDF, cleans and chunks the content, generates embeddings using Sentence Transformers, stores them in ChromaDB, and performs semantic search over the document.

## Features

- Extract text from PDF files using PyMuPDF
- Clean and preprocess raw text
- Split text into manageable chunks
- Generate embeddings with Sentence Transformers
- Store embeddings in a local ChromaDB vector database
- Perform semantic search using natural language queries

## Project Structure

```text
pdf-rag-pipeline/
│
├── data/
│   └── fannie_mae.pdf
│
├── chroma_db/
│
├── src/
│   ├── extract.py
│   ├── clean.py
│   ├── chunk.py
│   ├── embed.py
│   ├── store.py
│   ├── search.py
│   ├── index.py
│   └── query.py
│
├── pyproject.toml
└── README.md
```

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
PDF
 │
 ▼
Extract Text
 │
 ▼
Clean Text
 │
 ▼
Chunk Text
 │
 ▼
Generate Embeddings
 │
 ▼
Store in ChromaDB
 │
 ▼
Semantic Search
```



## Learning Objectives

This project demonstrates how to:

- Process unstructured PDF documents
- Build a vector database
- Generate semantic embeddings
- Perform semantic search
- Understand the indexing stage of a Retrieval-Augmented Generation (RAG) system

## License

This project is for educational purposes.
