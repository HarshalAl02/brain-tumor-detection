// Smooth scrolling for navigation links
document.querySelectorAll('.nav a').forEach(link => {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        const targetId = this.getAttribute('href').slice(1);
        document.getElementById(targetId).scrollIntoView({ behavior: 'smooth' });
    });
});

// Call-to-action button animation
const ctaButton = document.querySelector('.cta .btn-primary');
ctaButton.addEventListener('mouseenter', () => {
    ctaButton.style.transform = 'scale(1.1)';
});
ctaButton.addEventListener('mouseleave', () => {
    ctaButton.style.transform = 'scale(1)';
});

function toggleChatbot() {
    var chatbot = document.getElementById('chatbot');
    chatbot.classList.toggle('active');
}

document.getElementById('input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});