contents = ["Hi!! How are you?",
            "Whats your name?",
            "Where are from?"]

filenames = ["doc.txt", "report.txt", "presentation.txt"]
for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)