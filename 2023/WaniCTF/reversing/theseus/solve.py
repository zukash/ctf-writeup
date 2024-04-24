import angr
import code

proj = angr.Project('chall')
simgr = proj.factory.simgr()
simgr.explore(find=lambda s: b"Correct!" in s.posix.dumps(1))

code.InteractiveConsole(globals()).interact()
