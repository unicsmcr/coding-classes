def login():
	import spotipy 
	import spotipy.util as util
	token = util.prompt_for_user_token('Python Classes','user-library-read',
			    client_id='76b2fa9353c84080a56db4ab3857503b',
			    client_secret='5b99dc662e3f47b188ea08bdf706669a',
			    redirect_uri='http://localhost/')

	return spotipy.Spotify(auth=token)

def show_picture(url):
	from PIL import Image
	import requests
	from io import BytesIO
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))
	img.show()
	return

