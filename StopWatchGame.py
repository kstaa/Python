# Project for "Stopwatch: The Game"

import simplegui

# define global variables
current_time = 0
wins = 0
attempts = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = str(t/600)
    b = str((t%600)/100)
    c = str((t%100)/10)
    d = str(t%10)
     
    return a + ":" + b + c + "." + d
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    #global running
    timer.start()
    
    
def stop():
    global wins, attempts, running
    if running == True:
        attempts = attempts + 1
        if current_time % 10 == 0:
            wins = wins + 1
    timer.stop()
    running = False
    
def reset():
    global current_time, wins, attempts
    current_time = 0
    wins = 0
    attempts = 0
    timer.stop()
    

# define event handler for timer with 0.1 sec interval
def game_timer():
    global current_time, running
    if current_time < 6000:
        current_time = current_time + 1
        running = True
    else:
        running = False
        reset()


# define draw handler
def draw(canvas):
    canvas.draw_text(format(current_time), [100, 150], 40, "White")
    canvas.draw_text(str(wins) + "/" + str(attempts), [250, 30], 25, "Green")    

    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)


# register event handlers
timer = simplegui.create_timer(100, game_timer)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# start frame
frame.start()


