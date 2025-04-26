from os import getenv

def initialize_debugger_if_needed(port_number):
    print("initialing debugger 1")
    if getenv("DEBUGGER") == "True":        
        import debugpy
        print("initialing debugger 2")
      
        if port_number is None and getenv("DEBUGGER_PORT") is not None:
            port_number = int(getenv("DEBUGGER_PORT"))

        print("initialing debugger 3")
        print(port_number)
        
        if port_number is None:
            raise Exception("No port number provided for debugger. Set DEBUGGER_PORT environment variable or pass it as an argument.")

        print("initialing debugger 4")
      
        debugpy.listen(("0.0.0.0", port_number))
        print("⏳ VS Code debugger can now be attached, press F5 in VS Code ⏳", flush=True)
        debugpy.wait_for_client()
        print("🎉 VS Code debugger attached, enjoy debugging 🎉", flush=True)
