import webbrowser
import datetime

mydate = datetime.datetime.now()
mydate = mydate.strftime('%d%m%Y')

try:
    file = open('Udemy-PolskieKursy ' + mydate + '.txt')
    for i in file:
        webbrowser.open(i, new=2)
except ValueError:
    print('Błąd %s' % ValueError)


