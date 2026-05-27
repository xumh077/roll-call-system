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
    icon_file = os.path.join(base_path, 'icon.png')  # 运行时加载的任务栏图标

    # 创建窗口，完美全屏，去除了引发崩溃的 icon 传参
    window = webview.create_window(
        title='J254专属随机点名系统',
        url=html_file,
        width=1280,
        height=800,
        resizable=True,
        fullscreen=True,     # 启动时自动全屏展示
        text_select=False,
        confirm_close=True
    )
    
    # 正确的运行时图标注入方式
    webview.start(icon=icon_file)
