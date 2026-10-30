from html.parser import HTMLParser
import sys

class ValidateHTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() not in self.void_tags:
            self.stack.append((tag.lower(), self.getpos()))

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower in self.void_tags:
            return
        if not self.stack:
            self.errors.append(f"Unexpected end tag </{tag}> at line {self.getpos()[0]}")
            return
        last_tag, pos = self.stack.pop()
        if last_tag != tag_lower:
            # Let's see if it was unclosed or misnested
            self.errors.append(f"Mismatched tag </{tag}> at line {self.getpos()[0]}, expected </{last_tag}> opened at line {pos[0]}")

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

parser = ValidateHTML()
try:
    parser.feed(html_content)
    if parser.errors:
        print(f"Found {len(parser.errors)} HTML nesting warnings/errors:")
        for err in parser.errors[:10]:
            print("  ", err)
    else:
        print("HTML tags nesting is 100% clean!")
except Exception as e:
    print(f"Parser exception: {e}")
