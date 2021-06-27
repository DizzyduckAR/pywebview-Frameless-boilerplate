import webview
import webbrowser
import win32api
import pyautogui
import time
import sys

#WebView Start Settings
strattitle='Blank Frameless Window'
startlink='Html/Blank.html'
sizew=800
sizeh=600
#WebView Start Settings

#On UI Show. Auto stop On top after 3 secs from Ui show.
def on_shown():
    print('on shown')
    time.sleep(3)
    window.on_top = False
#allow to call your funcs with onclick="pywebview.api.Funcname()"  on your html.
class Api:

    #Resize Window
    def resizedrag(self):
        c = 1
        state_left = win32api.GetAsyncKeyState(0x01)
        beforex, beforey = pyautogui.position()
        beforex= str(beforex).rjust(4)
        beforey=str(beforey).rjust(4)
        # print(beforex,beforey)
        winWbefore=window.width
        winHbefore=window.height
        while True:
            a = win32api.GetAsyncKeyState(0x01) & 0x8000
            if a != state_left:
                state_left = a
                print(a)
                if a != 0:
                    print('Left Button Pressed')
                else:
                    print('Left Button Released')
                    break

                
            print("running")
            afterx, aftery = pyautogui.position()
            afterx= str(afterx).rjust(4)
            aftery=str(aftery).rjust(4)
            try:
                totalx=int(beforex)-int(afterx)
                totaly=int(beforey)-int(aftery)
                print('totals',totalx,totaly)
            except:
                print('fail')
            if totalx > 0:
                print('reduce x')
              #  print(totalx*-1)
                changerx=winWbefore+(totalx*-1)
            else:
                print('expend x')
                changerx=winWbefore+(totalx*-1)
               # print(totalx*-1)
            
            if totaly > 0:
                print('reduce y')
               # print(totaly*-1)
                changerY=winHbefore+(totaly*-1)
            else:
                print('expend y')
                #print(totalx*-1)
                changerY=winHbefore+(totaly*-1)
            #
            print('changed',changerx, changerY)
            window.resize(changerx, changerY)
            time.sleep(0.1)
        
    #Top Window Handlers
    def topbar(self,code):
        if code == "mini":
            window.minimize()
        if code == "full":
            window.toggle_fullscreen()
            window.move(0, 0)
        if code == "close":
            import sys
            window.destroy()
            sys.exit()

    #Link to Site Top window Handler
    def bottbar(self,code):
        if code == "website":
            webbrowser.open('http://botplace.hopto.org')

        if code == "discord":
            webbrowser.open('https://discord.gg/ggRCXS2')


DRAG_REGION_SELECTOR = '.pywebview-drag-region'


if __name__ == '__main__':

    api = Api()
    window = webview.create_window(strattitle,
                            startlink,on_top=True,
                            width=sizew, height=sizeh,
                            resizable=True,
                            frameless=True,js_api=api)
    window.shown += on_shown
    webview.start()
