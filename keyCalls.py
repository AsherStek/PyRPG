# This class is used to keep our code clean and to have an easy way to create commands and bind them to a key
class KeyCalls(object):

    # Close program
    def quitOut(self, event, window):
        window.destroy()
        print("Program was manually closed")