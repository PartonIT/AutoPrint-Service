# Quick Start Guide

Get AutoPrint Service running in 5 minutes!

## Prerequisites Checklist

- [ ] Python 3.7+ installed
- [ ] Google Chrome installed
- [ ] IMAP email account credentials
- [ ] Printer connected and set as default

## Installation (5 minutes)

### Step 1: Get the Code (1 min)
```bash
git clone https://github.com/yourusername/autoprint-service.git
cd autoprint-service
```

### Step 2: Install Dependencies (1 min)
```bash
pip install colorama
```

### Step 3: Configure (2 min)

Open `autoprint.py` and update these lines:

```python
IMAP_HOST = "imap.gmail.com"           # Your email provider's IMAP server
IMAP_USERNAME = "you@example.com"       # Your email address
IMAP_PASSWORD = "your-password"         # Your password or app-specific password
SUBJECT_PREFIX = "[PRINT]"              # Emails starting with this will print
```

### Step 4: Test Run (1 min)
```bash
python autoprint.py
```

You should see the dashboard. Press Ctrl+C to stop.

## Quick Configuration Examples

### Gmail
```python
IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
IMAP_USERNAME = "yourstore@gmail.com"
IMAP_PASSWORD = "xxxx xxxx xxxx xxxx"  # App password required
```
Get app password: https://myaccount.google.com/apppasswords

### Outlook/Office 365
```python
IMAP_HOST = "outlook.office365.com"
IMAP_PORT = 993
IMAP_USERNAME = "yourstore@outlook.com"
IMAP_PASSWORD = "your-password"
```

### Yahoo Mail
```python
IMAP_HOST = "imap.mail.yahoo.com"
IMAP_PORT = 993
IMAP_USERNAME = "yourstore@yahoo.com"
IMAP_PASSWORD = "app-password"  # Generate at account.yahoo.com
```

## Shopify Flow Setup (3 minutes)

1. Go to Shopify Admin → Settings → Notifications
2. Create new workflow: **Order Created**
3. Add action: **Send Email**
4. Configure:
   ```
   To: your-monitored-email@example.com
   Subject: [PRINT] Order #{{ order.name }}
   Body: [Your HTML packing slip template]
   ```
5. Save and test with a test order

## Testing Your Setup

### Test 1: Send a Test Email
1. Send yourself an email with subject: `[PRINT] Test Order`
2. Include some HTML content in the body
3. Within 30 seconds, AutoPrint should detect and print it

### Test 2: Manual Print Mode
For testing, set:
```python
AUTO_PRINT_ENABLED = False  # Opens print dialog instead
```

This lets you preview before printing.

## Common Quick Fixes

### Chrome Not Found?
Set the path manually:
```python
# Windows
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Linux
CHROME_PATH = "/usr/bin/google-chrome"

# macOS
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
```

### Emails Not Detected?
1. Check `SUBJECT_PREFIX` matches your emails exactly
2. Verify IMAP credentials are correct
3. Look at `autoprint.log` for error messages

### Nothing Printing?
1. Check your default printer is set correctly
2. Try manual mode: `AUTO_PRINT_ENABLED = False`
3. Increase wait time: `CHROME_PRINT_WAIT_SECONDS = 10`

## Key Configuration Options

```python
# Check email every 30 seconds
POLL_INTERVAL_SECONDS = 30

# Open print dialog for confirmation (good for testing)
AUTO_PRINT_ENABLED = False

# Delete emails after successful print (use with caution!)
DELETE_EMAIL_AFTER_PRINT = True

# Monitor a different folder
MAILBOX = "Orders"  # Default is "Inbox"
```

## Running 24/7

### Windows (Task Scheduler)
1. Create Basic Task
2. Trigger: "When computer starts"
3. Action: Start `python.exe` with argument `C:\path\to\autoprint.py`
4. Check "Run whether user is logged on or not"

### Linux (systemd)
```bash
sudo nano /etc/systemd/system/autoprint.service
# [Copy service configuration from INSTALL.md]
sudo systemctl enable autoprint
sudo systemctl start autoprint
```

### macOS (launchd)
```bash
nano ~/Library/LaunchAgents/com.autoprint.service.plist
# [Copy plist configuration from INSTALL.md]
launchctl load ~/Library/LaunchAgents/com.autoprint.service.plist
```

## Dashboard Overview

```
╔═══════════════════════════════════════════════════════════╗
║              AUTOPRINT SERVICE v1.0                       ║
║         🖨️  Open-Source Email Print Automation  🖨️        ║
╚═══════════════════════════════════════════════════════════╝
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📧 Mailbox: yourstore@example.com
📁 Folder: Inbox
🔍 Filter: [PRINT]
🖨️  Mode: Enabled ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚡ Status: Idle - Waiting for next check 😴
🕐 Last Check: 14:30:15
🕑 Next Check: 14:30:45
⏱️  Next Check In: 25s
[████████████████░░░░░░░░] 67%

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 Messages Found: 3
✅ Jobs Processed: 12
⏳ Jobs Pending: 0

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 Recent Jobs:
   • [14:28:45] [PRINT] Order #1234 - Auto-printed ✓
   • [14:25:30] [PRINT] Order #1233 - Auto-printed ✓
   • [14:20:15] [PRINT] Order #1232 - Auto-printed ✓
```

## File Structure

```
autoprint-service/
├── autoprint.py           # Main application
├── README.md              # Full documentation
├── INSTALL.md             # Detailed installation guide
├── QUICKSTART.md          # This file
├── requirements.txt       # Python dependencies
├── config.example.py      # Configuration examples
├── setup.py              # Interactive setup wizard
├── LICENSE               # MIT License
├── CONTRIBUTING.md       # How to contribute
├── CHANGELOG.md          # Version history
├── .gitignore           # Git ignore rules
├── printed_uids.txt     # Generated: tracks printed emails
└── autoprint.log        # Generated: application logs
```

## Getting Help

- 📖 **Full docs**: [README.md](README.md)
- 🔧 **Installation help**: [INSTALL.md](INSTALL.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/autoprint-service/issues)
- 💬 **Questions**: [GitHub Discussions](https://github.com/yourusername/autoprint-service/discussions)

## Next Steps

1. ✅ Get it running locally
2. ✅ Test with a few emails
3. ✅ Configure your Shopify Flow
4. ✅ Set up as a service for 24/7 operation
5. ✅ Monitor the logs for a few days
6. ✅ Enable `DELETE_EMAIL_AFTER_PRINT` if desired (optional)

## Pro Tips

💡 **Start conservative**: Use manual print mode initially to verify everything works

💡 **Test thoroughly**: Send 5-10 test emails before connecting to live orders

💡 **Keep backups**: Save `printed_uids.txt` regularly to prevent duplicate prints

💡 **Monitor logs**: Check `autoprint.log` daily for the first week

💡 **Staged rollout**: Start with low-volume stores before high-volume ones

💡 **Update regularly**: Pull new versions for bug fixes and features

---

**That's it! You're ready to automate your printing.** 🎉

Questions? Check [README.md](README.md) or open an issue on GitHub!
