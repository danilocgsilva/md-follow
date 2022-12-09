import os
import argparse
from md_follow.GenerateHtmlPage import GenerateHtmlPage

def generateHtml(markdownCandidate, documentation_folder):
    
    print("The file " + markdownCandidate + " will be converted to a html file.")

    generateHtmlPage = GenerateHtmlPage()
    
    with open(markdownCandidate, 'r') as file:
        text = file.read()
        html = generateHtmlPage.generate(text)
    
    file_name_base = markdownCandidate + ".html"
    if documentation_folder:
        os.makedirs('documentation')
        newFileName = 'documentation/' + file_name_base
    else:
        newFileName = file_name_base
        
    with open(newFileName, 'w') as wfile:
        wfile.write(html)
        
    print('New file generated: ' + newFileName)
    
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--documentation-folder',
        '-d',
        required=False,
        action='store_true'
    )
    return parser.parse_args()
    
def main():
    
    arguments = get_arguments()
    
    markdownCandidate = 'README.md'
    if not os.path.isfile(markdownCandidate):
        print('The file ' + markdownCandidate + ' was not found in current directory.')
    else:
        generateHtml(markdownCandidate, arguments.documentation_folder)
    