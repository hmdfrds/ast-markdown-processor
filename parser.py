from nodes import DocumentNode, HeadingNode, ParagraphNode, TextNode


class Parser:

    def __init__(self, markdown_text: str):
        self.lines = markdown_text.strip().split("\n")
        self.document = DocumentNode()
        self.current_line_number = 0

    def parse(self) -> DocumentNode:
        while self.current_line_number < len(self.lines):
            current_line_text = self.lines[self.current_line_number]
            if current_line_text.startswith("#"):
                self.parse_heading()
            elif current_line_text.strip() == "":
                self.current_line_number += 1
            else:
                self.parse_paragraph()
        return self.document

    def parse_heading(self):
        line = self.lines[self.current_line_number]

        level = 0
        while level < len(line) and line[level] == "#":
            level += 1

        text = line[level:].lstrip()

        heading_node = HeadingNode(level)
        text_node = TextNode(text)
        heading_node.children.append(text)

        self.document.children.append(text_node)

        self.current_line_number += 1

    def parse_paragraph(self):

        paragraph_text = ""

        while (
            self.current_line_number < len(self.lines)
            and self.lines[self.current_line_number].strip() != ""
            and not self.lines[self.current_line_number].startswith("#")
        ):

            line = self.lines[self.current_line_number]

            if paragraph_text:
                paragraph_text += " "
            paragraph_text += line.strip()

            self.current_line_number += 1

        if paragraph_text:
            p_node = ParagraphNode()
            p_node.children.append(TextNode(paragraph_text))
            self.document.children.append(p_node)

