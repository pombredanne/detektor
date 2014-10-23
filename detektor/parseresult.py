class ParseResult(object):
    """
    Language parsers create objects of this class to store their results.
    """
    def __init__(self):
        self.keywords = []
        self.operators = []

        # Should be a string that when compared with another ParseResult
        # means that the ParseResults are very similar if they match.
        self.normalized_sourcecode = u''

    def __unicode__(self):
        return u'ParserResult(={keywords!r}, operators={operators!r})'.format(
            keywords=self.keywords,
            operators=self.operators)

    def __str__(self):
        return unicode(self).encode('ascii', 'replace')

    def __repr__(self):
        return str(self)

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
