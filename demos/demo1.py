if __name__ == '__main__':
    import detektor

    #
    #
    # Parse 2 fairly similar programs, and 2 only slightly similar ones
    #
    #
    parser = detektor.parser.make_parser('python')

    parseresult1 = parser.make_parseresult(label='program1.py')
    parser.parse(parseresult1, """
    import os

    def add(a, b):
        return a + b

    print 'Hello %s!' % 'world'
    a = 1
    print '%s + %s equals %s' % (a, a, add(a, a))
    """)

    parseresult2 = parser.make_parseresult(label='program2.py')
    parser.parse(parseresult2, """
    import os

    def sum(x, y):
        return x + y

    print 'Hello %s!' % 'world'
    mynumber = 1
    print '{} + {} = {}'.format(mynumber, mynumber, sum(mynumber, mynumber))
    """)

    parseresult3 = parser.make_parseresult(label='program3.py')
    parser.parse(parseresult3, """
    import os

    def add(a, b):
        return a + b

    print 'Hello %s!' % 'world'
    firstnumber = 10
    secondnumber = 20
    print '{firstnumber} + {secondnumber} equals {result}'.format(
        firstnumber=firstnumber,
        secondnumber=secondnumber,
        result=add(firstnumber, secondnumber))
    """)

    print 'Comparison result ordered with best matches first'
    comparemany = detektor.parseresultcomparer.ParseResultCompareMany([
        parseresult1, parseresult2, parseresult3])
    comparemany.sort_by_points_descending()
    for comparetwo in comparemany:
        print comparetwo
