
#Imports for Window Handler and Window API
####################################
# window resize calc libs
from ctypes import windll, Structure, c_long, byref

# App imports
from AppComponents.mr_importer import *

# App window info Object From main
from main import mywindow
####################################



# Window Resize classes and Functions
####################################
class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

def doresize(window):
    state_left =  windll.user32.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    winWbefore=window.width
    winHbefore=window.height

    mouseactive=queryMousePosition()
    beforex= mouseactive['x']
    beforey=mouseactive['y']
   
    while True:
        a =  windll.user32.GetKeyState(0x01)
        if a != state_left:  # Button state changed
            state_left = a
            print(a)
            if a < 0:
                print('Left Button Pressed')
                break
            else:
                print('Left Button Released')
                break

        mouseactive=queryMousePosition()
        afterx= mouseactive['x']
        aftery=mouseactive['y']
        try:
            totalx=int(beforex)-int(afterx)
            totaly=int(beforey)-int(aftery)
           
        except:
            print('fail')
        if totalx > 0:
            changerx=winWbefore+(totalx*-1)
        else:
         
            changerx=winWbefore+(totalx*-1)
          
        if totaly > 0:
            changerY=winHbefore+(totaly*-1)
        else:
            changerY=winHbefore+(totaly*-1)
    
        window.resize(changerx, changerY)

        time.sleep(0.01)

#Window Set size be %
def setsizer(window,perW,perH):
    user32 = windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    

    window.move(10,10)
    
    w= (w*(perW/100)) #resize to 80% of user screen W
    y= (h*(perH/100)) #resize to 80% of user screen H
    # print(w,y)
    window.resize(round(w), round(y))
####################################

# Event Triggers on window load/shown/close/closed ..
####################################
#On Load Events
def on_closed():
    print('pywebview window is closed')

def on_closing():
    print('pywebview window is closing')

def on_shown():
    print('pywebview window shown')

def on_minimized():
    print('pywebview window minimized')

def on_restored():
    print('pywebview window restored')

def on_maximized():
    print('pywebview window maximized')

def on_loaded():
    print('DOM is ready')
    #Cancel window on_Top 
    mywindow.targetwindow.on_top = False

    #Set Head
    dict = {'appname': mywindow.Appname,'appver': mywindow.AppVer,'applogo': mywindow.winlogo}
    jsrunner('wintophandlers','innerHTML',"=",htmlread('tophandlers.html').format(**dict),mywindow.targetwindow)

    #set bottom
    jsrunner('winbothandlers','innerHTML',"=",htmlread('bottomhandler.html'),mywindow.targetwindow)

    #set main
    jsrunner('allmain','innerHTML',"=",htmlread('wrap.html'),mywindow.targetwindow)


    # api.startappwindow()

    # unsubscribe event listener
    webview.windows[0].events.loaded -= on_loaded
####################################

def jsrunner(mainid='',doter='',typer="=",valuer='',window=''):
    try:
        dict = {'id': mainid,'doter': doter,'valuer': valuer}
        
        if typer == "=":
                testvar = '''document.getElementById('{id}').{doter} = `{valuer}` '''.format(**dict)
        if typer == ".":
                testvar = '''document.getElementById('{id}').{doter}{valuer} '''.format(**dict)
        
        window.evaluate_js(testvar)
    except:
        print('fail to write jsrunner')

def htmlread(filename):
    HTMLFile = open("AppComponents\\HtmlParticles\\"+filename, "r")
    return HTMLFile.read()

class Api ():

    #allow to reload home page with logo and app name
    def refreshhome(self):
        mywindow.targetwindow.events.loaded += on_loaded

    # Set window app icon and title
    def startappwindow(self):
        print('Start startappwindow',mywindow.Appname,mywindow.AppVer)
        #Set title
        jsrunner('titleappname','innerHTML',"=",mywindow.Appname+''' v'''+mywindow.AppVer,mywindow.targetwindow)
        #set LOGO
        jsrunner('titleapplogo','src',"=",mywindow.winlogo,mywindow.targetwindow)

    # Handle Window Resize
    def resizedrag(self):
        doresize(mywindow.targetwindow)  #utilcode/Frameless.py window is the target object window.

    #Top Window Handlers mini / full screen , Exit
    def topbar(self,code):
        
        if code == "mini":
            mywindow.targetwindow.minimize()
        if code == "full":
            mywindow.targetwindow.toggle_fullscreen()
            # self.targetwindow.move(0, 0)
        if code == "close":
            mywindow.targetwindow.destroy()
            sys.exit()
      
    #Link to Site Top window Handler
    def bottbar(self):
        print('page link')

    #set modal data
    def modaldata(self):
        datademo=''' 
        <div class='mt-2'> 
            <h2> Python modaldata Write demo inside mr_API.py def modaldata </h2>  
            <h3 class="p-1">You just got Luigi'd</h3> 
            <button
                @click="showModal = false"
                class="btn mt-6 bg-success font-medium text-white hover:bg-success-focus focus:bg-success-focus active:bg-success-focus/90">
                Close
            </button>
        </div> 
        '''

        jsrunner('modalbody','innerHTML',"=",datademo,mywindow.targetwindow)

    #set modal data
    def notidata(self):
        # Demo .format(**dict) to use python vars into HTML code. you can pass any data to any element
        #our demo image
        myimg='images/awards/award-1.svg'
        #img src to dict
        dict = {'myimg': myimg}  
        #dict usage with {myimg} to pass our var to html
        jsrunner('msgimg','innerHTML',"=",
                 ''' <img
                        class="rounded-full mt-3"
                        src="{myimg}"
                        alt="avatar"
                    /> 
                '''.format(**dict) ,mywindow.targetwindow)
        jsrunner('msghead','innerHTML',"=",''' <h2 class='pt-1'> Checking </h2> ''' ,mywindow.targetwindow)
        jsrunner('msgbody','innerHTML',"=",''' <h3 class='pt-1'> </h3>looking for stuff behind you ''' ,mywindow.targetwindow)
        time.sleep(2.5)
        jsrunner('msghead','innerHTML',"=",''' <h2 class='pt-1'> Done Checking!! </h2> ''' ,mywindow.targetwindow)
        jsrunner('msgbody','innerHTML',"=",''' <h3 class='pt-1'> Relex, it was just a gaint spider </h3> ''' ,mywindow.targetwindow)

    # lottie player Demo
    def lottiebtn(self):
        
        mydata='''
                <h2 class="text-center p-1"> lottiefiles  </h2> 
                <p></p>
                <lottie-player id="lopper" src="js/dabar.json"  background="transparent"  speed="1"  style="width: 90%; height: 90%;"  loop  autoplay>
                </lottie-player> 
                '''
        jsrunner('emptydata','innerHTML',"=",mydata ,mywindow.targetwindow)

    # Loading bar
    def loaderdemo(self):
        mydata='''
            <div class="text-center mt-4 gap-2 justify-center flex items-stretch py-2 pt-5" id="updatetext">
            <i>Checking</i>
            <i class="fa-brands fa-github"></i>
            <!-- <i class="fa-solid fa-dragon"></i> -->
            <i>For Client Update</i>
          </div>
         
          <div class="px-8 mt-4 pt-5 ">
            <div class="progress h-5 bg-slate-150 dark:bg-navy-500 ">
              <div
                class="is-active   overflow-hidden rounded-full bg-secondary " id="updatestatus" style="width: 0%"
              ></div>
            </div>
          </div>
        '''
        jsrunner('emptydata','innerHTML',"=",mydata ,mywindow.targetwindow)
        time.sleep(1)
        jsrunner('updatestatus','setAttribute',".",('style','width:25%'),mywindow.targetwindow)
        time.sleep(0.5)
        jsrunner('updatestatus','setAttribute',".",('style','width:66%'),mywindow.targetwindow)
        time.sleep(1)
        jsrunner('updatestatus','setAttribute',".",('style','width:100%'),mywindow.targetwindow)
        time.sleep(0.5)
        jsrunner('emptydata','innerHTML',"=",''' <h2 class="text-center"> All Done! </h2> ''' ,mywindow.targetwindow)
        time.sleep(1)
        api.emptydatareset()

    #Reset #emptydata
    def emptydatareset(self):
        jsrunner('emptydata','innerHTML',"=",'' ,mywindow.targetwindow)




# Condition for Build New window / API
if __name__ == '__main__' or __name__ == 'AppComponents.mr_API':
    #APi class in mr_API.py control window functions
    api = Api()
    targetwindow = webview.create_window(mywindow.Appname,
                            mywindow.HTMLPath,on_top=True,
                            width=mywindow.AppSizeW, height=mywindow.AppSizeH,
                            resizable=True,
                            frameless=True,js_api=api)
    
    #Set window handler into mywindow Object
    mywindow.targetwindow=targetwindow

    #Trigger Events Tester optional can comment out all 
    targetwindow.events.closed += on_closed
    targetwindow.events.closing += on_closing
    targetwindow.events.shown += on_shown
    targetwindow.events.loaded += on_loaded
    targetwindow.events.minimized += on_minimized
    targetwindow.events.maximized += on_maximized
    targetwindow.events.restored += on_restored

    # Window Start call. with Debug Server and User Agent
    webview.start(debug=mywindow.DebugUI, \
              http_server=False, user_agent=None)