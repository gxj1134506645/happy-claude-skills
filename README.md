[English](README.md) | [中文](README.zh-CN.md)

# Happy Claude Skills

A collection of practical skill plugins designed for Claude Code.

## Included Skills

### docx-format-replicator
Extract formatting from existing Word documents and generate new documents with the same format.

**Use Cases:**
- Corporate document template replication
- Batch generation of consistently formatted documents
- Technical specification document series
- Standardized documentation like development task sheets

### video-processor
Download and process videos from YouTube and other platforms. Supports video download, audio extraction, format conversion, and Whisper transcription.

**Use Cases:**
- Download videos from YouTube and other platforms
- Extract audio from video files
- Convert videos to MP4/WebM formats
- Transcribe audio/video to text using Whisper

## Installation

### Install from GitHub

First, add this repository as a plugin marketplace in Claude Code:
```
/plugin marketplace add iamzhihuix/happy-claude-skills
```

Then install the skills:
```
/plugin install happy-skills@happy-claude-skills
```

### Local Development Installation

After cloning the repository, use the `--plugin-dir` parameter:
```bash
git clone https://github.com/iamzhihuix/happy-claude-skills.git
claude --plugin-dir /path/to/happy-claude-skills
```

## Usage

After installation, simply describe your needs in Claude Code:

> "I have a document template and need to generate 5 new documents with the same format"

> "Download this YouTube video and transcribe it to text"

Claude will automatically identify and invoke the appropriate skill.

## Dependencies

### docx-format-replicator
- Python 3.7+
- python-docx

```bash
pip install python-docx
```

### video-processor
- Python 3.7+
- yt-dlp
- FFmpeg
- openai-whisper

```bash
pip install yt-dlp openai-whisper
brew install ffmpeg  # macOS
```

## Project Structure

```
happy-claude-skills/
├── .claude-plugin/
│   └── marketplace.json         # Marketplace configuration
├── skills/
│   ├── docx-format-replicator/
│   │   ├── SKILL.md             # Skill definition
│   │   ├── scripts/             # Python scripts
│   │   ├── assets/              # Example files
│   │   └── references/          # Reference docs
│   └── video-processor/
│       ├── SKILL.md             # Skill definition
│       └── scripts/             # Python scripts
├── README.md
└── LICENSE
```

## Acknowledgments

- **video-processor** skill is adapted from [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) by [@disler](https://github.com/disler)

## Contributing

Issues and Pull Requests are welcome!

## License

MIT License
