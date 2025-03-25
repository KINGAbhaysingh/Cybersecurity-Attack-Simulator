# Cybersecurity Attack Simulator
A project to simulate cyberattacks with animations.

## Requirements
- Kali Linux
- Python 3, requests, manim
- hping3, dsniff, hydra
- Victim VM (e.g., Ubuntu with Apache, SSH, DVWA)

## Setup
1. Clone repo: `git clone <repo-url>`
2. Install dependencies: `sudo apt install python3 python3-pip hping3 dsniff hydra && sudo pip3 install requests manim`
3. Update IPs in `main.py`
4. Run: `sudo python3 main.py`