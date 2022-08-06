import eel
import random
import time


#initialisation main menu
@eel.expose
def cover_init():
    eel.init('web')
    eel.start('Cover.html', size=(520, 480))

@eel.expose
def Letter_test():
    print('you are looser')
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
            eel.debag()();
            window.location.href = 'Letter_test_results.html';
            eel.debag()();
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
    print('shalom')
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
    red_percent = correct_red_letters / (correct_red_letters + skipped_red_letters) * 1000 if (correct_red_letters + skipped_red_letters) != 0 else 1
    blue_percent = correct_blue_letters / (correct_blue_letters + skipped_blue_letters) * 1000 if (correct_blue_letters + skipped_blue_letters) != 0 else 1
    total_percent = (incorrect_red_letters + incorrect_blue_letters + skipped_red_letters + skipped_blue_letters) / total_count * 1000
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
    file.write((str(int(red_percent))[:-1] + '.' + str(int(red_percent))[-1] if red_percent != 0 else '0')  + ' %')
    file.write(results[6])
    file.write(str(correct_blue_letters))
    file.write(results[7])
    file.write(str(incorrect_blue_letters))
    file.write(results[8])
    file.write(str(skipped_blue_letters))
    file.write(results[9])
    file.write(str(correct_blue_letters + skipped_blue_letters))
    file.write(results[10])
    file.write((str(int(blue_percent))[:-1] + '.' + str(int(blue_percent))[-1] if blue_percent != 0 else '0') + ' %')
    file.write(results[11])
    file.write(str(incorrect_red_letters + incorrect_blue_letters + skipped_red_letters + skipped_blue_letters))
    file.write(results[12])
    file.write(str(int(total_percent))[:-1] + '.' + str(int(total_percent))[-1] + ' %')
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
    file.write('Total percentage of correct red letters: ' + (str(int(red_percent))[:-1] + '.' + str(int(red_percent))[-1] if red_percent != 0 else '0')  + ' %' + '\n')
    file.write('Count of correct blue letters: ' + str(correct_blue_letters) + '\n')
    file.write('Count of incorrect blue letters: ' + str(incorrect_blue_letters) + '\n')
    file.write('Count of skipped blue letters: ' + str(skipped_blue_letters) + '\n')
    file.write('Total number of blue letters: ' + str(correct_blue_letters + skipped_blue_letters) + '\n')
    file.write('Total percentage of correct blue letters: ' + (str(int(blue_percent))[:-1] + '.' + str(int(blue_percent))[-1] if blue_percent != 0 else '0') + ' %' + '\n')
    file.write('Total failure: ' + str(incorrect_red_letters + incorrect_blue_letters + skipped_red_letters + skipped_blue_letters) + '\n')
    file.write('Percentage of failures:' + str(incorrect_red_letters + incorrect_blue_letters + skipped_red_letters + skipped_blue_letters) + '\n')
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

@eel.expose
def debug():
    print('hello')







letter_text = ''
letter_cash = []
blue_letter = 'a'
red_letter = 'b'
time_start = 0

Theme_color = 'black'


# initialisation app
cover_init()

