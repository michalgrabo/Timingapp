from guizero import App, PushButton, Text, TextBox, Window, TitleBox, Box, Picture, Waffle, Slider
import time, pickle
#global variables to be accesed later by specific functions
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

#Function saves the average reaction time and age of participant in a file called "Final pickle"
def save(filename):
    global all_time_list, all_average_list
    #print(all_age_list, all_average_list)
    name_and_time_list = all_age_list + all_average_list + times_and_age_reconstructed
    with open(filename, "wb") as outfile:
        pickle.dump(name_and_time_list, outfile)

#Function that opens the saved file "Final pickle" and acceses the list saved within
def loading(filename):
    global times_and_age_reconstructed
    with open(filename, "rb") as infile:
        times_and_age_reconstructed = pickle.load(infile)

    print(times_and_age_reconstructed)

#Creating the main menu
def open_window():
    global count

    def game():
    #Creating the window and layouts for game page
        global count, end, i, start, window, all_time_list
        loading("final_pickle")
        window = Window(app, title ="Game window", height=600, width=600)
        window.bg = "#205a60"
        window.show(wait=True)
        app.hide()
        #Making layouts for game window
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
                #Lighting all three red lights

                waffle[i, 0].color = "red"
                app.after(1000, light)
            else:
                #Turning lights green after all red lights are on
                waffle[0, 0].color = "green"
                waffle[1, 0].color = "green"
                waffle[2, 0].color = "green"
                start = time.time()
            i += 1
        def timer():
            global start, all_time_list

            if start == 0:
                #Detecting fase starts
                false_start()
            else:
                #Calculating the reaction time and reseting game 2 times
                end = time.time()
                reaction_time = round(end - start, 2)
                all_time_list.append(reaction_time)
                text_2 = Text(current_time, text=  str(reaction_time) , align="bottom", size = 12)
                #print(all_time_list)
                resetgame()

        def resetgame():
            global start, i, count
            if count == 0:
                #Reseting lights to red and restarting countdown procedure
                waffle[0, 0].color = "white"
                waffle[1, 0].color = "white"
                waffle[2, 0].color = "white"
                time.sleep(1)
                login_window()
            else:
                #Going to login process
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
        #triggering the lights countdown
        window.after(1000, light)

    def analyse():
        global window3
        window3 = Window(app, title ="Analysis window", height=600, width=600)
        loading("final_pickle")
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
        #Back button moves user back to main menu

        def textbox_changed():
            #Checks text box value
                global requested_age
                requested_age = age_group_text_box.value

        def calculation():
            global requested_age,times_and_age_reconstructed

            #Following function code was sorced from https://www.codingem.com/index-of-in-python/#:~:text=To%20find%20the%20index%20of%20a%20list%20element%20in%20Python,built%2Din%20index()%20method.&text=To%20find%20the%20index%20of%20a%20character%20in%20a%20string,()%20method%20on%20the%20string.&text=This%20is%20the%20quick%20answer.
            def all_indexes_list(list_of_interest, age):
                #Finding all indexes of the float entered by user in textbox
                for index, element in enumerate(list_of_interest):
                    if element == age:
                        all_final_index.append(index)

            all_final_index = []
            all_indexes_list(times_and_age_reconstructed, float(requested_age))
            analyse_times = []
            for i in range(len(all_final_index)):
                #adding the times associated to age selected on the base of their previously found index to seperate list
                final_pos = all_final_index[i] +1
                analyse_times.append(times_and_age_reconstructed[final_pos])


            fastest_times_per_age = min(analyse_times)
            slowest_times_per_age = max(analyse_times)
            lenght = len(analyse_times)
            average_times_per_age = round(sum(analyse_times)/ lenght,2)
            #Analysing list for minimum maximum and average of the listcheck
            fast1 = Text(fastesttime, text = str(fastest_times_per_age), align="left", size = 20, color = "#f2e4d9")
            slow2 = Text(slowesttime, text = str(slowest_times_per_age), align="left", size = 20, color = "#f2e4d9")
            avg3 = Text(averagetime, text = str(average_times_per_age), align="left", size = 20, color = "#f2e4d9")

            #Adding gathered values to appropriet text boxes


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
        #Loads calculation

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
    #current_time_box = Box(center_box, width= 100, height = 40, align = "left", border = False)
    #current_time_box.bg = "#f2e4d9"
    #average_time_box = Box(center_box, width= 100, height = 40, align = "right", border = False)
    #average_time_box.bg = "#f2e4d9"
    play_button_box = Box(center_box, width= 200, height = 200, align = "top", border = False)
    bottom_spacer = Box(app,  width= "fill", height = 30, align = "top", border = False)
    analysis_button_box = Box(app, width= 220, height = 100, align = "top", border = False)
    title = Picture(title_box, image = "Main title.png", width = 420, height = 80)
    information = Picture(info_box, image = "Maintext2.png", width = 450, height = 100)
    small_title = Picture (top_spacer4, image = "Small_tittle.png", width = 150, height = 60)
    play_button = Picture(play_button_box, image="Reaction_game_button.png", width = 200, height = 200)
    analysis_button = Picture(analysis_button_box, image="analysis1.png", width = 160, height = 60, align= "bottom")
    #Creating layout
    play_button.when_clicked = game
    #When "Go" button is pressed program starts the game
    analysis_button.when_clicked = analyse
    #When "leaderboard" button is pressed program starts the analitics function



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
    #Creating window and layout for login
    if wrong == 1:
        #adding warning message if inputs are not valid
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
    #print(average_times)
    wrong = 0

    fast = Text(fastesttime, text = "Fastest time: " + str(fastest_times), align="left", size = 20, color = "#f2e4d9")
    slow = Text(slowesttime, text = "Slowest time: " + str(slowest_times), align="left", size = 20, color = "#f2e4d9")
    avg = Text(averagetime, text = "Average time: " + str(average_times), align="left", size = 20, color = "#f2e4d9")
    name = Text(nametittle, text = "Enter name:", align="left", size = 20, color = "#f2e4d9")
    name_text_box = TextBox(namebox, align="left")
    age = Text(agetittle, text = "Enter your age:", align="left", size = 20, color = "#f2e4d9")
    def textbox_changed():
        #Checking user input
        global final_participant_age
        final_participant_age = age_text_box.value

    continuebutton = PushButton(window2, text="Continue", command = check, width= 10, height= 5)
    age_text_box = TextBox(agebox, command=textbox_changed, text = "",  align="left")

def check():
    global final_participant_age, wrong, average_times, all_average_list, all_age_list
    #Checking if inputs are valid, between 12-18 years old
    if int(final_participant_age) <= 18 and int(final_participant_age) >= 12:
        destruction1()
        all_age_list =[]
        all_average_list = []
        all_age_list.append(float(final_participant_age))
        all_average_list.append(average_times)
        #print(all_age_list)
        #print(all_average_list)
        save("final_pickle")

    else:
        window2.destroy()
        wrong = 1
        login_window()



app = App(title= "Main window", height=600, width=600)
app.bg = "#205a60"

def false_start():
    global window, window4, i, count, start
    #Directing user to main menu if false start is detected
    window4 = Window(app, title ="False Start", height=600, width=600)
    window4.bg = "#205a60"
    window4.show(wait=True)
    window.destroy()
    i = 0
    count = 2
    side1_box4 = Box(window4, width= 20, height = "fill", align = "right", border = False)
    side2_box4 = Box(window4, width= 20, height = "fill", align = "left", border = False)
    top_spacer4 = Box(window4, width= "fill", height = 50, align = "top", border = False)
    false_box = Box(window4, width= "fill", height = 150, align = "top", border = False)
    false_start_message = Picture(false_box, image = "False_start.png", width = 400, height = 130)
    backbutton = PushButton(window4, text="Continue", command = destruction2, width= 10, height= 5)
    #

    #start = 0


def destruction1():
    global window2
    #Destroys login window and returns to main menu
    app.show()
    window2.destroy()


def destruction2():
    #Destroys game window and returns to main menu if false start is detected
    global window4
    app.show()
    window4.hide()

def destruction3():
    #Destroys analysis window and returns to main menu
    global window3
    app.show()
    window3.destroy()



#original_pic()
open_window()
app.display()
#Showing the application and creating the main menu

