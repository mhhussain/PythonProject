def app():
    docs = ReadFile("../ap_docs.txt")
    search = []

    option = 0
    while option != 3:
        print ("What would you like to do?")
        print ("1. Search for documents")
        print ("2. Read Document")
        print ("3. Quit program")
        option = input(">")

        if int(option) == 1:
            searchString = input("Enter search words: ")
            search = SearchDocs(searchString, docs)
            print ("Documents fitting search: ", end="")
            for i in search:
                print (i, end=" ")
            print ()

        if int(option) == 2:
            docnum = input("Enter document number: ")
            doc = RetrieveDocument(int(docnum), docs)
            print ("Document #", docnum)
            print ("----------------------------", end="")
            print (doc)

        if int(option) == 3:
            return

    return


## Read data from file
def ReadFile(file):
    f = open(file, "r")

    return [i for i in f.read().split("<NEW DOCUMENT>") if len(i) > 0]

## Search documents 'docs' for string 's'. String is split on spaces to search for
## multiple words
def SearchDocs(s, docs):
    searchStrings = s.split()
    retVal = set()
    for i in searchStrings:
        for j in range(len(docs)):
            if i.lower() in docs[j].lower():
                retVal.add(j + 1)

    return retVal

## Retrieve document from 'docs'. Document array is zero indexed, and document number
## provided is one indexed, so an adjustment must happen.
def RetrieveDocument(num, docs):
    return docs[num - 1]


app()
