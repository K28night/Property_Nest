// import smtplib
// import ssl
// from email.message import EmailMessage
// import schedule
// import time
// import pandas as pd

// # Email configuration
// EMAIL_ADDRESS = 'your_email@example.com'
// EMAIL_PASSWORD = 'your_email_password'
// SMTP_SERVER = 'smtp.gmail.com'
// SMTP_PORT = 465  # For SSL

// # Function to generate the report (replace with your logic)
// def generate_report():
//     # Create a dummy DataFrame to simulate a report
//     data = {
//         'Date': ['2024-08-29', '2024-08-30', '2024-08-31'],
//         'Metric1': [100, 200, 150],
//         'Metric2': [300, 400, 350]
//     }
//     df = pd.DataFrame(data)
    
//     # Save the report as a CSV file
//     report_file = 'daily_report.csv'
//     df.to_csv(report_file, index=False)
    
//     return report_file

// # Function to send the email
// def send_email(report_file):
//     msg = EmailMessage()
//     msg['Subject'] = 'Daily Report'
//     msg['From'] = EMAIL_ADDRESS
//     msg['To'] = 'recipient@example.com'
//     msg.set_content('Please find the attached daily report.')

//     # Attach the report file
//     with open(report_file, 'rb') as f:
//         file_data = f.read()
//         file_name = f.name
    
//     msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
//     # Set up the secure SSL context and send the email
//     context = ssl.create_default_context()
    
//     with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
//         server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
//         server.send_message(msg)
//         print('Email sent!')

// # Function to generate and send the report
// def job():
//     report_file = generate_report()
//     send_email(report_file)

// # Schedule the job every day at a specific time
// schedule.every().day.at("09:00").do(job)

// print("Scheduler started...")

// # Keep the script running
// while True:
//     schedule.run_pending()
//     time.sleep(1)

// schedule.every().day.at("09:00").do(job)
