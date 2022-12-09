import unittest
from md_follow.GenerateHtmlPage import GenerateHtmlPage

class testGenerateHtmlPage(unittest.TestCase):
    
    def testEmpty(self):
        generateHtmlPage = GenerateHtmlPage()
        generatedText = generateHtmlPage.generate('')

        expectedResult = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body></body>
</html>'''

        self.assertEqual(expectedResult, generatedText)
