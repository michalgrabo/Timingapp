from guizero import App, PushButton, Text, TextBox, Window, TitleBox, Box, Picture, Waffle, Slider
import time, pickle
count = 2
i = 0
start = 0
all_time_list = []
all_names_list = []
all_age_list = []
all_average_list = []
window = None
window2 = None
window4 = None
requested_age = 0
times_and_age_reconstructed = []
final_participant_age = 0
wrong = 0
average_times = 0



def save(filename):
    global all_age_list,all_average_list,times_and_age_reconstructed
    print(all_age_list, all_average_list)
    name_and_time_list = all_age_list + all_average_list + times_and_age_reconstructed
    with open(filename, "wb") as outfile:
        pickle.dump(name_and_time_list, outfile)
        #outfile.close()

"""
    with open("time.pickle", "rb") as infile:
        times_reconstructed = pickle.load(infile)
"""

def loading(filename):
    global times_and_age_reconstructed
    with open(filename, "rb") as infile:
        times_and_age_reconstructed = pickle.load(infile)
        #infile.close()
    print(times_and_age_reconstructed)

"""""
def save2():
    with open("name.pickle", "wb") as outfile:
        pickle.dump(all_names_list, outfile)

    with open("name.pickle", "rb") as infile:
        names_reconstructed = pickle.load(infile)
"""
"""""
def save3():
    global all_age_list, age_reconstructed
    print(all_age_list)
    with open("age.pickle", "wb") as outfile:
        pickle.dump(all_age_list, outfile)

    with open("age.pickle", "rb") as infile:
        age_reconstructed = pickle.load(infile)
    print(age_reconstructed)
"""""

def open_window():
    global count

    def game():

        global count, end, i, start, window, all_time_list
        loading("pickleforstorage")
        window = Window(app, title ="Game window", height=600, width=600)
        window.bg = "#205a60"
        window.show(wait=True)
        app.hide()
        #side3_box = Box(app, width= 60, height = "fill", align = "right", border = True)
        #side4_box = Box(app, width= 60, height = "fill", align = "left", border = True)
        top_spacer = Box(window, width= "fill", height = 200, align = "top", border = False)
        bottom_space = Box(window, width= "fill", height = 30, align = "bottom", border = False)
        current_time = Box(window, width= 200, height = 50, align = "bottom", border = False)
        current_time.bg = "#f2e4d9"
        info_time = Box(window, width= 200, height = 30, align = "bottom", border = False)
        info_time.bg = "#f2e4d9"
        text_1 = Text(info_time, text="Your times: ", align="bottom", size=12)


        def light():
            global i, start

            if i < 3:
                waffle[i, 0].color = "red"
                app.after(1000, light)
            else:
                waffle[0, 0].color = "green"
                waffle[1, 0].color = "green"
                waffle[2, 0].color = "green"
                start = time.time()
            i += 1
        def timer():
            global start, all_time_list

            if start == 0:
                #text_2 = Text(window, text="False start", align="bottom")
                false_start()
            else:
                end = time.time()
                reaction_time = round(end - start, 2)
                all_time_list.append(reaction_time)
                text_2 = Text(current_time, text=  str(reaction_time) , align="bottom", size = 12)
                print(all_time_list)
                resetgame()

        def resetgame():
            global start, i, count
            if count == 0:
                waffle[0, 0].color = "white"
                waffle[1, 0].color = "white"
                waffle[2, 0].color = "white"
                time.sleep(1)
                login_window()
            else:
                count -= 1
                i = 0
                start = 0
                waffle[0, 0].color = "white"
                waffle[1, 0].color = "white"
                waffle[2, 0].color = "white"
                time.sleep(2)
                window.after(1000, light)


        waffle = Waffle(window, width=3, height=1, dotty=True, dim = 50)
        open_button = PushButton(window, text="STOP", command= timer, width= 10, height= 5)
        window.after(1000, light)

        """""
        if count == 0:
            second_window()
        else:
            start = time.time()
            print("HI")
            play_button.image = "Final_game_button.png"
            app.update()
            beg = 1
            end = 4
            wait_time = random.randint(beg, end)
            time.sleep(wait_time)
            print("hello")
            play_button.image = "Reaction_game_button.png"
            def final():
                end = time.time()
                app.update()
                count -= 1
                end = time.time()
                final_time = end - start
                rounded_time = round(final_time, 1)
                final_time_text = Text(current_time_box, text= rounded_time)
                app.update()
            play_button.when_clicked = final
        """
    def analyse():
        global window3
        window3 = Window(app, title ="Analysis window", height=600, width=600)
        loading("pickleforstorage")
        window3.bg = "#205a60"
        window3.show(wait=True)
        app.hide()
        top_space = Box(window3, width= "fill", height = 20, align = "top", border = False)
        side1_box2 = Box(window3, width= 10, height = "fill", align = "right", border = False)
        side2_box2 = Box(window3, width= 100, height = "fill", align = "right", border = False)
        side3_box2 = Box(window3, width= 20, height = "fill", align = "left", border = False)
        top_spacer2 = Box(window3, width= "fill", height = 20, align = "top", border = False)
        tittle2_box = Box(window3, width= 400, height= 80, align= "top", border= False)
        tittle3 = Text(tittle2_box, text = "Analysis", align="left", size = 30, color = "#f2e4d9")
        top_spacer3 = Box(window3, width= "fill", height = 20, align = "top", border = False)
        age_group_tittle = Box(window3, width= "fill", height = 40, align = "top", border = False)
        top_spacer7 = Box(window3, width= "fill", height = 20, align = "top", border = False)
        age_group_box = Box(window3, width= "fill", height = 40, align = "top", border = False)
        age_group = Text(age_group_tittle, text = "Enter age group: ", align="left", size = 20, color = "#f2e4d9")
        bakcbutton = PushButton(side2_box2, text="Back", align = "top", command = destruction3, width= 4, height= 2)

        def textbox_changed():
                global requested_age
                requested_age = age_group_text_box.value

        def calculation():
            global requested_age,times_and_age_reconstructed
            print(requested_age,times_and_age_reconstructed)

            def all_indexes_list(list_of_interest, obj):
                for index, elem in enumerate(list_of_interest):
                    if elem == obj:
                        yield index

            final_index = all_indexes_list(times_and_age_reconstructed, float(requested_age))
            all_final_index = list(final_index)
            print(all_final_index)
            analyse_times = []
            for i in range(len(all_final_index)):
                final_pos = all_final_index[i] +1
                analyse_times.append(times_and_age_reconstructed[final_pos])
            print(list(analyse_times))

            fastest_times_per_age = min(analyse_times)
            slowest_times_per_age = max(analyse_times)
            lenght = len(analyse_times)
            average_times_per_age = round(sum(analyse_times)/ lenght,2)
            fast = Text(fastesttime, text = str(fastest_times_per_age), align="left", size = 20, color = "#f2e4d9")
            slow = Text(slowesttime, text = str(slowest_times_per_age), align="left", size = 20, color = "#f2e4d9")
            avg = Text(averagetime, text = str(average_times_per_age), align="left", size = 20, color = "#f2e4d9")


        age_group_text_box = TextBox(age_group_box, command= textbox_changed, align="left")
        fastesttime = Box(window3, width= "fill", height= 50, align= "top", border= False)
        top_spacer4 = Box(window3, width= "fill", height = 20, align = "top", border = False)
        slowesttime = Box(window3, width= "fill", height= 50, align= "top", border= False)
        top_spacer5 = Box(window3, width= "fill", height = 20, align = "top", border = False)
        averagetime = Box(window3, width= "fill", height= 50, align= "top", border= False)
        top_spacer6 = Box(window3, width= "fill", height = 20, align = "top", border = False)
        fast = Text(fastesttime, text = "Fastest time for age group:" , align="left", size = 20, color = "#f2e4d9")
        slow = Text(slowesttime, text = "Slowest time for age group: " , align="left", size = 20, color = "#f2e4d9")
        avg = Text(averagetime, text = "Average time for age group:" , align="left", size = 20, color = "#f2e4d9")
        continuebutton = PushButton(window3, text="Load", command = calculation, width= 4, height= 2)


        """
        all_indexes = []
        for i in range(len(times_and_age_reconstructed)):
            if times_and_age_reconstructed[i] == int(requested_age):
                all_indexes.append(requested_age)
                i += 1
            else:
                i += 1
        analyse_times = []
        for i in range(len(all_indexes)):
            final_pos = int(all_indexes[i]) -1
            analyse_times.append(times_and_age_reconstructed[final_pos])
        """
    #Following function code was sorced from https://www.codingem.com/index-of-in-python/#:~:text=To%20find%20the%20index%20of%20a%20list%20element%20in%20Python,built%2Din%20index()%20method.&text=To%20find%20the%20index%20of%20a%20character%20in%20a%20string,()%20method%20on%20the%20string.&text=This%20is%20the%20quick%20answer.








    side1_box = Box(app, width= 20, height="fill", align = "right", border = False)
    side2_box = Box(app, width= 20, height="fill", align = "left", border = False)
    top_spacer = Box(app, width= "fill", height = 20, align = "top", border = False)
    title_box = Box(app, width= 400, height= 80, align= "top", border= False)
    top_spacer2 = Box(app,  width= "fill", height = 20, align = "top", border = False)
    info_box = Box(app, width= 450, height= 100, align= "top", border= False)
    top_spacer3 = Box(app, width= "fill", height = 30, align = "top", border = False)
    middle_box = Box(app, width= "fill", height= 70, align= "top", border= False)
    top_spacer4 = Box(middle_box, width= 200, height = 40, align = "top", border = False)
    center_box = Box(app, width= "fill", height = 200, align = "top", border = False)
    current_time_box = Box(center_box, width= 100, height = 40, align = "left", border = False)
    current_time_box.bg = "#f2e4d9"
    average_time_box = Box(center_box, width= 100, height = 40, align = "right", border = False)
    average_time_box.bg = "#f2e4d9"
    play_button_box = Box(center_box, width= 200, height = 200, align = "top", border = False)
    bottom_spacer = Box(app,  width= "fill", height = 30, align = "top", border = False)
    leaderboard_button = Box(app, width= 220, height = 50, align = "top", border = False)
    title = Picture(title_box, image = "Main title.png", width = 420, height = 80)
    information = Picture(info_box, image = "Main_text.png", width = 450, height = 100)
    small_title = Picture (top_spacer4, image = "Small_tittle.png", width = 150, height = 60)
    play_button = Picture(play_button_box, image="Reaction_game_button.png", width = 200, height = 200)
    leaderboard = Picture(leaderboard_button, image="Leaderboard_button.png", width = 160, height = 60, align= "bottom")
    #login_window()
    play_button.when_clicked = game
    leaderboard.when_clicked = analyse





"""""
    leaderboard = PushButton(app, image="Leaderboard_button.png", width = 150, height = 50, align= "bottom")
    leaderboard.bg = "#f2e4d9"
    space_3 = Text(box, text="hello", align="right")
    space_4 = Text(box, text="hello", align="right")
    average_time = Text(box, text = "average time", size = 14, align = "right")
    average_time.bg = "#f2e4d9"
"""""


def login_window():
    global all_time_list, window2, count, i, start, final_participant_age, wrong, average_times, all_average_list
    window2 = Window(app, title ="Login window", height=600, width=600)
    window2.bg = "#205a60"
    window2.show(wait=True)
    window.hide()
    side1_box2 = Box(window2, width= 20, height = "fill", align = "right", border = False)
    side2_box2 = Box(window2, width= 20, height = "fill", align = "left", border = False)
    top_spacer2 = Box(window2, width= "fill", height = 20, align = "top", border = False)
    tittle2_box = Box(window2, width= 400, height= 80, align= "top", border= False)
    tittle3 = Text(tittle2_box, text = "Login", align="left", size = 30, color = "#f2e4d9")
    top_spacer_3_login = Box(window2, width= "fill", height = 20, align = "top", border = False)
    fastesttime = Box(window2, width= "fill", height= 50, align= "top", border= False)
    top_spacer4 = Box(window2, width= "fill", height = 20, align = "top", border = False)
    slowesttime = Box(window2, width= "fill", height= 50, align= "top", border= False)
    top_spacer5 = Box(window2, width= "fill", height = 20, align = "top", border = False)
    averagetime = Box(window2, width= "fill", height= 50, align= "top", border= False)
    top_spacer6 = Box(window2, width= "fill", height = 20, align = "top", border = False)
    nametittle = Box(window2, width= "fill", height = 40, align = "top", border = False)
    top_spacer7 = Box(window2, width= "fill", height = 20, align = "top", border = False)
    namebox = Box(window2, width= "fill", height = 40, align = "top", border = False)
    top_spacer8 = Box(window2, width= "fill", height = 20, align = "top", border = False)
    agetittle = Box(window2, width= "fill", height = 40, align = "top", border = False)
    top_spacer9 = Box(window2, width= "fill", height = 20, align = "top", border = False)
    agebox = Box(window2, width= "fill", height = 40, align = "top", border = False)
    bottom_box = Box(window2, width= "fill", height = 20, align = "bottom", border = False)
    if wrong == 1:
        message = Text(top_spacer_3_login, text = "Age input must be between 18-12 years", align="left", size = 14, color = "#f2e4d9")
    count = 2
    i = 0
    start = 0
    lenght = int(len(all_time_list))
    individual = [all_time_list[lenght-1], all_time_list[lenght-2], all_time_list[lenght-3]]
    fastest_times = min(individual)
    slowest_times = max(individual)
    average_times = 0
    average_times = round((individual[0] + individual[1] + individual[2])/3, 2)
    print(average_times)
    wrong = 0

    fast = Text(fastesttime, text = "Fastest time: " + str(fastest_times), align="left", size = 20, color = "#f2e4d9")
    slow = Text(slowesttime, text = "Slowest time: " + str(slowest_times), align="left", size = 20, color = "#f2e4d9")
    avg = Text(averagetime, text = "Average time: " + str(average_times), align="left", size = 20, color = "#f2e4d9")
    name = Text(nametittle, text = "Enter name:", align="left", size = 20, color = "#f2e4d9")
    name_text_box = TextBox(namebox, align="left")
    age = Text(agetittle, text = "Enter your age:", align="left", size = 20, color = "#f2e4d9")
    def textbox_changed():
        global final_participant_age
        final_participant_age = age_text_box.value



    continuebutton = PushButton(window2, text="Continue", command = check, width= 10, height= 5)
    age_text_box = TextBox(agebox, command=textbox_changed, text = "",  align="left")

def check():
    global final_participant_age, wrong, average_times, all_average_list, all_age_list
    print(final_participant_age)
    try:
        testing = int(final_participant_age)
        if int(final_participant_age) <= 18 and int(final_participant_age) >= 12:
            destruction1()
            all_age_list.append(float(final_participant_age))
            all_average_list.append(average_times)
            print(all_age_list)
            print(all_average_list)
            openwindow()
    except ValueError:
        wrong = 1
        login_window()

        #save(all_age_list, "final_storage_pickle")

        #average_times = 0
        all_age_list =[]
        all_average_list = []

    else:
        wrong = 1
        login_window()



    """""
    age_text_box.update_command(check)
    def check():
        age_text_box_value = int(age_text_box.value)
        if  age_text_box_value<=18 and age_text_box_value>=12:
            all_age_list.append(age_text_box.value)
            save3()
            destruction1()
        else:
            window2.update()
            text = Text(bottom_box, text="Enter valid input 12-18")
    """


        #if int(age_text_box.value) > 0 and int(age_text_box.value) <= 13:
    #all_names_list.append(name_text_box.value)
    #save2()

        #else:
            #login_window()
    #else:
        #login_window()


app = App(title= "Main window", height=600, width=600)
app.bg = "#205a60"

def false_start():
    global window, window4, i, count, start
    window4 = Window(app, title ="False Start", height=600, width=600)
    window4.bg = "#205a60"
    window4.show(wait=True)
    window.hide()
    side1_box4 = Box(window4, width= 20, height = "fill", align = "right", border = True)
    side2_box4 = Box(window4, width= 20, height = "fill", align = "left", border = True)
    top_spacer4 = Box(window4, width= "fill", height = 50, align = "top", border = True)
    false_box = Box(window4, width= "fill", height = 150, align = "top", border = True)
    false_start_message = Picture(false_box, image = "False_start.png", width = 400, height = 130)
    backbutton = PushButton(window4, text="Continue", command = destruction2, width= 10, height= 5)
    count = 2
    i = 0
    start = 0

def destruction1():
    global window2
    app.show()
    window2.destroy()


def destruction2():
    global window4
    app.show()
    window4.hide()

def destruction3():
    global window3
    app.show()
    window3.destroy()



#original_pic()
open_window()
app.display()

