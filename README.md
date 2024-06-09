# Personalized Email Sender

## Overview
The **Personalized Email Sender** is a web-based application that allows users to send customized emails to multiple recipients efficiently. Users can add personalized content, including headers, body text, and footers, dynamically insert recipient-specific details, and upload recipient details via CSV files. The tool provides real-time feedback on email delivery status, ensuring a seamless communication experience.

## Features
- **Customizable Email Content**: Add your own headers, content, and footers.
- **CSV Integration**: Upload recipient details through a CSV file.
- **Dynamic Personalization**: Insert recipient-specific details into each email.
- **Real-Time Feedback**: Get confirmation for sent emails and error notifications.
- **Secure Sending**: Uses Gmail's SMTP server with App Passwords for secure authentication.

## Installation

### Prerequisites
- Python 3.11
- Flask
- Pandas

### Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/personalized-email-sender.git
    cd personalized-email-sender
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Gmail App Password:
    - Follow the instructions to create an App Password [here](https://support.google.com/accounts/answer/185833?hl=en).
    - Update `config.py` with your Gmail address and App Password.

## Usage

1. Run the Flask application:
    ```bash
    python personalized_email_sender.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000`.

3. Upload your CSV file with recipient details.

4. Customize your email with a header, content, and footer.

5. Click send and monitor real-time feedback for email status.

## Configuration

In the `config.py` file, set up your Gmail credentials:
```python
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-app-password'
```

Ensure you have the following columns in your CSV file:
- `email`: Recipient's email address.
- `name`: Recipient's name (or other dynamic content fields you wish to use).

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
If you have any questions, feel free to reach out:

- Email: mbinasifmba18
- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/mbinasif/)

---
