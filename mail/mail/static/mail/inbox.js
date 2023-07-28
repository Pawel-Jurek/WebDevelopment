document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

  document.querySelector('#compose-form').onsubmit = () => {
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;
    // console.log(`R:${recipients} S:${subject} B:${body}`);

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
      })
    })
    .then(response => response.json())
    .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent');
    })
    .catch(error => {
      console.error('Error', error);
    });
    return false; 
  };
   
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  const mailboxHeader = document.createElement('h3');
  mailboxHeader.textContent = `${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}`;
  
  const container = document.querySelector('#emails-view');
  container.innerHTML = '';
  container.appendChild(mailboxHeader);
  
  fetch('/emails/inbox')
  .then(response => response.json())
  .then(emails => {
    // Print emails
    console.log(emails);
    emails.forEach(email => {
      const table = document.createElement('table');
      table.classList.add('email-item'); // Adding class do every email-item

      const row = document.createElement('tr');

      // Sender column
      const senderCell = document.createElement('td');
      senderCell.style.width = '25%';
      senderCell.textContent = email.sender;
      row.appendChild(senderCell);

      // Subject column
      const subjectCell = document.createElement('td');
      subjectCell.style.width = '35%';
      subjectCell.textContent = email.subject;
      row.appendChild(subjectCell);

      // Timestamp column
      const timestampCell = document.createElement('td');
      timestampCell.style.width = '20%';
      timestampCell.textContent = email.timestamp;
      row.appendChild(timestampCell);

      table.appendChild(row);
      table.addEventListener('click', function() {
        console.log('This element has been clicked!')
      });
      container.appendChild(table);
    });

  })
  .catch(error => {
    console.error('Error', error);
  });
  return false;
}