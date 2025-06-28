from typing import List

from nodes import (
    DocumentNode,
    HeadingNode,
    ItalicNode,
    Node,
    ParagraphNode,
    StrongNode,
    TextNode,
)


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

        nodes = []
        current_text = ""
        i = 0

        while i < len(text):

            if text[i : i + 2] == "**":

                if current_text:
                    nodes.append(TextNode(current_text))
                    current_text = ""

                found_index = text.find("**", i + 2)

                if found_index != -1:
                    content = text[i + 2 : found_index]
                    strong_node = StrongNode()
                    strong_node.children.extend(self.parse_inline(content))
                    nodes.append(strong_node)
                    i = found_index + 2

                else:
                    current_text += text[i : i + 2]
                    i = i + 2

            elif text[i] == "*":

                if current_text:
                    nodes.append(TextNode(current_text))
                    current_text = ""

                found_index = text.find("*", i + 1)
                if found_index != -1:
                    content = text[i + 1 : found_index]
                    italic_node = ItalicNode()
                    italic_node.children.extend(self.parse_inline(content))
                    nodes.append(italic_node)
                    i = found_index + 1
                else:
                    current_text = text[i]
                    i += 1

            else:
                current_text += text[i]
                i += 1

        if current_text:
            nodes.append(TextNode(current_text))

        return nodes
