const vscode = require('vscode');

function activate(context) {
    let disposable = vscode.commands.registerCommand('extension.terminateAndRunTask', function () {
        const terminal = vscode.window.activeTerminal;

        if (terminal) {
            terminal.dispose();
        }

        vscode.commands.executeCommand('workbench.action.tasks.terminate');
        vscode.commands.executeCommand('workbench.action.tasks.runTask', 'Run main.py');
    });

    context.subscriptions.push(disposable);
}

exports.activate = activate;

exports.activate = activate;