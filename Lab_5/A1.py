text = 'Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (()).'
print(text)

for i in text:
    position1 = text.find('(')
    position2 = text.find(')')
    text = text.replace(text[position1:position2 + 1], '')
    text = text.replace("  ", " ") and text.replace(" .", ".")


print(text)
