import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

ref = {'01': 'January', '02': 'February', '03': 'March',
       '04': 'April', '05': 'May', '06': 'June',
       '07': 'July', '08': 'August', '09': 'September',
       '10': 'October', '11': 'November', '12': 'December'}

file = open('scientists.json', 'r')
data = json.load(file)
months = list()
for i in data.values():
    months.append(ref[i[:2]])

new = dict()
for month in ref.values():
    new[month] = 0
for month, count in Counter(months).items():
    new[month] = count

output_file("scientists.html")

x = [month for month in new.keys()]
y = [count for count in new.values()]

p = figure(x_range=x)
p.vbar(x=x, top=y, width=0.5, color='pink') # Create a histogram
show(p)
