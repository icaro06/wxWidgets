
from wxPython.wx import *

#---------------------------------------------------------------------------

class TestComboBox(wxPanel):
    def __init__(self, parent, log):
        self.log = log
        wxPanel.__init__(self, parent, -1)

        sampleList = ['zero', 'one', 'two', 'three', 'four', 'five',
                      'six', 'seven', 'eight']

        wxStaticText(self, -1, "This example uses the wxComboBox control.",
                               wxPoint(8, 10))

        wxStaticText(self, -1, "Select one:", wxPoint(15, 50), wxSize(75, 18))
        wxComboBox(self, 500, "default value", wxPoint(80, 50), wxSize(95, -1),
                   sampleList, wxCB_DROPDOWN)
        EVT_COMBOBOX(self, 500, self.EvtComboBox)
        EVT_TEXT(self, 500, self.EvtText)


    def EvtComboBox(self, event):
        self.log.WriteText('EvtComboBox: %s\n' % event.GetString())

    def EvtText(self, event):
        self.log.WriteText('EvtText: %s\n' % event.GetString())

#---------------------------------------------------------------------------

def runTest(frame, nb, log):
    win = TestComboBox(nb, log)
    return win

#---------------------------------------------------------------------------












overview = """\
A combobox is like a combination of an edit control and a listbox. It can be displayed as static list with editable or read-only text field; or a drop-down list with text field; or a drop-down list without a text field.

"""
