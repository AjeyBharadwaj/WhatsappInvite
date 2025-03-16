# WhatsappInvite
Code to send whatsapp messages in bulk

Add each number in phone_numbers.txt.
Change the message in message.txt file.

Open default browser and do whatsapp web login.

For each phone number : 
    1. Open a new window with whatsapp web login
    2. Put the message
    3. Send "ENTER" to send the message.
    4. Close the window

How to run : 
    1. python3 -m venv venv
    2. source venv/bin/activate
    3. pip install -r requrements.txt
    4. python main.py

NOTE : 
To ensure all links are loaded, increase LOADING_TIME
To ensure message is end properly, increase CLOSING_WAIT_TIME
