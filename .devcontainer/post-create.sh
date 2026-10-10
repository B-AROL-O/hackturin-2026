#!/bin/bash
# Post-create setup for the devcontainer: installs Claude Code.

echo "DEBUG: BEGIN $0"

# Optional directory with host config (settings), e.g. bind-mounted by the user.
FROM_HOST=/opt/from_host

echo "INFO: Setup Claude Code"

if ! command -v claude &> /dev/null; then
    echo "DEBUG: Claude Code not found in PATH, let us install it"
    npm install -g @anthropic-ai/claude-code
fi
if [ -e "$FROM_HOST/.claude/settings.json" ]; then
    if [ ! -e "$HOME/.claude/settings.json" ]; then
        echo "DEBUG: Copying Claude Code settings from host"
        mkdir -p "$HOME/.claude"
        cp "$FROM_HOST/.claude/settings.json" "$HOME/.claude/settings.json"
    fi
fi

echo "INFO: Setup shell completions for CLI tools"

COMPLETION_DIR="$HOME/.local/share/bash-completion/completions"
mkdir -p "$COMPLETION_DIR"

if command -v uv &> /dev/null; then
    uv generate-shell-completion bash > "$COMPLETION_DIR/uv"
fi
if command -v docker &> /dev/null; then
    docker completion bash > "$COMPLETION_DIR/docker"
fi
if command -v gh &> /dev/null; then
    gh completion -s bash > "$COMPLETION_DIR/gh"
fi

echo "DEBUG: END $0"

# EOF
