if __name__ == '__main__':
    import os
    import pprint
    import detektor

    #
    #
    # Parse 2 fairly similar programs, and one only slightly similar one
    #
    #
    parser = detektor.parser.make_parser('python')

    parseresult1 = parser.parse("""
    import os

    def add(a, b):
        return a + b

    print 'Hello %s!' % 'world'
    a = 1
    print '%s + %s equals %s' % (a, a, add(a, a))
    """, label='program1.py')

    parseresult2 = parser.parse("""
    import os

    def sum(x, y):
        return x + y

    print 'Hello %s!' % 'world'
    mynumber = 1
    print '{} + {} = {}'.format(mynumber, mynumber, sum(mynumber, mynumber))
    """, label='program2.py')

    parseresult3 = parser.parse("""
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
    """, label='program3.py')


    print 'Comparison result ordered with best matches first'
    comparemany = detektor.parseresultcomparer.ParseResultCompareMany([
        parseresult1, parseresult2, parseresult3])
    comparemany.sort_by_points_descending()
    for comparetwo in comparemany:
        print comparetwo
