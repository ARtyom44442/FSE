text = 'Падал (куда он там падал) прошлогодний (значит очень старый) снег (а почему не дождь) () (()).'
print(text)

for i in text:
    position1 = text.rfind('(')
    position2 = text.rfind(')')
    text = text.replace(text[position1:position2 + 1], '')

print(text)
