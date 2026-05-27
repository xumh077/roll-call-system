import os
import sys
import webview


def get_base_path():
    # 完美兼容 PyInstaller 单文件打包后的临时解压路径
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    base_path = get_base_path()
    
    # 使用标准绝对路径，防止跨系统打包时路径解析死锁
    html_file = os.path.normpath(os.path.join(base_path, 'index.html'))
    icon_file = os.path.normpath(os.path.join(base_path, 'icon.png'))

    # 创建窗口（将引发报错的 icon 参数从 create_window 中移除）
    window = webview.create_window(
        title='J254专属随机点名系统',
        url=html_file,
        width=1280,
        height=800,
        resizable=True,
        fullscreen=True,     # 默认全屏启动，完美适配多媒体大屏
        text_select=False,
        confirm_close=True
    )
    
    # 这才是老版本 pywebview 正确的任务栏图标注入方式
    if os.path.exists(icon_file):
        webview.start(icon=icon_file)
    else:
        webview.start()
