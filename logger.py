#Logs a post ID
def log(postId):
    with open("PostIds.log", "a") as postFile:
        postFile.write(postId + "\n")

#Opens the file to look through it
def openFile():
    with open("PostIds.log", "r") as postFile:
        return postFile.read().splitlines()