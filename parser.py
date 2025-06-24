from nodes import DocumentNode, TextNode, HeadingNode

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
                self.current_line_number +=1 
            else:
                self.parse_paragraph()
    
    def parse_heading(self):
        line = self.lines[self.current_line_number]

        level = line.count('#')
        text = line.strip('# ')

        text_node = TextNode(text)
        heading_node = HeadingNode(level)
        heading_node.children.append(text_node)

        self.document.children.append(heading_node)
        self.current_line_number += 1
        
    def parse_paragraph(self):
        pass