import unittest
from leafnode import LeafNode

class LeafTest(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_1(self):
        node = LeafNode("a", "Annoying ads", {"href" : "https:www.//ads.com"})
        self.assertEqual(node.to_html(), '<a href="https:www.//ads.com">Annoying ads</a>')
    def test_3(self):
        node = LeafNode("tagged", "this is errored one")
        with self.assertRaises(Exception):
            node.to_html()
    def test_4(self):
        node = LeafNode("a", "no props")
        with self.assertRaises(ValueError):
            node.to_html()
    def test_5(self):
        node = LeafNode("p", "extra props", {"href" : "https:www.//google.com"})
        self.assertEqual(node.to_html(), "<p>extra props</p>")
if __name__ == "__main__":
    unittest.main()