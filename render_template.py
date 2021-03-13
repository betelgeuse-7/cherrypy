from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

def render_template(html, obj):
    """ 
    takes 2 args: a '.html' file under templates folder and 
    a python dictionary corresponding to the 
    keys in the html file.
    """
    assert isinstance(html, str), "html file must be a string"
    assert isinstance(obj, dict), "obj must be a dictionary"
    template = env.get_template(html)
    return template.render(obj)