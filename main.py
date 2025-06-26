from parser import Parser

sample_markdown = """
# This is a Main Heading

This is the first paragraph. It's a simple one.

## This is a Sub-Heading

This is a second paragraph.
It has two lines.

This is the final paragraph.
"""

parser = Parser(sample_markdown)

document_ast = parser.parse()

print(document_ast)
