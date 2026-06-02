import webbrowser
user_term = input("Enter your search item: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + user_term)


