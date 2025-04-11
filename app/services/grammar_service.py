import language_tool_python
from bs4 import BeautifulSoup

class GrammarService:
    @staticmethod
    def parse_text(text):
        # Use the BeautiSoup library to parse html text first
        soup = BeautifulSoup(text, 'html.parser')
        # get space separated plain text
        plainText = soup.get_text(separator = ' ')
        tool = language_tool_python.LanguageTool('en-US')

        matches = tool.check(text)

        is_correct = len(matches) == 0

        
        suggestions = [(m.ruleId, m.message, m.replacements) for m in matches]
        return suggestions


# TODO
# 1. Add a function to get the grammar rules for a given text
# 2. Check whether some document is grammatically correct or not, and return the boolean result, not the corrected code
# 3. Return suggested grammar for a text
# 4. Check Grammar of plain text

     