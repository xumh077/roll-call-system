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
    icon_file = os.path.join(base_path, 'icon.png')  # 绑定你的新图标

    window = webview.create_window(
        title='J254专属随机点名系统',
        url=html_file,
        icon=icon_file,      # 【新增】加入自定义图标
        width=1280,
        height=800,
        resizable=True,
        fullscreen=True,     # 启动自动全屏，免去手动拉大
        text_select=False
                             # 【已修改】删除了 confirm_close=True，关闭时不再弹窗确认
    )
    webview.start()
