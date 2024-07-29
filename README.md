# 中国高中考试成绩分析系统

简体中文 | [English](README_EN.md)
## 功能

### 用途
本程序用于分析考试成绩，提供可显示的表格和数据。

### 用户
适用于教师、班主任或辅导老师。
* （可能仅适用于中国高中及其子项目）

## 实现方法

### 框架
该项目中有三个文件（如果需要重构，可能会有更多）：

1. `main.py`: 这是主脚本，程序在此运行。它基本展示了工作流程。
2. `Show_Web_GUI.py`: 包含使用 Gradio 构建的 Web 界面。
3. `Ulties.py`: 包含处理文件操作的实用函数。

## 功能

- 上传并分析包含学生成绩的多个 Excel 文件。
- 将 Excel 文件转换为 JSON 以便进一步分析。
- 创建必要的目录以组织输入和输出。

## 安装

1. 克隆此仓库：
    ```bash
    git clone https://github.com/LingYiWu015/System_of_Analysizing_Score.git
    ```
2. 进入项目目录：
    ```bash or powershell
    cd gitclone_path/System_of_Analysizing_Score
    ```
3. 安装所需的依赖项：
    ```bash or powerShell
    pip install -r requirements.txt
    ```

## 使用

1. 运行主脚本以启动应用程序：
    ```bash or powerShell
    python main.py
    ```

2. 应用程序将初始化并显示 Web 界面。

## 贡献

我们欢迎贡献！请阅读我们的 [CONTRIBUTING.md](CONTRIBUTING.md) 以了解如何向本项目做出贡献。

## 许可证

本项目采用 GPLv3 许可证。详见 [LICENSE](LICENSE) 文件。

## 致谢

- 感谢所有帮助实现此项目的贡献者。
- 特别感谢 Gradio 的开发人员，他们提供了出色的库。
