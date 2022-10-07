import tkinter as tk

root = tk.Tk()
root.attributes("-topmost", True)
root.geometry('200x100')
root.title('FunStrech')

timerLabel = tk.Label(text='30', font=('Arial', 80))
timerLabel.pack()

BASE_EXERCICE_TIME = 60
BASE_PAUSE_TIME = 15

global exerciceTime, pauseTime, isPausedTime
exerciceTime = BASE_EXERCICE_TIME
pauseTime = BASE_PAUSE_TIME
isPausedTime = False

def update():
    global exerciceTime, pauseTime, isPausedTime
    timeToDisplay = 0
    if isPausedTime:
        root.config(bg="#f00")
        pauseTime -= 1
        timeToDisplay = pauseTime
    else:
        root.config(bg="#0f0")
        exerciceTime -= 1
        timeToDisplay = exerciceTime

    if timeToDisplay == 0:
        isPausedTime = not isPausedTime
        exerciceTime = BASE_EXERCICE_TIME
        pauseTime = BASE_PAUSE_TIME

    timerLabel.config(text=timeToDisplay)
    timerLabel.after(1000, update)

update()
root.mainloop()
