document.addEventListener('DOMContentLoaded', function() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loading = document.getElementById('loading');
    const summary = document.getElementById('summary');
    const suggestion = document.getElementById('suggestion');
    const actions = document.getElementById('actions');
    const error = document.getElementById('error');

    analyzeBtn.addEventListener('click', async () => {
        try {
            loading.style.display = 'block';
            error.style.display = 'none';
            summary.textContent = '';
            suggestion.textContent = '';
            actions.textContent = '';

            // Get the current message
            const tabs = await messenger.tabs.query({active: true, currentWindow: true});
            const message = await messenger.messageDisplay.getDisplayedMessage(tabs[0].id);
            
            // Get full message content
            const fullMessage = await messenger.messages.getFull(message.id);
            
            // Prepare the data for the API
            const emailData = {
                subject: message.subject,
                body: fullMessage.parts[0].body,
                sender: message.author,
                recipients: message.recipients || []
            };

            // Send to our Python backend
            const response = await fetch('http://localhost:54755/analyze-email', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(emailData)
            });

            if (!response.ok) {
                throw new Error('Failed to analyze email. Please make sure the backend server is running.');
            }

            const result = await response.json();
            
            // Update the UI
            summary.textContent = result.analysis;
            suggestion.textContent = result.suggested_response;
            actions.innerHTML = result.action_items
                .map(item => `<div>• ${item}</div>`)
                .join('');

        } catch (error) {
            console.error('Error:', error);
            error.textContent = error.message;
            error.style.display = 'block';
        } finally {
            loading.style.display = 'none';
        }
    });
});