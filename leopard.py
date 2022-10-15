class Leopard:
    import csv

    def __init__(self, csvfile):
        import csv
        self.csvfile = csvfile
        try:
            with open(self.csvfile) as file:
                self.data = None
                self.header = []
                sh = csv.reader(file)
                try:
                    self.header = next(sh)
                except:
                    self.header = None
                self.data = [row for row in sh]
        except FileNotFoundError:
            self.data = []
            self.header = None
            raise FileNotFoundError

    def get_header(self):
        if self.data == [] or self.header is None:
            return "Data not loaded"
        else:
            return self.header

    def get_dimension(self):
        if self.data == [] or self.header is None:
            return "Data not loaded"
        else:
            self.dimension = [len(self.data), len(self.data[0])]
            return self.dimension

    def total_missing(self):
        if self.data == [] or self.header is None:
            return "Data not loaded"
        else:
            num = 0
            haveornot = 0
            rows = len(self.data)
            cols = len(self.data[0])
            for i in range(rows):
                for j in range(cols):
                    if self.data[i][j] == "" or\
                            self.data[i][j] == " " or\
                            self.data[i][j] == "?" or\
                            self.data[i][j] == "NA":
                        haveornot += 1
                if not haveornot == 0:
                    num += 1
                    haveornot = 0
            return num

    def count_instances(self, column_heading, value):
        if self.data == [] or self.header is None:
            return "Data not loaded"
        else:
            self.new = self.data
            self.new.insert(0, self.header)
            a = self.new
            sum = 0
            column_heading = column_heading.upper()
            value = value.upper()
            for i in range(len(a)):
                for j in range(len(a[0])):
                    a[i][j] = a[i][j].upper()
            for j in range(len(a[0])):
                if a[0][j] == column_heading:
                    for i in range(len(a)):
                        if a[i][j] == value:
                            sum += 1
            return sum
