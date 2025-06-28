from nodes import (
    DocumentNode,
    HeadingNode,
    ItalicNode,
    Node,
    ParagraphNode,
    StrongNode,
    TextNode,
)


class Renderer:

    def render(self, document: DocumentNode) -> str:
        return self._render_node(document)

    def _render_node(self, node: Node) -> str:
        if isinstance(node, DocumentNode):
            return "\n".join(self._render_node(child) for child in node.children)

        elif isinstance(node, TextNode):
            return node.value

        elif isinstance(node, HeadingNode):
            return f"<h{node.level}>{"".join(self._render_node(child) for child in node.children)}</h{node.level}>"

        elif isinstance(node, ParagraphNode):
            return (
                f"<p>{"".join(self._render_node(child) for child in node.children)}</p>"
            )

        elif isinstance(node, StrongNode):
            return f"<strong>{"".join(self._render_node(child) for child in node.children)}</strong>"

        elif isinstance(node, ItalicNode):
            return f"<em>{"".join(self._render_node(child) for child in node.children)}</em>"

        else:
            raise TypeError(f"Unknown node type: {type(node).__name__}")
