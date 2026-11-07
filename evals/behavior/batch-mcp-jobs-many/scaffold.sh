#!/usr/bin/env bash
set -euo pipefail
mkdir -p "$(dirname 'manifest.csv')" && cat > 'manifest.csv' <<'TXT'
id,video,audio
intro,https://example.com/v/presenter.mp4,https://example.com/a/intro.wav
pricing,https://example.com/v/presenter.mp4,https://example.com/a/pricing.wav
outro,https://example.com/v/presenter.mp4,https://example.com/a/outro.wav
TXT
