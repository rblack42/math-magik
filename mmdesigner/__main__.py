import logging

from mmdesigner import get_main_window, _state


def main():
    _state.init()
    main_window = get_main_window()
    main_window.withdraw()
    # setup widgets
    main_window.deiconify()
    try:
        main_window.mainloop()
    finally:
        # save settings
        pass
    logging.info("Exiting mmdesigner normlly...")


# python -m math_magik
if __name__ == '__main__':
    main()
