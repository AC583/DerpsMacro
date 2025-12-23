

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(Layers())

encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.D7, board.D0),  # (A, B)
)

encoder.map = [
    (
        (KC.VOLD, KC.VOLU),   # Layer 0: CCW, CW
    ),
    (
        (KC.VOLD, KC.VOLU),   # Layer 1 (or whatever)
    ),
]


PINS = [    
    board.D1,board.D2,
    board.D4,board.D3,board.D26,
    board.D27,board.D28,board.D29,]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    # ────────────── Layer 0 (AI Assistant) ──────────────
    [
        # 1. Open ChatGPT
        KC.MACRO(
            Press(KC.LWIN), Tap(KC.R), Release(KC.LWIN),  # Win+R
            Tap(KC.C), Tap(KC.H), Tap(KC.R), Tap(KC.O), Tap(KC.M), Tap(KC.E), # type 'chrome'
            Tap(KC.SPACE),
            # type URL
            *[Tap(k) for k in "https://chat.openai.com"],
            Tap(KC.ENTER),
        ),

        # 2. Paste selected text to ChatGPT
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),
            Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT),
            *[Tap(k) for k in "Explain this clearly: "],
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),
            Tap(KC.ENTER),
        ),

        # 3. Screenshot → paste into ChatGPT
        KC.MACRO(
            Tap(KC.PSCR),                                    # Screenshot
            Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT),   # Switch to ChatGPT
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),   # Paste screenshot
        ),
        # 4. New Chat (CTRL + L to focus / ENTER)
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.L), Release(KC.LCTRL),
            Tap(KC.ENTER),
        ),
        # 5. Rewrite selected text
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),
            Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT),
            *[Tap(k) for k in "Rewrite this clearer and more professional: "],
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),
            Tap(KC.ENTER),
        ),
        # 6. Coding helper
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),
            Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT),
            *[Tap(k) for k in "Explain this code, then suggest improvements:\n"],
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),
            Tap(KC.ENTER),
        ),
        # 7. Emoji Picker
        KC.MACRO(
            Press(KC.LWIN), Tap(KC.DOT), Release(KC.LWIN),
        ),

        # 8 Switch to Layer 1 (Typing)
        KC.DF(1),    # Return to Layer 1
    ],

    # ────────────── Layer 1 (Typing) ──────────────
    [
        # 1. Open Windows Emoji Picker
        KC.MACRO(
            Press(KC.LWIN), Tap(KC.DOT), Release(KC.LWIN)
        ),

        # 2. Surround selected text with double quotes
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),   # Copy selection
            Tap(KC.QUOTE),                                   # "
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),   # Paste text
            Tap(KC.QUOTE),                                   # "
        ),

        # 3. Surround selected text with parentheses
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),   
            Tap(KC.LEFT_PAREN),                              
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),   
            Tap(KC.RIGHT_PAREN),                             
        ),
        # 4. Surround selected text with /* */
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),   
            Tap(KC.SLASH), Tap(KC.KP_ASTERISK),               
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),   
            Tap(KC.SLASH), Tap(KC.KP_ASTERISK)               
        ),
        # 5. Surround with []
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),
            Tap(KC.LBRACKET),
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),
            Tap(KC.RBRACKET),
        ),
        # 6. Surround with <>
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),
            Tap(KC.LABK),
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),
            Tap(KC.RABK),
        ),
        # 7. Surround with ||
        KC.MACRO(
            Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL),
            Tap(KC.PIPE),
            Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL),
            Tap(KC.PIPE),
        ),

        # 8 Switch to Layer 0 (AI Assistant)
        KC.DF(0),   # Return to Layer 0
    ]
]

if __name__ == '__main__':
    keyboard.go()


