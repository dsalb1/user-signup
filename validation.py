import re

class Validate:
	def __init__(self, username=None, password=None, ver_password=None, email=None):
		self.username = username
		self.password = password
		self.ver_password = ver_password
		self.email = email

	def username_val(self):
		USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
		return USER_RE.match(self.username)

	def password_val(self):
		PASS_RE = re.compile(r"^.{3,20}$")
		return PASS_RE.match(self.password)

	def equal(self):
		valid = False
		if self.password == self.ver_password:
			valid = True
		return valid

	def email_val(self):
		if self.email:
			 EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
			 return EMAIL_RE
		else:
			return True
		
	def validate(self):
		if self.username_val() and self.password_val() and self.equal() and self.email_val():
			return True
