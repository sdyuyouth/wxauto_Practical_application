# wxauto_Practical_application
Help the monitor to send messages automatically to urge the incomplete student

## Aim
Are you still annoyed that your classmates can't fill in the activities in the class group in time?

It takes a lot of time and energy to remind each student who has not completed a private chat, and it also makes you upset!

The script can solve your troubles!

(Thanks to the open source predecessors, this script relies on the wxauto library, please refer to the details：https://github.com/cluic/wxauto.git)


## Features
- Automatic message sending script based on wxauto.
- Ability to check incomplete students according to the set list.
- Customize the message to be sent as a prompt or reminder.

## System Requirements
-python 3.x

-wxauto pandas

-Windows operating system

-Wechat version 3.9.11.x

## Usage
1. Ensure Python 3.x is installed on your system.
2. Save this script as a `.py` file,
   for example, `wechat.py`.
3. Open Command Prompt or PowerShell and navigate to the directory where the script is located.
4. Run the script:
python wechat.py

## Example
1、Make sure you have installed the python runtime, wxauto, and pandas libraries

2、Replace the corresponding section in the source code with a list of all people, in the form of a list

3、Specify the path of an excel table, enter the list of completed students in the table, the column title must be "name", if there is a table header, please set header=1, if not, change to 0

4、Enter the message you want to send when prompted

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This script is for educational and research purposes only. Please ensure you comply with all applicable laws and regulations when using it. The author assumes no responsibility for any loss or damage caused during its use.
