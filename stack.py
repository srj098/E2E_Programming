import tkinter

stack = []
index = -1
lastPoppedElement = "NA"

window = tkinter.Tk()
window.title("Stack Demo")
window.geometry("400x400")

def getStackCount():
	global index
	return index+1

def textChanged(petb):
	text = petb.get()
	if(text != "") :
		pushButton['state'] = tkinter.NORMAL
	else :
		pushButton["state"] = tkinter.DISABLED

def sizeChanged(ss):
	size = getStackCount()
	if(size == 0 and popButton["state"] ==tkinter.NORMAL):
		popButton["state"]=tkinter.DISABLED
	else:
		popButton["state"]=tkinter.NORMAL

pe = tkinter.StringVar()
pe.set(lastPoppedElement)
ss = tkinter.StringVar()
ss.set(getStackCount())
petb = tkinter.StringVar()
petb.trace("w", lambda name, index, mode, petb=petb: textChanged(petb))
ss.trace("w", lambda name, index, mode, ss=ss: sizeChanged(ss))
sv = tkinter.StringVar()
sv.set(stack)

def push(element):
	global index
	stack.append(element)
	index = index+1

def pop():
	global index
	ret_val = stack.pop(index)
	index = index-1
	return ret_val


def pushButtonPressed():
	text = pushElementTextBox.get()
	pushElementTextBox.delete(0, tkinter.END)
	push(text)
	ss.set(getStackCount())
	sv.set(stack)

def popButtonPressed():
	global lastPoppedElement
	lastPoppedElement = pop()
	pe.set(lastPoppedElement)
	ss.set(getStackCount())
	sv.set(stack)


pushButtonLabel = tkinter.Label(window, text="Enter Element to Psuh: ")
pushButtonLabel.pack()

pushElementTextBox = tkinter.Entry(window, textvariable=petb)
pushElementTextBox.pack()

pushButton = tkinter.Button(window, text="PUSH", command=pushButtonPressed)
pushButton.pack()
pushButton["state"] = tkinter.DISABLED

popButton = tkinter.Button(window, text="POP", command=popButtonPressed)
popButton.pack()
popButton["state"] = tkinter.DISABLED

popElementLabel = tkinter.Label(window, text="Last Popped Element: ")
popElementLabel.pack()

popElementValueLabel = tkinter.Label(window, textvariable=pe)
popElementValueLabel.pack()

countLabel = tkinter.Label(window, text="Stack Size: ")
countLabel.pack()

countValueLabel = tkinter.Label(window, textvariable=ss)
countValueLabel.pack()

stackLabel = tkinter.Label(window, textvariable=sv)
stackLabel.pack()

window.mainloop()