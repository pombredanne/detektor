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
        self.codeblocktype = codeblocktype
        self.label = label

        #: Dict mapping keywords to the number of occurrences of that keyword
        self.keywords = dict.fromkeys(set_of_all_keywords, 0)

        #: Dict mapping operators to the number of occurrences of that operator
        self.operators = dict.fromkeys(set_of_all_operators, 0)

        #: Number of operators
        self.number_of_operators = 0

        #: Number of keywords
        self.number_of_keywords = 0

        #: A string with all the operators and keywords appended in the order
        #: they occur in the code. Handled automatically in :meth:`.add_keyword`
        #: and :meth:`.add_operator`, so you should not have to edit this.
        self.operators_and_keywords_string = u''

        #: Should be a string that when compared with another ParseResult
        #: means that the ParseResults are very similar if they match.
        #: This is typically populated by a smart language parser that
        #: normalizes sourcecode in a way that makes it very unlikely that
        #: programs differ if this string is 100% equal in two programs.
        #: If the language does not use this, it should be left as ``None``,
        #: to indicate that this should be ignored when comparing programs.
        self.normalized_sourcecode = None

        #: List of ParseResult objects - one for each parsed function.
        #: This is only used when ``codeblocktype`` is ``program``.
        self.parsed_functions = []

    def __unicode__(self):
        return \
            u'ParserResult('\
            u'keywords={keywords!r}, '\
            u'operators={operators!r})'.format(
                keywords=self.keywords,
                operators=self.operators)

    def __str__(self):
        return unicode(self).encode('ascii', 'replace')

    def __repr__(self):
        return str(self)

    def is_program(self):
        return self.codeblocktype == 'program'

    def add_keyword(self, keyword):
        self.number_of_keywords += 1
        self.keywords[keyword] += 1
        self.operators_and_keywords_string += keyword

    def add_operator(self, operator):
        self.number_of_operators += 1
        self.operators[operator] += 1
        self.operators_and_keywords_string += operator

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
