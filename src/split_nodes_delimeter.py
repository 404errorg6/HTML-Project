from textnode import TextType, TextNode

def split_nodes_delimeter(old_nodes, delimeter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if delimeter not in node.text or node.text_type != TextType.TEXT:
            new_nodes.append(node)
            
        elif node.text.count(delimeter) % 2 != 0:
            raise Exception(f"text section missing: {delimeter}")
        
        else:
            splitted = node.text.split(delimeter)
            if splitted[-1] == '':
                splitted.remove('')
            i = 0
            while (i < len(splitted)):
                if i == 0 or i % 2 == 0:
                    new_nodes.append(TextNode(splitted[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(splitted[i], text_type))
                i += 1
    return new_nodes