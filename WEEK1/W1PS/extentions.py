#this is a program that prompts the user for the name of a file and then outputs that file’s media type

#prompte the user for a file name and output its type

def main():
    file = input("Please, enter the name of your file: ").strip().lower()
    categorize(file)

#categorize files based on extensions and print media types

def categorize(file):
    if file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".jpeg"):
        print("image/jpeg")
    elif file.endswith(".jpg"):
        print("image/jpg")
    elif file.endswith(".png") :
        print("image/png")   
    elif file.endswith(".txt") :
        print("text/plain")
    elif file.endswith(".pdf") :
        print("application/pdf")
    elif file.endswith(".zip") :
        print("application/zip")

#Run main function

main()