############### The class that compares the key-values ################

from report import ReportGen

class Comparer:
    def __init__(self, programs, percentage):
        self.programs = programs
        self.total_comparisons = 0
        self.percentage = percentage
        self.result = {}
        self.do_the_work()
        
    def do_the_work(self):
        self.point_dict = {}
        self.avg_points_dict = {}

        for i in range(0, len(self.programs), 1):
            for j in range(i+1, len(self.programs), 1):
                sum_points = self.compare(self.programs[i], self.programs[j])
                self.total_comparisons  += 1
                if not sum_points in self.result:
                    self.result[sum_points] = []
                self.result[sum_points].append((self.programs[i], self.programs[j]))
        self.sum_points = sum_points / len(self.programs)
        print "Total number of comparisons was " + str(self.total_comparisons) + "\n"

        #     sum_points = 0
        #     # get a list of all deliveries of a specific file
        #     ulist = self.programs[key]
        #     # get data for a hand in (from ulist)
        #     for i in range(0, len(ulist), 1):
        #         a = ulist[i]
        #         # get data for all others and compare
        #         for j in range(i+1, len(ulist), 1):
        #             b = ulist[j]
        #             sum_points += self.compare(a,b)
        #             self.total_comparisons += 1
        #     if not len(ulist):
        #         self.avg_points_dict[key] = 0
        #     else:
        #         self.avg_points_dict[key] = sum_points / len(ulist)
        # print "Total number of comparisons was " + str(self.total_comparisons) + "\n"

    def compare(self, a, b):
        # using points 
        self.points = 0
        shares = 0
        summary = '' # a list of lines which make up the summary for a given compare
        if a.codesignature.bigstring == b.codesignature.bigstring:
            self.points += 10
            # The string containing keywords and operators match.
            summary += "Programs very similar. Look for use of query-replace. <BR>"
            shares = 1
        if a.codesignature.keywordstring == b.codesignature.keywordstring:
            self.points += 3
            # Same number of each keywords used.
            if not a.codesignature.bigstring == b.codesignature.bigstring:
                summary += "The two programs has equal number of keyword. <BR>"
            shares = 1
        if a.codesignature.operatorstring == b.codesignature.operatorstring:
            self.points += 3
            if not a.codesignature.bigstring == b.codesignature.bigstring:
                summary += "Same number of each operator used. <BR>"
            shares = 1
        if a.codesignature.number_of_keywords == b.codesignature.number_of_keywords:
            self.points += 1
            if not a.codesignature.bigstring == b.codesignature.bigstring:
                summary += "Equal total number of keywords. <BR>"
            shares = 1
        if a.codesignature.number_of_operators == b.codesignature.number_of_operators:
            self.points += 1
            if not a.codesignature.bigstring == b.codesignature.bigstring:
                summary += "Equal number of operators. <BR>"
            shares = 1
        num_equal_funcs = 0
        for fhash1 in a.codesignature.list_of_functions:
            for fhash2 in b.codesignature.list_of_functions:
                if fhash1 == fhash2:
                    self.points += 3
                    num_equal_funcs += 1
                    shares = 1
        if num_equal_funcs:
            if not a.codesignature.bigstring == b.codesignature.bigstring:
                summary += "Query-replace might have been used to make function(s) look different. <BR>"
                
        summary = summary[:-4]
        key = ''
        if not shares:
            if self.VERBOSE: print 'Test passed!'
        else:
            # make a page where the user can view the two programs
            #view_file = a.file + "_" + a.name + "_" + b.name + ".html"
            #view_report = ReportGen(self.report_dir, self.directory, view_file)
            #view_report.make_diff_page(a.file, a.name, b.name)
            #val = (a.file, a.name, b.name, summary, view_file)
            #key = self.points
            #if not self.point_dict.has_key(key):
            #    self.point_dict[key] = []
            #self.point_dict[key].append(val)
            print 'Points:',self.points,'\n'
        return self.points
        
    def get_result(self):
        return self.result

    def build_result(self):
        res = []
        keys = self.point_dict.keys()
        #limit = avg + avg * self.percentage / 100
        # limit = 1
        keys.sort()
        # print the highest scores first
        for i in range(len(keys)-1, -1, -1):
            for p in self.point_dict[keys[i]]:
                avg = self.avg_points_dict[p[0]]
                if not avg:
                    break
                limit = avg + avg * self.percentage / 100
                if keys[i] >= limit:
                    #print keys[i],'points:',p[:-1],''
                    t = (p[0], p[1], p[2], p[3], keys[i], avg, p[4])
                    res.append(t)
                if keys[i] < limit:
                    break # break out of this inner loop
        return res

