import unittest
from textnode import TextNode, TextType
from split_nodes_delimeter import split_nodes_delimeter

class split_node_Test(unittest.TestCase):
    def test_min(self):
        node = TextNode("this is simply bolded", TextType.BOLD)
        tmp = split_nodes_delimeter([node], '**',  text_type=TextType.BOLD)
        self.assertEqual(tmp, [
            TextNode("this is simply bolded", TextType.BOLD)
        ])
    

    def test_code(self):
        node = TextNode("got a `code` going here", TextType.TEXT)
        tmp = split_nodes_delimeter([node], '`', TextType.CODE)
        self.assertEqual(tmp, [
            TextNode("got a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" going here", TextType.TEXT)
        ])
    def test_bold(self):
        node = TextNode("this is **bolded text**", TextType.TEXT)
        tmp = split_nodes_delimeter([node], '**', TextType.BOLD)
        self.assertEqual(tmp, [
            TextNode("this is ", TextType.TEXT),
            TextNode("bolded text", TextType.BOLD),
            #TextNode(" here", TextType.TEXT)
        ])
    def test_italic(self):
        node = TextNode("its *italic* going on here", TextType.TEXT)
        tmp = split_nodes_delimeter([node], '*', TextType.ITALIC)
        self.assertEqual(tmp, [
            TextNode("its ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" going on here", TextType.TEXT)
        ])
    


    def err(self):
        with self.assertEqual(Exception):
            node = TextNode("buggy **one** with no **last star", TextType.BOLD)
            new = split_nodes_delimeter([node], "**", TextType.BOLD)