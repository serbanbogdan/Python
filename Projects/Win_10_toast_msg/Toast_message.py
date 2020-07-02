from win10toast import ToastNotifier

title = input('Enter Title here! ')
message = input('Enter Message here! ')

toaster = ToastNotifier()
toaster.show_toast(title, message, duration=30)