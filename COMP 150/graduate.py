def main():
    credits = int(input("How many credits do you currently have? "))
    if credits >= 120:
        print('Now you can graduate!')

    else:
        print("You won't be allowed to graduate.")
        print('You are missing',120 - credits, 'credits.')
main()