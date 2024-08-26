import webview
import subprocess
import time
import requests

def is_server_running(url, timeout=5):
    """Check if the server is running by sending a request to the URL."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            pass
        time.sleep(1)
    return False

# Start the Django development server
server = subprocess.Popen(['python', 'manage.py', 'runserver'])

# Wait until the server is running
if not is_server_running('http://127.0.0.1:8000/'):
    print("Error: Django server did not start.")
    server.terminate()
else:
    try:
        # Create a window and display the web app
        window = webview.create_window('Motivational Quotes App', 'http://127.0.0.1:8000/')
        
        # Start the webview
        webview.start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Stop the Django server when the app is closed
        server.terminate()
