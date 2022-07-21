import os
import win32gui
import win32console
from win32com.shell import shell, shellcon

ventana = win32console.GetConsoleWindow()
win32gui.ShowWindow(ventana,0)

def main():

    os.chdir("C:/")

    ruta = (os.getcwd())

    ##print(ruta)

    ##print(os.listdir(os.getcwd()))

    os.system("del *.tmp /s /f /q")

    try:
        shell.SHEmptyRecycleBin (
			None,
			None,
			shellcon.SHERB_NOCONFIRMATION
			| shellcon.SHERB_NOPROGRESSUI
			| shellcon.SHERB_NOSOUND
			)
        
    except:
        pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo...")
        exit()