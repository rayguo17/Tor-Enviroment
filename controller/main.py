from stem.control import Controller

CONTPORT = 9051
CONTPASS= "password"

controller = Controller.from_port(port=CONTPORT)
controller.authenticate(CONTPASS)
print("control gained!")
# microDes = controller.get_microdescriptors()
# #how does tor client know relay does not accept dedicated ip:port
# for des in microDes:
#     print(des)
    
exit_policy = controller.get_exit_policy()
print(exit_policy)