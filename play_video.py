from IPython.display import HTML
from base64 import b64encode

def play_video(vido_file):
    mp4 = open(vido_file, 'rb').read()
    data_url = 'data:video/mp4;base64,' + b64encode(mp4).decode()
    HTML(f"""
    <video width="80%" height="80%" controls>
          <source src="{data_url}" type="video/mp4">
    </video>""")