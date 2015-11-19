import pythoncom, pyHook

mospos = None

def OnMouseEvent(event):
    print event.Position,
    mospos = event.Position
    return True

hm = pyHook.HookManager()
hm.MouseAll = OnMouseEvent
hm.HookMouse()
pythoncom.PumpMessages()
