import config


# A class that represents assignements
class Assignment:
    """ This is the class that represents each assignent delivered.
    The objects is stored in a list for each assignment of this
    file. E.g all handed in 'find.py' files in a list. The lists for
    each assignment given is stored in the 'stud_prog' dict with the
    filename used as key. Values stored for each assignment:
    
    - hash for string of number of each keyword used
    - hash for string of number of each operator used
    - hash for string of keywords and operators
    - number of keywords used
    - number of operators used
    - a list of strings build of keywords and operators from the
      big-string. This enables comparing of singular functions in two
      assignments
    """
    
    def __init__(self, *args, **kwargs):
        self.keywordstring = kwargs.get('keywordstring')
        self.operatorstring = kwargs.get('operatorstring')
        self.bigstring = kwargs.get('bigstring')
        self.bigstringhash = kwargs.get('bigstringhash')
        self.number_of_keywords = kwargs.get('number_of_keywords')
        self.number_of_operators = kwargs.get('number_of_operators')
        self.list_of_functions = kwargs.get('list_of_functions')

    def __repr__(self):
        return u"""
Keywords: {}
Operators: {}
Bigstring: {}
Bigstringhash: {}
Number of keywords: {}
Number of operators: {}
Functions: {}
        """.format(self.keywordstring, self.operatorstring, self.bigstring,
            self.bigstringhash, self.number_of_keywords,
            self.number_of_operators, self.list_of_functions)

