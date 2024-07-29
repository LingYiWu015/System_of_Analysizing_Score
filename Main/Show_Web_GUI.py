import gradio as gr


with gr.Blocks() as Main_Window:
    with gr.Tab("上传文件"):
        with gr.Row(equal_height=True):
            with gr.Column():
                gr.Markdown("## 首次上传，请在下面传入所有文件")
                gr.File(label="上传文件",type="filepath",file_count="multiple" ,file_types=["xlsx"])

            with gr.Column():
                gr.Markdown("## 原来用过，请在此处上传上次保存的日志文件")
                gr.File(label="上传文件",type="filepath",file_count="multiple" ,file_types=["xlsx"])
    with gr.Tab("处理文件方式"):
        gr.Markdown("## 正在开发中，请联系作者以寻求帮助")
        gr.Markdown("## 联系方式：[QQ邮箱](mailto:1591775242@qq.com)")
        gr.Markdown("## 联系方式：[Outlook邮箱](mailto:wang.zhongbo@outlook.com)")
        gr.Markdown("## Github主页：[Github](https://github.com/LingYiWu015)")
    with gr.Tab("班级总体情况"):
        gr.Markdown("## 正在开发中，请联系作者以寻求帮助")
        gr.Markdown("## 联系方式：[QQ邮箱](mailto:1591775242@qq.com)")
        gr.Markdown("## 联系方式：[Outlook邮箱](mailto:wang.zhongbo@outlook.com)")
        gr.Markdown("## Github主页：[Github](https://github.com/LingYiWu015)")
    with gr.Tab("个人详细情况"):
        gr.Markdown("## 正在开发中，请联系作者以寻求帮助")
        gr.Markdown("## 联系方式：[QQ邮箱](mailto:1591775242@qq.com)")
        gr.Markdown("## 联系方式：[Outlook邮箱](mailto:wang.zhongbo@outlook.com)")
        gr.Markdown("## Github主页：[Github](https://github.com/LingYiWu015)")