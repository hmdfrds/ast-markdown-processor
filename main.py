from parser import Parser

from renderer import Renderer

sample_markdown1 = """
# This is a Main Heading

This is the first paragraph. It's a simple one.

## This is a Sub-Heading

This is a second paragraph.
It has two lines.

This is the final paragraph.
"""

sample_markdown2 = "This is a paragraph with **some bold text** in the middle."

sample_markdown3 = "This **is a *very* important** message."

sample_markdown4 = """
# This is the Final Test!

And it's a **good** one. Our parser should handle this paragraph,
which includes *nested inline elements* like **bold *and* italic**.

Pretty cool.
"""

print("\n--- Markdown ---")

print(sample_markdown4)

print("\n--- PARSING ---")
my_parser = Parser(sample_markdown4)
document_ast = my_parser.parse()
print("AST Created Successfully!")
print(document_ast)


print("\n--- RENDERING ---")
my_renderer = Renderer()
html_output = my_renderer.render(document_ast)
print("HTML Rendered Successfully!")
print("\n--- FINAL HTML OUTPUT ---")
print(html_output)
