import cherrypy, random, string

from render_template import render_template

from post import post_index, create_post

reactions = {
    "shocked_pikachu_face" : "https://i.kym-cdn.com/entries/icons/original/000/027/475/Screen_Shot_2018-10-25_at_11.02.15_AM.png",
    "sad_cat": "https://i.kym-cdn.com/entries/icons/original/000/026/489/crying.jpg"
}


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return render_template("index.html", {
            "greet":"MAMA",
            "object":"AHA"
        })

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
        return render_template('befriend.html', {})

    @cherrypy.expose
    def nice_to_meet_you(self, name):
        if not name.isspace() and name != '':
            return f"<p style='color: rgb(10, 220, 40);'>Nice to meet you {name} , my name is CherryPy</p>"
        return self.sad()

    def sad(self):
        return f"<img src={reactions['sad_cat']} />"

    @cherrypy.expose
    def posts(self):
        return post_index()
    
    @cherrypy.expose
    def new_post(self, title, text, date):
        print(title, text, date)
        return create_post(title, text, date)

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())