// Mock API endpoint
const apiEndpoint = "https://example.com/api/messages";

// Function to add a message to the chat box
function addMessage(sender, text) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message';
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom
}

// Function to send a message
function sendMessage() {
    const messageInput = document.getElementById('message');
    const messageText = messageInput.value.trim();
    if (messageText === '') return;

    // Add message to chat box (mock)
    addMessage('You', messageText);

    // Send the message to the server (mock)
    fetch(apiEndpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: messageText })
    })
    .then(response => response.json())
    .then(data => {
        // Handle server response if needed
        console.log('Message sent:', data);
    })
    .catch(error => {
        console.error('Error sending message:', error);
    });

    // Clear the input field
    messageInput.value = '';
}

// Function to simulate receiving messages (mock)
function receiveMessages() {
    fetch(apiEndpoint)
    .then(response => response.json())
    .then(data => {
        // Mock data processing
        data.messages.forEach(msg => {
            addMessage(msg.sender, msg.text);
        });
    })
    .catch(error => {
        console.error('Error fetching messages:', error);
    });
}

// Polling for new messages every 5 seconds
setInterval(receiveMessages, 5000);
