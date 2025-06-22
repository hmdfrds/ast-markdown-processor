from typing import List

class Node:
    def __init__(self):
        self.children: List('Node') = []

    def __repr__(self):
        return f"{self.__class__.__name__}({self.children})"

class DocumentNode(Node):
    pass

class TextNode(Node):
    def __init__(self, value):
        super().__init__()
        self.value: str = value

    def __repr__(self):
        return f"TextNode(value='{self.value}')"

class ParagraphNode(Node):
    pass

class HeadingNode(Node):
    def __init__(self, level):
        super().__init__()
        self.level: int = level
    
    def __repr__(self):
        return f"HeadingNode(level={self.level}, children={self.children})"

class StrongNode(Node):
    pass

class ItalicNode(Node):
    pass