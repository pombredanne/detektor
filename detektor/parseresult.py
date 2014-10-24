class ParseResult(object):
    """
    Language parsers create objects of this class to store their results.
    """
    def __init__(self, set_of_all_operators, set_of_all_keywords, codeblocktype, label):
        """
        Parameters:
            set_of_all_keywords (set): A set of keywords supported by this language.
                used to create stable digest of keywords and the number of occurrences.
            codeblocktype: The type of code this result is for. Must be one of: "program", "function".
            label: A label that can be set to give the ParseResult a name/context.
                Used to name functions in the list of functions
                when the codeblocktype is ``function``.
        """
        self.set_of_all_operators = set_of_all_operators
        self.set_of_all_keywords = set_of_all_keywords
        self.codeblocktype = codeblocktype
        self.label = label

        #: List of keywords in the order they occur in the sourcecode
        self.keywords = []

        #: List of operators in the order they occur in the sourcecode
        self.operators = []

        #: Should be a string that when compared with another ParseResult
        #: means that the ParseResults are very similar if they match.
        self.normalized_sourcecode = u''

        #: List of ParseResult objects - one for each parsed function.
        #: This is only used when ``codeblocktype`` is ``program``.
        self.parsed_functions = []

    def __unicode__(self):
        return u'ParserResult(={keywords!r}, operators={operators!r})'.format(
            keywords=self.keywords,
            operators=self.operators)

    def __str__(self):
        return unicode(self).encode('ascii', 'replace')

    def __repr__(self):
        return str(self)

    def is_program(self):
        return self.codeblocktype == 'program'

    def add_keyword(self, keyword):
        self.keywords.append(keyword)

    def add_operator(self, operator):
        self.operators.append(operator)

    ## TODO: Port this from the old codeparser
    # def get_code_signature(self):
    #     kwh, oph, bigstring, bigstringhash, num_kw, num_op = self.parse_file()
    #     list_of_functions = defgetter('python', bigstring)
    #     return {
    #         'keywordstring': kwh,
    #         'operatorstring': oph,
    #         'bigstring': bigstring,
    #         'bigstringhash': bigstringhash,
    #         'number_of_keywords': num_kw,
    #         'number_of_operators': num_op,
    #         'list_of_functions': list_of_functions,
    #     }


class DumbParseResult(ParseResult):
    """
    If you do not have a smart way of creating the ``normalized_sourcecode``
    attribute of :class:`.ParseResult`, you can use this class to just
    create it automatically from the operators and keywords.
    """

    def add_keyword(self, keyword):
        super(DumbParseResult, self).add_keyword(keyword)
        self.normalized_sourcecode += keyword

    def add_operator(self, operator):
        super(DumbParseResult, self).add_operator(operator)
        self.normalized_sourcecode += operator
