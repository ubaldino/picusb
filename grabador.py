import wx , os , subprocess

BASE_DIR = os.path.dirname( __file__)





"""
print( "Ejecutando bootloader" )

salida = subprocess.call( [ BASE_DIR+"/hid_bootloaderp" , BASE_DIR+"/BLINK.hex" ] )
subprocess.check_output(["echo", "Hello World!"], universal_newlines=True)
'Hello World!\n'
"""

class Vista( wx.Frame ):
  
    def __init__(self, parent, title):
        super( Vista , self ).__init__( parent , title=title , size=(300, 200) )
        
        #self.Background( "#f13");    
        self.Centre()
        self.Show()

class Controlador(object):
	def __init__(self):
		vista = Vista( None , title='picusb' ) 
		modelo = Modelo()
		
class Modelo(object):
	def __init__(self ):
		self.list_pics = []
		

if __name__ == '__main__':
    app = wx.App()
    Controlador()
    app.MainLoop()
