from flask import Flask , url_for , redirect , render_template , request , flash
import pytube
import os
app = Flask(__name__)
app.secret_key = "mitesh"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/download',methods=["POST" , "GET"])
def download():
    SAVE_PATH = 'C:' + '/BMADE-Youtube Video'
    url = request.form["yt_url"]
    youtube = pytube.YouTube(url)
    video = youtube.streams.first()
    video.download(SAVE_PATH)
    flash("Your video is downloaded successfully at "+ SAVE_PATH +", Enter other link below to download video.")
    # flash(SAVE_PATH)
    return render_template("index.html")

if __name__ == '__main__':
    app.run( debug = True )
