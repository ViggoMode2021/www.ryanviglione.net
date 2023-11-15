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

        // Execute the command
        executeCommand(command);

        // Clear input
        terminalInput.value = '';
    }

    function executeCommand(command) {
        let output = '';

        // Basic commands
        if (command.toLowerCase() === 'help') {
            output = 'Available commands: show websites, visit';
        } else if (command.toLowerCase() === 'clear') {
            terminalOutput.innerHTML = '';
            return;
        } else if (command.toLowerCase() === 'visit linkedin') {
            window.location.href = 'https://www.linkedin.com/in/ryan-viglione/';
        } else if (command.toLowerCase() === 'show websites') {
            output = "LinkedIn GitHub VigLMS PowerShell Projects EliteShell";
        } else if (command.toLowerCase() === 'visit GitHub') {
            window.location.href = 'https://www.github.com/viggomode2021';
        } else {
            output = `Command not found: ${command}`;
        }
        appendOutput(`<div>${output}</div>`);
    }

    function appendOutput(content) {
        terminalOutput.innerHTML += content;
        // Scroll to the bottom of the output
        terminalOutput.scrollTop = terminalOutput.scrollHeight;
    }
});
