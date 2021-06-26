from mmdesigner.Gui import Gui
import mmdesigner

def test_Tk_initialized(mocked_tk):
    gui = Gui(500,400)
    mocked_tk.assert_called_once()

def test_view_get_tkinter_root_sets_title(mocked_tk_title):
        gui = Gui(500,400)
        mocked_tk_title.assert_called_once()
        mocked_tk_title.assert_called_with("mmdesigner")

def test_constructor_sets_geometry(mocked_tk_geometry):
    gui = Gui(500, 400)
    mocked_tk_geometry.assert_called_with("500x400")

def test_run_calls_mainloop(mocked_tk_mainloop):
    gui = Gui(500, 400)
    gui.run()
    mocked_tk_mainloop.assert_called_once()

def test_constructor_calls_protocol(mocked_tk_protocol):
    gui = Gui(500, 400)
    quit = gui.quit
    mocked_tk_protocol.assert_called_with("WM_DELETE_WINDOW", quit)

def test_exit_calls_destroy(mocked_tk_destroy):
    gui = Gui(500, 400)
    gui.quit()
    mocked_tk_destroy.assert_called_once()
