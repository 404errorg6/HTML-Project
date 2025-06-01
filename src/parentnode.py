from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        self.tag = tag
        self.props = props
        self.children = children 
    def to_html(self):
        if not self.tag:
            raise ValueError("input tag")
        elif not self.children:
            raise ValueError("input children")
        else:
            
            string = ""
            
            for child in self.children:
                    string += child.to_html()
            return f"<{self.tag}>{string}</{self.tag}>" 