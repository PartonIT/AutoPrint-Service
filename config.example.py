# AutoPrint Service - Configuration Examples

# ============================================================
# EXAMPLE 1: Basic Shopify Setup
# ============================================================

IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
IMAP_USE_SSL = True
IMAP_USERNAME = "store@yourbusiness.com"
IMAP_PASSWORD = "your-app-specific-password"  # Use app-specific password for Gmail

MAILBOX = "Inbox"
POLL_INTERVAL_SECONDS = 30
SUBJECT_PREFIX = "[SHOPIFY ORDER]"

AUTO_PRINT_ENABLED = True
DELETE_EMAIL_AFTER_PRINT = False  # Keep emails for safety
CHROME_PRINT_WAIT_SECONDS = 8
TEMP_FILE_CLEANUP_HOURS = 6

# ============================================================
# EXAMPLE 2: High-Volume Store (Check every 10 seconds)
# ============================================================

IMAP_HOST = "outlook.office365.com"
IMAP_PORT = 993
IMAP_USE_SSL = True
IMAP_USERNAME = "fulfillment@highvolume-store.com"
IMAP_PASSWORD = "secure-password-here"

MAILBOX = "Inbox"
POLL_INTERVAL_SECONDS = 10  # Check more frequently
SUBJECT_PREFIX = "[PRINT]"

AUTO_PRINT_ENABLED = True
DELETE_EMAIL_AFTER_PRINT = True  # Auto-delete after successful print
CHROME_PRINT_WAIT_SECONDS = 5  # Faster for high volume
TEMP_FILE_CLEANUP_HOURS = 2  # More frequent cleanup

# ============================================================
# EXAMPLE 3: Manual Review Mode (For Testing)
# ============================================================

IMAP_HOST = "mail.privateemail.com"
IMAP_PORT = 993
IMAP_USE_SSL = True
IMAP_USERNAME = "test@teststore.com"
IMAP_PASSWORD = "test-password"

MAILBOX = "Inbox"
POLL_INTERVAL_SECONDS = 60  # Less frequent for testing
SUBJECT_PREFIX = "[TEST PRINT]"

AUTO_PRINT_ENABLED = False  # Open print dialog for manual confirmation
DELETE_EMAIL_AFTER_PRINT = False
CHROME_PRINT_WAIT_SECONDS = 8
TEMP_FILE_CLEANUP_HOURS = 12

# ============================================================
# EXAMPLE 4: Multiple Store Setup (Run multiple instances)
# ============================================================

# Store 1 Configuration (save as autoprint_store1.py)
IMAP_HOST = "imap.gmail.com"
IMAP_USERNAME = "store1@business.com"
SUBJECT_PREFIX = "[STORE1]"
LOG_FILE = "autoprint_store1.log"
PRINTED_UIDS_FILE = "printed_uids_store1.txt"

# Store 2 Configuration (save as autoprint_store2.py)
IMAP_HOST = "imap.gmail.com"
IMAP_USERNAME = "store2@business.com"
SUBJECT_PREFIX = "[STORE2]"
LOG_FILE = "autoprint_store2.log"
PRINTED_UIDS_FILE = "printed_uids_store2.txt"

# ============================================================
# EXAMPLE 5: Custom Chrome Path
# ============================================================

# Windows
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Linux
CHROME_PATH = "/usr/bin/google-chrome"

# macOS
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ============================================================
# COMMON EMAIL PROVIDER SETTINGS
# ============================================================

# Gmail
IMAP_HOST = "imap.gmail.com"
IMAP_PORT = 993
# Note: Requires app-specific password or OAuth2
# https://support.google.com/accounts/answer/185833

# Outlook / Office 365
IMAP_HOST = "outlook.office365.com"
IMAP_PORT = 993

# Yahoo Mail
IMAP_HOST = "imap.mail.yahoo.com"
IMAP_PORT = 993
# Note: Requires app password
# https://help.yahoo.com/kb/generate-third-party-passwords-sln15241.html

# iCloud
IMAP_HOST = "imap.mail.me.com"
IMAP_PORT = 993
# Note: Requires app-specific password
# https://support.apple.com/en-us/HT204397

# ProtonMail (via Bridge)
IMAP_HOST = "127.0.0.1"
IMAP_PORT = 1143
IMAP_USE_SSL = False  # Bridge handles encryption locally

# Zoho Mail
IMAP_HOST = "imap.zoho.com"
IMAP_PORT = 993

# FastMail
IMAP_HOST = "imap.fastmail.com"
IMAP_PORT = 993

# ============================================================
# SECURITY NOTES
# ============================================================

# 1. Never commit passwords to version control
# 2. Use app-specific passwords when available
# 3. Consider using environment variables:
#    IMAP_PASSWORD = os.environ.get('AUTOPRINT_PASSWORD')
# 4. Restrict email account permissions to read-only if possible
# 5. Enable 2FA on your email account
# 6. Regularly rotate passwords
# 7. Monitor the log file for unauthorized access attempts
