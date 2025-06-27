from parser import Parser

sample_markdown1 = """
# This is a Main Heading

This is the first paragraph. It's a simple one.

## This is a Sub-Heading

This is a second paragraph.
It has two lines.

This is the final paragraph.
"""

sample_markdown2 = "This is a paragraph with **some bold text** in the middle."

parser = Parser(sample_markdown2)

document_ast = parser.parse()

print(document_ast)
