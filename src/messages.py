from command import Command
class GpioCommand(Command):
    def __init__(self,commandid,origin, gpioID, value):
        cont = dict()
        cont['GPIO'] = gpioID
        cont['value'] = value
        Command.__init__(self,'GPIO',origin,cont)