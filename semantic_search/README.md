# Semantic Search using Endee Vector Database

## Overview
This project demonstrates a **Semantic Search system** built using **Endee**, a high-performance vector database.
Text documents are converted into vector embeddings and stored in Endee. User queries are embedded and matched
using vector similarity instead of exact keyword matching.

This project was developed as part of the **Endee Labs project-based evaluation**.

---

## Problem Statement
Traditional keyword-based search systems fail to capture semantic meaning and context.
As a result, they often return irrelevant results when queries are phrased differently
from the stored content.

This project addresses this limitation by using **vector embeddings and similarity search**
to retrieve contextually relevant results, even when exact keywords do not match.

---

## Use Case
**Semantic Search (Vector Similarity Search)**

---

## Tech Stack
- Endee (Vector Database)
- Python
- Sentence Transformers
- NumPy

---

## System Design / Technical Approach
1. Input text documents are converted into vector embeddings using a Sentence Transformer model.
2. These embeddings are stored in the Endee vector database.
3. User search queries are embedded using the same transformer model.
4. Endee performs vector similarity search to retrieve the most relevant documents.
5. Results are ranked based on vector distance scores.

---

## How Endee Is Used
Endee serves as the **core vector database** in this project.
It is responsible for storing high-dimensional embeddings and performing efficient
similarity search during query execution, making it suitable for AI/ML applications
where vector search is central.

---

## Project Structure
