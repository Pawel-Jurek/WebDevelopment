document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email(replying_email = None) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-details').style.display = 'none';

  // Clear out composition fields
  if(replying_email){
    document.querySelector('#compose-recipients').value = replying_email.sender;
    if(replying_email.subject.startsWith("Re:")){
      document.querySelector('#compose-subject').value = replying_email.subject;
    } else{
      document.querySelector('#compose-subject').value = `Re: ${replying_email.subject}`;
    }
    document.querySelector('#compose-body').value = `On ${replying_email.timestamp} ${replying_email.sender} wrote: \n'${replying_email.body}'\n\n`;
    document.querySelector('#compose-recipients').disabled = true;
    document.querySelector('#compose-subject').disabled = true;
  }else{
    document.querySelector('#compose-recipients').value = '';
    document.querySelector('#compose-subject').value = '';
    document.querySelector('#compose-body').value = '';
  }

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
  document.querySelector('#email-details').style.display = 'none';

  // Show the mailbox name
  const mailboxHeader = document.createElement('h3');
  mailboxHeader.textContent = `${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}`;
   
  const container = document.querySelector('#emails-view');
  container.innerHTML = '';
  container.appendChild(mailboxHeader);

  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    
    // Print emails

    console.log(emails);
    //selected_emails.forEach(email => {
    emails.forEach(email => {
      const table = document.createElement('table');
      table.classList.add('email-item'); // Adding class do every email-item

      const row = document.createElement('tr');

      // Sender column
      const senderCell = document.createElement('td');
      senderCell.style.width = '25%';
      const senderBold = document.createElement('b');
      senderBold.textContent = email.sender;
      senderCell.appendChild(senderBold);
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
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
              read: true
          })
        })

        mail_details(email, mailbox);
      });
      if(email.read === true){
        table.style.backgroundColor = 'white';
      }else{
        table.style.backgroundColor = '#e3dfdf';
      }
      container.appendChild(table);
    });

  })
  .catch(error => {
    console.error('Error', error);
  });
  return false;
}

function mail_details(email, mailbox) {
  document.querySelector('#email-details').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-view').style.display = 'none';

  const main_container = document.querySelector('#email-details');
  main_container.innerHTML = '';

  const subject = document.createElement('h3');
  subject.textContent = `${email.subject}`;
  main_container.appendChild(subject);

  let detailsDiv = document.createElement('div');
  detailsDiv.innerHTML  = `<b>From:</b> ${email.sender}`;
  main_container.appendChild(detailsDiv);

  detailsDiv = document.createElement('div');
  detailsDiv.innerHTML  = `<b>To:</b> ${email.recipients}`;
  main_container.appendChild(detailsDiv);

  detailsDiv = document.createElement('div');
  detailsDiv.innerHTML  = `<b>Timestamp:</b> ${email.timestamp}`;
  main_container.appendChild(detailsDiv);

  const archive_button = document.createElement('button');
  let text = "";
  if(email.archived){
    text = 'Disarchive';
    archive_button.style.backgroundColor = 'rgb(93, 192, 93)';
  } else {
    text = 'Archive';
    archive_button.style.backgroundColor = 'rgb(247, 78, 78)';
  }
   
  archive_button.textContent = text;
  archive_button.style.marginTop = '10px';

  archive_button.addEventListener('click', function() {
    fetch(`/emails/${email.id}`, {
      method: 'PUT',
      body: JSON.stringify({
          archived: !email.archived
      })
    })
    .then(updatedEmail => {
      email.archived = updatedEmail.archived;
      load_mailbox(mailbox);
    })
  })
  main_container.appendChild(archive_button);

  if(mailbox !== 'sent')
  {
    const reply_button = document.createElement('button');
    reply_button.style.backgroundColor = '#f2eabb';
    reply_button.textContent = "Reply";
    reply_button.style.marginLeft = '5px';
    reply_button.addEventListener('click', function() {
      compose_email(email);
    })
    main_container.appendChild(reply_button);
  }
  

  const hr = document.createElement('hr');
  main_container.appendChild(hr);

  detailsDiv = document.createElement('div');
  detailsDiv.textContent = `${email.body}`;
  main_container.appendChild(detailsDiv);

}