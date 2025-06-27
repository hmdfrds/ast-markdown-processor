from typing import List

from nodes import DocumentNode, HeadingNode, Node, ParagraphNode, StrongNode, TextNode


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
        inline_node = self.parse_inline(text)
        heading_node.children.extend(inline_node)

        self.document.children.append(heading_node)

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
            inline_node = self.parse_inline(paragraph_text)
            p_node.children.extend(inline_node)
            self.document.children.append(p_node)

    def parse_inline(self, text: str) -> List[Node]:

        parts = text.split("**")
        inline_nodes = []

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                inline_nodes.append(TextNode(part))
            else:
                strong_node = StrongNode()
                strong_node.children.append(TextNode(part))
                inline_nodes.append(strong_node)
        return inline_nodes
