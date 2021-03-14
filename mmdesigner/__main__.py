import logging

from mmdesigner.gui import Gui


def main():
    gui = Gui("mmdesigner", "800x600")
    main_window = gui.get_main_window()
    main_window.withdraw()
    # setup widgets
    main_window.deiconify()
    try:
        main_window.mainloop()
    finally:
        # save settings
        pass


# python -m math_magik
if __name__ == '__main__':
    main()
