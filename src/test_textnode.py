import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_neq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_edge_case(self):
        node = TextNode("this is edge case", TextType.BOLD, None)
        node2 = TextNode("this is edge case", TextType.BOLD)
        self.assertEqual(node, node2)


class text_to_html_TEST(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_1(self):
        node = TextNode("this node has code text", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "code")
    
    def test_2(self):
        node = TextNode("link, again", TextType.LINK, "https://www.google.com")
        html = text_node_to_html_node(node)
        self.assertEqual(html.props, {'href':"https://www.google.com"})
    
    def test_3(self):
        node = TextNode("unknown image",TextType.IMAGE, "https://www.image.com" )
        html = text_node_to_html_node(node)
        self.assertEqual(html.props, {"src" : "https://www.image.com", "alt" : "unknown image"})
    
    def err_1(self):
        with self.assertRaises(ValueError):
            node = TextNode("unknown image",TextType.IMAGE)
            html = text_node_to_html_node(node)
    
    def err_2(self):
        with self.assertRaises(ValueError):
            node = TextNode("errored one", TextType.LINK)
            html = text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()