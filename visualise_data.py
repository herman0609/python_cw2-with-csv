import matplotlib
import matplotlib.pyplot as plt
import csv


def barchart_occurences(csvfile, column_heading, xlabel=None,
                        ylabel=None, title=None):
    try:
        with open(csvfile) as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [row for row in reader]
    except:
        print("File error")
        return
    list1 = []
    new = data
    new.insert(0, header)
    a = new
    column_heading = column_heading.upper()
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = a[i][j].upper()
    for j in range(len(a[0])):
        if a[0][j] == column_heading:
            for i in range(len(a)):
                    list1.append(a[i][j])
    if column_heading not in a[0]:
        print("column heading not found")
        return
    del(list1[0])
    freq_dict = {}
    for x in list1:
        freq_dict[x] = freq_dict.get(x, 0) + 1
    freq_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1],
                            reverse=False))
    x_list = []
    num_list = []
    for key, value in freq_dict.items():
        x_list.append(key)
        num_list.append(value)
    matplotlib.rcParams['axes.unicode_minus'] = False
    sh = len(x_list)
    a = 0
    x = []
    while a != sh:
        a += 1
        x.append(a)
    rects = plt.bar(x, height=num_list, width=0.4, alpha=0.5,
                    color='red', label=column_heading)
    plt.ylabel(ylabel, fontsize=20)
    plt.xticks([index for index in x], x_list)
    plt.xlabel(xlabel, fontsize=20)
    plt.title(title, fontsize=30)
    plt.legend()
    plt.xticks(rotation=90)
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 0.2,
                 str(height), ha='center', va='bottom')
    plt.show()


def scatterplot_xy(csvfile, column_heading_x,
                   column_heading_y, xlabel=None,
                   ylabel=None, title=None):
    try:
        with open(csvfile) as file:
            reader = csv.reader(file)
            header = next(reader)
            data = [row for row in reader]
    except:
        print("File error")
        return
    list1 = []
    list2 = []
    new = data
    new.insert(0, header)
    a = new
    column_heading_x = column_heading_x.upper()
    column_heading_y = column_heading_y.upper()
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = a[i][j].upper()
    for j in range(len(a[0])):
        if a[0][j] == column_heading_x:
            for i in range(len(a)):
                    list1.append(a[i][j])
        elif a[0][j] == column_heading_y:
            for i in range(len(a)):
                    list2.append(a[i][j])
    if column_heading_x not in a[0]:
        print("column heading not found")
        return
    if column_heading_y not in a[0]:
        print("column heading not found")
        return
    del(list1[0])
    del(list2[0])
    for thing1 in list1:
        thing1.replace(".", "")
        if thing1.isdigit():
            list1 = list(map(lambda item: int(item), list1))
    for thing2 in list2:
        thing2.replace(".", "")
        if thing2.isdigit():
            list2 = list(map(lambda item: int(item), list2))
    fig = plt.figure(figsize=(20, 10), dpi=80)
    plt.scatter(list1, list2, s=500, c='r', alpha=0.3)
    plt.xlabel(xlabel, fontsize=40)
    plt.ylabel(ylabel, fontsize=40)
    plt.xticks(rotation=90, fontsize=30)
    plt.yticks(fontsize=30)
    plt.title(title, fontsize=60)
    fig.patch.set_facecolor('lightgray')
    plt.grid()
    plt.show()
