from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError('Invalid html: no tag')
    if self.children is None:
      raise ValueError('Invalid html: parent node must have children')
    result = ''
    for child in self.children:
      result += child.to_html()
    return f'<{self.tag}{self.props_to_html()}>{result}</{self.tag}>'
  
  def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}, {self.props})"