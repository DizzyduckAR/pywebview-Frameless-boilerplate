
### PyWebView Clean Frameless Boiler
### Main Start File. ctrl+Left Mouse click (VS Code) to follow into the Class/Function


#App Components [

## Import libs from list (you must install the libs first on local env with PIP before import calls)
####################################
from AppComponents.mr_importer import *
####################################

## Window Object Class
####################################
from AppComponents.mr_windowinfo import windowinfo
#app vars
DebugUI=False  # True/False
Appname='MyAppName'   # Will be copied to the window Title
AppVer="1.0.0"  # also copied to the window title
HTMLPath='UI/index.html'  # local or online Path for the web
AppSizeW=1000    # W size
AppSizeH=860    # H size
winlogo= 'images/favicon.png'

# class init into mywindow as object with Appname AppVer targetwindow ...
mywindow= windowinfo(Appname,AppVer,'targetwindow will self write from mywindow.targetwindow=targetwindow',DebugUI,HTMLPath,AppSizeW,AppSizeH,winlogo)
####################################

## App python to js and js to python API will also start the UI
####################################
import AppComponents.mr_API 
####################################

    
# ] End App Components