Using a tool from ARTIFAX. Most used for mining text and tables from pdfs in context of training LLMS
https://artifex.com/news/introducing-pymupdf4llm-a-breakthrough-in-pdf-to-markdown-conversion-for-python-developers
Concluded that it was not needed for my use case, and it was slower than alternatives

More info on regular pymupdf: https://pymupdf.readthedocs.io/en/latest/
Also some info on pymusql: 

You only need to create an environment with pymupdf4llm
pip install pymupdf4llm

I have heard that pdfplumber can be better with images, so I want to use that also. Hence two programs. One for general purpose and other for llm purposes.
conda create --name pdf_md
pip install pdfplumber markdownify

Running program
The program can be runned in the terminal in format python pdf_2_markdown.py in_path out_dir

