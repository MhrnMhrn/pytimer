# CLI Timer App with Progress Bar and Windows Notification

This is a simple CLI timer app that allows you to set a timer for a specific number of minutes and get a progress bar as well as a Windows notification when the time is up. You can also choose the color of the progress bar from a list of available options.

## Requirements
- Python 3.6 or higher
- tqdm
- colorama
- playsound

## Installation

You can install the required packages using pip:

```bash
pip install tqdm colorama playsound

## Usage

You can use the following command to set a timer for a specific number of minutes:

```bash
python timer.py <minutes> <task> -c <color>

   
   
   
    minutes: The number of minutes to set the timer for.
    task: The task you are working on.
    color (optional): The color of the progress bar. You can choose from a list of available options including black, red, green, yellow, blue, magenta, cyan, and white.

The app will display a progress bar that shows the remaining time. When the timer is up, it will play a sound and display a Windows notification with the message "Time is up! Go Get Some Rest!".

The app also logs the timer event to a file named timer.log, which includes the date and time when the timer finished, the duration of the timer, and the task you were working on.

## Example

Here is an example of how to use the app:

```bash
python timer.py 25 "Write a GitHub README file" -c blue

This will set a timer for 25 minutes with a blue progress bar and the task "Write a GitHub README file".

