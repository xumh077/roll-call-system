import os
import sys
import webview


def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    base_path = get_base_path()
    html_file = os.path.join(base_path, 'index.html')

    window = webview.create_window(
        title='班级专属随机点名系统',
        url=html_file,
        width=900,
        height=700,
        resizable=True,
        text_select=False,
        confirm_close=True
    )
    webview.start()