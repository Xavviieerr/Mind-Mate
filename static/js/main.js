const contentDiv = document.getElementById("main-content");

const observer = new MutationObserver(() => {
    contentDiv.scrollTo({
        top: contentDiv.scrollHeight,
        behavior: 'smooth'
    });
});
observer.observe(contentDiv, { childList: true, subtree: true });

function clearFunction() {
    const fileInput = document.getElementById("fileInputId");
    fileInput.value = '';
    alert("Successfully cleared!!!")
}

function createChatBubble(name, message, timeStamp) {
    const chatBubble = document.createElement('div');
    chatBubble.classList.add('chat-bubble');
  
    const chatBubbleHeader = document.createElement('div');
    chatBubbleHeader.classList.add('chat-bubble-header');
  
    const nameSpan = document.createElement('span');
    nameSpan.textContent = name;
  
    const timeStampSpan = document.createElement('span');
    timeStampSpan.textContent = timeStamp;
  
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-bubble-message');
    messageDiv.innerText = message;
  
    chatBubbleHeader.appendChild(nameSpan);
    chatBubbleHeader.appendChild(timeStampSpan);
    chatBubble.appendChild(chatBubbleHeader);
    chatBubble.appendChild(messageDiv);
  
    return chatBubble;
}

function createUserChatBubble(name, message, timeStamp) {
    const chatBubble = document.createElement('div');
    chatBubble.classList.add('chat-bubble2');
  
    const chatBubbleHeader = document.createElement('div');
    chatBubbleHeader.classList.add('chat-bubble-header2');
  
    const nameSpan = document.createElement('span');
    nameSpan.textContent = name;
  
    const timeStampSpan = document.createElement('span');
    timeStampSpan.textContent = timeStamp;
  
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-bubble-message2');
    messageDiv.innerText = message;
  
    chatBubbleHeader.appendChild(nameSpan);
    chatBubbleHeader.appendChild(timeStampSpan);
    chatBubble.appendChild(chatBubbleHeader);
    chatBubble.appendChild(messageDiv);
  
    return chatBubble;
}

function updateText(event) {
    fetch('/get_text')
        .then(response => response.text())
        .then(data => {
            document.getElementById('main-content').appendChild(createChatBubble("User", data, "12:00 PM"));
        });
        event.preventDefault();
    return
}

async function send_user_prompt() {
    const prompt = document.getElementById("my_prompt").value;
  
    if (prompt === "") {
      alert("please insert answer to the question");
      return;
    } else {
      document.getElementById('main-content').appendChild(createUserChatBubble("User", prompt, "12:00 PM"));
    }
  
    try {
      const response = await fetch('/get_prompt', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: prompt })
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      const comparison = data.comparison;
      document.getElementById('main-content').appendChild(createChatBubble("Mind Mate", comparison, "12:01 PM"));
      document.getElementById("my_prompt").value = ""
    } catch (error) {
      console.error('Error:', error);
    }
}

function disabledButtonAndInput() {
    // input field
    const inputField = document.getElementById("my_prompt");
    inputField.disabled = false;

    // button
    const button = document.getElementById("generate-button");
    button.disabled = false; 
}