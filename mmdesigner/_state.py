import tkinter
import logging

_root = None

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    filename='mmdesigner.log',
    encoding='utf-8',
    level=logging.DEBUG)


def init():
    global _root
    logging.debug("_state.init() starting")

    _root = tkinter.Tk()
    _root.protocol('WM_DELETE_WINDOW', quit)
    photo = tkinter.PhotoImage(file='mmdesigner/lpp.png')
    _root.iconphoto(False, photo)
    logging.debug("_state.init() done")


def get_main_window():
    if _root is None:
        raise RuntimeError("mmdesigner is not running")
    return _root


def quit():
    assert _root is not None
    logging.debug("quit called")
    _root.destroy()
