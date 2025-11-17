# Installation Guide

This guide provides detailed installation instructions for AutoPrint Service on different platforms.

## Table of Contents

- [Windows Installation](#windows-installation)
- [Linux Installation](#linux-installation)
- [macOS Installation](#macos-installation)
- [Running as a Service](#running-as-a-service)
- [Docker Installation](#docker-installation-coming-soon)

---

## Windows Installation

### Prerequisites

1. **Python 3.7+**
   - Download from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"
   - Verify: Open Command Prompt and run `python --version`

2. **Google Chrome**
   - Download from [google.com/chrome](https://www.google.com/chrome/)
   - AutoPrint will automatically detect the installation

### Installation Steps

1. **Download AutoPrint Service**
   ```cmd
   cd C:\
   git clone https://github.com/yourusername/autoprint-service.git
   cd autoprint-service
   ```

   Or download the ZIP from GitHub and extract it.

2. **Install Dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Configure Settings**
   - Open `autoprint.py` in your favorite text editor
   - Update the configuration section with your email settings
   - Save the file

4. **Test Run**
   ```cmd
   python autoprint.py
   ```
   - Press `Ctrl+C` to stop

### Running as Windows Service

#### Option 1: Task Scheduler (Recommended)

1. Open Task Scheduler
2. Click "Create Basic Task"
3. Name it "AutoPrint Service"
4. Trigger: "When the computer starts"
5. Action: "Start a program"
   - Program: `C:\Python39\python.exe` (adjust to your Python path)
   - Arguments: `C:\autoprint-service\autoprint.py`
   - Start in: `C:\autoprint-service`
6. Check "Run whether user is logged on or not"
7. Check "Run with highest privileges"

#### Option 2: NSSM (Advanced)

1. Download NSSM from [nssm.cc](https://nssm.cc/download)
2. Extract and open Command Prompt as Administrator
3. Install service:
   ```cmd
   nssm install AutoPrint "C:\Python39\python.exe" "C:\autoprint-service\autoprint.py"
   nssm set AutoPrint AppDirectory "C:\autoprint-service"
   nssm start AutoPrint
   ```

4. Manage service:
   ```cmd
   nssm stop AutoPrint
   nssm restart AutoPrint
   nssm remove AutoPrint confirm
   ```

---

## Linux Installation

### Prerequisites

1. **Python 3.7+**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   python3 --version
   ```

2. **Google Chrome or Chromium**
   ```bash
   # Chrome
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo dpkg -i google-chrome-stable_current_amd64.deb
   sudo apt-get install -f

   # Or Chromium
   sudo apt install chromium-browser
   ```

### Installation Steps

1. **Download AutoPrint Service**
   ```bash
   cd ~
   git clone https://github.com/yourusername/autoprint-service.git
   cd autoprint-service
   ```

2. **Install Dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configure Settings**
   ```bash
   nano autoprint.py
   # Update configuration, then Ctrl+X to save
   ```

4. **Test Run**
   ```bash
   python3 autoprint.py
   # Press Ctrl+C to stop
   ```

### Running as Linux Service (systemd)

1. **Create Service File**
   ```bash
   sudo nano /etc/systemd/system/autoprint.service
   ```

2. **Add Configuration**
   ```ini
   [Unit]
   Description=AutoPrint Service
   After=network.target

   [Service]
   Type=simple
   User=yourusername
   WorkingDirectory=/home/yourusername/autoprint-service
   ExecStart=/usr/bin/python3 /home/yourusername/autoprint-service/autoprint.py
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

3. **Enable and Start Service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable autoprint
   sudo systemctl start autoprint
   ```

4. **Check Status**
   ```bash
   sudo systemctl status autoprint
   sudo journalctl -u autoprint -f  # View logs
   ```

5. **Manage Service**
   ```bash
   sudo systemctl stop autoprint
   sudo systemctl restart autoprint
   sudo systemctl disable autoprint
   ```

---

## macOS Installation

### Prerequisites

1. **Python 3.7+**
   ```bash
   # Using Homebrew
   brew install python3
   python3 --version
   ```

2. **Google Chrome**
   - Download from [google.com/chrome](https://www.google.com/chrome/)
   - Or install via Homebrew: `brew install --cask google-chrome`

### Installation Steps

1. **Download AutoPrint Service**
   ```bash
   cd ~
   git clone https://github.com/yourusername/autoprint-service.git
   cd autoprint-service
   ```

2. **Install Dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configure Settings**
   ```bash
   nano autoprint.py
   # Update configuration
   ```

4. **Test Run**
   ```bash
   python3 autoprint.py
   ```

### Running as macOS Service (launchd)

1. **Create Launch Agent**
   ```bash
   nano ~/Library/LaunchAgents/com.autoprint.service.plist
   ```

2. **Add Configuration**
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.autoprint.service</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/local/bin/python3</string>
           <string>/Users/yourusername/autoprint-service/autoprint.py</string>
       </array>
       <key>WorkingDirectory</key>
       <string>/Users/yourusername/autoprint-service</string>
       <key>RunAtLoad</key>
       <true/>
       <key>KeepAlive</key>
       <true/>
       <key>StandardOutPath</key>
       <string>/Users/yourusername/autoprint-service/stdout.log</string>
       <key>StandardErrorPath</key>
       <string>/Users/yourusername/autoprint-service/stderr.log</string>
   </dict>
   </plist>
   ```

3. **Load and Start Service**
   ```bash
   launchctl load ~/Library/LaunchAgents/com.autoprint.service.plist
   launchctl start com.autoprint.service
   ```

4. **Check Status**
   ```bash
   launchctl list | grep autoprint
   ```

5. **Manage Service**
   ```bash
   launchctl stop com.autoprint.service
   launchctl unload ~/Library/LaunchAgents/com.autoprint.service.plist
   ```

---

## Running as a Service

### Best Practices

1. **Set Up Logging**
   - Ensure `LOG_FILE` is set to a writable location
   - Use log rotation to prevent disk space issues
   - Monitor logs regularly for errors

2. **Configure Auto-Restart**
   - All service configurations include restart on failure
   - Set appropriate restart delays (10-30 seconds)

3. **Security**
   - Run service with minimal required permissions
   - Use app-specific passwords for email accounts
   - Regularly update the service and dependencies

4. **Monitoring**
   - Set up alerts for service failures
   - Monitor disk space (temp files and logs)
   - Check printer connectivity regularly

### Verifying Service is Running

#### Windows
```cmd
tasklist | findstr python
```

#### Linux
```bash
ps aux | grep autoprint
sudo systemctl status autoprint
```

#### macOS
```bash
launchctl list | grep autoprint
```

---

## Docker Installation (Coming Soon)

Docker support is planned for a future release. This will provide:
- Easy deployment across platforms
- Isolated environment
- Simple updates and rollbacks
- Better resource management

Stay tuned!

---

## Troubleshooting

### Common Issues

1. **"Could not find Chrome"**
   - Set `CHROME_PATH` manually in configuration
   - Verify Chrome is installed correctly

2. **IMAP Connection Failed**
   - Check email credentials
   - Verify IMAP is enabled on your email account
   - Check firewall settings

3. **Service Won't Start**
   - Check Python path in service configuration
   - Verify file permissions
   - Review service logs for specific errors

4. **Prints Not Appearing**
   - Check default printer settings
   - Test manually with `AUTO_PRINT_ENABLED = False`
   - Increase `CHROME_PRINT_WAIT_SECONDS`

### Getting Help

- Check the [README.md](README.md) for general documentation
- Review [autoprint.log](autoprint.log) for error details
- Open an issue on [GitHub](https://github.com/yourusername/autoprint-service/issues)

---

## Updating AutoPrint Service

### Update Process

1. **Stop the service**
2. **Backup your configuration**
   ```bash
   cp autoprint.py autoprint.py.backup
   ```
3. **Pull latest changes**
   ```bash
   git pull origin main
   ```
4. **Restore your configuration** (merge changes if needed)
5. **Restart the service**

---

## Uninstallation

### Windows
1. Stop Task Scheduler task or remove NSSM service
2. Delete the `autoprint-service` folder
3. Remove Python if no longer needed

### Linux
```bash
sudo systemctl stop autoprint
sudo systemctl disable autoprint
sudo rm /etc/systemd/system/autoprint.service
sudo systemctl daemon-reload
rm -rf ~/autoprint-service
```

### macOS
```bash
launchctl unload ~/Library/LaunchAgents/com.autoprint.service.plist
rm ~/Library/LaunchAgents/com.autoprint.service.plist
rm -rf ~/autoprint-service
```

---

**Need more help?** Open an issue on GitHub or check the discussions forum!
