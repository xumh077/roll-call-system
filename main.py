import os
import sys
import webview


def get_base_path():
    # 兼容 PyInstaller 打包后的临时解压路径
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    base_path = get_base_path()
    html_path = os.path.normpath(os.path.join(base_path, 'index.html'))
    icon_path = os.path.normpath(os.path.join(base_path, 'icon.png'))

    # 安全防御：如果临时目录真没解压出 HTML，弹窗报错而不是默默闪退
    if not os.path.exists(html_path):
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("系统错误", f"未找到核心网页文件 index.html\n路径: {html_path}")
        sys.exit(1)

    # 【核心修正】直接读取 HTML 文件的文本内容，彻底解决路径加载导致的闪退
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 创建窗口（把 url=html_file 改为 html=html_content）
    window = webview.create_window(
        title='J254专属随机点名系统',
        html=html_content,    # 直接注入 HTML 源码，稳如磐石
        width=1280,
        height=800,
        resizable=True,
        fullscreen=True,     # 默认全屏启动，上屏效果拉满
        text_select=False,
        confirm_close=True
    )
    
    # 启动应用并注入任务栏图标
    if os.path.exists(icon_path):
        webview.start(icon=icon_path)
    else:
        webview.start()
