from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        self.tag = tag
        self.value = value 
        self.props = props
        self.VALID_TAGS = ['p', 'b', 'i', 'u', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'code', 'blockquote', 'span', 'div', 'body', 'html', 'title', 'head', 'ul', 'ol'] #except a and img
    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return self.value
        else:
            if (self.tag == "a" or self.tag == "img") and not self.props:
                raise ValueError(f"<{self.tag}> tag requires props value")
            
            elif self.tag == "a" or self.tag == "img":
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            
            elif self.tag in self.VALID_TAGS:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            
            else:
                raise Exception("invalid input")