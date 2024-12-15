#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import json
import re
from typing import List, Dict
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import spacy
import logging

# Load spaCy NLP model (use en_core_web_sm or other available free models)
nlp = spacy.load("en_core_web_sm")

# Define structured fields for extraction
FIELDS = [
    "Bid Number", "Title", "Due Date", "Bid Submission Type", "Term of Bid",
    "Pre Bid Meeting", "Installation", "Bid Bond Requirement", "Delivery Date",
    "Payment Terms", "Any Additional Documentation Required", "MFG for Registration",
    "Contract or Cooperative to use", "Model_no", "Part_no", "Product", "contact_info",
    "company_name", "Bid Summary", "Product Specification", "Value"
]

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a PDF file using PyPDF2."""
    try:
        reader = PdfReader(file_path)
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text
    except Exception as e:
        logging.error(f"Failed to extract text from PDF {file_path}: {e}")
        raise

def extract_text_from_html(file_path: str) -> str:
    """Extracts text from an HTML file using BeautifulSoup."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            text = soup.get_text(separator="\n")
        return text
    except Exception as e:
        logging.error(f"Failed to extract text from HTML {file_path}: {e}")
        raise

def extract_fields_with_spacy(text: str) -> Dict[str, str]:
    """Extracts structured fields from text using spaCy and regex patterns."""
    doc = nlp(text)
    structured_data = {field: "" for field in FIELDS}

    # Example regex patterns for key fields (adjust as needed)
    patterns = {
        "Bid Number": r"(?i)bid number[:\s]*([\w-]+)",
        "Due Date": r"(?i)due date[:\s]*([\w\s,]+)",
        "Title": r"(?i)title[:\s]*([\w\s]+)",
        "Payment Terms": r"(?i)payment terms[:\s]*([\w\s]+)",
        "contact_info": r"(?i)(?:contact[:\s]*|email[:\s]*)([\w\.-]+@[\w\.-]+)"
    }

    # Apply regex patterns
    for field, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            structured_data[field] = match.group(1).strip()

    # Use spaCy to extract company names or entities
    for ent in doc.ents:
        if ent.label_ == "ORG" and not structured_data["company_name"]:
            structured_data["company_name"] = ent.text

    return structured_data

def process_document(file_path: str) -> Dict[str, str]:
    """Processes a document (PDF or HTML) and extracts structured data."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext == ".html":
        text = extract_text_from_html(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    structured_data = extract_fields_with_spacy(text)
    return structured_data

def main(input_folder: str, output_file: str):
    """Main function to process all documents in a folder and output JSON."""
    results = []

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith((".pdf", ".html")):
            logging.info(f"Processing: {file_name}")
            try:
                structured_data = process_document(file_path)
                structured_data["source_file"] = file_name
                results.append(structured_data)
            except Exception as e:
                logging.error(f"Error processing {file_name}: {e}")

    # Write results to output JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)

    logging.info(f"Processing complete. Results saved to {output_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract structured data from RFP documents.")
    parser.add_argument("--input_folder", type=str, required=True, help="Path to the folder containing input documents (PDF/HTML).")
    parser.add_argument("--output_file", type=str, required=True, help="Path to the output JSON file.")

    args = parser.parse_args()

    main(args.input_folder, args.output_file)


# In[6]:


import os
import json
import re
from typing import List, Dict
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import spacy
import logging

# Load spaCy NLP model (use en_core_web_sm or other available free models)
nlp = spacy.load("en_core_web_sm")

# Define structured fields for extraction
FIELDS = [
    "Bid Number", "Title", "Due Date", "Bid Submission Type", "Term of Bid",
    "Pre Bid Meeting", "Installation", "Bid Bond Requirement", "Delivery Date",
    "Payment Terms", "Any Additional Documentation Required", "MFG for Registration",
    "Contract or Cooperative to use", "Model_no", "Part_no", "Product", "contact_info",
    "company_name", "Bid Summary", "Product Specification", "Value"
]

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a PDF file using PyPDF2."""
    try:
        reader = PdfReader(file_path)
        text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text
    except Exception as e:
        logging.error(f"Failed to extract text from PDF {file_path}: {e}")
        raise

def extract_text_from_html(file_path: str) -> str:
    """Extracts text from an HTML file using BeautifulSoup."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
            text = soup.get_text(separator="\n")
        return text
    except Exception as e:
        logging.error(f"Failed to extract text from HTML {file_path}: {e}")
        raise

def extract_fields_with_spacy(text: str) -> Dict[str, str]:
    """Extracts structured fields from text using spaCy and regex patterns."""
    doc = nlp(text)
    structured_data = {field: "" for field in FIELDS}

    # Example regex patterns for key fields (adjust as needed)
    patterns = {
        "Bid Number": r"(?i)bid number[:\s]*([\w-]+)",
        "Due Date": r"(?i)due date[:\s]*([\w\s,]+)",
        "Title": r"(?i)title[:\s]*([\w\s]+)",
        "Payment Terms": r"(?i)payment terms[:\s]*([\w\s]+)",
        "contact_info": r"(?i)(?:contact[:\s]*|email[:\s]*)([\w\.-]+@[\w\.-]+)"
    }

    # Apply regex patterns
    for field, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            structured_data[field] = match.group(1).strip()

    # Use spaCy to extract company names or entities
    for ent in doc.ents:
        if ent.label_ == "ORG" and not structured_data["company_name"]:
            structured_data["company_name"] = ent.text

    return structured_data

def process_document(file_path: str) -> Dict[str, str]:
    """Processes a document (PDF or HTML) and extracts structured data."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    if ext == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif ext == ".html":
        text = extract_text_from_html(file_path)
    else:
        raise ValueError(f"Unsupported file format: {ext}")

    structured_data = extract_fields_with_spacy(text)
    return structured_data

def main(input_folder: str, output_file: str):
    """Main function to process all documents in a folder and output JSON."""
    results = []

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith((".pdf", ".html")):
            logging.info(f"Processing: {file_name}")
            try:
                structured_data = process_document(file_path)
                structured_data["source_file"] = file_name
                results.append(structured_data)
            except Exception as e:
                logging.error(f"Error processing {file_name}: {e}")

    # Write results to output JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4)

    logging.info(f"Processing complete. Results saved to {output_file}")

# Example usage for Jupyter/IDE
input_folder = "C:/Users/deept/OneDrive/Desktop/Campus hiring-2024-2025 assignment/Bid"  # Replace with your folder path
output_file = "output.json"  # Replace with desired output file name

main(input_folder, output_file)


# In[ ]:




