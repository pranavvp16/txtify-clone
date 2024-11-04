import lxml
from copy import deepcopy

def get_formated(node):

    html, txt = "", ""

    node_cleaned = deepcopy(node)

def _remove_negativescores_nodes(self, top_node):
    """If there are elements inside our top node that have a
    negative gravity score, let's give em the boot.
    """
    gravity_items = top_node.xpath(".//*[@gravityScore]")
    for item in gravity_items:
        score = item.attrib.get("gravityScore", "0")
        score = float(score)
        if score < 1:
            item.getparent().remove(item)


