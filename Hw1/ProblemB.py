import os

# filePairs method
# returns a list of tuples that contain files that are the same within a certain number of bytes.
# args: dtree, nBytes
# returns: list
def filePairs(dtree, nBytes):
    totalTree = os.path.abspath(dtree)
    allFiles = []
    os.path.walk(totalTree,getFiles,allFiles)
    myList = checkForDupes(allFiles,nBytes)
    return myList

# getFiles method
# gets all of the files in a given file tree.
# args: files list, directory root, list of paths
def getFiles(files, rootDir, myList):
    for aFile in myList:
        pathName = rootDir + '\\' + aFile
        if( os.path.isfile(pathName)):
            files.append(pathName)

# checkForDupes method
# checks for any duplicate files in the directory tree and returns the pair as a tuple if there are any.
# args: fileList, numBytes
# returns: List of duplicate files
def checkForDupes(fileList,numBytes):
    returnList = []
    for f in range(0,len(fileList)):
        dupeFound = False
        for i in range(f,len(fileList)):
            if(f != i):
                for x in range(1,numBytes):
                    oFile = open(fileList[f])
                    oFile2 = open(fileList[i])
                    fd1 =  oFile.fileno()
                    fd2 =  oFile2.fileno()
                    check1 = os.read(fd1,x)
                    check2 = os.read(fd2,x)
                    if(check1 == check2):
                        dupeFound = True
                    else:
                        dupeFound = False
            if(dupeFound):
                returnList.append((fileList[f],fileList[i]))

    return returnList

l1 = filePairs('C:\Users\josep\Desktop\TestDir',3)
print l1
