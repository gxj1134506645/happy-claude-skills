[English](README.md) | [中文](README.zh-CN.md)

# Happy Claude Skills

一组为 Claude Code 设计的实用技能插件。

## 包含的 Skills

### docx-format-replicator
从现有 Word 文档提取格式，并用相同格式生成新文档。

**适用场景：**
- 企业文档模板复制
- 批量生成格式一致的文档
- 技术规范文档系列
- 研制任务书等标准化文档

### video-processor
从 YouTube 等平台下载和处理视频。支持视频下载、音频提取、格式转换和 Whisper 语音转文字。

**适用场景：**
- 从 YouTube 等平台下载视频
- 从视频文件中提取音频
- 将视频转换为 MP4/WebM 格式
- 使用 Whisper 将音频/视频转录为文字

### wechat-article-writer
公众号文章自动化写作流程，4 步完成高质量文章：搜索资料、撰写文章、生成标题、排版优化。

**适用场景：**
- 撰写微信公众号文章
- 生成爆款标题
- 自媒体内容创作
- 文章排版优化

## 安装方法

### 从 GitHub 安装

首先，在 Claude Code 中添加此仓库为插件市场：
```
/plugin marketplace add iamzhihuix/happy-claude-skills
```

然后安装你需要的 skills：
```
/plugin install docx-format-replicator@happy-claude-skills
/plugin install video-processor@happy-claude-skills
/plugin install wechat-article-writer@happy-claude-skills
```

### 本地开发安装

克隆仓库后，使用 `--plugin-dir` 参数：
```bash
git clone https://github.com/iamzhihuix/happy-claude-skills.git
claude --plugin-dir /path/to/happy-claude-skills
```

## 使用方法

安装后，在 Claude Code 中直接描述您的需求：

> "我有一个研制任务书模板，需要用相同格式生成5份新文档"

> "下载这个 YouTube 视频并转录成文字"

> "帮我写一篇关于 AI 编程技巧的公众号文章"

Claude 会自动识别并调用相应的 skill。

## 依赖

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

## 项目结构

```
happy-claude-skills/
├── .claude-plugin/
│   └── marketplace.json         # 市场配置
├── skills/
│   ├── docx-format-replicator/
│   │   ├── SKILL.md             # Skill 定义
│   │   ├── scripts/             # Python 脚本
│   │   ├── assets/              # 示例文件
│   │   └── references/          # 参考文档
│   ├── video-processor/
│   │   ├── SKILL.md             # Skill 定义
│   │   └── scripts/             # Python 脚本
│   └── wechat-article-writer/
│       └── SKILL.md             # Skill 定义
├── README.md
└── LICENSE
```

## 鸣谢

- **video-processor** skill 改编自 [@disler](https://github.com/disler) 的 [claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) 项目

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
