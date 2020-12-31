import re

def import_names(file_path):
    names = open(file_path, 'r')
    names = names.read()
    names = re.sub('([A-Z])', r' \1', names)
    names = names.split()
    return names
