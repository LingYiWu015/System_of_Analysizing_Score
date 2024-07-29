# !!!Note: This project is a work in progress, and developers are actively working on it. If you encounter any issues or errors, please attempt to resolve them yourself first. Only submit an issue if you are unable to fix it!!!



# The Exam Score Process System
[简体中文](README.md) | English
## Function

### Using For
This Program is used for analyzing exam scores, providing displayable tables and data.

### User
For teachers, classmasters, or tutors.
* (Maybe only for Chinese Senior High School and its subs)

## The Method to Achieve It

### The Frame
There are three files in this project (maybe more if you want to refactor it):

1. `main.py`: This is the main script where the program runs. It shows the workflow basically.
2. `Show_Web_GUI.py`: Contains the web interface built with Gradio.
3. `Ulties.py`: Contains utility functions for handling file operations.

## Features

- Upload and analyze multiple Excel files containing student scores.
- Convert Excel files to JSON for further analysis.
- Create necessary directories for organizing inputs and outputs.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/LingYiWu015/System_of_Analysizing_Score.git
    ```
2. Navigate to the project directory:
    ```bash
    cd gitclone_path/System_of_Analysizing_Score
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script to start the application:
    ```bash
    python main.py
    ```

2. The application will initialize and display the web interface.

## Contributing

We welcome contributions! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the GPLv3 License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thank you to all the contributors who have helped make this project a reality.
- Special thanks to the developers of Gradio for their fantastic libraries.
