#ΜΗΝ ΠΕΡΙΜΕΝΕΙΣ ΤΟΝ ΑΛΓΟΡΙΘΜΟ ΝΑ ΣΟΥ ΠΕΙ ΤΙ ΝΑ ΨΗΦΙΣΕΙΣ - ΞΕΡΕΙΣ !

(ωστόσο for fun πάρτε ενα scriptακι)

Τα φιλιά μας από Αντίσταση - Attack 
και το πιο σημαντικό : ΔΕΝ ΑΠΕΧΟΥΜΕ !

---

# Φοιτητικές Εκλογές - Ερωτηματολόγιο Θέσεων (Student Elections - Position Questionnaire)

This project provides a graphical user interface (GUI) for users to participate in a questionnaire regarding student elections. Based on the user input, the program returns an evaluation, showing the user's position on various political aspects.

---

## Table of Contents

* [Installation](#installation)

  * [Windows](#windows)
  * [Linux](#linux)
* [Usage](#usage)
* [License](#license)

---

## Installation

### Windows

To install and build the application on **Windows**, follow these steps:

1. **Install Python 3.7+**
   Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Git**
   Download and install Git from [git-scm.com](https://git-scm.com/).

3. **Install Dependencies**
   Open a terminal (Command Prompt or PowerShell), and install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. **Build the Executable**
   Use **PyInstaller** to generate the `.exe` file for Windows:

   ```bash
   pyinstaller --onefile --windowed foithtikes_ekloges_gui.py
   ```

5. **Find the Executable**
   After building, the `.exe` file will be located in the `dist/` folder.

---

### Linux

To build the application on **Linux** (Ubuntu/Debian):

1. **Install Python 3.7+**
   If not already installed, install Python via your package manager:

   ```bash
   sudo apt-get install python3 python3-pip python3-venv
   ```

2. **Install Dependencies**
   Install the required dependencies with:

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Build the Executable**
   Use **PyInstaller** to create the `.bin` executable for Linux:

   ```bash
   pyinstaller --onefile --windowed foithtikes_ekloges_gui.py
   ```

4. **Find the Executable**
   The generated `.bin` executable will be located in the `dist/` folder.

---

## Usage

1. **Run the Executable**
   After building the application, navigate to the `dist/` folder and run the executable for your platform:

   * On **Windows**: Run `foithtikes_ekloges_gui.exe`.
   * On **Linux**: Run `./foithtikes_ekloges_gui`.

2. **Follow the On-Screen Prompts**
   The application will present a series of yes/no questions. Click **Yes** or **No** for each question.

3. **Submit the Questionnaire**
   Once all questions are answered, click **Submit**. The result will be displayed next to the button or in a pop-up window.

---



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:

* This project uses **PyQt5** for the graphical user interface and **PyInstaller** for packaging the app into standalone executables.
* Ensure your environment meets the required dependencies listed in `requirements.txt` before building the project.
