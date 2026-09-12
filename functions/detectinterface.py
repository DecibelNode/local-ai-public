import psutil

def process(process_name):
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
                return True

            if proc.info['cmdline'] and any(process_name.lower() in arg.lower() for arg in proc.info['cmdline']):
                return True
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    return False
