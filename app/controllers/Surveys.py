from system.core.controller import *
class Surveys(Controller):
	def __init__(self, action):
		super(Surveys, self).__init__(action)
		
		self.load_model('WelcomeModel')
		self.db = self._app.db
	
		
	def index(self):
		count = 0
		session['count'] = count
		return self.load_view('index.html')
		
	def process(self):
		session['count'] = int(session['count']) + 1
		session['form_info'] = request.form['name']
		session['city'] = request.form['test2']
		session['lang'] = request.form['muhName']
		session['comment'] = request.form['comment']
		print session['form_info']
		print session['city']
		print session['lang']
		return redirect('/result')
		
	def result(self):
		return self.load_view('Results.html',name = session['form_info'], location = session['city'],lang = session['lang'],comment = session['comment'], x = session['count'])
	
	def returnTo(self):
		return redirect('/survey/process')