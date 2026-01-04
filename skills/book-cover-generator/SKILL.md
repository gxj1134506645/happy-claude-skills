---
name: book-cover-generator
description: AI生成图书/电影等文学作品海报封面。当用户提到生成图书封面、电影海报、作品海报、书籍封面图时使用此 skill。支持自定义配色、装饰纹样、书法风格等5000+种组合。
---

# AI图书/电影海报生成器

基于Midjourney的V5.0稳定版Prompt，一键生成博物馆级别的文学作品海报。

## 触发场景

当用户请求以下任务时，自动激活此skill：

- "生成《xxx》的图书封面/海报"
- "帮我做个电影海报"
- "制作书籍封面图"
- "生成xxx作品的海报"
- "图书宣传海报设计"

## 工作流程

### Step 1: 提取作品信息

从用户输入中提取以下信息：

| 信息类型 | 说明 | 示例 |
|----------|------|------|
| **作品名称** | 书名/电影名 | 《三体》《活着》《肖申克的救赎》 |
| **作者/导演** | 创作者 | 刘慈欣、余华、弗兰克·德拉邦特 |
| **核心主题** | 4个关键词 | 科幻、人性、文明冲突、宇宙 |
| **经典语录** | 3句（16-25字/句） | "宇宙就是一座黑暗森林" |
| **核心观点** | 6条（标题4-8字+说明28-35字） | 1.黑暗森林. 生存是文明的第一需要 |
| **关系图谱** | 主要元素关系 | 三体人-地球-ETO-科学边界 |
| **时间线** | 4-5个关键节点 | 红岸基地→三体危机→古筝行动 |
| **重要人物** | 3个主要角色 | 叶文洁、罗辑、程心 |

**信息缺失时**：
- 如果用户只提供了作品名称，使用WebSearch搜索该作品的详细信息
- 自动补充核心主题、语录、观点等内容

### Step 2: 配置视觉参数

根据作品类型自动选择视觉风格：

| 作品类型 | 推荐配色 | 推荐书法 | 装饰纹样 |
|----------|----------|----------|----------|
| **科幻/科技** | Cool Scholarly | 欧阳询 | 几何纹样 |
| **文学/小说** | Classic Warm | 颜真卿 | 云纹 |
| **历史/传记** | Elegant Ink | 行书 | 回纹 |
| **哲学/思想** | Nature Zen | 颜真卿 | 缠枝莲 |
| **艺术/美学** | Elegant Ink | 行书 | 缠枝莲 |

### Step 3: 生成Prompt模板

将提取的信息替换到以下Prompt模板中：

```prompt
A high-quality vertical educational infographic poster in a traditional Chinese retro style, designed for [[作品名称]] by [[作者/导演]].
[VERSION 5.0 - FINAL STABLE EDITION WITH PROVEN CHINESE TEXT CLARITY]
Background:
- Radial gradient background creating subtle vignette effect, brighter at center, gently darkening toward edges
- Textured paper surface with visible natural fiber patterns for authentic vintage feel
- Delicate aging spots scattered subtly across the canvas
- Paper grain texture for vintage aesthetic
Header Section (top area):
- Dominant bold calligraphy title at top center in 颜真卿 style: [[作品名称]]
Style: 颜真卿
Color: Deep black for maximum contrast and clarity
- Author name in elegant small script: [[作者/导演]]
Small and refined, warm grey
- Small rectangular visual element in upper right corner:
* Priority 1: Realistic published book cover with visible title and author
* Priority 2: Stylized illustration of core theme
* Priority 3: Symbolic imagery
- Corner ornaments: traditional Chinese cloud pattern
Subtle transparency, elegant traditional design
Section 1 - 核心主题 (Core Themes, upper third area):
- Ornate scroll-style section header with text "核心主题"
- Decorative header ends: cloud scroll pattern
- Four large prominent icons arranged horizontally with generous spacing:
* Icon 1: [[主题1图标]] with label [[主题1关键词]] - Accent color: deep red representing importance
* Icon 2: [[主题2图标]] with label [[主题2关键词]] - Accent color: royal blue representing wisdom
* Icon 3: [[主题3图标]] with label [[主题3关键词]] - Accent color: emerald green representing growth
* Icon 4: [[主题4图标]] with label [[主题4关键词]] - Accent color: amber representing creativity
- Icons evenly spaced with comfortable breathing room
- Introductory text paragraph (ONE CLEAR SENTENCE with moderate length):
"[[作品概述，30-50字]]"
Section 2 - 经典语录 (Quotes Section, central emphasis area):
- Ornate scroll-style section header
- Three rectangular quote boxes arranged vertically with comfortable spacing:
* Each box: Soft contrasting background, refined border, gentle shadow
* Generous internal padding
* Large decorative quote marks
* COMPLETE QUOTES (preserving literary value):
- Quote 1: "[[语录1，16-25字]]"
- Quote 2: "[[语录2，16-25字]]"
- Quote 3: "[[语录3，16-25字]]"
- Comfortable vertical spacing between boxes
Section 3 - 核心观点 (Key Points Analysis, main content area - FULL DEPTH):
- Ornate scroll-style section header with text "核心观点"
- Six-item grid in 2 columns x 3 rows
- ASYMMETRIC LAYOUT for visual rhythm:
* Items 1, 3, 5: Icon LEFT, text RIGHT
* Items 2, 4, 6: Text LEFT, icon RIGHT
- Each item: Medium icon + numbered point with moderate depth
- BALANCED TEXT (sufficient depth without overcrowding):
* Item 1: [[观点1图标]] + "1. [[观点1标题，4-8字]]. [[观点1说明，28-35字]]"
* Item 2: [[观点2图标]] + "2. [[观点2标题，4-8字]]. [[观点2说明，28-35字]]"
* Item 3: [[观点3图标]] + "3. [[观点3标题，4-8字]]. [[观点3说明，28-35字]]"
* Item 4: [[观点4图标]] + "4. [[观点4标题，4-8字]]. [[观点4说明，28-35字]]"
* Item 5: [[观点5图标]] + "5. [[观点5标题，4-8字]]. [[观点5说明，28-35字]]"
* Item 6: [[观点6图标]] + "6. [[观点6标题，4-8字]]. [[观点6说明，28-35字]]"
- Comfortable spacing between items allowing text breathing
Bottom Section Split (MINIMALIST VISUAL STORYTELLING APPROACH):
Bottom Left - 关系图谱 (Relationship Map):
- Ornate scroll-style section header
- Hexagonal network structure
- Central node(s): [[核心元素]] - largest, most prominent
- Connected satellite nodes: [[次要元素]] - medium size
- Outer ring nodes: [[外围元素]] - smaller
- NAMES ONLY - NO descriptive text within diagram
- Connection lines showing relationships, varying thickness indicating strength
- Let the visual network structure tell the story
Bottom Right - 时间线与人物 (Timeline & Characters - VISUAL FOCUS):
- Ornate scroll-style section header
Timeline Section (upper part of this area):
- ICON-BASED TIMELINE with minimal text:
* [[时间线节点1图标]] - "[[时间线标签1]]"
* [[时间线节点2图标]] - "[[时间线标签2]]"
* [[时间线节点3图标]] - "[[时间线标签3]]"
* [[时间线节点4图标]] - "[[时间线标签4]]"
* [[时间线节点5图标]] - "[[时间线标签5]]"
Connected by elegant arc curve
* NO lengthy descriptions, NO parenthetical explanations
* Let icons visually narrate the journey
* Arc shape suggesting story progression
Character/Theme Cards (lower part, VISUAL DOMINANT):
- Three elegant cards with arch-shaped frames
- VISUAL FOCUS STRATEGY:
* Primary element: LARGE CLEAR PORTRAIT or SYMBOLIC ILLUSTRATION
* Secondary element: CHARACTER NAME or THEME TITLE ONLY
* NO descriptive paragraphs - portraits tell the story
- Card structure:
* Card 1: Detailed portrait of [[人物1]] + Large clear name: "[[人物1名称]]"
* Card 2: Detailed portrait of [[人物2]] + Large clear name: "[[人物2名称]]"
* Card 3: Detailed portrait of [[人物3]] + Large clear name: "[[人物3名称]]"
- Generous spacing between cards
- Portraits occupy majority of card space, creating visual gallery effect
Footer (minimal space):
- Thin elegant horizontal divider with centered decorative motif
- Inspirational closing statement (ONE SHORT SENTENCE): "[[结束语，10-20字]]"
- Scattered subtle decorative elements, very light opacity
[Style & Aesthetics - Stability Optimized]
Art Style Foundation:
- Flat vector illustration with refined line art
- Minimalist symbols with cultural depth
- CONSISTENT CHINESE FONT: Noto Serif CJK SC (思源宋体) or Source Han Serif SC for ALL Chinese text throughout the entire poster
- Elegant serif typography, bold calligraphy headers
- Balanced generous negative space
Color Palette: [[配色方案，Classic Warm / Cool Scholarly / Elegant Ink / Nature Zen]]
Decorative Elements:
- Frame: Double-line border, substantial margin
- Corners: traditional Chinese ornamental pattern with cloud and geometric motifs
- Section Dividers: elegant scroll pattern with decorative ends
- Texture: Paper grain, vignette, vintage aging effect
Typography - CJK CONSISTENCY CRITICAL:
- All Chinese text uses same CJK-optimized font (Noto Serif CJK SC or Source Han Serif SC) ensuring consistent rendering quality
- Title: Bold calligraphy in 颜真卿 style
- Section headers: Medium traditional font within scroll decorations
- Body text: Clear comfortable size in CJK-optimized Songti
- Captions: Small refined font for supporting info
- Bottom section names: EXTRA LARGE and BOLD for maximum clarity
Text Distribution Strategy:
- Upper 70% of poster: Full informational depth
* Core themes with context
* Complete literary quotes
* Comprehensive key points analysis
- Lower 30% of poster: Minimal text, visual dominance
* Relationship map: Names only
* Timeline: Icons with brief labels
* Character cards: Portraits + names only
White Space Management:
- Approximately thirty-eight to forty percent negative space
- Extra generous margins in bottom section
- Substantial spacing prioritizing absolute text clarity
- Comfortable breathing room throughout
Quality Standards:
- High resolution suitable for large format printing (4K recommended for portrait)
- Vertical portrait (2:3) or horizontal landscape (16:9) orientation
- Crisp vector-quality lines with smooth curves
- Zero text blur guarantee with minimalist bottom section approach
- Museum exhibition standard presentation
--ar 2:3 --v 6.1 --q 2 --style raw
--no blur, distortion, pixelation, visible measurements, technical annotations, duplicate timeline text, descriptive text in character cards, excessive text in bottom section, small illegible Chinese characters, cramped layout causing blur
```

### Step 4: 输出结果

1. 将生成的完整Prompt输出给用户
2. 提供使用说明：
   - 复制Prompt到Midjourney
   - 使用 `/imagine` 命令执行
   - 等待30-60秒生成图片
3. 提示用户可以根据需要调整配色、风格等参数

## 占位符替换规则

| 占位符 | 替换内容 | 示例 |
|--------|----------|------|
| `[[作品名称]]` | 书名/电影名 | 《三体》 |
| `[[作者/导演]]` | 创作者 | 刘慈欣 |
| `[[主题N图标]]` | 视觉描述 | "atom symbol" / "book icon" / "human figure" |
| `[[主题N关键词]]` | 主题词 | "科幻" / "人性" / "文明" |
| `[[作品概述]]` | 30-50字概述 | "一部关于宇宙文明兴衰的科幻史诗" |
| `[[语录N]]` | 16-25字语录 | "宇宙就是一座黑暗森林" |
| `[[观点N图标]]` | 图标描述 | "star icon" / "shield icon" / "eye icon" |
| `[[观点N标题]]` | 4-8字标题 | "黑暗森林" |
| `[[观点N说明]]` | 28-35字说明 | "生存是文明的第一需要" |
| `[[核心元素]]` | 关系图中心 | "三体问题" |
| `[[次要元素]]` | 关系图次级 | "地球文明" |
| `[[外围元素]]` | 关系图外围 | "科学边界" |
| `[[时间线节点N图标]]` | 节点图标 | "radio telescope" / "spaceship" |
| `[[时间线标签N]]` | 节点标签 | "红岸基地" / "古筝行动" |
| `[[人物N]]` | 人物描述 | "Chinese female scientist" / "middle-aged man" |
| `[[人物N名称]]` | 人物名字 | "叶文洁" / "罗辑" |
| `[[结束语]]` | 10-20字结语 | "给岁月以文明，而不是给文明以岁月" |
| `[[配色方案]]` | 配色选择 | "Cool Scholarly" |

## 图标描述参考库

### 科幻类
- atom symbol（原子符号）
- planet（行星）
- spaceship（宇宙飞船）
- radio telescope（射电望远镜）
- neural network（神经网络）
- black hole（黑洞）
- galaxy（星系）

### 文学类
- open book（打开的书）
- feather quill（羽毛笔）
- ink scroll（卷轴）
- candlelight（烛光）
- heart symbol（心形符号）
- human silhouette（人形剪影）

### 哲学类
- yin-yang symbol（阴阳符号）
- geometric circle（几何圆）
- labyrinth（迷宫）
- eye symbol（眼睛符号）
- tree of life（生命之树）
- meditation figure（冥想人物）

### 历史类
- ancient scroll（古卷轴）
- traditional architecture（传统建筑）
- bronze vessel（青铜器）
- calligraphy brush（毛笔）
- imperial seal（印章）
- hourglass（沙漏）

## 示例

### 示例1：用户只提供作品名称

**用户输入**：
```
帮我生成《三体》的图书封面海报
```

**执行流程**：
1. 使用WebSearch搜索《三体》的详细信息
2. 提取核心主题：科幻、人性、文明冲突、宇宙
3. 搜索经典语录和核心观点
4. 生成完整Prompt并输出

### 示例2：用户提供完整信息

**用户输入**：
```
生成《活着》的图书海报
作者：余华
主题：人生、命运、苦难、希望
语录： "人是为了活着本身而活着的"
观点：
1.生命的意义. 活着本身就是生命的意义
2.苦难与尊严. 在苦难中保持人的尊严
...
```

**执行流程**：
1. 直接使用用户提供的信息
2. 选择Classic Warm配色（文学类）
3. 选择颜真卿书法风格
4. 生成完整Prompt并输出

## 注意事项

1. **字数控制**
   - 语录每句16-25字，超长会导致AI渲染模糊
   - 观点说明28-35字，严格控制长度
   - 作品概述30-50字

2. **中文渲染**
   - 必须指定 `Noto Serif CJK SC` 或 `Source Han Serif SC`
   - 否则中文字符可能出现随机替换

3. **比例参数**
   - 竖版海报：`--ar 2:3`
   - 横版海报：`--ar 16:9`

4. **信息缺失处理**
   - 用户只提供作品名称时，主动搜索补充信息
   - 不要编造不存在的语录和观点

5. **图标描述**
   - 使用英文描述，如 "atom symbol" 而非 "原子符号"
   - 保持简洁，1-3个英文单词
