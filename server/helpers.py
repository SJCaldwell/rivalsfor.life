import string

def pounds_to_kilos(pounds):
	return pounds/2.1

def kilos_to_pounds(kilos):
	return kilos * 2.1

def meets_password_complexity_requirements(password):
	has_num = False
	for char in password:
		if char.isdigit():
			has_num = True
	has_special = False
	for char in password:
		if char in string.punctuation:
			has_special = True
	if has_num and has_special and len(password) >= 8:
		return True
	else:
		return False