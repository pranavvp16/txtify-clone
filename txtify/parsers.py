def get_tags(node):
    body = node.body
    tags_list = list(set([element.name for element in body.find_all(True)]))
    return tags_list

def reduce_article(doc):
    body_tag = get_tags(doc)
    for item in body_tag:
        if item not in [
            "p",
            "br",
            "h1",
            "h2",
            "h3",
            "h4",
            "h5",
            "h6",
            "ul",
            "body",
            "article",
            "section",
        ]:
            if doc.find_all(item):
                item.drop_tag()

    return doc