class ParseResultCompareTwo(object):
    matchmap = {
        'operators_and_keywords_string_equal': {
            'points': 10,
            'label': 'Programs very similar. Look for use of query-replace.'
        },
        'operators_string_equal': {
            'points': 3,
            'label': 'Equal number of each operator used.'
        },
        'keywords_string_equal': {
            'points': 3,
            'label': 'Equal number of each keyword used.'
        },
        'total_operatorcount_equal': {
            'points': 1,
            'label': 'Equal number total operators.'
        },
        'total_keywordcount_equal': {
            'points': 1,
            'label': 'Equal number total keywords.'
        }
    }

    def __init__(self, parseresult1, parseresult2, scale=100):
        """
        Parameters:
            parseresult1: A obj:`detektor.parseresult.ParseResults` object.
            parseresult2: A obj:`detektor.parseresult.ParseResults` object.
            scale (int): A number to multiply all the points produced on
                matches by. Used internally to scale functions less than
                whole programs.
        """
        self.parseresult1 = parseresult1
        self.parseresult2 = parseresult2
        self.scale = scale

        # Points are collected by the _compare() function.
        # When the comparison has completed, the number of points indicates
        # how similar the two programs are
        self.points = 0

        #: List of matchids. We use get_description_for_matchid() to get a human
        #: readable string for a matchid.
        self.summary = []

    def __unicode__(self):
        return u'Points: {points}, summary: {summary}'.format(
            points=self.get_scaled_points(),
            summary=self.get_summary_descriptions_as_string())

    def __str__(self):
        return unicode(self).encode('ascii', 'replace')

    def __repr__(self):
        return str(self)

    def get_scaled_points(self):
        return self.points * self.scale

    def get_summary_descriptions_as_list(self):
        return [self.get_description_for_matchid(matchid) for matchid in self.summary]

    def get_summary_descriptions_as_string(self):
        return u' '.join(self.get_summary_descriptions_as_list())

    def get_description_for_matchid(self, matchid):
        return self.matchmap[matchid]['label']

    def get_points_for_matchid(self, matchid):
        return self.matchmap[matchid]['points']

    def _add_match_if_matched(self, matchid):
        if matchid is not None:
            self.summary.append(matchid)
            self.points += self.matchmap[matchid]['points']

    def compare(self):
        self._add_match_if_matched(self._compare_operators_and_keywords_string_equal())
        self._add_match_if_matched(self._compare_operators_string_equal())
        self._add_match_if_matched(self._compare_keywords_string_equal())

    #
    #
    # Compare-methods
    # ===============
    # Each of them return a key from :obj:`.matchmap` if they find a match.
    # If they do not return None, we use :meth:`._add_match_if_matched` to
    # look them up in :obj:`.matchmap` to find the points awarded for the
    # match.
    #
    #

    def _compare_operators_and_keywords_string_equal(self):
        a = self.parseresult1
        b = self.parseresult2
        if a.get_operators_and_keywords_string() == b.get_operators_and_keywords_string():
            return 'operators_and_keywords_string_equal'
        else:
            return None

    def _compare_operators_string_equal(self):
        if self.parseresult1.get_operators_string() == self.parseresult2.get_operators_string():
            return 'operators_string_equal'
        else:
            return None

    def _compare_keywords_string_equal(self):
        if self.parseresult1.get_keywords_string() == self.parseresult2.get_keywords_string():
            return 'keywords_string_equal'
        else:
            return None

    def _compare_total_operatorcount_equal(self):
        if self.parseresult1.get_number_of_operators() == self.parseresult2.get_number_of_operators():
            return 'total_operatorcount_equal'
        else:
            return None

    def _compare_total_keywordcount_equal(self):
        if self.parseresult1.get_number_of_keywords() == self.parseresult2.get_number_of_keywords():
            return 'total_keywordcount_equal'
        else:
            return None


class ParseResultCompareMany(object):
    """

    """
    def __init__(self, parseresults):
        self.compare_results = []
        for index1, parseresult1 in enumerate(parseresults):
            for index2 in xrange(index1 + 1, len(parseresults)):
                parseresult2 = parseresults[index2]
                comparetwo = ParseResultCompareTwo(parseresult1, parseresult2)
                self.compare_results.append(comparetwo)

    def sort_by_points_descending(self):
        """
        Sort by points in place.
        """
        self.compare_results.sort(cmp=lambda a, b: cmp(b.points, a.points))

    def __iter__(self):
        return self.compare_results.__iter__()
