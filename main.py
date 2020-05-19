import kivy.utils
import requests
import json
from kivy.clock import Clock
from kivy.app  import App 
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from birthdaybanner import BirthdayBanner 
from headerbanner import HeaderBanner 


class PreLoginScreen(Screen):
	def skip(self, dt):
		self.manager.current  = 'login_screen'

	def on_enter(self, *args):
		Clock.schedule_once(self.skip, 5)

class LoginScreen(Screen):
	pass

class HomeScreen(Screen):
	pass


GUI = Builder.load_file("main.kv")
class MainApp(App): 
	def build(self):
		return GUI

	def validate_user(self):

		user  = self.root.ids['login_screen'].ids['username_field']
		pwd   = self.root.ids['login_screen'].ids['pwd_field']
		info  = self.root.ids['login_screen'].ids['info']

		uname = (user.text).replace(" ", "")
		passw = (pwd.text).replace(" ", "")

		if uname == '' or passw == '':
			info.text = '[color=#FF0000]username and/ or password required[/color]'
		else:
			if uname == 'admin' and passw == 'admin':
				self.change_screen('home_screen')
			else:
				info.text = '[color=#FF0000]Invalid Username and/or Password[/color]'
		pass


	def change_screen(self, screen_name):
		# Get the screen manager from kv files
		screen_manager = self.root.ids['screen_manager']
		screen_manager.current = screen_name

	def on_start(self):
		# Get Google firebase data
		#####################################################################
		# Put your google firebase realtime database url
		url = "firebase_realtime_url" + "/.json"
		result = requests.get(url)
		######################################################################
		print("Okay?", result.ok)
		data = json.loads(result.content.decode())
		keys = list(data.keys())

		header_grid = self.root.ids['home_screen'].ids['header_grid']
		H = HeaderBanner(header="Birthdays")
		header_grid.add_widget(H)

		banner_grid = self.root.ids['home_screen'].ids['banner_grid']
		for key in keys:
			B = BirthdayBanner(name = '{0} {1}'.format(data[key]['firstName'],data[key]['lastName']),
							   birthdate = '{0}/{1}/{2}'.format(data[key]['birthMonth'],data[key]['birthDay'],data[key]['birthYear']))
			banner_grid.add_widget(B)


MainApp().run()
