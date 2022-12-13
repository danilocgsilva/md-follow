import markdown

class GenerateHtmlPage:

    def __init__(self) -> None:
        self.title = "Document"

    def setTitle(self, title: str):
        self.title = title

    def generate(self, mardown_text):

        header_text = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{0}</title>
</head>
<body>'''
        footer_text = '''</body>
</html>'''

        return header_text.format(self.title) + markdown.markdown(mardown_text) + footer_text
