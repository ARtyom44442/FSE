import string
password = input("Введите пароль: ")
errors = []
if len(password) != 8:
    errors.append("Длина пароля не равна 8")
if not any(symbol.isupper() for symbol in password):
    errors.append("В пароле отсутствуют заглавные буквы")
if not any(symbol.islower() for symbol in password):
    errors.append("В пароле отсутствуют строчные буквы")
if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")
if not any(symbol in '*-#' for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")
allowed = string.ascii_letters + string.digits + '*-#'
if not all(symbol in allowed for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")
if not errors:
    print("Надежный пароль")
else:
    print("\n".join(errors))
