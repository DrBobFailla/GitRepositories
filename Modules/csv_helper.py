import csv
from datetime import datetime


class csvData:

    def __init__(self, filename, headers):
        self.filename = filename
        cfile = open(self.filename, newline='')
        database = csv.reader(cfile)
        if headers:
            self.headers = next(database)
        self.data = list(database)
        cfile.close()

    def database_size(self):
        return len(self.data)

    def neat_print_all(self):
        # Specific to research project.  Can be deleted.  Prints formatted
        # fields of interest.
        for i in self.data:
            print("%-70s %20s %20s %20s %5s" % (i[1], i[2], i[3], i[4], i[5]))

    def pipe_print_all(self):
        # Prints a pipe delimited list
        for i in self.data:
            print(i[0], "|", i[1], "|", i[2], "|", i[3], "|", i[4], "|", i[5], "|", i[6], "|", i[7], "|", i[8], "|",
                  i[9], "|", i[10], "|", i[11], "|", i[12], "|", i[13], "|", i[14], "|", i[15])

    def summarize_csv_columns_skipping_columns(self, skip):
        # finds the unique values in all columns counts them, and prints them.  Skips any column listed in skip.
        # Future, return a dictionary so other code can manipulate the output.
        for i in range(len(self.headers)):
            if i not in skip:
                temp_dictionary = {}
                for j in self.data:
                    if j[i] in temp_dictionary:
                        temp_dictionary[j[i]] += 1
                    else:
                        temp_dictionary[j[i]] = 1
                print("Summarizing ", self.headers[i])
                print(sorted(temp_dictionary.items()))
                print(len(temp_dictionary), "unique items.")
                print()

    def summarize_csv_columns(self, include):
        # Finds the unique values in the columns in the include list and counts them.
        # Future return the output instead of printing it so other code can
        # manipulate the output.
        for i in range(len(self.headers)):
            if i in include:
                temp_dictionary = {}
                for j in self.data:
                    if j[i] in temp_dictionary:
                        temp_dictionary[j[i]] += 1
                    else:
                        temp_dictionary[j[i]] = 1
                print("Summarizing ", self.headers[i])
                print(sorted(temp_dictionary.items()))
                print(len(temp_dictionary), "unique items.")
                print()

    def index_csv_columns_skipping_columns(self, skip):
        # Finds the unique values in all columns except those in the skip list.  Prints the sorted values.
        # Future - return the list so other code can process the output.
        for i in range(len(self.headers) - 1):
            if i not in skip:
                temp_dictionary = {}
                for j in self.data:
                    if j[i] in temp_dictionary:
                        temp_dictionary[j[i]] += 1
                    else:
                        temp_dictionary[j[i]] = 1
                print("Indexing ", self.headers[i])
                print(sorted(temp_dictionary.keys()))
                print()

    def index_csv_columns(self, include):
        # Finds the unique values in the columns specified.
        for i in range(len(self.headers) - 1):
            if i in include:
                temp_dictionary = {}
                for j in self.data:
                    if j[i] in temp_dictionary:
                        temp_dictionary[j[i]] += 1
                    else:
                        temp_dictionary[j[i]] = 1

        return temp_dictionary

    def print_column(self, include):
        # Prints all the values in the columns given
        for i in self.data:
            print(i[include])

    def limit_data_to_years(self, years, column):
        # Removes data not associated with the dates specified.
        # Future - too broad an exception.  Fix this.
        temp = []
        for i in enumerate(self.data):
            try:
                dt = datetime.strptime(i[1][column], "%m/%d/%Y")
            except BaseException:
                print("Error: Date element is probably not in the right format - month/day/4 digit year.\
                  Unceremoneously exiting.")
                exit()
            if dt.year in years:
                temp.append(i[1])
        self.data = []
        self.data = temp

    def find_minimum_date_in_column(self, column):
        # Finds the minimum date in the column specified.
        # Future - like the others, allows several columns to be specified.
        # Future - Allow different date formats and detect them automatically
        minimum = datetime.strptime(self.data[1][column], "%m/%d/%Y")
        try:
            for i in enumerate(self.data):
                if datetime.strptime(i[1][column], "%m/%d/%Y") < minimum:
                    minimum = datetime.strptime(i[1][column], "%m/%d/%y")
        except BaseException:
            pass
        return minimum

    def find_maximum_date_in_column(self, column):
        # Finds the maximum date in the column specified.
        # Future - like the others, allows several columns to be specified.
        # Future - Allow different date formats and detect them automatically
        maximum = datetime.strptime(self.data[1][column], "%m/%d/%Y")
        try:
            for i in enumerate(self.data):
                if datetime.strptime(i[1][column], "%m/%d/%Y") > maximum:
                    maximum = datetime.strptime(i[1][column], "%m/%d/%y")
        except BaseException:
            pass
        return maximum

    def find_target_in_any_column(self, target):
        # A search function.
        # Future allow user to limit search to specific columns
        for i in self.data:
            if target in i:
                print(i)

    def total_columns(self, columns):
        # Totals the columns specified.
        # Future input checking and error handling if input is not a number.
        # Future - detect integers and return an integer.  Same with float.
        totals = {}
        for i in columns:
            totals[i] = 0

        for i in self.data:
            for j in totals:
                try:
                    totals[j] += float(i[j])
                except BaseException:
                    pass
        return totals

    def calc_mean_on_columns(self, columns):
        # Future input checking and error hadling if input is not a number.
        # Future - detect integers and return an integer.  Same with float.
        totals = self.total_columns(columns)
        averages = {}
        for i in totals:
            averages[i] = totals[i] / len(self.data)
        return averages

    def cal_median_on_columns(self, columns):
        # Future input checking and error handling if input is not a number.
        # Future - detect integers and return an integer.  Same with float.
        values = {}
        sorted_values = {}
        median_value = {}
        for i in columns:
            values[i] = []

        for i in self.data:
            for j in columns:
                if i[j] == '':
                    values[j].append(0)
                else:
                    values[j].append(int(i[j].replace(",", "")))

        for i in values:
            sorted_values[i] = sorted(values[i])

        for i in values:
            if len(sorted_values[i]) % 2 == 0:
                median_value[i] = (sorted_values[i][int(len(
                    sorted_values[i]) / 2)] + sorted_values[i][int((len(sorted_values[i]) / 2) + 1)]) / 2
            else:
                median_value[i] = sorted_values[i][int(
                    (len(sorted_values) / 2) + 1)]

        return median_value
