document.addEventListener('DOMContentLoaded', function () {
    const terminalOutput = document.getElementById('terminalOutput');
    const terminalInput = document.getElementById('terminalInput');

    terminalInput.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            handleCommand();
        }
    });

    function handleCommand() {
        const command = terminalInput.value;
        appendOutput(`<div><span>&gt;</span> ${command}</div>`);

        // Handle the command - you can add your logic here

        // Clear input
        terminalInput.value = '';
    }

    function appendOutput(content) {
        terminalOutput.innerHTML += content;
        // Scroll to the bottom of the output
        terminalOutput.scrollTop = terminalOutput.scrollHeight;
    }
});
