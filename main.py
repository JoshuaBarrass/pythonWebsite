from website import create_app
import os
import pywintypes
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("Notes Website", "Website Started",duration=10)

os.chdir(r"E:\Coding\python\website")

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)  #If debug on the page will update to code changes live

    
