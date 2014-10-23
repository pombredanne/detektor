import re
from detektor.languageparser.shlexparser import ShlexLanguageParserBase
import keyword


class PythonLanguageParser(ShlexLanguageParserBase):
    operators = {
        '+', '-', '*', '**', '/', '//', '%', '<<', '>>', '&', '|',
        '^', '~', '<', '>', '<=', '>=', '==', '!=', '<>',
    }
    keywords = set(keyword.kwlist)

    # Used by :meth:`._normalize_space_around_operators`. We need the list of operators,
    # but escaped for use in a regex
    normalize_whitespace_operators = [re.escape(operator) for operator in operators]
    normalize_whitespace_pattern = re.compile(
        r'(\w)\s*(' +
        '|'.join(normalize_whitespace_operators) +
        r')\s*(\w)')

    def _normalize_space_around_operators(self, sourcecode):
        """
        We need to add space around the operators to ensure that they are
        tokenized even when they are pressed against other tokens on both
        sizes (I.E.: We want ``a==10`` to be 3 tokens, not one).
        """
        return self.normalize_whitespace_pattern.sub(r'\1 \2 \3', sourcecode)

    def get_cleaned_sourcecode(self):
        return self._normalize_space_around_operators(self.sourcecode)
