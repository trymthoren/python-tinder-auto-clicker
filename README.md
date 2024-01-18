# Auto Key Presser

The Auto Key Presser is a simple Python application that allows users to automate key presses on their keyboard with customizable settings. This tool is particularly useful for repetitive tasks that require keyboard input. It includes a basic GUI for ease of use.

## Features

- **Automated Key Pressing:** Simulate the pressing of the right arrow key on the keyboard.
- **Customizable Press Count and Delay:** Users can specify the number of key presses and the minimum and maximum delay between presses.
- **Start and Stop Functionality:** Easily start and stop the key pressing sequence.
- **Simple GUI:** User-friendly interface to input settings and control the key presses.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your system.
- `pyautogui` library installed. If you don't have it installed, you can install it via pip:

  ```bash
  pip install pyautogui
  ```

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/auto-key-presser.git
```

Navigate to the cloned directory:

```bash
cd auto-key-presser
```

## Usage

Run the script using Python:

```bash
python auto_key_presser.py
```

Upon running the script, a GUI will appear where you can:
- Enter the number of key presses you want.
- Set the minimum and maximum delay between each key press.
- Click 'Start Pressing' to begin the process.
- Use the 'Stop Pressing' button to halt the operation at any time.

## Caution

- The script will simulate key presses wherever your keyboard focus is. Make sure to focus on the correct window.
- Be mindful of the settings, especially in a work or school environment.

## Contributing

Contributions to the Auto Key Presser are welcome. Please ensure to update tests as appropriate.
