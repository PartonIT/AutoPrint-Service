# AutoPrint Service

**Free, open-source Shopify order printing solution** - No subscriptions, no per-order fees, complete control.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

A Python-based service that monitors IMAP email accounts and automatically prints emails matching specified subject filters. When paired with Shopify Flow email triggers, it becomes a powerful free alternative to expensive auto-print subscription apps.

---

## 🎯 Why AutoPrint Service?

### Cost Comparison
- **Paid Shopify Apps**: $10-30/month + per-order fees
- **AutoPrint Service**: **FREE forever**

### Perfect Pairing with Shopify Flow
1. Set up a Shopify Flow that emails formatted documents on order events
2. AutoPrint Service monitors your inbox and prints them automatically
3. No monthly subscriptions, no per-order fees
4. Complete control over your printing workflow

---

## ✨ Features

- 📧 **Real-time IMAP monitoring** - Checks mailbox every 30 seconds (configurable)
- 🖨️ **Automatic Chrome printing** - Uses Chrome's kiosk mode for reliable printing
- 🔍 **Smart filtering** - Only prints emails matching your custom subject prefix
- 🔄 **Duplicate prevention** - Tracks printed emails to avoid reprints
- 🗑️ **Optional email deletion** - Auto-delete processed emails (disabled by default)
- 🧹 **Automatic cleanup** - Removes old temp files every 6 hours
- 📊 **Live dashboard** - Beautiful console UI with real-time statistics
- 📝 **Detailed logging** - Complete audit trail in `dwc_orders.log`
- 🎨 **Colored output** - Optional colorama support for better readability

---

## 🛍️ Common Use Cases

- ✅ Order confirmations and packing slips
- 📦 Shipping labels and customs forms
- 📋 Pick lists for warehouse teams
- 🧾 Customer invoices and receipts
- ↩️ Return authorization forms
- 📄 Custom fulfillment documents

---

## 📋 Requirements

- **Python 3.7+**
- **Google Chrome** (installed and accessible)
- **IMAP-enabled email account** (Gmail, Outlook, custom domain, etc.)
- **Shopify Flow** or any email automation tool (optional but recommended)

---

## 🚀 Quick Start

### 1. Install Python Dependencies

```bash
# Required
pip install colorama

# That's it! Only one dependency needed.
```

### 2. Configure the Service

Open `autoprint_service.py` and edit the configuration section:

```python
# ==========================
# CONFIGURATION
# ==========================

# Email Settings
IMAP_HOST = "mail.example.com"          # Your IMAP server
IMAP_PORT = 993                          # Usually 993 for SSL
IMAP_USE_SSL = True                      # Use SSL connection
IMAP_USERNAME = "orders@yourdomain.com"  # Your email address
IMAP_PASSWORD = "your_password_here"     # Your email password

# Mailbox Settings
MAILBOX = "Inbox"                        # Mailbox folder to monitor
POLL_INTERVAL_SECONDS = 30               # Check every 30 seconds

# Print Filter
SUBJECT_PREFIX = "[PRINT ORDER]"         # Only print emails with this subject prefix

# Print Behavior
AUTO_PRINT_ENABLED = True                # True = auto-print, False = open print dialog
CHROME_PATH = ""                         # Leave empty for auto-detection
CHROME_PRINT_WAIT_SECONDS = 8            # Wait time for Chrome to print

# File Management
PRINTED_UIDS_FILE = "printed_uids.txt"   # Tracks processed emails
TEMP_FILE_CLEANUP_HOURS = 6              # Clean temp files older than 6 hours

# Email Deletion (⚠️ USE WITH CAUTION)
DELETE_EMAIL_AFTER_PRINT = False         # Set to True to delete emails after printing

# Logging
LOG_FILE = "dwc_orders.log"              # Log file location
DEBUG = False                             # Enable debug mode
```

### 3. Run the Service

```bash
python autoprint_service.py
```

You should see the AutoPrint Service dashboard appear with live statistics!

---

## ⚙️ Configuration Guide

### Email Settings

#### `IMAP_HOST`
Your email provider's IMAP server address.

**Common providers:**
- Gmail: `imap.gmail.com`
- Outlook/Office365: `outlook.office365.com`
- Yahoo: `imap.mail.yahoo.com`
- Custom domain: Usually `mail.yourdomain.com` or `imap.yourdomain.com`

#### `IMAP_PORT`
IMAP server port number.
- **993** - SSL/TLS (recommended)
- **143** - Non-SSL (not recommended)

#### `IMAP_USE_SSL`
Enable SSL/TLS encryption.
- `True` - Secure connection (recommended)
- `False` - Unencrypted (not recommended)

#### `IMAP_USERNAME`
Your full email address (e.g., `orders@yourdomain.com`)

#### `IMAP_PASSWORD`
Your email password or app-specific password.

**⚠️ Security Notes:**
- For Gmail: Use an [App Password](https://support.google.com/accounts/answer/185833), not your main password
- For Office365: May need to [enable IMAP access](https://support.microsoft.com/en-us/office/pop-imap-and-smtp-settings-8361e398-8af4-4e97-b147-6c6c4ac95353)
- Never commit passwords to version control
- Consider using environment variables for production

---

### Mailbox Settings

#### `MAILBOX`
Which email folder to monitor.
- `"Inbox"` - Main inbox (most common)
- `"Orders"` - Custom folder
- `"INBOX"` - Alternative inbox name (some servers)

#### `POLL_INTERVAL_SECONDS`
How often to check for new emails (in seconds).
- `30` - Check every 30 seconds (recommended)
- `60` - Check every minute (less frequent)
- `10` - Check every 10 seconds (more responsive, but more load)

---

### Print Filter

#### `SUBJECT_PREFIX`
Only emails with subjects starting with this text will be printed.

**Examples:**
```python
SUBJECT_PREFIX = "[PRINT ORDER]"      # For Shopify orders
SUBJECT_PREFIX = "[PRINT PACKING]"    # For packing slips
SUBJECT_PREFIX = "[PRINT LABEL]"      # For shipping labels
SUBJECT_PREFIX = "🖨️ PRINT:"          # Can use emojis!
```

**Case-insensitive matching:**
- `[PRINT ORDER]` matches `[PRINT ORDER]`, `[print order]`, `[Print Order]`

---

### Print Behavior

#### `AUTO_PRINT_ENABLED`
Control printing behavior.
- `True` - Automatically print without user interaction (recommended for automation)
- `False` - Open Chrome with print dialog (manual confirmation required)

#### `CHROME_PATH`
Path to Chrome executable. Leave empty for auto-detection.

**Manual paths (if auto-detection fails):**
```python
# Windows
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Windows (x86)
CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

# Leave empty for auto-detection (recommended)
CHROME_PATH = ""
```

#### `CHROME_PRINT_WAIT_SECONDS`
How long to wait for Chrome to finish printing before closing.
- `8` - Default (recommended)
- `5` - Faster for simple documents
- `15` - Longer for complex documents or slow printers

---

### File Management

#### `PRINTED_UIDS_FILE`
File that tracks processed email UIDs to prevent duplicate printing.
- Default: `"printed_uids.txt"`
- **Important**: Don't delete this file while the service is running
- Delete it to reprocess all emails (useful for testing)

#### `TEMP_FILE_CLEANUP_HOURS`
How often to clean up old temporary HTML files.
- `6` - Clean up files older than 6 hours (default)
- `24` - Keep files for 1 day
- `1` - Aggressive cleanup every hour

**Temp file locations:**
- Modified print files: System temp directory (`print_*.html`)
- Job files: `<temp_dir>/print_pack_jobs/`

---

### Email Deletion

#### `DELETE_EMAIL_AFTER_PRINT`
**⚠️ DANGEROUS SETTING - USE WITH CAUTION**

Controls whether emails are permanently deleted after successful printing.

```python
DELETE_EMAIL_AFTER_PRINT = False  # Safe default - keeps emails
DELETE_EMAIL_AFTER_PRINT = True   # ⚠️ Deletes emails after printing
```

**How it works:**
- `False` - Emails remain in inbox after printing (safe default)
- `True` - Emails are **permanently deleted** after successful print

**Important notes:**
- Only deletes after **successful** print
- If printing fails, email stays in inbox for retry
- Deletion is **permanent** - emails cannot be recovered
- Email is still marked as "read" even if `DELETE_EMAIL_AFTER_PRINT = False`
- Temp files are managed separately regardless of this setting

**Recommended workflow:**
1. Start with `False` and test thoroughly
2. Create email filters to move printed emails to an archive folder
3. Only enable `True` if you're absolutely certain

---

### Logging

#### `LOG_FILE`
Location of the detailed log file.
- Default: `"dwc_orders.log"`
- Logs include: connections, prints, errors, cleanup events
- Rotates automatically (appends to existing file)

#### `DEBUG`
Enable debug mode for troubleshooting.
- `False` - Normal operation (default)
- `True` - Verbose logging (for development)

---

## 🔧 Shopify Flow Setup

### Example Workflow

1. **Create a Shopify Flow:**
   - Trigger: "Order created"
   - Condition: "Order is paid"
   - Action: "Send email"

2. **Configure Email Action:**
   - **To**: Your monitoring email (e.g., `orders@yourdomain.com`)
   - **Subject**: `[PRINT ORDER] Order #{{ order.name }}`
   - **Body**: Your formatted HTML packing slip/invoice

3. **Configure AutoPrint Service:**
   ```python
   IMAP_USERNAME = "orders@yourdomain.com"
   IMAP_PASSWORD = "your_password"
   SUBJECT_PREFIX = "[PRINT ORDER]"
   AUTO_PRINT_ENABLED = True
   ```

4. **Run and Test:**
   ```bash
   python autoprint_service.py
   ```

5. **Place a test order** - it should auto-print!

---

## 📊 Dashboard Overview

When running, you'll see a live dashboard:

```
    ██████╗ ██╗    ██╗ ██████╗     ██████╗ ██████╗ ██████╗ ███████╗██████╗ ███████╗
    ██╔══██╗██║    ██║██╔════╝    ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝
    ██║  ██║██║ █╗ ██║██║         ██║   ██║██████╔╝██║  ██║█████╗  ██████╔╝███████╗
    ██║  ██║██║███╗██║██║         ██║   ██║██╔══██╗██║  ██║██╔══╝  ██╔══██╗╚════██║
    ██████╔╝╚███╔███╔╝╚██████╗    ╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║███████║
    ╚═════╝  ╚══╝╚══╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝
                       🖨️  Automatic Email Print Service  🖨️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    📧 Mailbox: orders@yourdomain.com
    📁 Folder: Inbox
    🔍 Filter: [PRINT ORDER]
    🖨️  Mode: Enabled ✓
    🗑️  Delete After Print: Disabled ✓

─────────────────────────────────────────────────────────────────────────────────

    ⚡ Status: Idle - Waiting for next check 😴
    🕐 Last Check: 14:32:15
    🕑 Next Check: 14:32:45
    ⏱️  Next Check In: 23s
    [███████████████████░░░░░░░░] 73%

─────────────────────────────────────────────────────────────────────────────────

    📊 Messages Found: 45
    ✅ Jobs Processed: 12
    ⏳ Jobs Pending: 0

─────────────────────────────────────────────────────────────────────────────────

    🧹 Last Cleanup: 14:00:00
    🕐 Next Cleanup: 20:00:00

─────────────────────────────────────────────────────────────────────────────────

    📋 Recent Jobs:
       • [14:31:05] [PRINT ORDER] Order #1234 - Auto-printed ✓
       • [14:28:32] [PRINT ORDER] Order #1233 - Auto-printed ✓
       • [14:25:18] [PRINT ORDER] Order #1232 - Auto-printed ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              Press Ctrl+C to exit
```

**Dashboard Features:**
- ⚡ Live status updates
- 📊 Real-time statistics
- 🎨 Animated progress bar
- 📋 Recent job history
- ⚠️ Error notifications
- 🧹 Cleanup tracking

---

## 🐛 Troubleshooting

### Chrome not found
**Error**: `Could not find Chrome. Set CHROME_PATH in config.`

**Solution**: Set `CHROME_PATH` manually:
```python
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

---

### IMAP connection failed
**Error**: `IMAP error - Reconnecting...`

**Solutions:**
1. **Check credentials**: Verify `IMAP_USERNAME` and `IMAP_PASSWORD`
2. **Enable IMAP**: Some providers require enabling IMAP in settings
3. **App passwords**: Gmail/Outlook require app-specific passwords
4. **Firewall**: Ensure port 993 is not blocked
5. **Server address**: Double-check `IMAP_HOST`

---

### Emails not printing
**Possible causes:**

1. **Subject prefix mismatch**
   - Check email subject starts with exact `SUBJECT_PREFIX`
   - Matching is case-insensitive but must be at the start

2. **Already printed**
   - Check `printed_uids.txt` - email UID might be logged
   - Delete file to reprocess (for testing only)

3. **Wrong mailbox**
   - Verify `MAILBOX = "Inbox"` is correct
   - Some servers use `"INBOX"` (uppercase)

4. **Email not in HTML**
   - Service works best with HTML emails
   - Plain text is converted but may not format well

---

### Colorama not working
**Warning**: `Note: Install colorama for colored output`

**Solution**: Install colorama for colored dashboard:
```bash
pip install colorama
```

Service works fine without it, just no colors.

---

### Print dialog opens instead of auto-printing
**Issue**: Chrome opens with print dialog instead of auto-printing

**Solution**: Ensure `AUTO_PRINT_ENABLED = True` in config.

If still happening:
- Check Chrome permissions
- Try increasing `CHROME_PRINT_WAIT_SECONDS`
- Ensure default printer is set in OS

---

## 📁 File Structure

```
autoprint-service/
├── autoprint_service.py    # Main service script
├── printed_uids.txt         # Tracks processed emails (auto-generated)
├── dwc_orders.log           # Detailed log file (auto-generated)
├── README.md                # This file
└── LICENSE                  # GPL-3.0 License
```

**Generated at runtime:**
- `printed_uids.txt` - UID tracking (don't delete while running)
- `dwc_orders.log` - Rotating log file
- Temp files in system temp directory

---

## 🔐 Security Best Practices

1. **Use app-specific passwords** for Gmail/Outlook
2. **Never commit** `autoprint_service.py` with real passwords to Git
3. **Use environment variables** for production:
   ```python
   import os
   IMAP_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
   ```
4. **Restrict file permissions** on config file
5. **Use SSL/TLS** connections (`IMAP_USE_SSL = True`)
6. **Monitor logs** regularly for suspicious activity
7. **Backup** `printed_uids.txt` to prevent reprocessing

---

## 🚀 Running as a Service

### Windows (using NSSM)

1. Download [NSSM](https://nssm.cc/)
2. Install service:
   ```cmd
   nssm install AutoPrintService "C:\Python39\python.exe" "C:\path\to\autoprint_service.py"
   nssm set AutoPrintService AppDirectory "C:\path\to"
   nssm start AutoPrintService
   ```

### Linux (systemd)

1. Create service file `/etc/systemd/system/autoprint.service`:
   ```ini
   [Unit]
   Description=AutoPrint Email Service
   After=network.target

   [Service]
   Type=simple
   User=youruser
   WorkingDirectory=/path/to/autoprint
   ExecStart=/usr/bin/python3 /path/to/autoprint_service.py
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

2. Enable and start:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable autoprint
   sudo systemctl start autoprint
   ```

3. Check status:
   ```bash
   sudo systemctl status autoprint
   ```

---

## 📝 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

### What this means:
- ✅ Free to use, modify, and distribute
- ✅ Can use commercially
- ✅ Can modify and create derivatives
- ⚠️ Must disclose source code
- ⚠️ Must use same GPL-3.0 license for derivatives
- ⚠️ Must state changes made

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Areas for contribution:
- Additional email providers documentation
- Docker containerization
- Web-based configuration UI
- Multi-printer support
- Email template validation
- Additional logging formats

---

## ⭐ Support

If this project saves you money on expensive Shopify apps, consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs and issues
- 📖 Improving documentation
- 🔧 Contributing code

---

## 📧 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/autoprint-service/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/autoprint-service/discussions)

---

## 🙏 Acknowledgments

Created as a free alternative to expensive Shopify auto-print subscription services. Built with ❤️ for small business owners who want control over their workflows without breaking the bank.

---

**Happy Printing! 🖨️**
