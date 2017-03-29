import webapp2
from validation import Validate

form="""
<!DOCTYPE HTML>
<html>
<head>
	<title>User-Signup</title>
	<style type="text/css">
		.error {
		color:red;
		}
	</style>
</head>
<body>
	<h2>Signup</h2>
	<form method="post">
		<table>
			<tr>
				<td>Username</td>
				<td><input type="text" required name="username" value=%(username)s></td>
				<td><span class="error">%(username_error)s</span></td>
			</tr>
			<tr>
				<td>Password</td>
				<td><input type="password" name="password" required></td>
				<td><span class="error">%(password_error)s</span></td>
			</tr>
			<tr>
				<td>Verify Password</td>
				<td><input type="password" name="verify" required></td>
				<td><span class="error">%(verify_error)s</span></td>
			</tr>
			<tr>
				<td>Email (optional)</td>
				<td><input type="email" name="email" value=%(email)s></td>
				<td><span class="error"></span></td>
			</tr>
		</table>
		<p><input type="Submit" value="Submit" /></p>
</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
	def write_form(self, username="", username_error="", password_error="", verify_error="", email=""):
		self.response.write(form % {"username":username, "username_error":username_error, 
			"password_error":password_error, 
			"verify_error":verify_error,
			"email":email})
		
	def get(self):
		self.write_form()

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")

		user = Validate(username, password, verify, email)

		username_error = ""
		password_error =""
		verify_error =""
	

		if user.validate():
			self.redirect("/welcome?username={0}".format(username))
		else:
			if not user.username_val():
				username_error="That isn't a valid username."
			else:
				username_error = ""
			if not verify:
				verify_error="Please verify your password."""
			else:
				verify_error= ""
			if password and verify:
				if not user.equal():
					verify_error="Passwords do not match."					
				elif not user.password_val():
					password_error="That isn't a valid password."
				else:
					verify_error=""
					password_error=""
						

		
		self.write_form(username, username_error, password_error, verify_error, email)
			#username_error, password_error, verify_error, email_error


class WelcomeHandler(webapp2.RequestHandler):
	def get(self):
		username = self.request.get("username")
		content = "<h1>Welcome, " + username + "</h1>"
		self.response.write(content)

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/welcome', WelcomeHandler)
], debug=True)
