# Pimoroni RGB Macro Keypad - Unleash Your Productivity!

Transform your Pimoroni RGB Keypad into a customizable command center with this CircuitPython-powered project.  Streamline your workflow, launch applications, and execute complex key combinations with a single tap.

## Features

* **Vibrant Customization:**  Make it your own! The keypad lights up in a mesmerizing rainbow pattern, and you can easily modify the colors to match your style.
* **Three Layers of Power:** Access a multitude of commands across three different virtual button layout layers, activated by three dedicated keys.
* **Intuitive Key Mapping:**  Assign keyboard shortcuts, application launches, or even custom scripts to each key.
* **Easy to Use:**  Plug and play with CircuitPython – no complex setup required.

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/norton287/RGB-Macro-Keypad.git](https://github.com/norton287/RGB-Macro-Keypad.git)

Install CircuitPython:

Download and install CircuitPython on your Raspberry Pi Pico from the official website: https://circuitpython.org/board/raspberry_pi_pico/
Copy the Code:

Save the code.py file from this repository onto your Pico (it will appear as a USB drive when connected).

Customize Your Keypad:

Open the code.py file in a text editor (I use Thonny).
Modify the key mappings in each layer to suit your needs (Refer to the comment in the code for the HID keymaps).
Experiment with different colors and patterns!

Key Mapping Examples
Here's a glimpse of how you can map keys (customize to your liking):

Layer 1:
Key 3: Ctrl+V (Paste)
Key 4: Ctrl+Z (Undo)
Key 7: Alt+F4 (Close Window)

Layer 2:
Key 3: Win+A (Open Action Center)
Key 5: Win+L (Lock Screen)
Key 9: Win+Shift+S (Screenshot)

Layer 3:
Key 4: Alt+F (File Menu)
Key 6: Ctrl+1 (Switch to Tab 1)
Key 15: Alt+F (File Menu)
Feel free to explore the extensive list of keycodes in the adafruit_hid.keycode module for even more possibilities!

Contributing
Contributions are welcome! If you have ideas for new features, improvements, or additional key mappings, please open an issue or submit a pull request.
