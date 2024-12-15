# EMPLAY-ASSIGNMENT-2
This Python script processes bid documents in PDF and HTML formats to extract structured data using Natural Language Processing (NLP). The script extracts fields such as "Bid Number", "Title", "Due Date", "Payment Terms", and others, saving the results as JSON files.


# Overview
The script is designed to:

Extract text from bid documents in both PDF and HTML formats.
Use a question-answering NLP model to identify and structure important information.
Output structured data in JSON format for each processed document.
# Dependencies
Make sure the following Python packages are installed before running the script:

pdfplumber: For extracting text from PDF files.
beautifulsoup4: For extracting text from HTML files.
transformers: For using Hugging Face's question-answering models.
torch: Required as the backend for Hugging Face models.
json: To format and save the extracted data as JSON files.
# To install the necessary dependencies, run:

pip install pdfplumber beautifulsoup4 transformers torch
