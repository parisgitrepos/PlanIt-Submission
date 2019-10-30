import datetime
import pickle
import tkinter

def get_current_date_time(list_to_append_to: list):
    hour = datetime.datetime.now().strftime('%I')
    time_of_day = datetime.datetime.now().strftime('%p')
    if time_of_day == 'PM':
        hour = int(hour) + 12

    else:
        pass
    list_to_append_to.append(hour)

    minutes = datetime.datetime.now().strftime('%m')
    list_to_append_to.append(minutes)

    day_of_the_week = datetime.datetime.now().weekday()
    list_to_append_to.append(day_of_the_week)

time_now = []

get_current_date_time(time_now)

def used_before():
    with open('used_before.pickle', 'rb') as file:
        f = pickle.load(file)
        f = f[0]
    if f == 0:
        return False
    elif f == 1:
        return True

def get_colors_activate_plan():
    weekday = time_now[2]
    if weekday is 0:
        today = 'Monday'
    elif weekday is 1:
        today = 'Tuesday'
    elif weekday is 2:
        today = 'Wednesday'
    elif weekday is 3:
        today = 'Thursday'
    elif weekday is 4:
        today = 'Friday'
    elif weekday is 5:
        today = 'Saturday'
    elif weekday is 6:
        today = 'Sunday'

    day_hours = 24

    with open('Days\\Monday.pickle', 'rb')as file:
        m_avail_hours = pickle.load(file)
    m_avail_hours = day_hours - sum(m_avail_hours)

    with open('Days\\Tuesday.pickle', 'rb') as file:
        t_avail_hours = pickle.load(file)
    t_avail_hours = day_hours - sum(t_avail_hours)

    with open('Days\\Wednesday.pickle', 'rb') as file:
        w_avail_hours = pickle.load(file)
    w_avail_hours = day_hours - sum(w_avail_hours)

    with open('Days\\Thursday.pickle', 'rb') as file:
        th_avail_hours = pickle.load(file)
    th_avail_hours = day_hours - sum(th_avail_hours)

    with open('Days\\Friday.pickle', 'rb') as file:
        f_avail_hours = pickle.load(file)
    f_avail_hours = day_hours - sum(f_avail_hours)

    with open('Days\\Saturday.pickle', 'rb') as file:
        s_avail_hours = pickle.load(file)
    s_avail_hours = day_hours - sum(s_avail_hours)

    with open('Days\\Sunday.pickle', 'rb') as file:
        su_avail_hours = pickle.load(file)
    su_avail_hours = day_hours - sum(su_avail_hours)

    with open('Homework\\Monday.pickle', 'rb') as file:
        m_hw_hours = pickle.load(file)
        append_list = []
        for a in range(10):
            append_list.append(m_hw_hours[a])
        m_hw_hours = sum(append_list)

    with open('Homework\\Tuesday.pickle', 'rb') as file:
        t_hw_hours = pickle.load(file)
        append_list = []
        for a in range(10):
            append_list.append(t_hw_hours[a])
        t_hw_hours = sum(append_list)

    with open('Homework\\Wednesday.pickle', 'rb') as file:
        w_hw_hours = pickle.load(file)
        append_list = []
        for a in range(10):
            append_list.append(w_hw_hours[a])
        w_hw_hours = sum(append_list)

    with open('Homework\\Thursday.pickle', 'rb') as file:
        th_hw_hours = pickle.load(file)
        append_list = []
        for a in range(10):
            append_list.append(th_hw_hours[a])
        th_hw_hours = sum(append_list)

    with open('Homework\\Friday.pickle', 'rb') as file:
        f_hw_hours = pickle.load(file)
        append_list = []
        for a in range(10):
            append_list.append(f_hw_hours[a])
        f_hw_hours = sum(append_list)

    with open('Homework\\Saturday.pickle', 'rb') as file:
        s_hw_hours = pickle.load(file)
        append_list = []
        for a in range(10):
            append_list.append(s_hw_hours[a])
        s_hw_hours = sum(append_list)

    with open('Homework\\Sunday.pickle', 'rb') as file:
        su_hw_hours = pickle.load(file)
        append_list = []
        for a in range(10):
            append_list.append(su_hw_hours[a])
        su_hw_hours = sum(append_list)

    if m_avail_hours == m_hw_hours:
        m_schedule = 'yellow'
    elif m_avail_hours < m_hw_hours:
        m_schedule = 'red'
    elif m_avail_hours > m_hw_hours:
        m_schedule = 'green'

    if t_avail_hours == t_hw_hours:
        t_schedule = 'yellow'
    elif t_avail_hours < t_hw_hours:
        t_schedule = 'red'
    elif t_avail_hours > t_hw_hours:
        t_schedule = 'green'

    if w_avail_hours == w_hw_hours:
        w_schedule = 'yellow'
    elif w_avail_hours < w_hw_hours:
        w_schedule = 'red'
    elif w_avail_hours > w_hw_hours:
        w_schedule = 'green'

    if th_avail_hours == th_hw_hours:
        th_schedule = 'yellow'
    elif th_avail_hours < th_hw_hours:
        th_schedule = 'red'
    elif th_avail_hours > th_hw_hours:
        th_schedule = 'green'

    if f_avail_hours == f_hw_hours:
        f_schedule = 'yellow'
    elif f_avail_hours < f_hw_hours:
        f_schedule = 'red'
    elif f_avail_hours > f_hw_hours:
        f_schedule = 'green'

    if s_avail_hours == s_hw_hours:
        s_schedule = 'yellow'
    elif s_avail_hours < s_hw_hours:
        s_schedule = 'red'
    elif s_avail_hours > s_hw_hours:
        s_schedule = 'green'

    if su_avail_hours == su_hw_hours:
        su_schedule = 'yellow'
    elif su_avail_hours < su_hw_hours:
        su_schedule = 'red'
    elif su_avail_hours > su_hw_hours:
        su_schedule = 'green'

    plan(m_schedule, t_schedule, w_schedule, th_schedule, f_schedule, s_schedule, su_schedule)

def plan(m, t, w, th, f, s, su):
    global window
    window.destroy()
    window = tkinter.Tk()
    window.state('zoomed')
    window.title('PlanIt')
    window.config(bg = 'blue')
#    window.iconbitmap('PlanIt.ico')

    key_yellow = tkinter.Label(text = 'Yellow means that you have the same amount of available hours as you do assignment, meaning you have no time to waste!', bg = 'yellow')
    key_red = tkinter.Label(text = "Red means you don't have enough available hours as you do assignment, meaning you need to modify your schedule!", bg = 'red')
    key_green = tkinter.Label(text = 'Green means you have more than enough available hours than you do assignment, meaning you are ok, but you should still get your work done early!', bg = 'green')
    spacer = tkinter.Label(bg = 'blue')

    key_yellow.pack()
    key_red.pack()
    key_green.pack()
    spacer.pack()

    m_label = tkinter.Label(text = 'Monday:', bg = 'blue')
    spacer2 = tkinter.Label(bg = 'blue')
    t_label = tkinter.Label(text = 'Tuesday:', bg = 'blue')
    spacer3 = tkinter.Label(bg = 'blue')
    w_label = tkinter.Label(text = 'Wednesday:', bg = 'blue')
    spacer4 = tkinter.Label(bg = 'blue')
    th_label = tkinter.Label(text = 'Thursday:', bg = 'blue')
    spacer5 = tkinter.Label(bg = 'blue')
    f_label = tkinter.Label(text = 'Friday:', bg = 'blue')
    spacer6 = tkinter.Label(bg = 'blue')
    s_label = tkinter.Label(text = 'Saturday:', bg = 'blue')
    spacer7 = tkinter.Label(bg = 'blue')
    su_label = tkinter.Label(text = 'Sunday:', bg = 'blue')
    spacer8 = tkinter.Label(bg = 'blue')

    m_color = tkinter.Label(bg = m)
    t_color = tkinter.Label(bg = t)
    w_color = tkinter.Label(bg = w)
    th_color = tkinter.Label(bg = th)
    f_color = tkinter.Label(bg = f)
    s_color = tkinter.Label(bg = s)
    su_color = tkinter.Label(bg = su)

    m_label.pack()
    m_color.pack(fill = 'x')
    spacer2.pack()

    t_label.pack()
    t_color.pack(fill = 'x')
    spacer3.pack()

    w_label.pack()
    w_color.pack(fill = 'x')
    spacer4.pack()

    th_label.pack()
    th_color.pack(fill = 'x')
    spacer5.pack()

    f_label.pack()
    f_color.pack(fill = 'x')
    spacer6.pack()

    s_label.pack()
    s_color.pack(fill = 'x')
    spacer7.pack()

    su_label.pack()
    su_color.pack(fill = 'x')
    spacer8.pack()

    back = tkinter.Button(text = 'Back', bg = 'yellow', command = choose_window)
    back.pack(side = 'bottom')

    window.mainloop()

def day_submit(day):
    global sleep_time
    global wakeup_time
    global school
    global dinner
    global a1
    global a2
    global a3
    global a4
    global a5

    sleep_time = float(sleep_time.get())
    wakeup_time = float(wakeup_time.get())
    school = float(school.get())
    dinner = float(dinner.get())
    a1 = float(a1.get())
    a2 = float(a2.get())
    a3 = float(a3.get())
    a4 = float(a4.get())
    a5 = float(a5.get())

    create_list = [
        sleep_time,
        wakeup_time,
        school,
        dinner,
        a1,
        a2,
        a3,
        a4,
        a5
    ]

    day_file_to_open = 'Days\\' + day + '.pickle'

    with open(day_file_to_open, 'wb') as file:
        pickle.dump(create_list, file)

    config_times()

def day_config(day):
    global window
    window.destroy()
    window = tkinter.Tk()
    window.config(bg = 'green')
    window.title('PlanIt')
#    window.iconbitmap('PlanIt.ico')

    global sleep_time
    global wakeup_time
    global school
    global dinner
    global a1
    global a2
    global a3
    global a4
    global a5

    day_to_be_read = 'Days\\' + day + '.pickle'

    with open(day_to_be_read, 'rb') as file:
        pickle_load = pickle.load(file)

    sleep_time = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    sleep_time.delete(0, 'end')
    sleep_time.insert(0, pickle_load[0])

    wakeup_time = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    wakeup_time.delete(0, 'end')
    wakeup_time.insert(0, pickle_load[1])

    school = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    school.delete(0, 'end')
    school.insert(0, pickle_load[2])

    dinner = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    dinner.delete(0, 'end')
    dinner.insert(0, pickle_load[3])

    a1 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a1.delete(0, 'end')
    a1.insert(0, pickle_load[4])

    a2 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a2.delete(0, 'end')
    a2.insert(0, pickle_load[5])

    a3 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a3.delete(0, 'end')
    a3.insert(0, pickle_load[6])

    a4 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a4.delete(0, 'end')
    a4.insert(0, pickle_load[7])

    a5 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a5.delete(0, 'end')
    a5.insert(0, pickle_load[8])

    label1 = tkinter.Label(text = 'Time You Sleep Today (written in format as given in the previous screen):', bg = 'green')
    label2 = tkinter.Label(text = 'Time You Wakeup Today (written in format as given in the previous screen):', bg = 'green')
    label3 = tkinter.Label(text = 'Duration of School:', bg = 'green')
    label4 = tkinter.Label(text = 'Duration of Dinner:', bg = 'green')
    label5 = tkinter.Label(text = 'Misc. Activity 1 Duration:', bg = 'green')
    label6 = tkinter.Label(text = 'Misc. Activity 2 Duration:', bg = 'green')
    label7 = tkinter.Label(text = 'Misc. Activity 3 Duration:', bg = 'green')
    label8 = tkinter.Label(text = 'Misc. Activity 4 Duration:', bg = 'green')
    label9 = tkinter.Label(text = 'Misc. Activity 5 Duration:', bg = 'green')

    spacer = tkinter.Label(bg = 'green')
    spacer2 = tkinter.Label(bg = 'green')
    spacer3 = tkinter.Label(bg = 'green')
    spacer4 = tkinter.Label(bg = 'green')
    spacer5 = tkinter.Label(bg = 'green')
    spacer6 = tkinter.Label(bg = 'green')
    spacer7 = tkinter.Label(bg = 'green')
    spacer8 = tkinter.Label(bg = 'green')
    spacer9 = tkinter.Label(bg = 'green')

    save_goback = tkinter.Button(bg = 'blue', text = 'Save And Go Back', command = lambda: day_submit(day))

    label1.pack()
    sleep_time.pack()
    spacer.pack()

    label2.pack()
    wakeup_time.pack()
    spacer2.pack()

    label3.pack()
    school.pack()
    spacer3.pack()

    label4.pack()
    dinner.pack()
    spacer4.pack()

    label5.pack()
    a1.pack()
    spacer5.pack()

    label6.pack()
    a2.pack()
    spacer6.pack()

    label7.pack()
    a3.pack()
    spacer7.pack()

    label8.pack()
    a4.pack()
    spacer8.pack()

    label9.pack()
    a5.pack()
    spacer9.pack()

    save_goback.pack(side = 'bottom')

def weekend_config(day_of_weekend):
    global window
    window.destroy()
    window = tkinter.Tk()
    window.config(bg = 'green')
    window.title('PlanIt')
#    window.iconbitmap('PlanIt.ico')

    global sleep_time
    global wakeup_time
    global school
    global dinner
    global a1
    global a2
    global a3
    global a4
    global a5

    day_to_be_read = 'Days\\' + day_of_weekend + '.pickle'

    with open(day_to_be_read, 'rb') as file:
        pickle_load = pickle.load(file)

    sleep_time = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    sleep_time.delete(0, 'end')
    sleep_time.insert(0, pickle_load[0])

    wakeup_time = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    wakeup_time.delete(0, 'end')
    wakeup_time.insert(0, pickle_load[1])

    school = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    school.delete(0, 'end')
    school.insert(0, pickle_load[2])

    dinner = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    dinner.delete(0, 'end')
    dinner.insert(0, pickle_load[3])

    a1 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a1.delete(0, 'end')
    a1.insert(0, pickle_load[4])

    a2 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a2.delete(0, 'end')
    a2.insert(0, pickle_load[5])

    a3 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a3.delete(0, 'end')
    a3.insert(0, pickle_load[6])

    a4 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a4.delete(0, 'end')
    a4.insert(0, pickle_load[7])

    a5 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    a5.delete(0, 'end')
    a5.insert(0, pickle_load[8])

    label1 = tkinter.Label(text = 'Time You Sleep Today (written in format as given in the previous screen):', bg = 'green')
    label2 = tkinter.Label(text = 'Time You Wakeup Today (written in format as given in the previous screen):', bg = 'green')
    label3 = tkinter.Label(text = 'Duration of Religious Time:', bg = 'green')
    label4 = tkinter.Label(text = 'Duration of All Meal Times Combined:', bg = 'green')
    label5 = tkinter.Label(text = 'Misc. Activity 1 Duration:', bg = 'green')
    label6 = tkinter.Label(text = 'Misc. Activity 2 Duration:', bg = 'green')
    label7 = tkinter.Label(text = 'Misc. Activity 3 Duration:', bg = 'green')
    label8 = tkinter.Label(text = 'Misc. Activity 4 Duration:', bg = 'green')
    label9 = tkinter.Label(text = 'Misc. Activity 5 Duration:', bg = 'green')

    spacer = tkinter.Label(bg = 'green')
    spacer2 = tkinter.Label(bg = 'green')
    spacer3 = tkinter.Label(bg = 'green')
    spacer4 = tkinter.Label(bg = 'green')
    spacer5 = tkinter.Label(bg = 'green')
    spacer6 = tkinter.Label(bg = 'green')
    spacer7 = tkinter.Label(bg = 'green')
    spacer8 = tkinter.Label(bg = 'green')
    spacer9 = tkinter.Label(bg = 'green')

    save_goback = tkinter.Button(bg = 'blue', text = 'Save And Go Back', command = lambda: day_submit(day_of_weekend))

    label1.pack()
    sleep_time.pack()
    spacer.pack()

    label2.pack()
    wakeup_time.pack()
    spacer2.pack()

    label3.pack()
    school.pack()
    spacer3.pack()

    label4.pack()
    dinner.pack()
    spacer4.pack()

    label5.pack()
    a1.pack()
    spacer5.pack()

    label6.pack()
    a2.pack()
    spacer6.pack()

    label7.pack()
    a3.pack()
    spacer7.pack()

    label8.pack()
    a4.pack()
    spacer8.pack()

    label9.pack()
    a5.pack()
    spacer9.pack()

    save_goback.pack(side = 'bottom')

def config_times():
    global window
    window.destroy()
    window = tkinter.Tk()
    window.config(bg = 'green')
    window.title('PlanIt')
#    window.iconbitmap('PlanIt.ico')

    about = tkinter.Label(text='Please add any activities you are not able to do homework during and how many',
                          bg='green')
    about2 = tkinter.Label(text='hours the activity lasts. You must also enter the time that you go to sleep',
                           bg='green')
    about3 = tkinter.Label(text='that day (must be written as [blank] hours before 12 AM for sleeping and',
                           bg='green')
    about4 = tkinter.Label(text=' [blank] hours after 12 AM for waking up). All units are in half hour', bg='green')
    about5 = tkinter.Label(text = 'increments. For extra activity boxes, just type in 0.', bg = 'green')

    about.pack()
    about2.pack()
    about3.pack()
    about4.pack()
    about5.pack()

    config_m = tkinter.Button(text = 'Monday', bg = 'blue', command = lambda: day_config('Monday'))
    config_t = tkinter.Button(text = 'Tuesday', bg = 'blue', command = lambda: day_config('Tuesday'))
    config_w = tkinter.Button(text = 'Wednesday', bg = 'blue', command = lambda: day_config('Wednesday'))
    config_th = tkinter.Button(text = 'Thursday', bg = 'blue', command = lambda: day_config('Thursday'))
    config_fr = tkinter.Button(text = 'Friday', bg = 'blue', command = lambda: day_config('Friday'))
    config_s = tkinter.Button(text = 'Saturday', bg = 'blue', command = lambda: weekend_config('Saturday'))
    config_su = tkinter.Button(text = 'Sunday', bg = 'blue', command = lambda: weekend_config('Sunday'))

    spacer = tkinter.Label(bg = 'green')
    spacer2 = tkinter.Label(bg = 'green')
    spacer3 = tkinter.Label(bg = 'green')
    spacer4 = tkinter.Label(bg = 'green')
    spacer5 = tkinter.Label(bg = 'green')
    spacer6 = tkinter.Label(bg = 'green')
    spacer7 = tkinter.Label(bg = 'green')
    spacer8 = tkinter.Label(bg = 'green')

    save_quit = tkinter.Button(bg = 'red', text = 'Save And Go Back', command = choose_window)

    spacer.pack()

    config_m.pack()
    spacer2.pack()
    config_t.pack()
    spacer3.pack()
    config_w.pack()
    spacer4.pack()
    config_th.pack()
    spacer5.pack()
    config_fr.pack()
    spacer6.pack()
    config_s.pack()
    spacer7.pack()
    config_su.pack()
    spacer8.pack()

    save_quit.pack(side = 'bottom')

    window.mainloop()

def homework_save(day):
    global h1
    global h2
    global h3
    global h4
    global h5
    global h6
    global h7
    global h8
    global h9
    global h10
    global name1
    global name2
    global name3
    global name4
    global name5
    global name6
    global name7
    global name8
    global name9
    global name10

    h1 = float(h1.get())
    h2 = float(h2.get())
    h3 = float(h3.get())
    h4 = float(h4.get())
    h5 = float(h5.get())
    h6 = float(h6.get())
    h7 = float(h7.get())
    h8 = float(h8.get())
    h9 = float(h9.get())
    h10 = float(h10.get())
    name1 = str(name1.get())
    name2 = str(name2.get())
    name3 = str(name3.get())
    name4 = str(name4.get())
    name5 = str(name5.get())
    name6 = str(name6.get())
    name7 = str(name7.get())
    name8 = str(name8.get())
    name9 = str(name9.get())
    name10 = str(name10.get())

    create_list = [
        h1,
        h2,
        h3,
        h4,
        h5,
        h6,
        h7,
        h8,
        h9,
        h10,
        name1,
        name2,
        name3,
        name4,
        name5,
        name6,
        name7,
        name8,
        name9,
        name10
    ]

    path_to_write_to = 'Homework\\' + day + '.pickle'

    with open(path_to_write_to, 'wb') as file:
        pickle.dump(create_list, file)
    homework_config()

def add_homework(day):
    global window
    window.destroy()
    window = tkinter.Tk()
    window.config(bg = 'green')
    window.state('zoomed')
#    window.iconbitmap('PlanIt.ico')

    global h1
    global h2
    global h3
    global h4
    global h5
    global h6
    global h7
    global h8
    global h9
    global h10
    global name1
    global name2
    global name3
    global name4
    global name5
    global name6
    global name7
    global name8
    global name9
    global name10

    hw_day_to_open = 'Homework\\' + day + '.pickle'

    with open(hw_day_to_open, 'rb') as file:
        pickle_load = pickle.load(file)

    h1 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h1.delete(0, 'end')
    h1.insert(0, pickle_load[0])

    h2 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h2.delete(0, 'end')
    h2.insert(0, pickle_load[1])

    h3 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h3.delete(0, 'end')
    h3.insert(0, pickle_load[2])

    h4 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h4.delete(0, 'end')
    h4.insert(0, pickle_load[3])

    h5 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h5.delete(0, 'end')
    h5.insert(0, pickle_load[4])

    h6 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h6.delete(0, 'end')
    h6.insert(0, pickle_load[5])

    h7 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h7.delete(0, 'end')
    h7.insert(0, pickle_load[6])

    h8 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h8.delete(0, 'end')
    h8.insert(0, pickle_load[7])

    h9 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h9.delete(0, 'end')
    h9.insert(0, pickle_load[8])

    h10 = tkinter.Spinbox(from_ = 0, to = 24, increment = 0.5)
    h10.delete(0, 'end')
    h10.insert(0, pickle_load[9])

    name1 = tkinter.Entry(bg = 'green')
    name1.delete(0, 'end')
    name1.insert(0, pickle_load[10])

    name2 = tkinter.Entry(bg = 'green')
    name2.delete(0, 'end')
    name2.insert(0, pickle_load[11])

    name3 = tkinter.Entry(bg = 'green')
    name3.delete(0, 'end')
    name3.insert(0, pickle_load[12])

    name4 = tkinter.Entry(bg = 'green')
    name4.delete(0, 'end')
    name4.insert(0, pickle_load[13])

    name5 = tkinter.Entry(bg = 'green')
    name5.delete(0, 'end')
    name5.insert(0, pickle_load[14])

    name6 = tkinter.Entry(bg = 'green')
    name6.delete(0, 'end')
    name6.insert(0, pickle_load[15])

    name7 = tkinter.Entry(bg = 'green')
    name7.delete(0, 'end')
    name7.insert(0, pickle_load[16])

    name8 = tkinter.Entry(bg = 'green')
    name8.delete(0, 'end')
    name8.insert(0, pickle_load[17])

    name9 = tkinter.Entry(bg = 'green')
    name9.delete(0, 'end')
    name9.insert(0, pickle_load[18])

    name10 = tkinter.Entry(bg = 'green')
    name10.delete(0, 'end')
    name10.insert(0, pickle_load[19])

    save_goback = tkinter.Button(text = 'Save And Go Back', bg = 'blue', command = lambda: homework_save(day))

    spacer = tkinter.Label(bg = 'green')
    spacer2 = tkinter.Label(bg = 'green')
    spacer3 = tkinter.Label(bg = 'green')
    spacer4 = tkinter.Label(bg = 'green')
    spacer5 = tkinter.Label(bg = 'green')
    spacer6 = tkinter.Label(bg = 'green')
    spacer7 = tkinter.Label(bg = 'green')
    spacer8 = tkinter.Label(bg = 'green')
    spacer9 = tkinter.Label(bg = 'green')
    spacer10 = tkinter.Label(bg = 'green')

    name1.pack()
    h1.pack()
    spacer.pack()
    name2.pack()
    h2.pack()
    spacer2.pack()
    name3.pack()
    h3.pack()
    spacer3.pack()
    name4.pack()
    h4.pack()
    spacer4.pack()
    name5.pack()
    h5.pack()
    spacer5.pack()
    name6.pack()
    h6.pack()
    spacer6.pack()
    name7.pack()
    h7.pack()
    spacer7.pack()
    name8.pack()
    h8.pack()
    spacer8.pack()
    name9.pack()
    h9.pack()
    spacer9.pack()
    name10.pack()
    h10.pack()
    spacer10.pack()
    save_goback.pack(side = 'bottom')

    window.mainloop()

def homework_config():
    global window
    window.destroy()
    window = tkinter.Tk()
    window.config(bg = 'green')
    window.title('PlanIt')
#    window.iconbitmap('PlanIt.ico')

    about = tkinter.Label(text = 'Here you can add different assignments and input an estimated value on how long they will take. Units', bg = 'green')
    about2 = tkinter.Label(text = 'are in half hour increments. For extra boxes, set it to 0. You can store up to ten assignments per day.', bg = 'green')
    about3 = tkinter.Label(text = 'You can also set each of the assignments name by clicking on the title of the assignment. NOTE: PlanIt', bg = 'green')
    about4 = tkinter.Label(text = 'does not automatically split up assignments. Ex. if your assignment is to study everyday, you need to write', bg = 'green')
    about5 = tkinter.Label(text = '"Study" everyday and how long you want to study for.', bg = 'green')

    config_m = tkinter.Button(text = 'Monday', bg = 'blue', command = lambda: add_homework('Monday'))
    config_t = tkinter.Button(text = 'Tuesday', bg = 'blue', command = lambda: add_homework('Tuesday'))
    config_w = tkinter.Button(text = 'Wednesday', bg = 'blue', command = lambda: add_homework('Wednesday'))
    config_th = tkinter.Button(text = 'Thursday', bg = 'blue', command = lambda: add_homework('Thursday'))
    config_fr = tkinter.Button(text = 'Friday', bg = 'blue', command = lambda: add_homework('Friday'))
    config_s = tkinter.Button(text = 'Saturday', bg = 'blue', command = lambda: add_homework('Saturday'))
    config_su = tkinter.Button(text = 'Sunday', bg = 'blue', command = lambda: add_homework('Sunday'))

    spacer = tkinter.Label(bg = 'green')
    spacer2 = tkinter.Label(bg = 'green')
    spacer3 = tkinter.Label(bg = 'green')
    spacer4 = tkinter.Label(bg = 'green')
    spacer5 = tkinter.Label(bg = 'green')
    spacer6 = tkinter.Label(bg = 'green')
    spacer7 = tkinter.Label(bg = 'green')
    spacer8 = tkinter.Label(bg = 'green')

    save_quit = tkinter.Button(bg = 'red', text = 'Save And Go Back', command = choose_window)

    about.pack()
    about2.pack()
    about3.pack()
    about4.pack()
    about5.pack()
    spacer.pack()
    config_m.pack()
    spacer2.pack()
    config_t.pack()
    spacer3.pack()
    config_w.pack()
    spacer4.pack()
    config_th.pack()
    spacer5.pack()
    config_fr.pack()
    spacer6.pack()
    config_s.pack()
    spacer7.pack()
    config_su.pack()
    spacer8.pack()
    save_quit.pack(side = 'bottom')

    window.mainloop()

def choose_window():
    global window
    window.destroy()
    window = tkinter.Tk()
    window.config(bg = 'green')
    window.title('PlanIt')
#    window.iconbitmap('PlanIt.ico')

    view_plan = tkinter.Button(text = 'View Plan', bg = 'blue', command = get_colors_activate_plan)
    view_plan.pack()

    spacer = tkinter.Label(bg = 'green')
    spacer.pack()

    add_assignments = tkinter.Button(text = 'Add/View Assignments', command = homework_config, bg = 'blue')
    add_assignments.pack()

    spacer2 = tkinter.Label(bg = 'green')
    spacer2.pack()

    view_and_configure_times = tkinter.Button(text = 'View and Configure Activities', command = config_times, bg = 'blue')
    view_and_configure_times.pack()

    window.mainloop()


global window
window = tkinter.Tk()

setup = used_before()

if setup is True:
    choose_window()

elif setup is False:
    config_times()
    with open('used_before.pickle', 'wb') as file:
        pickle.dump([1], file)
