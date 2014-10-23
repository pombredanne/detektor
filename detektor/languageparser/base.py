

class LanguageParserBase(object):
    """
    Base class for handling
    """
    def __init__(self, sourcecode):
        self.sourcecode = sourcecode

    def parse(self):
        """
        Parse the ``sourcecode``, and return the results. Must be
        overridden in subclasses.

        Returns:
            The parser results as a :class:`detector.parser_result.ParseResult`
            object.
        """
        raise NotImplementedError()
