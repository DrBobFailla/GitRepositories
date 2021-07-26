import os


def walkPathReturnFileNames(pathname):
    # Walks the path supplied (pathname) and returns a list of filenames.

    fileNameList = []
    for root, dirs, files in os.walk(pathname, topdown=False):
        for name in files:
            fileNameList.append(os.path.join(root, name))
    return fileNameList
