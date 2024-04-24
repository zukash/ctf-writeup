import angr
proj = angr.Project('scarface')
simgr = proj.factory.simgr()
simgr.explore(find=lambda s: b"Well done!" in s.posix.dumps(1))

"""
   0x56132965e57c <main+130>:   call   0x56132965e0e0 <strlen@plt>
=> 0x56132965e581 <main+135>:   cmp    rax,0x1f


   0x5644acae959e <main+164>:   add    QWORD PTR [rbp-0x20],0x1
   0x5644acae95a3 <main+169>:   mov    rax,QWORD PTR [rbp-0x20]
=> 0x5644acae95a7 <main+173>:   movzx  eax,BYTE PTR [rax]
   0x5644acae95aa <main+176>:   cmp    al,0x3d


0xb3 
RAX: 0x81 
RDX: 0xb3 
"""
