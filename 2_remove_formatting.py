import os
import markdown2
import html2text

def convert_markdown_to_text(markdown_content):
    """Convert Markdown content to plain text using markdown2 and html2text."""
    html_content = markdown2.markdown(markdown_content)
    
    html_to_text = html2text.HTML2Text()
    html_to_text.ignore_links = True
    plain_text = html_to_text.handle(html_content)
    
    return plain_text

def remove_phrases(text, phrases_to_remove):
    """Remove specified phrases from the text."""
    for phrase in phrases_to_remove:
        text = text.replace(phrase, '')
    return text

def process_files(input_directory, output_directory, phrases_to_remove):
    """Process all text files in the input directory and save cleaned plain text files in the output directory."""
    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Process each text file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_file_path = os.path.join(input_directory, filename)
            output_file_path = os.path.join(output_directory, filename)
            
            # Read the text file
            with open(input_file_path, 'r', encoding='utf-8') as txt_file:
                markdown_content = txt_file.read()

            # Convert Markdown content to plain text
            plain_text = convert_markdown_to_text(markdown_content)

            # Remove specified phrases from the plain text
            cleaned_text = remove_phrases(plain_text, phrases_to_remove)

            # Save the cleaned plain text to the output file
            with open(output_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(cleaned_text)

            print(f'Processed {filename} and saved cleaned text')

def main():
    input_directory = 'cases_text'
    output_directory = 'cases_cleaned_text'
    
    phrases_to_remove = [
        "Judgment Download PDF PDF X Close Window Judgments Homepage",
        '''This judgment text has undergone conversion so that it is mobile and web-
friendly. This may have created formatting or alignment issues. Please refer
to the PDF copy for a print-friendly version.''',
        # Add more phrases as needed
    ]

    process_files(input_directory, output_directory, phrases_to_remove)

if __name__ == "__main__":
    main()
