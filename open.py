import webbrowser

file = open('Udemy-PolskieKursy 08102021.txt')

for i in file:
    webbrowser.open(i, new=2)