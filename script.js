// Get button references
const manualBtn = document.getElementById('manualBtn');
const autoBtn = document.getElementById('autoBtn');
const onBtn = document.getElementById('onBtn');
const offBtn = document.getElementById('offBtn');

// Mode Toggle Logic
manualBtn.addEventListener('click', () => {
    manualBtn.classList.add('active');
    autoBtn.classList.remove('active');

    // Color Logic
    manualBtn.style.backgroundColor = '#4caf50'; // Green
    autoBtn.style.backgroundColor = '#dc3545';   // Red
});

autoBtn.addEventListener('click', () => {
    autoBtn.classList.add('active');
    manualBtn.classList.remove('active');

    // Color Logic
    autoBtn.style.backgroundColor = '#4caf50';   // Green
    manualBtn.style.backgroundColor = '#dc3545'; // Red
});

// On/Off Button Logic
onBtn.addEventListener('click', () => {
    onBtn.classList.add('active');
    offBtn.classList.remove('active');

    // Color Logic
    onBtn.style.backgroundColor = '#4caf50';  // Green
    offBtn.style.backgroundColor = '#dc3545'; // Red
});

offBtn.addEventListener('click', () => {
    offBtn.classList.add('active');
    onBtn.classList.remove('active');

    // Color Logic
    offBtn.style.backgroundColor = '#4caf50';  // Green
    onBtn.style.backgroundColor = '#dc3545';   // Red
});
