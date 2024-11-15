import subprocess
import time

# Step 1: Start the Flask server
server = subprocess.Popen(["python", "run.py"])

# Step 2: Wait for the server to start
time.sleep(3)  # Adjust this if your server takes longer to start

# Step 3: Run the test script
try:
    subprocess.run(["python", "app/testing/test_secure_endpoint.py"])
finally:
    # Step 4: Terminate the Flask server after testing
    server.terminate()
