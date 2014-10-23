from detektor.languageparser.python import PythonLanguageParser



class Parser(object):
    default_languageparsers = {
        # 'java': JavaLanguageParser,
        'python': PythonLanguageParser,
    }

    def __init__(self, language, sourcecode):
        self.language = language
        self.sourcecode = sourcecode

    def parse(self):
        """
        Parse the sourcecode and return the results as a :class:`.ParserResult` object.
        """
        languageparser_class = self.get_languageparser()
        return languageparser_class(self.sourcecode).parse()

    def get_languageparser(self):
        """
        Create a subclass of this class, and override this method to
        add custom language parsers or to replace the default language parsers.

        Returns:
            A :class:`detektor.languageparser.base.LanguageParserBase` subclass.
        """
        return self.default_languageparsers[self.language]
