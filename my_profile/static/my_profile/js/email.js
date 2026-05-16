

    function showEmail() {
        // Hide show button
        document.getElementById('showEmailBtn').style.display = 'none';
        // Show email
        document.getElementById('emailReveal').classList.remove('hidden');
    }

    function copyEmail() {
        navigator.clipboard.writeText('surajpatil9197@zohomail.in');

        const copyBtn = event.target;
        const originalText = copyBtn.textContent;
        copyBtn.textContent = '✅ Copied!';
        copyBtn.style.background = 'linear-gradient(to right, #10b981, #059669)';

        // After 3 seconds: Hide everything + Show button again
        setTimeout(() => {
            document.getElementById('emailReveal').classList.add('hidden');
            document.getElementById('showEmailBtn').style.display = 'block';
            copyBtn.textContent = originalText;
            copyBtn.style.background = '';
        }, 1000);
    }