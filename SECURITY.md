# Security Policy

## Supported Versions

We release patches for security vulnerabilities in the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

The Contact Manager team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report a Security Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via one of the following methods:

1. **Email**: Send an email to security@example.com (replace with actual email)
2. **Private Security Advisory**: Use GitHub's private vulnerability reporting feature

### What to Include in Your Report

To help us better understand and resolve the issue, please include:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline

- **Initial Response**: Within 48 hours of receiving your report
- **Status Update**: Within 7 days with our assessment and expected timeline
- **Fix Release**: Depends on severity and complexity
  - Critical: Within 7 days
  - High: Within 30 days
  - Medium: Within 90 days
  - Low: Next regular release

### What to Expect

1. **Acknowledgment**: We'll acknowledge receipt of your report
2. **Assessment**: We'll assess the vulnerability and determine its severity
3. **Development**: We'll work on a fix
4. **Testing**: We'll test the fix thoroughly
5. **Release**: We'll release a patched version
6. **Disclosure**: We'll coordinate public disclosure with you

## Security Best Practices for Users

### Data Storage

- Contact data is stored in `data/contacts.json` in plain text
- Sensitive contact information should be protected at the filesystem level
- Use appropriate file permissions to restrict access
- Consider encrypting the filesystem or data directory for sensitive data

### Running the Application

- Only run Contact Manager from trusted sources
- Keep your Python installation up to date
- Use virtual environments to isolate dependencies
- Review imported/exported files before processing

### Development

- Never commit sensitive data (contacts.json, .env files, etc.)
- Use the provided .gitignore to prevent accidental commits
- Keep development dependencies up to date
- Run security checks regularly:
  ```bash
  bandit -r src
  ```

## Known Security Considerations

### Data Storage

**Issue**: Contact data is stored in plain JSON format without encryption.

**Mitigation**:
- Users should protect the `data/` directory with appropriate filesystem permissions
- For sensitive data, consider storing the entire Contact Manager directory on an encrypted volume

**Future Plans**:
- Add optional encryption for contact data
- Support for password-protected contact databases

### Input Validation

**Current Protection**:
- Email validation prevents malformed email addresses
- Phone validation ensures proper format
- Input sanitization removes leading/trailing whitespace

**Best Practice**:
- We validate all user inputs
- No execution of user-provided code
- JSON parsing uses safe standard library functions

### Export Functionality

**Consideration**: Exported CSV/JSON files may contain sensitive information.

**Mitigation**:
- Users should be aware of where files are exported
- Exported files inherit system default permissions
- Users should secure exported files appropriately

## Security Update Process

1. Security issues are fixed in a private repository
2. A patch is prepared and tested
3. A security advisory is published
4. The patch is released
5. Users are notified through:
   - GitHub Security Advisories
   - Release notes
   - Project announcements

## Vulnerability Disclosure Policy

- We follow coordinated disclosure
- We aim to give users time to update before public disclosure
- We credit security researchers (if desired)
- We maintain a security hall of fame for researchers who help us

## Security Hall of Fame

We'd like to thank the following security researchers for responsibly disclosing vulnerabilities:

<!-- List will be updated as vulnerabilities are reported and fixed -->

*No vulnerabilities reported yet.*

## Additional Resources

- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories)

## Contact

For security issues: security@example.com (replace with actual email)

For general issues: [GitHub Issues](https://github.com/pyenthusiasts/Contact-Manager/issues)

---

Thank you for helping keep Contact Manager and its users safe!
