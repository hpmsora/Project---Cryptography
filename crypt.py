#---------------------------------------------------
#
# Won Yong Ha
#
# Python
#
# Cryptography Project
#
#---------------------------------------------------

# Variable


# main Function
def main():

    #Getting Name
    textName = input("Enter the document name(.txt): ")
    userPW = input("Enter password: ")
    outputName = input("Enter the name of the result file: ")
    
    #Open the file and get string
    textContents = open(textName, "r")
    
    #Split the string
    text = letterSplit(textContents)
    
    #Changed to ASCII
    text = letterListToIntList(text)

    #Changed to ASCII with length
    text = intListToIntLengthList(text)

    #Combine all element in the text
    text = listAllTogether(text)

    #Reverse the list
    text = reverseList(text)

    #Combine all element in the text
    text = listAllTogether(text)

    print(text)
    
    #Change pw to ASCII
    userPW = pwToInt(userPW)

    #Change pw to Binary
    userPW = pwIntToBinaryCode(userPW)

    print(userPW)

# letterSplit Function
# return letter list
def letterSplit(contents):
    return list(contents.read())

# letterListToIntList Function
# return str(int) list
def letterListToIntList(contents):
    intList = []
    for i in contents:
        intList.append(ord(i))
    return intList

# intListToIntLengthList Function
# return integer with length of its length
def intListToIntLengthList(contents):
    intList = []
    for i in contents:
        intList.append(int(str(len(str(i))) + str(i)))
    return intList

# listAllTogether Function
# return the string conbine all list together
def listAllTogether(contents):
    all = ""
    for i in contents:
        all += str(i)
    return all

# reverseList Function
# return the list of string that reversed
def reverseList(contents):
    contents = list(contents)
    length = len(contents)
    newList = []
    for i in range(length):
        newList.append(contents[length - 1 - int(i)])
    return newList

# pwToInt Function
# return the string integer cryptic of pw
def pwToInt(PW):
    newPW = ""
    for i in list(PW):
        newPW += str(ord(i))
    return newPW

# pwIntToBinaryCode Function
# return the string of Binary code for pw
def pwIntToBinaryCode(PW):
    newBinaryPW = ""
    for i in list(PW):
        j = int(i)
        binary = ""
        if j == 0:
            binary = "0"
        else:
            while j != 0:
                binary += str(j % 2)
                j = int(j / 2)
        newBinaryPW += binary
    return newBinaryPW

# crypting Function
# return crypted value
def crypting(contents, PW):
    count = 0
    newList = []
    contents = list(contents)
    PW = list(PW)
    length = len(contents)
    for i in range(length):
        j = int(contents[i])
        count += j



#Activating the main function
if __name__ == "__main__": main()
