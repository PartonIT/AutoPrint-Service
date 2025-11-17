# Changelog

All notable changes to AutoPrint Service will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-17

### Initial Release

#### Added
- Core IMAP email monitoring functionality
- Automatic HTML email printing via Chrome
- Beautiful terminal UI with real-time status updates
- Progress bar countdown to next check
- Subject prefix filtering for targeted printing
- Duplicate prevention with UID tracking
- Comprehensive logging system
- Automatic temp file cleanup
- Optional email deletion after successful print
- Manual print mode (opens print dialog)
- Multi-platform support (Windows, Linux, macOS)
- Colorama support for enhanced terminal colors
- Error handling and automatic reconnection
- Configuration examples for common email providers
- Detailed documentation and installation guides

#### Features
- **Real-time Dashboard**: Live status, statistics, and recent job history
- **Smart Filtering**: Only processes emails matching configured prefix
- **Reliability**: Automatic reconnection on connection failures
- **Safety**: Emails preserved by default, deletion optional
- **Performance**: Efficient polling with configurable intervals
- **Cleanup**: Automatic management of temporary HTML files
- **Logging**: Detailed timestamped logs for troubleshooting
- **Cross-Platform**: Works on Windows, Linux, and macOS

#### Documentation
- README.md with comprehensive feature overview
- INSTALL.md with platform-specific installation guides
- CONTRIBUTING.md with contribution guidelines
- config.example.py with multiple configuration examples
- MIT License for open-source distribution
- Interactive setup wizard (setup.py)

#### Configuration Options
- IMAP host, port, SSL settings
- Email credentials and mailbox selection
- Subject prefix filtering
- Auto-print vs. manual mode
- Polling interval customization
- Chrome path configuration
- Temp file cleanup intervals
- Optional email deletion after print

#### Known Limitations
- Requires Google Chrome or Chromium browser
- Email must contain HTML content for best results
- Plain text emails converted to basic HTML
- Attachments are not processed (by design)
- Single printer support (uses system default)

---

## [Unreleased]

### Planned Features

#### High Priority
- [ ] Support for multiple email accounts
- [ ] Email attachment printing (PDF, images)
- [ ] Print job queuing with retry logic
- [ ] Web-based configuration interface
- [ ] Docker containerization

#### Medium Priority
- [ ] Print templates and preprocessing
- [ ] Multiple printer support with rules
- [ ] Webhook support for non-email triggers
- [ ] REST API for remote control
- [ ] Email notification on print failure
- [ ] Statistics dashboard (web UI)

#### Low Priority
- [ ] OAuth2 support for Gmail/Outlook
- [ ] Print preview before printing
- [ ] Barcode/QR code generation
- [ ] Integration with shipping APIs
- [ ] Custom HTML preprocessing scripts
- [ ] Print job scheduling

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to propose changes to this project.

## Version History

- **v1.0.0** (2025-11-17): Initial public release

---

**Note**: This is the first public release of AutoPrint Service. Future versions will be documented here as features are added and improvements are made.
