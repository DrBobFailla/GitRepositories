""" Input 2 directories.  Drops file extension and compares filenames only.
Output 3 lists (in a and not in b, in b and not in a, in both.
"""
import os

def compare2Dirs(dir1, dir2):
    """
    Input 2 directories for comparison.  Computes file root (Ex. file.csv and file.txt have the
    same file root - file. Returns 3 sets -
    oneNotTwo - file roots in dir1 and not in dir2.
    twoNotOne - file roots in dir2 and not in dir1
    both - file roots in both dir1 and dir2
    """
    # Get the directory listings for each source directory
    originaldir1files = set(os.listdir(dir1))
    originaldir2filestemp = set(os.listdir(dir2))
    # Get the root filename only.
    dir1files = {x.split(".")[0] for x in originaldir1files}
    dir2files = {x.split(".")[0] for x in originaldir2filestemp}
    oneNotTwo = sorted(dir1files.difference(dir2files))
    twoNoteOne = sorted(dir2files.difference(dir1files))
    both = sorted(dir2files.intersection(dir1files))
    return oneNotTwo, twoNoteOne, both

def pathByFileRoot(filenamelist):
    """
    Inputs a list of {file roots, paths} (the file root for file.txt and file.csv is file.
    Outputs a dictionary of file roots with a count of the directories where each file root is found)
    """
    filenamedict = dict()
    for i in sorted(filenamelist):
        if i[0] in filenamedict:
            filenamedict[i[0]].append(i[1])
        else:
            filenamedict[i[0]] = [i[1]]
    return filenamedict

def countFileRootsInDir(filenamelist):
    """
    Inputs a list of {file roots, paths}
    Outputs a dictionary of [path, count]
    """

    dircount = dict()
    for i, j in filenamelist:
        if j in dircount:
            dircount[j] += 1
        else:
            dircount[j] = 1

def findSimilarDirectories(filenamelist):
    # We want to find directories that are 100% similar.
    # Start by creating a dictionary for each path with a list of file roots in that path
    p = dict()
    pathwithfiles = dict()
    for i, j in filenamelist:
        if j in p:
            p[j].append(i)
        else:
            p[j] = [i]
    # We're going to do set arithmetic, so convert the dictionary values to sets
    for i in p:
        pathwithfiles[i] = set(p[i])
    # Now do pairwise comparisons and identify directories that are 100% in common with one another
    r = []
    for i, x in enumerate(pathwithfiles):
        for j, y in enumerate(pathwithfiles):
            if i != j and pathwithfiles[x] == pathwithfiles[y] and pathwithfiles[x] not in r:
                r.append(pathwithfiles[x])
    for i in r:
        print(i)

if __name__ == "__main__":
    filenamelist = []
    # We need a two-tuple of filenames and their paths
    for root,dirs, files in os.walk("/Users/Bob 1", topdown=False):
        for x in files:
            filenamelist.append((x.split(".")[0], root))
    print(findSimilarDirectories(filenamelist))

    # for i, x in enumerate(resultsset):
    #     print(i, x)
    # iter_obj = iter(pathwithfiles)
    # while True:
    #     try:
    #         a = next(iter_obj)
    #         while True:
    #             try:
    #                 b = next(iter_obj)
    #                 if pathwithfiles[a] == pathwithfiles[b] and len(pathwithfiles[a]) > 1:
    #                     print(a, " and ", b, "are equivalent")
    #                     print(a, b)
    #                     print(pathwithfiles[a], pathwithfiles[b])
    #             except StopIteration:
    #                 break
    #     except StopIteration:
    #         break
    # oneNotTwo, twoNotOne, both = compare2Dirs(dir1, dir2)