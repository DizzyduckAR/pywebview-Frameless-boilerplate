from AppComponents.mr_logger import logger
# html dom writer with window handler

def jsrunner(mainid='',doter='',typer="=",valuer='',targetwindow=''):
    print('start js',)
    targetwindow.get_elements('#titleappname')
    # try:
    #     #add imports from list and Error out to log if fail
    #     print('my type',typer)
    #     dict = {'id': mainid,'doter': doter,'valuer': valuer}
    #     print(dict,window,typer)
        
    #     if typer == "=":
    #             testvar = '''document.getElementById('{id}').{doter} = `{valuer}` '''.format(**dict)
    #     if typer == ".":
    #             testvar = '''document.getElementById('{id}').{doter}{valuer} '''.format(**dict)
        
    #     window.evaluate_js(testvar)
    # except Exception as e:
    #     logger.error(e)
    