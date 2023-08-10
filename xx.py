from flask import Flask, render_template, request
from pytube import YouTube
import mahdix
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    modified_text = ""
    if request.method == 'POST':
        mahdi_get_url = request.form['mahdi_TY_url']
        try:
            openlink=YouTube(mahdi_get_url)
            video_title = openlink.title
            action = request.form['action']
            if action == 'video':
                stream = openlink.streams.get_highest_resolution()
                #video_filename = stream.default_filename
                stream.download()
                filename=f'Title : {video_title}'
                sucesstxt=f'Downloaded: {video_title}'
                return render_template('tub.html', titel=filename,modified_text=sucesstxt)
            if action == 'mp3':
                video=openlink.streams.filter(only_audio=True)
                liv=list(enumerate(video))
                for i in liv:
                    reju=i
                filename=f'Title : {video_title}'
                video[2].download()
                sucesstxt=f'Downloaded: {video_title}'
                return render_template('tub.html', titel=filename,modified_text=sucesstxt)
        except Exception as e:
            message = 'Error: ' + str(e)
            return render_template('tub.html', titel='Error',modified_text=message)

    return render_template('tub.html')

if __name__ == '__main__':
    app.run(debug=True)




# THis is a python project Dawnload YouTUb video in python flask .....also use HTML && JS