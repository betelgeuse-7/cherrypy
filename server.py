import cherrypy, random, string
from cherrypy._cprequest import Request
from auth import is_authenticated
import os.path
from render_template import render_template
from db import DBConnection
import bcrypt

reactions = {
    "shocked_pikachu_face" : "https://i.kym-cdn.com/entries/icons/original/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.png",
    "sad_cat": "https://i.kym-cdn.com/entries/icons/original/000/026/489/crying.jpg"
}


current_dir = os.path.dirname(os.path.abspath(__file__))
db = DBConnection()

class CherryPostApp(object):
    @cherrypy.expose
    def index(self):
        return render_template("index.html")

    @cherrypy.expose
    def generate(self, length=8):
        output = ""
        for i in range(int(length)):
            output += random.choice(string.ascii_letters)
        return render_template('generate.html', {
            "output":output,
            "length":length
        })
    @cherrypy.expose
    def befriend(self):
        return render_template('befriend.html')

    @cherrypy.expose
    def nice_to_meet_you(self, name):
        if not name.isspace() and name != '':
            return f"<p style='color: rgb(10, 220, 40);'>Nice to meet you {name.strip()} , my name is CherryPy</p>"
        return self.sad()

    def sad(self):
        return f"<img src={reactions['sad_cat']} />"

    @cherrypy.expose
    def posts(self):
        try:
            if is_authenticated(Request):
                db.cursor.execute("select p.title, p.content, u.username from posts p inner join users u on p.author = u.user_id")
                posts = db.cursor.fetchall()
                context = {
                    "posts": posts
                }
                return render_template("posts.html", context)
            else:
                return f"<p>Not authenticated</p>"
        except Exception as e:
            return f"<p>{e}</p>"

    """
    @cherrypy.expose
    def posts(self):
        db.cursor.execute("SELECT * FROM posts")
        context = {
            "posts": db.cursor.fetchall()
        }
        return render_template('posts.html', context)
    
    @cherrypy.expose
    def register(self, username=None, password=None, password2=None):
        #TODO form validation middleware.
        if username and password and password2 and not username.isspace() and not password.isspace() and not password2.isspace():
            if password == password2:
                hashed_pwd = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
                db.cursor.execute("INSERT INTO users VALUES(?, ?)", (username, hashed_pwd))
                db.con.commit()
                return render_template('login.html', {"msg":f"Successfully registered. You can now log in as {username}."})
            else:
                return render_template('register.html', {
                    "err":"Passwords do not match."
                })
        return render_template('register.html')
    
    @cherrypy.expose
    def login(self, username=None, password=None):
            #Auth middleware here. TODO
        return render_template('login.html')
    
    @cherrypy.expose
    def new_post(self, title=None, text=None, author=None):
        if title and text and author:
            try:
                db.cursor.execute("INSERT INTO posts VALUES (?, ?, ?)", (title, text, author))
                db.con.commit
                return self.posts()
            except Exception as e:
                print(e)
                return render_template("new_post.html", {
                    "err": "An error occured. Try again",
                    "pic": reactions["shocked_pikachu_face"]
                })
        return render_template("new_post.html")


"""

if __name__ == '__main__':
    cherrypy.quickstart(CherryPostApp(), config = {
        '/static': {
            "tools.staticdir.on":True,
            "tools.staticdir.dir":f"{current_dir}/static/"
        },
    })