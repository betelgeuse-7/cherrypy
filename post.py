import cherrypy
from render_template import render_template

from db import DBConnection

con = DBConnection('db.sqlite3')

def post_index():
    post_qs = con.fetch_all('posts')
    all_posts = []
    for p in post_qs:
        all_posts.append(post_objectifier(p))
        
    return render_template("posts.html", {
        "posts":all_posts
    })

def create_post(title, text, date):
    print(title, text, date)
    con.cursor.execute("INSERT INTO posts VALUES (?, ?, ?);", (title, text, date))
    raise cherrypy.HTTPRedirect('/posts')
    

#returning a post tuple to a post dict
# t = Tuple of a post
def post_objectifier(t):
    return {
        "title":t[0],
        "text":t[1],
        "date":t[2]
    }