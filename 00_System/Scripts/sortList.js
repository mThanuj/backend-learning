module.exports = async function (tp) {
    const file = tp.config.target_file;
    const content = await app.vault.read(file);

    const lines = content.split("\n");

    const startIndex = lines.findIndex(
        line => line.trim() === "## 🔗 Related Concepts"
    );

    if (startIndex === -1) return;

    let i = startIndex + 1;
    const related = [];

    while (
        i < lines.length &&
        lines[i].trim().startsWith("- ")
    ) {
        related.push(lines[i]);
        i++;
    }

    const sorted = related.sort((a, b) =>
        a.localeCompare(b)
    );

    lines.splice(
        startIndex + 1,
        related.length,
        ...sorted
    );

    await app.vault.modify(
        file,
        lines.join("\n")
    );
}