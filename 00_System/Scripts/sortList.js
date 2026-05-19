module.exports = async function (tp) {
    const editor = app.workspace.activeEditor.editor;

    const selected = editor.getSelection();

    if (!selected) {
        new Notice("Select a list first");
        return;
    }

    const lines = selected
        .split("\n")
        .filter(line => line.trim() !== "");

    const sorted = lines.sort((a, b) =>
        a.localeCompare(b)
    );

    editor.replaceSelection(sorted.join("\n"));

    new Notice("List sorted!");
}