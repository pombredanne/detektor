from detektor.codefilter.normalizeoperatorwhitespace import NormalizeOperatorWhitespace
from detektor.languageparser.shlexparser import ShlexLanguageParserBase


class JavaLanguageParser(ShlexLanguageParserBase):
    # http://docs.oracle.com/javase/tutorial/java/nutsandbolts/opsummary.html
    operators = {
        '!', '+', '-', '*', '**', '/', '//', '%', '<<', '>>', '>>>', '&', '|',
        '++', '--', '&&', '||', '?:',
        '^', '~', '<', '>', '<=', '>=', '==', '!=',
    }

    # http://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html
    keywords = {
        'abstract', 'continue', 'for', 'new', 'switch',
        'assert***', 'default', 'package', 'synchronized',
        'boolean', 'do', 'if', 'private', 'this',
        'break', 'double', 'implements', 'protected', 'throw',
        'byte', 'else', 'import', 'public', 'throws',
        'case', 'enum', 'instanceof', 'return', 'transient',
        'catch', 'extends', 'int', 'short', 'try',
        'char', 'final', 'interface', 'static', 'void',
        'class', 'finally', 'long', 'strictfp', 'volatile',
        'float', 'native', 'super', 'while',
    }

    sourcecode_preprocessor_classes = [
        NormalizeOperatorWhitespace
    ]
