import React, { useState } from 'react';
import axios from 'axios';



const EmailInterface = () => {
  const [emailSettings, setEmailSettings] = useState({
    smtp_server: '',
    smtp_port: '',
    imap_server: '',
    imap_port: '',
    email: '',
    password: ''
  });
  
  const [emailContent, setEmailContent] = useState({
    subject: '',
    body: '',
    to_email: ''
  });

  const updateSettings = () => {
    axios.put('/api/update_email_settings/', emailSettings)
      .then(response => {
        console.log("Settings updated");
      })
      .catch(error => {
        console.log("Error updating settings");
      });
  };

  const sendEmail = () => {
    axios.post('/api/send_email/', emailContent)
      .then(response => {
        console.log("Email sent");
      })
      .catch(error => {
        console.log("Error sending email");
      });
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
      <div>
        {/* Email editor */}
        <input type="text" placeholder="Subject" onChange={e => setEmailContent({ ...emailContent, subject: e.target.value })} />
        <textarea placeholder="Body" onChange={e => setEmailContent({ ...emailContent, body: e.target.value })}></textarea>
        <input type="email" placeholder="To" onChange={e => setEmailContent({ ...emailContent, to_email: e.target.value })} />
        <button onClick={sendEmail}>Send Email</button>
      </div>
      <div>
        {/* SMTP/IMAP settings */}
        <input type="text" placeholder="SMTP Server" onChange={e => setEmailSettings({ ...emailSettings, smtp_server: e.target.value })} />
        <input type="number" placeholder="SMTP Port" onChange={e => setEmailSettings({ ...emailSettings, smtp_port: e.target.value })} />
        <input type="text" placeholder="IMAP Server" onChange={e => setEmailSettings({ ...emailSettings, imap_server: e.target.value })} />
        <input type="number" placeholder="IMAP Port" onChange={e => setEmailSettings({ ...emailSettings, imap_port: e.target.value })} />
        <input type="email" placeholder="Email" onChange={e => setEmailSettings({ ...emailSettings, email: e.target.value })} />
        <input type="password" placeholder="Password" onChange={e => setEmailSettings({ ...emailSettings, password: e.target.value })} />
        <button onClick={updateSettings}>Update Settings</button>
      </div>
    </div>
  );
};

export default EmailInterface;
