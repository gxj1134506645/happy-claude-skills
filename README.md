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

### wechat-article-writer
Automated WeChat article writing workflow with 4 steps: research, writing, title generation, and formatting optimization.

**Use Cases:**
- Write WeChat official account articles
- Generate viral headlines
- Content creation for self-media
- Article formatting and optimization

### browser
Browser automation using Chrome DevTools Protocol. Start Chrome, navigate pages, execute JavaScript, take screenshots, and interactively pick DOM elements.

**Use Cases:**
- Web scraping with authenticated sessions
- Visual regression testing
- DOM inspection and data extraction
- Screenshot capture for documentation

### book-cover-generator
AI-powered book and movie poster generator using Midjourney V5.0 with 5000+ visual style combinations.

**Use Cases:**
- Generate book cover posters
- Create movie promotional posters
- Visual showcase for literary works
- Book recommendation posters for knowledge bloggers

**Core Features:**
- Automatic extraction of work information (themes, quotes, insights, characters, timeline)
- Intelligent visual style adaptation (color schemes, patterns, calligraphy styles)
- Chinese font optimization (Source Han Serif for clarity)
- Support for both portrait (2:3) and landscape (16:9) ratios

### report-generator
Automated weekly report generator based on git commit history. Creates structured work summaries for team communication.

**Use Cases:**
- Generate weekly work reports
- Team progress updates
- Project milestone summaries
- Enterprise OA system reporting (WeChat Work, DingTalk)

**Core Features:**
- Automatic extraction of this week's git commits
- Intelligently summarizes commits into 10 key items
- Each item is 20-30 characters
- Ordered list format (1, 2, 3...)
- Filters meaningless commits (merge, wip, tmp)
- Deduplicates and categorizes by module

## Installation

### Install from GitHub

First, add this repository as a plugin marketplace in Claude Code:
```
/plugin marketplace add gxj1134506645/happy-claude-skills
```

Then install the skills you need:
```
/plugin install docx-format-replicator@happy-claude-skills-gxj
/plugin install video-processor@happy-claude-skills-gxj
/plugin install wechat-article-writer@happy-claude-skills-gxj
/plugin install browser@happy-claude-skills-gxj
/plugin install book-cover-generator@happy-claude-skills-gxj
/plugin install report-generator@happy-claude-skills-gxj
```

### Local Development Installation

After cloning the repository, use the `--plugin-dir` parameter:
```bash
git clone https://github.com/gxj1134506645/happy-claude-skills.git
claude --plugin-dir /path/to/happy-claude-skills
```

## Usage

After installation, simply describe your needs in Claude Code:

> "I have a document template and need to generate 5 new documents with the same format"

> "Download this YouTube video and transcribe it to text"

> "Help me write a WeChat article about AI programming tips"

> "Scrape the product information from this webpage"

> "Generate a book cover poster for 'The Three-Body Problem'"

> "Generate a weekly report"

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

### browser
- Node.js 18+
- puppeteer-core
- Google Chrome

```bash
npm install --prefix skills/browser
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
│   ├── video-processor/
│   │   ├── SKILL.md             # Skill definition
│   │   └── scripts/             # Python scripts
│   ├── wechat-article-writer/
│   │   └── SKILL.md             # Skill definition
│   ├── browser/
│   │   ├── SKILL.md             # Skill definition
│   │   ├── package.json         # Node.js dependencies
│   │   └── scripts/             # Node.js scripts
│   ├── book-cover-generator/
│   │   └── SKILL.md             # Skill definition
│   └── report-generator/
│       └── SKILL.md             # Skill definition
├── README.md
└── LICENSE
```

## Acknowledgments

- **video-processor** skill is adapted from [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) by [@disler](https://github.com/disler)
- **browser** skill is based on [Mario Zechner](https://mariozechner.at)'s article [What if you don't need MCP?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/) ([GitHub](https://github.com/badlogic/browser-tools)), adapted from [Factory.ai](https://docs.factory.ai/guides/skills/browser)

## Contributing

Issues and Pull Requests are welcome!

## License

MIT License
