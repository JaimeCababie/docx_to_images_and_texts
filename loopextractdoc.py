import os
from docx2python import docx2python
from unidecode import unidecode
import re

import re

def remove_extra_spaces(text):
    # Replace multiple newline characters and whitespace with a single newline
    text = re.sub(r'\n\s*\n', '\n', text)

    return text


def process_docx_files_in_directory(directory_path):
    # List all files in the directory
    all_files = os.listdir(directory_path)

    # Filter only .docx files
    docx_files = [file for file in all_files if file.endswith('.docx')]

    with open('output.txt', 'w', encoding='utf-8', errors='ignore') as text_output:
        # Process each .docx file
        for docx_file in docx_files:
            file_path = os.path.join(directory_path, docx_file)
            with docx2python(file_path) as output:
                output.save_images('images')
                text = output.text

            # Convert the file name to an ASCII string
            ascii_filename = unidecode(docx_file)

            # Write the file name to the output file
            text_output.write(f"File name: {ascii_filename}\n")

            cleaned_text = remove_extra_spaces(text)
            text_output.write(cleaned_text)

            # Add a page break after each document's text
            text_output.write("\f")


# Main function
def main():
    directory_path = "Iso_manuals"
    process_docx_files_in_directory(directory_path)

if __name__ == "__main__":
    main()