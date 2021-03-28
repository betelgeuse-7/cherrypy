import cherrypy, random, string
import os.path
from render_template import render_template
from db import DBConnection
import bcrypt

reactions = {
    #"shocked_pikachu_face" : "https://i.kym-cdn.com/entries/icons/original/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.png",
    "sad_cat": "https://i.kym-cdn.com/entries/icons/original/000/026/489/crying.jpg"
}


current_dir = os.path.dirname(os.path.abspath(__file__))
db = DBConnection('cherryDb.sqlite3')

class HelloWorld(object):
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
        context = {
            "posts": db.select_all('posts')
        }
        return render_template('posts.html', context)
    
    @cherrypy.expose
    def register(self, username=None, password=None, password2=None):
        if not username.isspace() and not password.isspace() and not password2.isspace():
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
        """
            Auth middleware here. TODO
        """
        return render_template('login.html')




if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld(), config= {
        '/static': {
            "tools.staticdir.on":True,
            "tools.staticdir.dir":f"{current_dir}/static/"
        }
    })