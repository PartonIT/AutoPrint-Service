# AutoPrint Service 🖨️

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey.svg)]()

**A free, open-source alternative to paid Shopify auto-print apps.**

AutoPrint Service monitors your email inbox and automatically prints order confirmations, packing slips, invoices, and other documents sent via Shopify Flow triggers or any email automation system.

Perfect for e-commerce businesses, fulfillment centers, and anyone who needs reliable automated printing from email.

## ✨ Features

- 🔄 **Real-time Monitoring** - Continuously watches your IMAP mailbox for new emails
- 🖨️ **Automatic Printing** - Prints HTML email content directly to your default printer
- 🎯 **Smart Filtering** - Only processes emails matching your configured subject prefix
- 🧹 **Auto-Cleanup** - Manages temporary files with configurable retention periods
- 📊 **Live Dashboard** - Beautiful terminal UI showing real-time status and statistics
- 📝 **Comprehensive Logging** - Detailed logs for troubleshooting and audit trails
- 🔒 **Safe by Default** - Doesn't delete emails unless explicitly configured
- 🚀 **Lightweight** - Minimal dependencies, runs efficiently 24/7
- 🎨 **Cross-Platform** - Works on Windows, Linux, and macOS

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Google Chrome or Chromium browser
- IMAP-enabled email account

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/autoprint-service.git
cd autoprint-service
```

2. Install dependencies:
```bash
pip install colorama
```

3. Configure your settings in `autoprint.py`:
```python
IMAP_HOST = "mail.example.com"
IMAP_USERNAME = "your-email@example.com"
IMAP_PASSWORD = "your-password-here"
SUBJECT_PREFIX = "[PRINT]"  # Only emails starting with this will be printed
```

4. Run the service:
```bash
python autoprint.py
```

## ⚙️ Configuration

Edit the configuration section at the top of `autoprint.py`:

```python
# Email Settings
IMAP_HOST = "mail.example.com"      # Your IMAP server
IMAP_PORT = 993                      # Usually 993 for SSL
IMAP_USE_SSL = True                  # Use SSL connection
IMAP_USERNAME = "you@example.com"    # Your email address
IMAP_PASSWORD = "password"           # Your email password
MAILBOX = "Inbox"                    # Mailbox to monitor

# Print Settings
SUBJECT_PREFIX = "[PRINT]"           # Filter: only print emails with this prefix
AUTO_PRINT_ENABLED = True            # True = auto-print, False = manual dialog
POLL_INTERVAL_SECONDS = 30           # How often to check for new emails
CHROME_PRINT_WAIT_SECONDS = 8        # Seconds to wait for print job
TEMP_FILE_CLEANUP_HOURS = 6          # Hours before cleaning temp files

# Safety Settings
DELETE_EMAIL_AFTER_PRINT = False     # WARNING: Permanently deletes emails!
```

## 📧 Shopify Flow Integration

### Setting Up Email Triggers

1. In your Shopify admin, go to **Settings → Notifications → Shopify Flow**
2. Create a new workflow triggered by "Order created" (or your preferred trigger)
3. Add an action: **Send email**
4. Configure the email:
   - **To:** Your monitored email address
   - **Subject:** `[PRINT] Order #{{ order.name }}`
   - **Body:** Use HTML template with your packing slip design

### Example Shopify Flow Email Template

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .header { text-align: center; margin-bottom: 30px; }
        .order-info { margin: 20px 0; }
        .items { width: 100%; border-collapse: collapse; }
        .items th, .items td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        .items th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Packing Slip</h1>
        <p>Order #{{ order.name }}</p>
    </div>
    
    <div class="order-info">
        <strong>Customer:</strong> {{ order.customer.name }}<br>
        <strong>Email:</strong> {{ order.customer.email }}<br>
        <strong>Date:</strong> {{ order.created_at | date: "%B %d, %Y" }}
    </div>
    
    <table class="items">
        <thead>
            <tr>
                <th>Item</th>
                <th>SKU</th>
                <th>Quantity</th>
            </tr>
        </thead>
        <tbody>
            {% for line_item in order.line_items %}
            <tr>
                <td>{{ line_item.title }}</td>
                <td>{{ line_item.sku }}</td>
                <td>{{ line_item.quantity }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    
    <div class="order-info" style="margin-top: 30px;">
        <strong>Shipping Address:</strong><br>
        {{ order.shipping_address.name }}<br>
        {{ order.shipping_address.address1 }}<br>
        {% if order.shipping_address.address2 != blank %}
        {{ order.shipping_address.address2 }}<br>
        {% endif %}
        {{ order.shipping_address.city }}, {{ order.shipping_address.province_code }} {{ order.shipping_address.zip }}<br>
        {{ order.shipping_address.country }}
    </div>
</body>
</html>
```

## 🎯 Use Cases

- **E-commerce Order Fulfillment** - Print packing slips as orders arrive
- **Invoice Processing** - Auto-print invoices from accounting systems
- **Shipping Labels** - Print labels from carrier notification emails
- **Receipt Printing** - Print customer receipts from POS systems
- **Document Archival** - Print important documents for physical filing
- **Multi-Store Management** - Monitor multiple stores with different email filters

## 📊 Dashboard Features

The live terminal dashboard shows:

- ✅ Current connection status
- 📊 Total messages found and processed
- ⏱️ Countdown to next check with progress bar
- 📋 Recent print jobs (last 3)
- ⚠️ Recent errors (if any)
- 🧹 Automatic cleanup status

## 🔧 Advanced Configuration

### Custom Chrome Path

If Chrome isn't found automatically, set the path manually:

```python
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Windows
# or
CHROME_PATH = "/usr/bin/google-chrome"  # Linux
# or
CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # macOS
```

### Manual Print Mode

Set `AUTO_PRINT_ENABLED = False` to open the print dialog instead of auto-printing:

```python
AUTO_PRINT_ENABLED = False  # Opens print dialog for manual confirmation
```

### Email Deletion

**⚠️ Use with caution!** Enable automatic email deletion after successful prints:

```python
DELETE_EMAIL_AFTER_PRINT = True  # Permanently deletes emails after printing
```

**Note:** Emails are only deleted if the print job succeeds. Failed prints leave emails in your inbox for retry.

## 🛠️ Troubleshooting

### "Could not find Chrome" Error

Set `CHROME_PATH` to your Chrome installation path in the configuration.

### Emails Not Being Detected

1. Verify your `SUBJECT_PREFIX` matches your email subjects
2. Check IMAP credentials are correct
3. Ensure IMAP is enabled on your email account
4. Review `autoprint.log` for detailed error messages

### Print Jobs Not Appearing

1. Check your default printer is set correctly
2. Increase `CHROME_PRINT_WAIT_SECONDS` if print jobs are timing out
3. Try setting `AUTO_PRINT_ENABLED = False` to test the print dialog manually

### Connection Issues

1. Verify IMAP settings (host, port, SSL)
2. Check firewall/antivirus isn't blocking IMAP connections
3. Some email providers require app-specific passwords (Gmail, Yahoo, etc.)

## 📝 Logging

All events are logged to `autoprint.log` with timestamps:

```
[2025-11-17 14:30:15] [INFO] AutoPrint Service Started
[2025-11-17 14:30:16] [SUCCESS] Connected to mailbox successfully
[2025-11-17 14:30:45] [SUCCESS] Job processed: [PRINT] Order #1001 - Auto-printed ✓
[2025-11-17 14:31:12] [ERROR] Print failed for 'Order #1002': Connection timeout
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built as a free alternative to expensive Shopify auto-print subscriptions
- Inspired by the needs of small e-commerce businesses
- Designed for reliability and ease of use

## 💡 Tips for Production Use

1. **Run as a Service**
   - Linux: Use systemd service
   - Windows: Use Task Scheduler or NSSM
   - macOS: Use launchd

2. **Security Best Practices**
   - Use app-specific passwords instead of main account password
   - Restrict IMAP permissions to read-only if possible
   - Keep `printed_uids.txt` backed up to prevent duplicate prints

3. **Reliability**
   - Monitor the log file for errors
   - Set up alerts for extended downtime
   - Test with a few emails before enabling `DELETE_EMAIL_AFTER_PRINT`

4. **Performance**
   - Adjust `POLL_INTERVAL_SECONDS` based on your email volume
   - Lower `TEMP_FILE_CLEANUP_HOURS` if disk space is limited
   - Consider dedicating a printer specifically for this service

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/autoprint-service/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/autoprint-service/discussions)

## 🗺️ Roadmap

- [ ] Support for multiple email accounts
- [ ] Web-based configuration interface
- [ ] Email attachment printing
- [ ] Print job queuing with retry logic
- [ ] Webhook support for non-email triggers
- [ ] Docker containerization
- [ ] REST API for remote control
- [ ] Print templates and preprocessing

---

**Made with ❤️ for the e-commerce community**

*Save money, print automatically!*
