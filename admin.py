from flask.ext.admin import Admin, BaseView, expose


class AdminPanel(BaseView):

	@expose('/')
	def admin_index(self):
		return self.render('admin.html')