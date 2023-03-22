import time
import argparse
import sys
import ctypes
from colorama import Fore
from tqdm import tqdm
import logging
import time
from playsound import playsound



logging.basicConfig(filename='timer.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')
cyan = Fore.CYAN

def timer(minutes, color = cyan, task = ""):
    for i in tqdm(range(minutes * 60), desc='Timer', unit='sec', unit_scale=True , bar_format="{l_bar}%s{bar}%s{r_bar}" % (color, Fore.RESET)):
        time.sleep(1)
    
    
    title = 'Time is up!'
    message = 'Go Get Some Rest!'
    playsound('click.mp3', block=False)
    
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x0)
    log_string = f'Timer finished at {time.strftime("%Y-%m-%d %H:%M:%S")} with duration of  {minutes} minuets, and {task} task'
    logging.info(log_string)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple CLI timer app with progress bar and Windows notification.')
    parser.add_argument('minutes', type=int, help='number of minutes to set the timer for')
    parser.add_argument('task', type=str, help='task you are working on', default=None, nargs='*')
    parser.add_argument('-c', type=str, help="choose your color \n list of colors: \n black, red, green, yellow, blue, magenta, cyan, and white", nargs='?')
    args = parser.parse_args()

    match args.c:
        case "red": 
            selected_color = Fore.RED
        case "green":
                 selected_color =Fore.GREEN
        case "blue":
             selected_color = Fore.BLUE
        case "yellow":
            selected_color=  Fore.YELLOW
        case "black":
            selected_color=  Fore.BLACK
        case other:
            selected_color = Fore.CYAN
    


    task_str = ' '.join(args.task)
    print("currently working on : {}".format(task_str))
    timer(args.minutes, color=selected_color, task = (task_str))
    

