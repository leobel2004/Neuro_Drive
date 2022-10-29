import eel
import random
import time
import datetime


#initialisation main menu
@eel.expose
def cover_init():
    eel.init('web')
    eel.start('Cover.html')

@eel.expose
def Letter_test():
    return 1000


#generating random letters text for Letter_test
@eel.expose
def Letter_test_generate(timelimit):
    # strings for generation Letter_test.html
    letter_begin = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <title>Letter test</title>
        
    <script src="eel.js"></script>
    <link rel="icon" type="image/jpg" href="/favicon.jpg">
        
    <link rel="stylesheet" href="Letter_test.css">
    <link href="https://fonts.googleeapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
        
        
    <script type="text/javascript" src="/eel.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script type="text/javascript">
        async function finish(){
            eel.finish_Letter_test()();
            window.location.href = 'Letter_test_results.html';
        }
        
        async function right() {
            let string_now = document.getElementById('work_text').innerHTML;
            let res = await eel.right(string_now)();
            document.getElementById('work_text').innerHTML = res;
        }
        
        async function left() {
            let string_now = document.getElementById('work_text').innerHTML;
            let res = await eel.left(string_now)();
            document.getElementById('work_text').innerHTML = res;
        }
        
        async function up() {
            let string_now = document.getElementById('work_text').innerHTML;
            let res = await eel.up(string_now)();
            document.getElementById('work_text').innerHTML = res;
        }
        
        async function down() {
            let string_now = document.getElementById('work_text').innerHTML;
            let res = await eel.down(string_now)();
            document.getElementById('work_text').innerHTML = res;
        }
        
        document.addEventListener("keydown", function (event) {
            if (event.code == 'KeyD'){
                right();
        }
            if (event.code == 'KeyW'){
                up();
        }
            if (event.code == 'KeyS'){
                down();
        }
            if (event.code == 'KeyA'){
                left();
        }
            if (event.code == 'Escape'){
                window.location.href = '../Cover.html';
            }
            if (event.code == 'Enter'){
                finish();
            }
        });
    </script>
        
    <script type="text/javascript" id="timer_js">


        function formatTimeLeft(time) {
            const minutes = Math.floor(time / 60);
            let seconds = time % 60;
            if (seconds < 10) {
                seconds = `0${seconds}`;
            }
        
            return `${minutes}:${seconds}`;
        }
        
        
        var timeleft ='''
    letter_time = ''';
        var downloadTimer = setInterval(function(){
            if (timeleft != 100000000000){
            if(timeleft <= 0){
                clearInterval(downloadTimer);
                finish();
            } else {
                document.getElementById("timer").innerHTML = formatTimeLeft(timeleft);
            }
                timeleft -= 1;
                }else {
                    document.getElementById("timer").innerHTML = "+INF";
                }
            }, 1000);
        </script>
        
</head>
<body>
    <div id="header">
        <a href="../Cover.html" id="header_button"> Exit </a>
        <span id='header_text'> Letter test </span>
        <span id="timer">
            00:00
        </span>
    </div>
    <div align="center" id="main">
    <div id="work_text">
    '''
    letter_end = '''</div>
    </div>
</body>
</html>
    '''
    text = ''
    for i in range(5000):
        text += chr(ord('a') + random.randint(0, 25)) + ' '
    file = open('web/Letter_test/Letter_test.html', 'w')
    file.write(letter_begin)
    if timelimit:
        file.write(timelimit)
    else:
        file.write('100000000000')
    file.write(letter_time)
    file.write('<mark id="highlight">' + text[0] + "</mark>")
    file.write(text[1:])
    file.write(letter_end)
    file.close()
    global letter_text, letter_cash, time_start
    letter_text = text
    letter_cash = []
    time_start = time.time()
    return 0


#Letter_test text treatment
@eel.expose
def right(s): #click on KeyD
    global letter_cash
    letter_cash.append('right')
    l = s.split('<mark id="highlight">')
    new_s = l[0]
    new_s += l[1][0] + ' '
    new_s += '<mark id="highlight">' + l[1][9] + '</mark>' + l[1][10:]
    print('right')
    return new_s


@eel.expose
def up(s): #click on KeyW
    global letter_cash
    letter_cash.append('up')
    l = s.split('<mark id="highlight">')
    new_s = l[0]
    new_s += '<mark id="blue">' + l[1][0] + '</mark>' + ' '
    new_s += '<mark id="highlight">' + l[1][9] + '</mark>' + l[1][10:]
    print('up')
    return new_s


@eel.expose
def down(s): #click on KeyS
    global letter_cash
    letter_cash.append('down')
    l = s.split('<mark id="highlight">')
    new_s = l[0]
    new_s += '<mark id="red">' + l[1][0] + '</mark>' + ' '
    new_s += '<mark id="highlight">' + l[1][9] + '</mark>' + l[1][10:]
    print("down")
    return new_s


@eel.expose
def left(s): #click on KeyA
    global letter_cash
    letter_cash.append('left')
    l = s.split('<mark id="highlight">')
    if l[0].strip() == '':
        return s
    else:
        if l[0][-2] == '>':
            print(l[0])
            i = -2
            while l[0][i] != ' ':
                i -= 1
            new_s = l[0][:i] + ' id="highlight">' + l[0][-9:]
            new_s += l[1][0] + ' '
            new_s += l[1][9:]
            print(new_s)
            return new_s
        else:
            new_s = l[0][:-2] + '<mark id="highlight">' + l[0][-2] + '</mark>' + l[0][-1]
            new_s += l[1][0] + ' '
            new_s += l[1][9:]
            return new_s


@eel.expose
def get_letters(a, b):
    global red_letter, blue_letter
    red_letter = a if a else 'a'
    blue_letter = b if b else 'b'
    return 0


@eel.expose
def finish_Letter_test():
    global letter_cash, letter_text, red_letter, blue_letter, time_start
    results = ['''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Letter test</title>

    <script src="eel.js"></script>
    <script type="text/javascript" src="/eel.js"></script>
    <link rel="icon" type="image/jpg" href="/favicon.jpg">


    <link rel="stylesheet" href="Letter_test_results.css">
    <link href="https://fonts.googleeapis.com/css2?family=Roboto:wght@300;400;500&display=swap" rel="stylesheet">
    <script type="text\javascript">
        async function exit(){
            window.location.href = '../Cover.html';
        }
        
        document.addEventListener("keydown", function (event) {
            if (event.code == 'Enter'){
                window.location.href = '../Cover.html';
        }
            if (event.code == 'Escape'){
                window.location.href = '../Cover.html';
            }
        });
        
    </script>

</head>
<body>
<div align="center">
    <h1 >Results:</h1>
    <p class="name_of_res"> Total number of letters passed: <mark class="Num"> 
    ''', '''
</mark></p>
    <br>
    <p class="name_of_res"> Count of correct red letters: <mark class="Num">    
''', '''
</mark></p>
    <p class="name_of_res"> Count of incorrect red letters: <mark class="Num">
''','''
</mark></p>
    <p class="name_of_res"> Count of skipped red letters: <mark class="Num">
''', '''
</mark></p>
    <p class="name_of_res"> Total number of red letters: <mark class="Num">
''', '''
</mark></p>
<br>
    <p class="name_of_res"> Total percentage of correct red letters: <mark class="Num">
''', '''
</mark></p>
    <br>
    <p class="name_of_res"> Count of correct blue letters: <mark class="Num">
''', '''
</mark></p>
    <p class="name_of_res"> Count of incorrect blue letters: <mark class="Num">
''','''
</mark></p>
    <p class="name_of_res"> Count of skipped blue letters: <mark class="Num">
''', '''
</mark></p>
    <p class="name_of_res"> Total number of blue letters: <mark class="Num"> 
''', '''
</mark></p>
<br>
    <p class="name_of_res"> Total percentage of correct blue letters: <mark class="Num">
''', '''
</mark></p>
    <br>
    <p class="name_of_res"> Total failure: <mark class="Num">
''', '''
</mark></p>
    <p class="name_of_res"> Percentage of failures: <mark class="Num">
''', '''
</mark></p>
    <p class="name_of_res"> Total time(seconds): <mark class="Num">
''', '''
</mark></p>
    <a id="save_res" href="results.txt" download> Save results </a>
    <a href="../Cover.html" id='main_menu'> Main menu </a>
</div>
</body>
</html>
''']
    total_count = 0
    correct_red_letters = 0
    incorrect_red_letters = 0
    skipped_red_letters = 0
    correct_blue_letters = 0
    incorrect_blue_letters = 0
    skipped_blue_letters = 0
    actions = []
    try_time = time.time() - time_start
    for el in letter_cash:
        if el == 'left':
            actions.pop()
        elif el == 'right':
            actions.append(0)
        elif el == 'down':
            actions.append(1)
        else:
            actions.append(2)
    total_count = len(actions)
    for integer in range(total_count):
        if actions[integer] == 1:
            if letter_text[integer * 2] == red_letter:
                correct_red_letters += 1
            else:
                incorrect_red_letters += 1
        elif actions[integer] == 2:
            if letter_text[integer * 2] == blue_letter:
                correct_blue_letters += 1
            else:
                incorrect_blue_letters += 1
        else:
            if letter_text[integer * 2] == red_letter:
                skipped_red_letters += 1
            elif letter_text[integer * 2] == blue_letter:
                skipped_blue_letters += 1
    red_percent = correct_red_letters / (correct_red_letters + skipped_red_letters) * 100 if (correct_red_letters + skipped_red_letters) != 0 else 100
    blue_percent = correct_blue_letters / (correct_blue_letters + skipped_blue_letters) * 100 if (correct_blue_letters + skipped_blue_letters) != 0 else 100
    total_percent = (incorrect_red_letters + incorrect_blue_letters + skipped_red_letters + skipped_blue_letters) / total_count * 100
    file = open('web/Letter_test/Letter_test_results.html', 'w')
    file.write(results[0])
    file.write(str(total_count))
    file.write(results[1])
    file.write(str(correct_red_letters))
    file.write(results[2])
    file.write(str(incorrect_red_letters))
    file.write(results[3])
    file.write(str(skipped_red_letters))
    file.write(results[4])
    file.write(str(correct_red_letters + skipped_red_letters))
    file.write(results[5])
    file.write(str(round(red_percent, 1)) + ' %')
    file.write(results[6])
    file.write(str(correct_blue_letters))
    file.write(results[7])
    file.write(str(incorrect_blue_letters))
    file.write(results[8])
    file.write(str(skipped_blue_letters))
    file.write(results[9])
    file.write(str(correct_blue_letters + skipped_blue_letters))
    file.write(results[10])
    file.write(str(round(blue_percent, 1)) + ' %')
    file.write(results[11])
    file.write(str(incorrect_red_letters + incorrect_blue_letters + skipped_red_letters + skipped_blue_letters))
    file.write(results[12])
    file.write(str(round(total_percent)) + ' %')
    file.write(results[13])
    file.write(str(int(try_time)))
    file.write(results[14])
    file.close()
    file = open('web/Letter_test/results.txt', 'w')
    file.write("Total number of letters passed: "+ str(total_count) + '\n')
    file.write('Total failure: ' + str(incorrect_red_letters + incorrect_blue_letters + skipped_red_letters + skipped_blue_letters))
    file.write('Count of correct red letters: ' + str(correct_red_letters) + '\n')
    file.write('Count of incorrect red letters: ' + str(incorrect_red_letters) + '\n')
    file.write('Count of skipped red letters: ' + str(skipped_red_letters) + '\n')
    file.write('Total number of red letters: ' + str(correct_red_letters + skipped_red_letters) + '\n')
    file.write('Total percentage of correct red letters: ' + str(round(red_percent, 1)) + ' %' + '\n')
    file.write('Count of correct blue letters: ' + str(correct_blue_letters) + '\n')
    file.write('Count of incorrect blue letters: ' + str(incorrect_blue_letters) + '\n')
    file.write('Count of skipped blue letters: ' + str(skipped_blue_letters) + '\n')
    file.write('Total number of blue letters: ' + str(correct_blue_letters + skipped_blue_letters) + '\n')
    file.write('Total percentage of correct blue letters: ' + str(round(blue_percent, 1)) + ' %' + '\n')
    file.write('Total failure: ' + str(incorrect_red_letters + incorrect_blue_letters + skipped_red_letters + skipped_blue_letters) + '\n')
    file.write('Percentage of failures:' + str(round(total_percent)) + ' %' + '\n')
    file.write('Total time: ' + str(round(try_time, 1) - 1))
    file.close()
    return 0

@eel.expose
def change_theme():
    global Theme_color
    if Theme_color == 'white':
        Theme_color = 'black'
    else:
        Theme_color = 'white'


@eel.expose
def get_theme():
    global Theme_color
    return Theme_color

#functions for color test
@eel.expose
def Color_test_generate(timelimit):
    global Colors, words, words_colors, color_index, color_cash, time_start
    color_index = 0
    color_cash = []
    words = []
    words_colors = []
    if not(timelimit):
        timelimit = 70
    else:
        timelimit = int(timelimit)
    colors_pull = []
    for key in Colors:
        if Colors[key]:
            colors_pull.append(key)
    number_of_words = timelimit * 3
    for i in range(number_of_words):
        words.append(colors_pull[random.randint(0, len(colors_pull) - 1)])
        words_colors.append(colors_pull[random.randint(0, len(colors_pull) - 1)])
    file = open('web/Color_test/Color_test.html', 'w')
    file_ex = open('web/Color_test/Color_test_example.html', 'r')
    file.write(file_ex.read().replace('{timeleft}', str(timelimit)))
    file.close()
    file_ex.close()
    time_start = time.time()

@eel.expose
def finish_Color_test():
    global time_start, words, words_colors, color_cash
    example = open('web/Color_test/Color_test_results_example.html', 'r')
    res = open('web/Color_test/Color_test_results.html', 'w')
    results = open('web/Color_test/Color_test_results.txt', 'w')
    try_time = time.time() - time_start
    count = len(color_cash)
    correct_count = 0
    failure_count = 0
    for i in range(count):
        if words[i] == words_colors[i] and color_cash[i] == 'match':
            correct_count += 1
        elif words[i] != words_colors[i] and color_cash[i] == 'dismatch':
            correct_count += 1
        else:
            failure_count += 1
    string = example.read()
    string = string.replace('{Number_of_words}', str(count))
    string = string.replace('{Number_of_errors}', str(failure_count))
    string = string.replace('{Percent_of_errors}', str(round((failure_count / count if count else 1) * 100, 1)) + ' %')
    string = string.replace('{Total_time}', str(round(try_time, 0) - 1))
    res.write(string)
    results.write("Number of words: " + str(count) + '\n')
    results.write("Number of errors: " + str(failure_count) + '\n')
    results.write("Percentage of errors: " +  str(round((failure_count / count if count else 1) * 100, 1)) + ' %' + '\n')
    results.write('Total time: ' + str(round(try_time, 0) - 1))
    res.close()
    results.close()



@eel.expose
def color_match():
    global color_cash, color_index
    color_cash.append('match')
    color_index += 1

@eel.expose
def color_dismatch():
    global color_cash, color_index
    color_cash.append('dismatch')
    color_index += 1

@eel.expose
def get_word():
    global color_index, words, words_colors
    s = '<div class="'
    s += words_colors[color_index] + '"> ' + words[color_index] + '</div>'
    print(s)
    return s

@eel.expose
def change_colors(color):
    global Colors
    Colors[color] = not(Colors[color])

@eel.expose
def reset_colors():
    global Colors
    Colors = {'red': True, 'blue': True, 'green': True, 'yellow': True, 'purple': True, 'brown': True, 'white': True}


#functions for Array test
@eel.expose
def Array_test_generate(type, size, task, color):
    global time_start
    end = int(size) ** 2
    if type == 'simple':
        l = [f"<button class='{color}{size}' onclick='check_number({i + 1})' id='num{i + 1}'>{i + 1}</button>\n" for i in range(int(size) ** 2)]
    else:
        if task == 'white' or task == 'black':
            color1 = 'white'
            color2 = 'black'
            if task == 'black':
                color1, color2 = color2, color1
            l = [f"<button class='{color1 if i < ((end + 1) // 2) else color2}{size}' onclick='check_number({i + 1})' id='num{i + 1}'>{i % ((end + 1) // 2) + 1}</button>\n" for i in range(end)]
        else:
            color1 = 'white'
            color2 = 'black'
            if task == 'black_begin':
                color1, color2 = color2, color1
            l = [f"<button class='{(color2 if i % 2 else color1) if i <= (end + 1) // 2 or (end + 1) // 2 % 2 == 1 else (color1 if i % 2 else color2)}{size}' onclick='check_number({i + 1})' id='num{i + 1}'>{i + 1 if i <= (end + 1) // 2 else i - (end + 1) // 2 + 1}</button>\n" for i in range(end)]
            end = (end + 1) // 2
    random.shuffle(l)
    text = '<div class="work">\n'
    for i in range(int(size) ** 2):
        if i == int(size) ** 2:
            text += '</div>\n'
        elif i % int(size) == 0 and i != 0:
            text += '</div>\n<div class="work">\n'
        text += l[i]
    file = open('web/Array_test/Array_test.html', 'w')
    file_ex = open('web/Array_test/Array_test_example_simple.html', 'r')
    file.write((file_ex.read().replace('{work_text}', text)).replace("{end}", str(end)).replace('{type}', type).replace("{size}", size).replace("{task}", task))
    file.close()
    file_ex.close()
    time_start = time.time()

@eel.expose
def finish_Array_test(type, size, task, mistakes):
    timer = round(time.time() - time_start, 1)
    file = open('web/Array_test/Array_test_results.html', 'w')
    file_ex = open('web/Array_test/Array_test_results_example.html', 'r')
    txt_file = open('web/Array_test/Array_test_results.txt', 'w')
    text = file_ex.read()
    text = text.replace('{mistakes}', str(mistakes))
    text = text.replace('{type}', type)
    text = text.replace("{size}", size + " X " + size)
    text = text.replace('{timer}', str(timer))

    txt_file.write("Type: " + type + '\n')
    txt_file.write("Size: " + size + ' X ' + size + '\n')

    if type == 'double':
        task = 'all white cells -> all black cells'
        if task == 'black':
            task = 'all black cells -> all white cells'
        elif task == 'white_begin':
            task = "alternating white and black"
        elif task == 'black_begin':
            task = "alternating black and white"
        text_task = f'<p class="name_of_res" id="task"> Task: <mark class="Num"> {task} </mark></p>'
        text = text.replace('{task}', text_task)

        txt_file.write("Task: " + task + '\n')

    else:
        text = text.replace("{task}", '')

    txt_file.write("Total_time: " + str(timer) + '\n')
    txt_file.close()

    file.write(text)
    file.close()
    file_ex.close()


#functions for Reaction test
@eel.expose
def get_rt_time(time_rt, a, b, c, d, e, f):
    rt_time[0] = time_rt
    chances[0] = int(a)
    chances[1] = int(b)
    chances[2] = int(c)
    chances[3] = int(d)
    chances[4] = int(e)
    chances[5] = int(f)


@eel.expose
def Reaction_test_generate(count, colors, keys):
    name = 'web/Reaction_test/Reaction_test_' + str(count) + '_example.html'
    colors = list(colors.split())
    keys = list(keys.split(','))
    file_ex = open(name, 'r')
    file = open('web/Reaction_test/Reaction_test.html', 'w')
    text = file_ex.read()
    full_count[0] = int(count)
    for i in range(int(count)):
        if keys[i] != 'not':
            stimul_count[0] += 1
        n = str(i + 1)
        if chances[i] >= random.randint(0, 100):
            timer = random.randint(1, int(rt_time[0]))
        else:
            timer = 1000000000
        s_timer = '{timer_' + n + '}'
        key = '{key_' + n + '}'
        color = '{color_' + n + '}'
        text = text.replace(s_timer, str(timer))
        text = text.replace(key, "'" + keys[i] + "'")
        text = text.replace(color, "'" + colors[i] + "'")
    text = text.replace('{time}', rt_time[0])
    file.write(text)
    file.close()
    file_ex.close()


@eel.expose
def start_timer():
    global time_start
    time_start = time.time()


@eel.expose
def finish_timer():
    timer = time.time() - time_start
    results.append(timer)
    return str(round(timer, 3))

@eel.expose
def Reaction_test_finish(errors1, errors2):
    file = open('web/Reaction_test/Reaction_test_results.html', 'w')
    file_ex = open('web/Reaction_test/Reaction_test_results_example.html', 'r')
    text = file_ex.read()
    file_ex.close()
    text = text.replace('{total_time}', rt_time[0])
    text = text.replace('{best_time}', str(round(min(results), 3)))
    text = text.replace('{mean_time}', str(round(sum(results) / len(results), 3)))
    text = text.replace('{count_stimul}', str(stimul_count[0]))
    text = text.replace('{non_target_errors}', str(errors2) + ' / ' + str(round(int(errors2) / full_count[0], 2) * 100) + '%')
    text = text.replace('{target_errors}', str(errors1) + ' / ' + str(round(int(errors1) / stimul_count[0], 2) * 100) + '%')
    file.write(text)
    file.close()
    file = open('web/Reaction_test/results.txt', 'w')
    file.write(f'Time: {rt_time[0]} \n')
    file.write(f'Best Reaction Time: {str(round(min(results), 3))} \n')
    file.write(f'Average Reaction Time: {str(round(sum(results) / len(results), 3))} \n')
    file.write(f'Number of stimuli: {str(stimul_count[0])}\n')
    file.write(f'Error reactions to distractors: {str(errors2) + " / " + str(round(int(errors2) / full_count[0], 2) * 100) + "%"}\n')
    file.write(f'Error reactions to targeted stimuli:{errors1}\n')
    file.close()
    file = open('web/Reaction_test/statistics.txt', 'w')
    file.write('Times :\n')
    for el in results:
        file.write(str(el) + '\n')
    file.close()














#letter_test variables
letter_text = ''
letter_cash = []
blue_letter = 'a'
red_letter = 'b'

time_start = 0
Theme_color = 'black'

#color_test variables
Colors = {'red': True, 'blue': True, 'green': True, 'yellow': True, 'purple': True, 'brown': True, 'white': True}
words = []
words_colors = []
index = 0
color_cash = []

#reaction_test variables
rt_time = [10]
chances = [100, 100, 100, 100, 100, 100]
results = []
stimul_count = [0]
full_count = [0]


# initialisation app
cover_init()
# Array_test_generate('simple', '10', ' ', 'white')
