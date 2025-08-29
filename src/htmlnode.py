

class HTMLNode:

    """
    HTMLNode has everything default to None for theses assumptions:
    if tag is empty it will render as raw text
    if value is empty it is assumed to have children and vice versa for children
    if props is empty it simply won't have any html attributes

    """
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        #placeholder for child classes to override 
        raise NotImplementedError

    def props_to_html(self):
        keys = self.props.keys()

        result_string = ""

        for key in keys:
            result_string += f"{key}="
            result_string += self.props[key]
            result_string += " "

        return result_string

    def __repr__(self):
        return f"HTMLNode = tag={self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"

            
