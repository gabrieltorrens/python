from html.parser import HTMLParser
paragraphs = 0

class MyParser(HTMLParser):
    def handle_comment(self, data):
        print("Found a comment:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position:", pos[1])

    def handle_starttag(self, tag, attrs):
        print("Found a start tag:", tag)
        pos = self.getpos()
        print("At line:", pos[0], "position:", pos[1])

        global paragraphs
        if tag == "p":
            paragraphs += 1

    def handle_data(self, data):
        if data.isspace():
            return
        print("Found text data:", data)
        pos = self.getpos()
        print("At line:", pos[0], "position:", pos[1])

parser = MyParser()
f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read() # read the entire file
    parser.feed(contents)

print("Number of paragraphs:", paragraphs)