#this script automaticly add 15% to a bill


import PySimpleGUI as sg

layout = [[sg.Text("what is the bill amount")], [sg.Input()],
          [sg.Text("what % of tip do you want to add to your bill")],
          [sg.Button('5%'), sg.Button('10%')],
          [sg.Button('15%'), sg.Button('20%')],
          [sg.Button('quit')]]

window = sg.Window('Tip Calculator', layout)

while True:
    event, values =window.read()
    print(event, values)
    if event in ('quit'):
        break
    if event in ('5%'):
        values['-INPUT-'] * 1.5
    if event in ('10%'):
        break
    if event in ('15%'):
        break
    if event in ('20%'):
        break
window.close()




#bill_total = input('what was the total of the bill?:')

#total_tip = (int(bill_total) * 1.15)

#print(total_tip)