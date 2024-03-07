import subprocess
import os

def run_command(command):
    command = command.strip()
    sb = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    subprocess_return = sb.stdout.read()
    result = subprocess_return.decode(encoding='utf-8')
    return result


def open_ide(ide_path):

    cur_path = os.path.abspath(os.path.dirname(__file__))
    cur_path = f'"{cur_path}"'

    command = f"""
     {ide_path} {cur_path}
    """
    command = command.strip()

    print(command)
    result = run_command(command)


if __name__ == '__main__':

    # IDE_PATH= r'"C:\Users\qiliang.huang\AppData\Local\Programs\Microsoft VS Code\Code.exe"'
    IDE_PATH = r'"C:\Users\ps\AppData\Local\JetBrains\Toolbox\apps\PyCharm-P\ch-0\231.9011.38\bin\pycharm64.exe"'
    open_ide(IDE_PATH)