

class BaseFunctionExtractor(object):
    """
    Abstract base class for function extractors.

    A function extractor takes a sourcecode blob and
    extracts a list of functions and methods from it.
    """
    def extract(self, sourcecode):
        """
        Extract the functions in ``sourcecode`` and return the result as a
        list of ``(functionname, sourcecode)`` where:

            - ``functionname`` should be an as good as possible label for the
              function. This means that a method optimally should include the
              full path including any namespace, class name and arguments if possible.
            - ``sourcecode`` should be the sourcecode comprising the body of the function.

        Must be overridden in subclasses.
        """
        raise NotImplementedError()
