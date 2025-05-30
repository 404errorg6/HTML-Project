import unittest
from htmlnode import HTMLNode

class test_html(unittest.TestCase):
    def test_None(self):
        node = HTMLNode()
        node2 = HTMLNode(None, None, None, None)
        self.assertEqual(node, node2)
    def test_Nequal(self):
        node = HTMLNode("p", "fk off", None)
        node2 = HTMLNode("h1", "fk off")
        print(node)
        print(node2)
        self.assertNotEqual(node, node2)
    def test_props(self):
        dic = {
                "href" : "www.google.com",
                "target" : "testing..."
                }
        node = HTMLNode("h3", "How to get fked up", None, dic)
        print(node.props_to_html())
    def test_prop_edgeC(self):
        dic = {                                                                                             "href" : "www.google.com"}
        node = HTMLNode("h5", "Not again", None, dic)
        print(node.props_to_html())

    def test_print(self):
        dic = {                                                                                             "href" : "www.google.com"}
        node = HTMLNode("p", "hello world", None, dic)
        print(node)

if __name__ == "__main__":
    unittest.main()
