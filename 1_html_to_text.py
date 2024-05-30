import os
import html2text

def convert_html_to_text(html_content):
    """Convert HTML content to plain text using html2text."""
    h = html2text.HTML2Text()
    h.ignore_links = True
    return h.handle(html_content)

def process_files(input_directory, output_directory):
    """Process all HTML files in the input directory and save them as text files in the output directory."""
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each HTML file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.html'):
            input_file_path = os.path.join(input_directory, filename)
            output_filename = os.path.splitext(filename)[0] + '.txt'
            output_file_path = os.path.join(output_directory, output_filename)
            
            # Read the HTML file
            with open(input_file_path, 'r', encoding='utf-8') as html_file:
                html_content = html_file.read()

            # Convert HTML content to plain text
            plain_text = convert_html_to_text(html_content)

            # Save the plain text to the output file
            with open(output_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(plain_text)

            print(f'Converted {filename} to {output_filename}')

def main():
    # Directories for input HTML files and output text files
    input_directory = 'cases_html'
    output_directory = 'cases_text'

    # Process the files
    process_files(input_directory, output_directory)

if __name__ == "__main__":
    main()
