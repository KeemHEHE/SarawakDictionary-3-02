document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('add-word-form');
    const feedback = document.getElementById('feedback');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Hide previous feedback
        feedback.style.display = 'none';
        
        // Get form values
        const word = document.getElementById('word').value.trim();
        const definition = document.getElementById('definition').value.trim();
        const dialect = document.getElementById('dialect').value;
        
        // Validate inputs
        if (!word || !definition || !dialect) {
            showFeedback('Please fill in all fields', 'error');
            return;
        }
        
        try {
            const response = await fetch('/api/add-word', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    word: word,
                    definition: definition,
                    dialect: dialect
                })
            });
            
            const data = await response.json();
            
            if (response.ok) {
                showFeedback('Word added successfully!', 'success');
                form.reset();
            } else {
                showFeedback(data.error || 'Failed to add word', 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            showFeedback('Network error - please try again', 'error');
        }
    });
    
    function showFeedback(message, type) {
        feedback.textContent = message;
        feedback.className = type;
        feedback.style.display = 'block';
        
        // Scroll to feedback message
        feedback.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }
});