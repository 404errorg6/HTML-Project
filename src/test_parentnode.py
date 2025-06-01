import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class ParentNodeTest(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_1(self):
        child = LeafNode("p", "no tag")
        parent = ParentNode(None, children=[child])
        with self.assertRaises(ValueError):
            parent.to_html()
    def test_2(self):
        child = LeafNode("b", "no child")
        parent = ParentNode("h1", None)
        with self.assertRaises(ValueError):
            parent.to_html()
    def test_3(self):
        g_g_g_g_child = LeafNode("b", "bolded+italized")
        g_g_g_child = ParentNode("i", [g_g_g_g_child])
        g_g_child = ParentNode("u", [g_g_g_child])
        extra = LeafNode("p", "a paragraph in g_child")
        g_child = ParentNode("h3", [g_g_child, extra])
        child = ParentNode("h2", [g_child])
        parent = ParentNode("h1", [child])
        self.assertEqual(parent.to_html(), "<h1><h2><h3><u><i><b>bolded+italized</b></i></u><p>a paragraph in g_child</p></h3></h2></h1>")
    def test_3(self):
        g_child = LeafNode("i", "italized text")
        g2_child = LeafNode("a", "found an interesting link", {"href" : "https://www.rickroll.com"})
        child = ParentNode("p", [g_child, g2_child])
        header = LeafNode("h1", "this is header")
        parent = ParentNode("body", [header, child])
        self.assertEqual(parent.to_html(), '<body><h1>this is header</h1><p><i>italized text</i><a href="https://www.rickroll.com">found an interesting link</a></p></body>')

if __name__ == "__main__":
    unittest.main()