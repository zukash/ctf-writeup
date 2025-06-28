import gdb

def main():
    gdb.execute("file /bin/cat")
    gdb.execute("break read")
    gdb.execute("run")

    while True:
        try:
            command = input("(gdb) ")
            try:
                gdb.execute(command)
            except gdb.error as e:
                print(f"Error executing command '{command}': {e}")
        except:
            pass

if __name__ == "__main__":
    main()
