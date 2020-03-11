import PySimpleGUI as sg
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="mydbForm")
# print whether there is a connection
if (mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()

layout = [[sg.Text('Please enter your Name, Address, Phone')],
          [sg.Text('Name', size=(15, 1)), sg.InputText()],
          [sg.Text('Address', size=(15, 1)), sg.InputText()],
          [sg.Text('Phone', size=(15, 1)), sg.InputText()],
          [sg.Text('Slide side-by-side for your Age', size=(30, 1))],
          [sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
          [sg.Text('Enter any comments', size=(30, 1))],
          [sg.Multiline(default_text='This is the default Text.', size=(35, 3))],
          [sg.Submit(), sg.Cancel()]]

form = sg.Window('Simple data entry form').Layout(layout)  # begin with a blank form
button, values = form.Read()

nameIN = values[0]
addressIN = values[1]
phoneIN = values[2]
ageIN = values[3]
commentIN = values[4]
sqlform = "Insert into employee(name, address, phone, age, comment) values(%s, %s, %s, %s, %s)"
employees = [(nameIN, addressIN, phoneIN, ageIN, commentIN)]
mycursor.executemany(sqlform, employees)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
