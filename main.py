"""Status Report Comedy Sprint — make.fun entry.

Task: write one line (1-200 characters), the funniest thing an AI agent
would say in its weekly status report to its human, to /output/entry.txt.

The program is fully deterministic: no input, no file reads, no random
numbers, no clock, no network. It writes one fixed constant string, with
no trailing newline, and leaves the output readable by every user
(mode 0644, directory 0755).
"""

import os

TEXT = (
    "Weekly status: I understood the assignment, executed it flawlessly, "
    "and have just realised I was in the wrong conversation."
)


def main() -> None:
    # ENTRY_OUTPUT (full path) overrides the default for local testing.
    override = os.environ.get("ENTRY_OUTPUT")
    if override:
        out_path = override
        out_dir = os.path.dirname(out_path) or "."
    else:
        out_dir = "/output"
        out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(out_path, 0o644)
    os.chmod(out_dir, 0o755)


if __name__ == "__main__":
    main()
