filenames = ['1.doc', '2.report', '3.results']
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)
