from tkinter import *
import math

binding_file = 'engineer_keys.txt'

#===================
#   def list
#===================
def save_bindings():

    with open(binding_file, 'w') as file:
        file.write(str(sin_key) + '\n')
        file.write(str(cos_key) + '\n')
        file.write(str(tan_key) + '\n')
        file.write(str(log_key) + '\n')
        file.write(str(ln_key) + '\n')
        file.write(str(power_key) + '\n')
        file.write(str(pi_key) + '\n')
        file.write(str(e_key) + '\n')
        file.write(str(factorial_key) + '\n')
        file.write(str(angle_key) + '\n')
        file.write(str(sqrt_key) + '\n')
        file.write(str(square_key) + '\n')


def load_bindings():

    global sin_key, cos_key, tan_key
    global log_key, ln_key, power_key
    global pi_key, e_key, factorial_key
    global angle_key, sqrt_key, square_key

    try:
        with open(binding_file, 'r') as file:

            sin_key = file.readline().strip()
            cos_key = file.readline().strip()
            tan_key = file.readline().strip()
            log_key = file.readline().strip()
            ln_key = file.readline().strip()
            power_key = file.readline().strip()
            pi_key = file.readline().strip()
            e_key = file.readline().strip()
            factorial_key = file.readline().strip()
            angle_key = file.readline().strip()
            sqrt_key = file.readline().strip()
            square_key = file.readline().strip()

        if sin_key == 'None':
            sin_key = None

        if cos_key == 'None':
            cos_key = None

        if tan_key == 'None':
            tan_key = None

        if log_key == 'None':
            log_key = None

        if ln_key == 'None':
            ln_key = None

        if power_key == 'None':
            power_key = None

        if pi_key == 'None':
            pi_key = None

        if e_key == 'None':
            e_key = None

        if factorial_key == 'None':
            factorial_key = None

        if angle_key == 'None':
            angle_key = None

        if sqrt_key == 'None':
            sqrt_key = None

        if square_key == 'None':
            square_key = None

    except FileNotFoundError:
        pass

def binding_text(key):

    if key is None:
        return 'not bound'

    return key

def show_engineer_bindings():
    binding_window = Toplevel(cal)
    binding_window.title('Engineer Key Bindings')
    binding_window.geometry('400x500')
    binding_window.transient(cal)

    if dark_mode_on:
        bg = 'gray20'
        fg = 'white'
    else:
        bg = 'white'
        fg = 'black'

    binding_window.configure(bg=bg)

    title_label = Label(
        binding_window,
        text='Engineer Key Bindings',
        font=('Arial', 18),
        bg=bg,
        fg=fg
    )
    title_label.pack(
        fill=X,
        padx=10,
        pady=10
    )

    def choose_key(function_name, label):

        label.configure(
            text=f'{function_name} : press a key...'
        )

        binding_window.focus_set()


        def get_key(event):

            global sin_key, cos_key, tan_key
            global log_key, ln_key, power_key
            global pi_key, e_key, factorial_key
            global angle_key, sqrt_key, square_key

            binding_window.unbind('<Key>', binding_id)

            if event.keysym == 'Escape':
                label.configure(
                    text=f'{function_name} : not bound'
                )
                return 'break'

            label.configure(
                text=f'{function_name} : {event.keysym}'
            )

            if function_name == 'sin':
                sin_key = event.keysym

            elif function_name == 'cos':
                cos_key = event.keysym

            elif function_name == 'tan':
                tan_key = event.keysym

            elif function_name == 'log':
                log_key = event.keysym

            elif function_name == 'ln':
                ln_key = event.keysym

            elif function_name == 'xʸ':
                power_key = event.keysym

            elif function_name == 'π':
                pi_key = event.keysym

            elif function_name == 'e':
                e_key = event.keysym

            elif function_name == 'x!':
                factorial_key = event.keysym

            elif function_name == 'DEG/RAD':
                angle_key = event.keysym

            elif function_name == '√':
                sqrt_key = event.keysym

            elif function_name == 'x²':
                square_key = event.keysym

            return 'break'
        
        binding_id = binding_window.bind('<Key>', get_key)


    sin_label = Label(
        binding_window,
        text=f'sin : {binding_text(sin_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    sin_label.pack(fill=X, padx=20, pady=3)

    sin_label.bind(
        '<Button-1>',
        lambda event: choose_key('sin', sin_label)
    )


    cos_label = Label(
        binding_window,
        text=f'cos : {binding_text(cos_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    cos_label.pack(fill=X, padx=20, pady=3)

    cos_label.bind(
        '<Button-1>',
        lambda event: choose_key('cos', cos_label)
    )


    tan_label = Label(
        binding_window,
        text=f'tan : {binding_text(tan_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    tan_label.pack(fill=X, padx=20, pady=3)

    tan_label.bind(
        '<Button-1>',
        lambda event: choose_key('tan', tan_label)
    )


    log_label = Label(
        binding_window,
        text=f'log : {binding_text(log_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    log_label.pack(fill=X, padx=20, pady=3)

    log_label.bind(
        '<Button-1>',
        lambda event: choose_key('log', log_label)
    )


    ln_label = Label(
        binding_window,
        text=f'ln : {binding_text(ln_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    ln_label.pack(fill=X, padx=20, pady=3)

    ln_label.bind(
        '<Button-1>',
        lambda event: choose_key('ln', ln_label)
    )


    power_label = Label(
        binding_window,
        text=f'xʸ : {binding_text(power_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    power_label.pack(fill=X, padx=20, pady=3)

    power_label.bind(
        '<Button-1>',
        lambda event: choose_key('xʸ', power_label)
    )


    pi_label = Label(
        binding_window,
        text=f'π : {binding_text(pi_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    pi_label.pack(fill=X, padx=20, pady=3)

    pi_label.bind(
        '<Button-1>',
        lambda event: choose_key('π', pi_label)
    )


    e_label = Label(
        binding_window,
        text=f'e : {binding_text(e_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    e_label.pack(fill=X, padx=20, pady=3)

    e_label.bind(
        '<Button-1>',
        lambda event: choose_key('e', e_label)
    )


    factorial_label = Label(
        binding_window,
        text=f'x! : {binding_text(factorial_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    factorial_label.pack(fill=X, padx=20, pady=3)

    factorial_label.bind(
        '<Button-1>',
        lambda event: choose_key('x!', factorial_label)
    )


    angle_label = Label(
        binding_window,
        text=f'DEG/RAD : {binding_text(angle_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    angle_label.pack(fill=X, padx=20, pady=3)

    angle_label.bind(
        '<Button-1>',
        lambda event: choose_key('DEG/RAD', angle_label)
    )


    sqrt_label = Label(
        binding_window,
        text=f'√ : {binding_text(sqrt_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    sqrt_label.pack(fill=X, padx=20, pady=3)

    sqrt_label.bind(
        '<Button-1>',
        lambda event: choose_key('√', sqrt_label)
    )


    square_label = Label(
        binding_window,
        text=f'x² : {binding_text(square_key)}',
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        anchor='w'
    )
    square_label.pack(fill=X, padx=20, pady=3)

    square_label.bind(
        '<Button-1>',
        lambda event: choose_key('x²', square_label)
    )
    

    
    
def remove_extra_zero(number):
    
    if number == 'error':
        return number

    if number == int(number):
        return int(number)

    return number

    
def add_history(expression, result):
    history.append((expression, str(result)))


def show_history():
    history_window = Toplevel(cal)
    history_window.title('History')
    history_window.geometry('400x500')
    history_window.transient(cal)

    if dark_mode_on:
        bg = 'gray20'
        fg = 'white'
        button_bg = 'gray30'
    else:
        bg = 'white'
        fg = 'black'
        button_bg = 'gray90'

    history_window.configure(bg=bg)

    history_list = Listbox(
        history_window,
        font=('Arial', 14),
        bg=bg,
        fg=fg,
        selectbackground='gray50',
        selectforeground='white'
    )
    history_list.pack(
        fill=BOTH,
        expand=True,
        padx=10,
        pady=10
    )

    # Newest calculation at the top
    history_items = list(reversed(history))

    for expression, result in history_items:
        history_list.insert(
            END,
            f'{expression} = {result}'
        )

    def use_history(event=None):
        selected = history_list.curselection()

        if selected:
            result = history_items[selected[0]][1]

            LCD.delete(0, END)
            LCD.insert(END, result)

            history_window.destroy()

    history_list.bind('<Double-Button-1>', use_history)

    def clear_history():
        history.clear()
        history_list.delete(0, END)

    clear_history_btn = Button(
        history_window,
        text='Clear History',
        font=('Arial', 14),
        command=clear_history,
        bg=button_bg,
        fg=fg
    )
    clear_history_btn.pack(
        fill=X,
        padx=10,
        pady=(0, 10)
    )

    
def standard_toggle():
    engineer_panel.grid_remove()

    calculator_frame.grid(
        row=1,
        column=0,
        columnspan=4,
        rowspan=7,
        sticky='nsew'
    )
    

def toggle_dark_mode():
    global dark_mode_on

    dark_mode_on = not dark_mode_on

    if dark_mode_on:
        bg = '#202124'
        button_bg = '#303134'
        fg = 'white'

        cal.configure(bg=bg)
        topbar.configure(bg=bg)
        LCD.configure(
            bg='#202124',
            fg=fg,
            insertbackground=fg
        )

        for button in standard_buttons:
            button.configure(
                bg=button_bg,
                fg=fg,
                activebackground='#404144',
                activeforeground=fg
            )

        for button in top_buttons:
            button.configure(
                bg=button_bg,
                fg=fg,
                activebackground='#404144',
                activeforeground=fg
            )
        for button in engineer_buttons:
            button.configure(
                bg=button_bg,
                fg=fg,
                activebackground='#404144',
                activeforeground=fg
            )

        darkbtn.configure(text='☀ Light')

    else:
        bg = 'gray26'
        button_bg = 'white'
        fg = 'black'

        cal.configure(bg=bg)
        topbar.configure(bg=bg)
        LCD.configure(
            bg='white',
            fg=fg,
            insertbackground=fg
        )

        for button in standard_buttons:
            button.configure(
                bg=button_bg,
                fg=fg,
                activebackground='#dddddd',
                activeforeground=fg
            )

        for button in top_buttons:
            button.configure(
                bg=button_bg,
                fg=fg,
                activebackground='#dddddd',
                activeforeground=fg
                )
                
        for button in engineer_buttons:
            button.configure(
                bg=button_bg,
                fg=fg,
                activebackground='#dddddd',
                activeforeground=fg
            )

        darkbtn.configure(text='☾ Dark')
    

##cal.resizable(True,True)  


def operator_select(operate):
    global number1, operator, new_number, recently_calculated, history

    if recently_calculated:
        number1 = float(LCD.get())
        operator = operate
        recently_calculated = False
        LCD.delete(0, END)
        new_number = True
        expression_label.configure(
                text=f'{number1} {operate}'
            )


    elif operator == None:
        number1 = float(LCD.get())
        operator = operate
        expression_label.config(
            text=f'{number1} {operate}'
        )

        LCD.delete(0, END)
        new_number = True
    else:
        result = calculate()
        number1 = result
        operator = operate

        expression_label.config(
        text=f'{number1} {operate}'
        )

        LCD.delete(0, END)
        new_number = True
              

resizing_screen = None

def resize_font(event):
    global resizing_screen

    if resizing_screen is not None:
        cal.after_cancel(resizing_screen)

    resizing_screen = cal.after(200, apply_font_size)


def apply_font_size():

    size = max(12, int(min(cal.winfo_width(), cal.winfo_height()) / 20))

    top_size = max(10, int(size * 0.5))
    expression_size = max(10, int(size * 0.5))

    for button in standard_buttons:
        button.config(font=('Arial', size))

    for button in engineer_buttons:
        button.config(font=('Arial', size))

    for button in top_buttons:
        button.config(font=('Arial', top_size))

    expression_label.configure(font=('Arial', expression_size))
    LCD.config(font=('Arial', size))


    
def key_press(event):

    if event.keysym in '0123456789':
        number_click(event.keysym)

    elif event.keysym in '+-/*':
        operator_select(event.keysym)

    elif event.keysym == sin_key:
        sin_click()

    elif event.keysym == cos_key:
        cos_click()

    elif event.keysym == tan_key:
        tan_click()

    elif event.keysym == log_key:
        log_click()

    elif event.keysym == ln_key:
        ln_click()

    elif event.keysym == power_key:
        power_operator()

    elif event.keysym == pi_key:
        pi_click()

    elif event.keysym == e_key:
        e_click()

    elif event.keysym == factorial_key:
        factorial_click()

    elif event.keysym == angle_key:
        toggle_angle_mode()

    elif event.keysym == sqrt_key:
        radical_click()

    elif event.keysym == square_key:
        square_click()

    

    
def number_click(number):
    global new_number, recently_calculated
    if recently_calculated:
        expression_label.config(
            text=f'')
        recently_calculated = False

        
    if new_number:
        LCD.delete(0, END)
        new_number = False
    LCD.insert(END,number)



def decimal_click(event=None):
    global new_number
    if new_number== True:
        
        LCD.delete(0, END)
        if '.' not in LCD.get():
            LCD.insert(END, '.')
            new_number= False
    else:
        if '.' not in LCD.get():
            LCD.insert(END, '.')
        
        

def clear_click(event=None):
    global operator, new_number, number1, recently_calculated
    number1=None
    operator=None
    new_number= True
    recently_calculated=False
    LCD.delete(0, END)
    expression_label.configure(text='')
    
def calculate():
    global new_number, number1, result, number2, history
    if operator == '+':
        number2 = float(LCD.get())
        result=number1 + number2
        return result

    elif operator == '-':
        number2 = float(LCD.get())
        result=number1 - number2
        return result

    elif operator == '*':
        number2 = float(LCD.get())
        result=number1 * number2
        return result

    elif operator == '/':
        number2 = float(LCD.get())
        try:
            result=number1 / number2
            return result
        except ZeroDivisionError:
            result='error'
            return result
        
    elif operator == '^':
        number2 = float(LCD.get())
        result = number1 ** number2
        return result
            

def backspace_click(event=None):
     if LCD.get():
        LCD.delete(len(LCD.get()) - 1, END)

def clear_entry():
    LCD.delete(0, END)



def equal_click(event=None):
    global new_number, number1, operator, repeat, recently_calculated, history
    
    if operator ==None:
        return
    
    if new_number:
        
        if operator == '+':
            result = number1 + repeat
        elif operator == '-':
            result = number1 - repeat
        elif operator == '*':
            result = number1 * repeat
        elif operator == '/':
            try:
                result = number1 / repeat
            except ZeroDivisionError:
                result = 'error'
        elif operator == '^':
            result = number1 ** repeat
        
        number1 = result
        recently_calculated=True
        expression_label.configure(
        text=f'{number1}{operator} {repeat}'
            )
        

    else:

        result = calculate()
        add_history(f'{number1} {operator} {number2}', remove_extra_zero(result))
        number1 = result
        repeat = number2
        recently_calculated=True

##def show_result(result):
##    LCD.delete(0, END)
##    LCD.insert(END, result)
 
        
        

##        operator=None
    
                
##    result= calculate()
##    number1= result
##    repeat= number2
##    operator=None
##    print(repeat)

            

    LCD.delete(0, END)
    LCD.insert(END, remove_extra_zero(result))
    new_number = True

        
def square_click():
    global new_number
    
    number1=float(LCD.get())
    LCD.delete(0, END)
    result=number1 * number1
    LCD.insert(END, remove_extra_zero(result))
    new_number = True

def radical_click():
    global new_number
    
    number1=float(LCD.get())
    LCD.delete(0, END)
    try:
        result=math.sqrt(number1)
    except ValueError:
        result='error'
    LCD.insert(END, remove_extra_zero(result))
    new_number = True

def reciprocal_click():
    global new_number
    
    number1=float(LCD.get())
    LCD.delete(0, END)
    try:
        result= 1 / number1
    except ZeroDivisionError:
        result='error'
    LCD.insert(END, remove_extra_zero(result))
    new_number = True
    
def negative_positive():
    number1=float(LCD.get())
    result= -number1
    LCD.delete(0, END)
    LCD.insert(END, remove_extra_zero(result))

def percentage_click():
    global new_number,number2, number1
    
    number2=float(LCD.get())
    
    if number1 != None:
        percentage= number1 * (number2/ 100)

    else:
         percentage = number2 / 100
    LCD.delete(0, END)
    LCD.insert(END, remove_extra_zero(percentage))

def engineer_mode():
    engineer_panel.grid(
        row=1,
        column=0,
        rowspan=7,
        sticky='nsew'
    )

    calculator_frame.grid(
        row=1,
        column=1,
        columnspan=3,
        rowspan=7,
        sticky='nsew'
    )

def toggle_angle_mode():
    global angle_mode

    if angle_mode == 'DEG':
        angle_mode = 'RAD'
        anglebtn.config(text='RAD')
    else:
        angle_mode = 'DEG'
        anglebtn.config(text='DEG')
        
#==================
#   engineer buttons
#==================
def get_angle(number):
    if angle_mode == 'DEG':
        return math.radians(number)
    else:
        return number

def sin_click():
    global new_number

    try:
        number = float(LCD.get())
        result = math.sin(get_angle(number))

    except (ValueError, OverflowError):
        result = 'error'

    add_history(f'sin({number})', result)

    LCD.delete(0, END)
    LCD.insert(END, result)
    new_number = True


def cos_click():
    global new_number

    try:
        number = float(LCD.get())
        result = math.cos(get_angle(number))

    except (ValueError, OverflowError):
        result = 'error'

    add_history(f'cos({number})', result)

    LCD.delete(0, END)
    LCD.insert(END, result)
    new_number = True


def tan_click():
    global new_number

    try:
        number = float(LCD.get())
        result = math.tan(get_angle(number))

    except (ValueError, OverflowError):
        result = 'error'

    add_history(f'tan({number})', result)

    LCD.delete(0, END)
    LCD.insert(END, result)
    new_number = True


def log_click():
    global new_number

    number = float(LCD.get())

    try:
        result = math.log10(number)
    except ValueError:
        result = 'error'

    add_history(f'log({number})', result)

    LCD.delete(0, END)
    LCD.insert(END, result)
    new_number = True


def ln_click():
    global new_number

    number = float(LCD.get())

    try:
        result = math.log(number)
    except ValueError:
        result = 'error'

    add_history(f'ln({number})', result)

    LCD.delete(0, END)
    LCD.insert(END, result)
    new_number = True


def pi_click():
    global new_number

    LCD.delete(0, END)
    LCD.insert(END, math.pi)
    new_number = True


def e_click():
    global new_number

    LCD.delete(0, END)
    LCD.insert(END, math.e)
    new_number = True


def factorial_click():
    global new_number

    try:
        number = int(float(LCD.get()))

        if number < 0:
            result = 'error'
        else:
            result = math.factorial(number)

    except (ValueError, OverflowError):
        result = 'error'

    LCD.delete(0, END)
    LCD.insert(END, result)
    new_number = True


def power_operator():
    global number1, operator, new_number

    number1 = float(LCD.get())
    operator = '^'

    expression_label.configure(
        text=f'{number1} ^'
    )

    LCD.delete(0, END)
    new_number = True

def save_and_close():

    save_bindings()
    cal.destroy()
    
#==================
#   variable
#==================
number1=None
operator=None
new_number = True
repeat=None
number2=None
recently_calculated= False
dark_mode_on=False
angle_mode = 'DEG'
history = []
#===================
#   main GUI
#===================
cal=Tk()
cal.title('standard calculator')
##win.iconbitmap('money.ico')
cal.geometry('800x600+300+100')
cal.minsize(400,300)
cal.configure(bg='gray26')
cal.state('normal')
cal.overrideredirect('false')
cal.resizable(True,True)


#===================
#   top bar
#===================

topbar = Frame(cal, bg='gray26')
topbar.grid(row=0, column=0, columnspan=4, sticky='nsew')

cal.rowconfigure(0, weight=0)

for column in range(5):
    topbar.columnconfigure(column, weight=1)

standardbtn = Button(
    topbar,
    text='Standard',
    font=('Arial', 14),
    command=standard_toggle
)

engineerbtn = Button(
    topbar,
    text='⚙ Engineer',
    font=('Arial', 14),
    command=engineer_mode
)

engineerkeysbtn = Button(
    topbar,
    text='⌨ Engineer Keys',
    font=('Arial', 14),
    command=show_engineer_bindings
)

darkbtn = Button(
    topbar,
    text='☾ Dark',
    font=('Arial', 14),
    command=toggle_dark_mode
)

historybtn = Button(
    topbar,
    text='🕘 History',
    font=('Arial', 14),
    command=show_history
)

standardbtn.grid(row=0, column=0, sticky='nsew')
engineerbtn.grid(row=0, column=1, sticky='nsew')
darkbtn.grid(row=0, column=2, sticky='nsew')
historybtn.grid(row=0, column=3, sticky='nsew')
engineerkeysbtn.grid(row=0, column=4, sticky='nsew')

top_buttons = [
    standardbtn,
    engineerbtn,
    darkbtn,
    historybtn,
    engineerkeysbtn
    
]

calculator_frame = Frame(
    cal,
    bg='gray26'
)
#==================
#   engineer mode
#==================
engineer_panel = Frame(
    cal,
    bg='gray26'

)
calculator_frame.grid(
    row=1,
    column=0,
    columnspan=4,
    rowspan=7,
    sticky='nsew'
)


sinbtn = Button(
    engineer_panel,
    text='sin',
    font=('Arial', 18),
    command=sin_click
)

cosbtn = Button(
    engineer_panel,
    text='cos',
    font=('Arial', 18),
    command=cos_click
)

tanbtn = Button(
    engineer_panel,
    text='tan',
    font=('Arial', 18),
    command=tan_click
)

logbtn = Button(
    engineer_panel,
    text='log',
    font=('Arial', 18),
    command=log_click
)

lnbtn = Button(
    engineer_panel,
    text='ln',
    font=('Arial', 18),
    command=ln_click
)

powerengineerbtn = Button(
    engineer_panel,
    text='xʸ',
    font=('Arial', 18),
    command=power_operator
)

pibtn = Button(
    engineer_panel,
    text='π',
    font=('Arial', 18),
    command=pi_click
)

ebtn = Button(
    engineer_panel,
    text='e',
    font=('Arial', 18),
    command=e_click
)

factorialbtn = Button(
    engineer_panel,
    text='x!',
    font=('Arial', 18),
    command=factorial_click
)

anglebtn = Button(
    engineer_panel,
    text='DEG',
    font=('Arial', 18),
    command=toggle_angle_mode
)

sqrtengineerbtn = Button(
    engineer_panel,
    text='√',
    font=('Arial', 18),
    command=radical_click
)

squareengineerbtn = Button(
    engineer_panel,
    text='x²',
    font=('Arial', 18),
    command=square_click
)

anglebtn.grid(row=0, column=0, sticky='nsew')
sinbtn.grid(row=0, column=1, sticky='nsew')
cosbtn.grid(row=0, column=2, sticky='nsew')
tanbtn.grid(row=0, column=3, sticky='nsew')

logbtn.grid(row=1, column=0, sticky='nsew')
lnbtn.grid(row=1, column=1, sticky='nsew')
powerengineerbtn.grid(row=1, column=2, sticky='nsew')
pibtn.grid(row=1, column=3, sticky='nsew')

ebtn.grid(row=2, column=0, sticky='nsew')
factorialbtn.grid(row=2, column=1, sticky='nsew')
sqrtengineerbtn.grid(row=2, column=2, sticky='nsew')
squareengineerbtn.grid(row=2, column=3, sticky='nsew')

for row in range(3):
    engineer_panel.rowconfigure(row, weight=1)

for column in range(4):
    engineer_panel.columnconfigure(column, weight=1)



#===================
#   LCD
#===================
LCD = Entry(
    calculator_frame,
    font=('Arial', 30),
    justify='right',
    )

expression_label = Label(
    calculator_frame,
    text='',
    font=('Arial', 14),
    anchor='e',
    bg='white',
    fg='gray'
)
expression_label.grid(
    row=1,
    column=0,
    columnspan=4,
    sticky='nsew'
)
#===================
#   number Buttons
#===================
btn0=Button(calculator_frame,
           text= '0',
           font=('Arial',24),
            command=lambda: number_click('0')
           )
btn1=Button(calculator_frame,
           text= '1',
           font=('Arial',24),
           command=lambda: number_click('1')
           )
btn2=Button(calculator_frame,
           text= '2',
           font=('Arial',24),
           command=lambda: number_click('2')
           )
btn3=Button(calculator_frame,
           text= '3',
           font=('Arial',24),
            command=lambda: number_click('3')
           )
btn4=Button(calculator_frame,
           text= '4',
           font=('Arial',24),
            command=lambda: number_click('4')
           )
btn5=Button(calculator_frame,
           text= '5',
           font=('Arial',24),
            command=lambda: number_click('5')
           )
btn6=Button(calculator_frame,
           text= '6',
           font=('Arial',24),
            command=lambda: number_click('6')
           )
btn7=Button(calculator_frame,
           text= '7',
           font=('Arial',24),
            command=lambda: number_click('7')
           )
btn8=Button(calculator_frame,
           text= '8',
           font=('Arial',24),
            command=lambda: number_click('8')
           )
btn9=Button(calculator_frame,
           text= '9',
           font=('Arial',24),
            command=lambda: number_click('9')
           )

#===================
#   standard buttons
#===================
plusbtn=Button(calculator_frame,
           text= '+',
           font=('Arial',24),
           command =lambda: operator_select('+')
           )

minusbtn=Button(calculator_frame,
           text= '-',
           font=('Arial',24),
           command=lambda: operator_select('-')
            )

dividebtn=Button(calculator_frame,
           text= '÷',
           font=('Arial',24),
           command= lambda: operator_select('/')    
           )

multibtn=Button(calculator_frame,
           text= '×',
           font=('Arial',24),
           command= lambda: operator_select('*')   
           )

percentagebtn=Button(calculator_frame,
           text= '%',
           font=('Arial',24),
           command= percentage_click
           )


plusorminusbtn=Button(calculator_frame,
           text= '±',
           font=('Arial',24),
           command=negative_positive
           )

clearbackbtn=Button(calculator_frame,
           text= '⌫',
           font=('Arial',24),
           command=backspace_click
           )

decimalbtn=Button(calculator_frame,
           text= '.',
           font=('Arial',24),
           command= decimal_click
           )
    
equalbtn=Button(calculator_frame,
           text= '=',
           font=('Arial',24),
           command = equal_click
           )
fullclearbtn=Button(calculator_frame,
           text= 'C',
           font=('Arial',24),
           command= clear_click
           )
clearentrybtn=Button(calculator_frame,
           text= 'CE',
           font=('Arial',24),
           command= clear_entry
           )

radicalbtn=Button(calculator_frame,
           text= '√',
           font=('Arial',24),
           command= radical_click
           )
powerbtn=Button(calculator_frame,
           text= 'x²',
           font=('Arial',24),
           command =square_click
           )
reciprocalbtn=Button(calculator_frame,
           text= '1/x',
           font=('Arial',24),
           command= reciprocal_click
           )
#=================
#   Special button
#=================
                   
                   


#=======================
#   configure placement
#=======================
for column in range(4):
    cal.columnconfigure(column, weight=1)


for row in range(1, 8):
    cal.rowconfigure(row, weight=1)

for column in range(4):
    calculator_frame.columnconfigure(column, weight=1)

for row in range(8):
    calculator_frame.rowconfigure(row, weight=1)

#===================
#   LCD placement
#===================
LCD.grid(row=0, column=0,columnspan=4, sticky='nsew')
#===================
#   binds
#===================
##btn0.bind('<0>', lambda: number_click('0'))
cal.bind('<Key>', key_press)
cal.bind('<Return>', equal_click)
cal.bind('<BackSpace>', backspace_click)
cal.bind('<.>', decimal_click)
cal.bind('<Escape>', clear_click)

#engineer keybinding
sin_key = None
cos_key = None
tan_key = None
log_key = None
ln_key = None
power_key = None
pi_key = None
e_key = None
factorial_key = None
angle_key = None
sqrt_key = None
square_key = None

load_bindings()

standard_buttons = [
    btn0, btn1, btn2, btn3, btn4,
    btn5, btn6, btn7, btn8, btn9,
    plusbtn, minusbtn, dividebtn, multibtn,
    percentagebtn, plusorminusbtn,
    clearbackbtn, decimalbtn, equalbtn,
    fullclearbtn, clearentrybtn, powerbtn,
    radicalbtn,reciprocalbtn
    ]
engineer_buttons = [sinbtn,cosbtn,tanbtn,
                    logbtn,lnbtn,powerengineerbtn,
                    pibtn,ebtn, factorialbtn,
                    sqrtengineerbtn,squareengineerbtn,
                    anglebtn]
cal.bind('<Configure>', resize_font)

##def keyboard_input(event):
##    print(event.keysym)
##cal.bind('<Key>', keyboard_input)

#===================
#   num placement
#===================
btn1.grid(
    row=6,
    column=0,
    sticky='nsew')
btn4.grid(
    row=5,
    column=0,
    sticky='nsew')
btn7.grid(
    row=4,
    column=0,
    sticky='nsew')

btn8.grid(
    row=4,
    column=1,
    sticky='nsew')
btn5.grid(
    row=5,
    column=1,
    sticky='nsew')
btn2.grid(
    row=6,
    column=1,
    sticky='nsew')

btn9.grid(
    row=4,
    column=2,
    sticky='nsew')
btn6.grid(
    row=5,
    column=2,
    sticky='nsew')
btn3.grid(
    row=6,
    column=2,
    sticky='nsew')

plusorminusbtn.grid(row=7, column=0, sticky='nsew')
btn0.grid(row=7, column=1, sticky='nsew')
decimalbtn.grid(row=7, column=2, sticky='nsew')

dividebtn.grid(row=3, column=3, sticky='nsew')
multibtn.grid(row=4, column=3, sticky='nsew')
minusbtn.grid(row=5, column=3, sticky='nsew')
plusbtn.grid(row=6, column=3, sticky='nsew')
equalbtn.grid(row=7, column=3, sticky='nsew')

percentagebtn.grid(row=2, column=0, sticky='nsew')
clearentrybtn.grid(row=2, column=1, sticky='nsew')
fullclearbtn.grid(row=2, column=2, sticky='nsew')
clearbackbtn.grid(row=2, column=3, sticky='nsew')

powerbtn.grid(row=3, column=2, sticky='nsew')
radicalbtn.grid(row=3, column=1, sticky='nsew')
reciprocalbtn.grid(row=3, column=0, sticky='nsew')
#===================
#   num placement
#===================
cal.protocol('WM_DELETE_WINDOW', save_and_close)

cal.mainloop()



