import markdown

class GenerateHtmlPage:

    def generate(self, mardown_text):

        header_text = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>'''
        footer_text = '''</body>
</html>'''
        return header_text + markdown.markdown(mardown_text) + footer_text
