from guizero import App, PushButton, Text, TextBox, Window, TitleBox, Box, Picture, Waffle
import time, random
app = App()
count = 3
all_times_list = []
i = 0
start = 0

def open_window():
    global i, start, count, all_times_list




    def light():
        global i, start
        waffle[i, 0].color = "red"
        play_button = Picture(play_button_box, image="Reaction_game_button.png", width = 200, height = 200)
        i += 1
        if i < 3:
            app.after(1000, light)
        else:
            start = time.time()
            timer()

    def timer():
        global start
        if start == 0:
            text_2 = Text(app, text="False start", align="bottom")
            text_2.text_size=20
        else:
            end = time.time()
            reaction_time = end - start
            text_2 = Text(app, text=reaction_time, align="bottom")
            text_2.text_size=20

"""""
    def clicked():
        global count

        if count == 0:
            second_window()
        else:
            play_button.image = "Final_game_button.png"
            app.update()
            beg = 1
            end = 4
            wait_time = random.randint(beg, end)
            time.sleep(wait_time)
            play_button.image = "Reaction_game_button.png"
            start = time.time()
            app.update()
            count -= 1
            end = time.time()
            final_time = end - start
            rounded_time = round(final_time, 1)
            #final_time_text = Text(current_time_box, text= rounded_time)
            #app.update()
"""
    side1_box = Box(app, width= 20, height = "fill", align = "right", border = False)
    side2_box = Box(app, width= 20, height = "fill", align = "left", border = False)
    top_spacer = Box(app, width= "fill", height = 20, align = "top", border = False)
    title_box = Box(app, width= 400, height= 80, align= "top", border= False)
    top_spacer2 = Box(app,  width= "fill", height = 10, align = "top", border = False)
    info_box = Box(app, width= 450, height= 100, align= "top", border= False)
    top_spacer3 = Box(app, width= "fill", height = 15, align = "top", border = False)
    middle_box = Box(app, width= "fill", height= 70, align= "top", border= False)
    top_spacer4 = Box(middle_box, width= 200, height = 40, align = "top", border = False)
    top_spacer5 = Box(middle_box, width= 200, height = 500, align = "top", border = True)
    center_box = Box(app, width= "fill", height = 200, align = "top", border = False)
    current_time_box = Box(center_box, width= 100, height = 40, align = "left", border = False)
    average_time_box = Box(center_box, width= 100, height = 40, align = "right", border = False)
    average_time_box.bg = "#f2e4d9"
    play_button_box = Box(center_box, width= 200, height = 200, align = "top", border = False)
    bottom_spacer = Box(app,  width= "fill", height = 30, align = "top", border = False)
    leaderboard_button = Box(app, width= 220, height = 50, align = "top", border = False)
    title = Picture(title_box, image = "Main title.png", width = 420, height = 80)
    information = Picture(info_box, image = "Main_text.png", width = 450, height = 100)
    small_title = Picture (top_spacer4, image = "Small_tittle.png", width = 150, height = 60)
    play_button = Picture(play_button_box, image="Reaction_game_button.png", width = 200, height = 200)
    #leaderboard = Picture(leaderboard_button, image="Leaderboard_button.png", width = 160, height = 60, align= "bottom")
    leaderboard = Pushbutton(leaderboard_button, text="STOP", command= timer)
    lights = Waffle(top_spacer5, width=3, height=1, dotty=True)
    #start_button = Pushbutton(current_time_box, text="START", command= light)

    leaderboard.when_clicked = light
    play_button.when_clicked = light





"""""
    leaderboard = PushButton(app, image="Leaderboard_button.png", width = 150, height = 50, align= "bottom")
    leaderboard.bg = "#f2e4d9"
    space_3 = Text(box, text="hello", align="right")
    space_4 = Text(box, text="hello", align="right")
    average_time = Text(box, text = "average time", size = 14, align = "right")
    average_time.bg = "#f2e4d9"
"""""


def second_window():
    window = Window(app, title ="Second Window", height=600, width=600)
    window.bg = "#205a60"
    window.show(wait=True)
    app.hide()
    side3_box = Box(app, width= 60, height = "fill", align = "right", border = True)
    side4_box = Box(app, width= 60, height = "fill", align = "left", border = True)
    top_spacer = Box(app, width= "fill", height = 20, align = "top", border = True)


app = App(title= "Main window", height=600, width=600)
app.bg = "#205a60"

#original_pic()
open_window()
app.display()
