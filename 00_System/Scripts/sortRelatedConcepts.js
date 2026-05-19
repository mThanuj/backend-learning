module.exports = async (tp) => {
    const file = app.workspace.getActiveFile();
    let content = await app.vault.read(file);

    const regex = /(## 🔗 Related Concepts\n)((?:- .*\n?)*)/;

    const match = content.match(regex);

    if (!match) return;

    const header = match[1];

    const sorted = match[2]
        .split("\n")
        .filter(line => line.trim() !== "")
        .sort((a, b) => a.localeCompare(b));

    const replacement = header + sorted.join("\n") + "\n";

    content = content.replace(regex, replacement);

    await app.vault.modify(file, content);
};