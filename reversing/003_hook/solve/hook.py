import frida
import sys
import time


script_code = """
    var lastMessageTime = 0; 
    var isDetaching = false; 

    Interceptor.attach(Module.findExportByName('user32.dll', 'MessageBoxA'), {
        onEnter: function(args) {
          
            var titlePtr = args[0];
            var messagePtr = args[1];

           
            var title = Memory.readUtf8String(titlePtr) || ""; 
            var message = Memory.readUtf8String(messagePtr) || ""; 

        
            lastMessageTime = Date.now();

           
            if (message.includes("key: ")) {
                console.log("[*] Message: " + message);
            }
        }
    });

 
    setInterval(function() {
        var currentTime = Date.now();
      
        if (!isDetaching && (currentTime - lastMessageTime > 3000)) {
            console.log("[*] No messages received in the last 3 seconds. Detaching...");
            isDetaching = true; 
            Interceptor.detachAll(); 
            send("detached");
        }
    }, 1000); 
"""

def on_message(message, data):
    if 'payload' in message:
        print("[*] {}".format(message['payload']))
    elif message['type'] == 'send':
        if message['payload'] == "detached":
            print("[*] Hooking detached.")
            session.detach() 
            sys.exit(0) 
    else:
        print("[*] Received message without payload: {}".format(message))


device = frida.get_local_device()

print("Please start round.exe now...")
session = None


while True:
    try:
   
        session = device.attach('round.exe')
        print("Successfully attached to round.exe.")
        break
    except frida.ProcessNotFoundError:
        print("Waiting for round.exe to start...")
        time.sleep(1)


script = session.create_script(script_code)
script.on('message', on_message)


try:
    script.load()
    print("Script loaded successfully. Hooking the messages...")
except Exception as e:
    print(f"Failed to load script: {e}")
    session.detach()
    sys.exit(1)


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("[*] Detaching...")
    session.detach()
