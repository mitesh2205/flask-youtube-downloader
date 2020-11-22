from flask import Flask , url_for , redirect , render_template , request , flash
import pytube
from flask import send_file
import os
app = Flask(__name__)
app.secret_key = "mitesh"
# global title
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download',methods=["POST" , "GET"])
def download():
    SAVE_PATH = 'BMADE-Youtube Video/'
    url = request.form["yt_url"]
    youtube = pytube.YouTube(url)
    global title
    title = youtube.title
    video = youtube.streams.first()
    video.download(SAVE_PATH)
    flash("Video is available, Enter other link to download other video.")
    # flash(SAVE_PATH)
    return render_template("index.html", path = SAVE_PATH + title+".mp4" , title = title+".mp4")

@app.route('/downloadfile')
def downloadFile ():

    paths = "BMADE-Youtube Video/"
    return send_file(os.path.join(paths, title +".mp4"), as_attachment=True)

if __name__ == '__main__':
    app.run( debug = True )
