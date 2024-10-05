import pdfplumber
from markdownify import markdownify as md
import sys, re

def pdf_2_markdown(in_filepath, out_dir_path):

    #Creating a regex to grab the filename
    name_re = r'[^\\/]+(?=\.pdf)'
    
    #Windows is bs and uses single \ when copying file paths, hense input needs to be in r'' for it to work
    in_filepath = in_filepath.replace("\\", '/')
    out_dir_path = out_dir_path.replace("\\", '/')
    
    print(out_dir_path)

    #Find the file name with the expression
    file_name = re.search(name_re, in_filepath).group()


    # Open the PDF file
    with pdfplumber.open(in_filepath) as pdf:
        markdown_text = ""
        for page in pdf.pages:
            text = page.extract_text(layout=True)
            if text:
                markdown_text += md(text) + "\n\n"

    # Save the markdown text to a .md file
    with open(out_dir_path + '/' + file_name + '.md', "w") as md_file:
        md_file.write(markdown_text)
    
#pdf_2_markdown(r"C:\Users\Einar\Downloads\2024H_MA3.pdf", 'pdf_2_markdown/')

if __name__  == '__main__':
    in_path = fr'{sys.argv[1]}'
    out_dir = fr'{sys.argv[2]}'

    print(in_path, out_dir)

    pdf_2_markdown(in_path, out_dir)
