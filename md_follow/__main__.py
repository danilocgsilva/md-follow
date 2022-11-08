import markdown
import os

def generateHtml(markdownCandidate):
    
    print("The file " + markdownCandidate + " will be converted to a html file.")
    
    with open(markdownCandidate, 'r') as file:
        text = file.read()
        html = markdown.markdown(text)
        
    newFileName = markdownCandidate + ".html"
    with open(newFileName, 'w') as wfile:
        wfile.write(html)
        
    print('New file generated: ' + newFileName)

def main():
    
    markdownCandidate = 'README.md'
    if not os.path.isfile(markdownCandidate):
        print('The file ' + markdownCandidate + ' was not found in current directory.')
    else:
        generateHtml(markdownCandidate)
    