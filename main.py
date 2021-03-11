from website import create_app
import os
import pywintypes
from win10toast import ToastNotifier

toast = ToastNotifier()


os.chdir(r"E:\Coding\python\website")

app = create_app()

if __name__ == '__main__':
    toast.show_toast("Notes Website", "Website Started", duration=10)
    app.run(host='192.168.0.67', port=80)  #If debug on the page will update to code changes live
    #app.run(debug=True)
    
    

    
