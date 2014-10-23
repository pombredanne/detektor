import shlex

from detektor.languageparser.base import LanguageParserBase
from detektor.parseresult import ParseResult, DumbParseResult


class ShlexLanguageParserBase(LanguageParserBase):
    #: Set of operators supported by the language.
    #: # E.g.: ``operators = {'<', '==', '>', '&&'}``
    operators = None

    #: Set of keywords supported by the language.
    #: # E.g.: ``keywords = {'if', 'for', 'and', 'or'}``
    keywords = None

    def __init__(self, *args, **kwargs):
        super(ShlexLanguageParserBase, self).__init__(*args, **kwargs)
        parseresult_class = self.get_parseresultclass()
        self.parseresult = parseresult_class()

    def get_parseresultclass(self):
        return DumbParseResult

    def get_cleaned_sourcecode(self):
        """
        Get the sourcecode passed into the lexer.
        You should override this if you need to cleanup the
        sourcecode before sending it to the shlex lexer.
        """
        return self.sourcecode

    def get_shlexobject(self):
        """
        Get a ``shlex.shlex`` object. Can be overridden to
        customize the lexer.
        """
        lexer = shlex.shlex(self.get_cleaned_sourcecode())
        lexer.wordchars += ''.join(self.operators)
        return lexer

    def shlex_parse(self):
        lexer = self.get_shlexobject()
        while True:
            token = lexer.get_token()
            if not token:
                break
            self.shlex_parse_token(token)

    def shlex_parse_token(self, token):
        if token in self.keywords:
            self.parseresult.add_keyword(token)
        elif token in self.operators:
            self.parseresult.add_operator(token)

    def parse(self):
        self.shlex_parse()
        return self.parseresult
