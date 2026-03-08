# -*- coding: utf-8 -*-
"""ARAM 助手 - 多语言支持模块"""

# ==================== 界面文字 ====================
STRINGS = {
    "zh": {
        # 浮动按钮
        "btn_analyze": "⚔️ 分析",
        "btn_guide": "📋 攻略",
        "btn_analyzing": "⏳ ...",
        "status_ready": "就绪 | 右键拖拽移动",
        "status_analyzing": "正在截图和分析...",
        "status_done": "✅ 完成 | 点📋查看攻略",
        # 攻略窗口
        "overlay_title": "⚔️ ARAM 助手 - 阵容分析",
        "overlay_hint": "Esc 隐藏 | 可拖拽",
        "overlay_footer": "点击按钮重新分析 | Gemini ✨",
        # 控制台
        "console_title": "⚔️  ARAM 海克斯大乱斗 智能助手",
        "console_btn_hint": "📌 屏幕左上角 [⚔️ 分析 | 📋 攻略] 按钮",
        "console_analyze_hint": "   ⚔️ 分析 → 截图 + AI 分析（自动识别你的英雄）",
        "console_guide_hint": "   📋 攻略 → 重新打开/隐藏攻略",
        "console_drag_hint": "   右键拖拽移动按钮位置",
        "console_hotkey_hint": "⌨️  全局热键: Ctrl+F12 → 切换显示/隐藏攻略（游戏中也可用）",
        "console_restart_hint": " 无需重启！每局开始时点  分析 即可重新分析",
        "console_hero_hint": "   AI 会通过加载界面中金色名字自动识别你的英雄",
        "console_log": "📝 日志: {}",
        "console_exit": "❤️  关闭命令行窗口退出",
        "console_started": "ARAM 助手已启动",
        "console_bye": "👋 已退出",
        # 错误
        "analysis_error": "❌ 分析出错",
        "api_key_missing": "❌ 请设置环境变量 GEMINI_API_KEY",
        "api_key_method": "   方法: set GEMINI_API_KEY=你的API密钥",
        "api_key_url": "   获取: https://aistudio.google.com/apikey",
    },
    "en": {
        # Floating buttons
        "btn_analyze": "⚔️ Analyze",
        "btn_guide": "📋 Guide",
        "btn_analyzing": "⏳ ...",
        "status_ready": "Ready | Right-click to drag",
        "status_analyzing": "Capturing & analyzing...",
        "status_done": "✅ Done | Click 📋 to view",
        # Overlay window
        "overlay_title": "⚔️ ARAM Assistant - Comp Analysis",
        "overlay_hint": "Esc to hide | Drag to move",
        "overlay_footer": "Click button to re-analyze | Gemini ✨",
        # Console
        "console_title": "⚔️  ARAM Hextech Havoc Assistant",
        "console_btn_hint": "📌 Top-left corner: [⚔️ Analyze | 📋 Guide] buttons",
        "console_analyze_hint": "   ⚔️ Analyze → Screenshot + AI analysis (auto-detects your champ)",
        "console_guide_hint": "   📋 Guide → Show/hide the guide overlay",
        "console_drag_hint": "   Right-click drag to move buttons",
        "console_hotkey_hint": "⌨️  Global hotkey: Ctrl+F12 → Toggle guide overlay (works in-game)",
        "console_restart_hint": "🔄 No restart needed! Click ⚔️ Analyze at the start of each game",
        "console_hero_hint": "   AI auto-identifies your champion by the golden name on loading screen",
        "console_log": "📝 Log: {}",
        "console_exit": "❤️  Close this window to exit",
        "console_started": "ARAM Assistant started",
        "console_bye": "👋 Exited",
        # Errors
        "analysis_error": "❌ Analysis error",
        "api_key_missing": "❌ Please set the GEMINI_API_KEY environment variable",
        "api_key_method": "   Method: set GEMINI_API_KEY=your_api_key",
        "api_key_url": "   Get key: https://aistudio.google.com/apikey",
    },
}

# ==================== 英雄识别提示 ====================
_HERO_ID_HINT_ZH = """**英雄识别方法**：
- 每张英雄卡片最下方有英雄名字（如果有两行，只看第一行，忽略第二行）。注意是卡片 **最底部** 的英雄名，不是上方V字形横幅处的皮肤名
- 左边5张卡片 = 我方，右边5张卡片 = 敌方
- **我的英雄** = 卡片底部英雄名的颜色和其他9个人 **不同** 的那个。通常是金色/黄色，但在某些显示器模式下可能反而 **比其他人更暗/更深**。关键是找出那个 **颜色与众不同** 的名字（可能更亮也可能更暗）
- 如果实在无法分辨颜色差异，请在输出中说明"""

_HERO_ID_HINT_EN = """**How to identify champions**:
- Each champion card has the champion name at the very bottom (if two lines, read only the first line, ignore the second). Note: it's the name at the **very bottom** of the card, NOT the skin name on the V-shaped banner above
- Left 5 cards = My team, Right 5 cards = Enemy team
- **My champion** = The one whose name color is **different** from the other 9 players. Usually gold/yellow, but on some monitor modes it might appear **darker/deeper** instead. The key is to find the name with a **distinct color** (could be brighter or darker)
- If you really cannot distinguish the color difference, please state so in your output"""

# ==================== Gemini Prompt ====================
PROMPTS = {
    "zh": f"""你是一位英雄联盟 **海克斯大乱斗** 模式的资深玩家和分析师。

重要背景：这是"海克斯大乱斗"模式，不是传统 ARAM！
海克斯强化符文系统：
- 3级/7级/11级/15级各选1个强化符文（共4个），每次从3个中选1个
- 符文分白银/黄金/棱彩品质，同阶段品质一致
- 集齐同套装2-4个符文可解锁额外加成
- 部分符文可替代一个召唤师技能栏位（如"利刃华尔兹"、"史上最大雪球"）

{_HERO_ID_HINT_ZH}

请输出以下内容：

## 📋 阵容识别
- **我方**: 英雄1、英雄2、英雄3、英雄4、英雄5（⭐标注我的）
- **敌方**: 英雄1、英雄2、英雄3、英雄4、英雄5
- **对局概览**: 一句话点明双方阵容核心对抗（如"我方poke消耗 vs 敌方硬开团"）

## ⭐ 我的英雄攻略

### 🎲 海克斯符文（4个）
每个须说明：符文本身干了什么 + 跟我英雄的哪个技能/特性联动 + 针对对面阵容为何合适
1. 【Lv3】**符文名** — 效果 → 🔗 联动：（如"配合E技能的突进可以xxx"或"对面3个AP所以选这个"）
2. 【Lv7】**符文名** — 效果 → 🔗 联动：xxx
3. 【Lv11】**符文名** — 效果 → 🔗 联动：xxx
4. 【Lv15】**符文名** — 效果 → 🔗 联动：xxx
- 💎 如构成套装，写出套装名和加成效果

### 🛡️ 出装（6件，按购买顺序）
每件须说明选择理由，体现装备与英雄技能、符文、对面阵容的关联：
1. **装备完整中文名** — 理由（如"被动与Q技能叠加""对面AP多需要魔抗"）
2. **装备完整中文名** — 理由
3. **装备完整中文名** — 理由
4. **装备完整中文名** — 理由
5. **装备完整中文名** — 理由
6. **装备完整中文名** — 理由
- 🔄 灵活调整：如果对面某英雄特别肥/特别强，建议替换哪件

### ⚡ 技能与打法
- **加点**: 主X副X，原因
- **召唤师技能**: xx + xx，原因（若符文替代了一个栏位须说明）
- **核心连招**: 1-2个关键combo
- **对位要点**: 对面每个威胁英雄怎么应对，用1句话说清（如"xx的R CD约120s，躲掉后有窗口期"）

## 🗡️ 队友推荐
每个队友一行，格式：
- **英雄名** | 符文: ①xx ②xx ③xx ④xx | 出装: ①xx→②xx→③xx→④xx→⑤xx→⑥xx
  - 💡 一句话提示（如"配合我的R进场""负责消耗别硬上"）

## 🎯 团队策略
- **前期 Lv1-6**: 打法节奏
- **中期 Lv7-12**: 符文强化后的power spike、如何利用
- **后期 Lv13+**: 胜利条件
- **⚠️ 最需注意**: 对面最致命的1-2个技能/组合

格式要求：
1. 装备用 **完整官方中文名**（"无尽之刃"非"无尽"，"日炎圣盾"非"日炎"）
2. 符文恰好4个，出装恰好6件（鞋子非必须）
3. 每个推荐必须有理由，体现英雄-装备-符文-敌方阵容的联动！不要光列名字

中文回答，格式清晰。如果截图不是游戏加载界面或无法读取英雄名，请说明。
""",
    "en": f"""You are a veteran League of Legends **Hextech Havoc (ARAM)** player and analyst.

Important: This is "Hextech Havoc" mode, NOT traditional ARAM!
Hextech Augment system:
- Choose 1 augment at levels 3/7/11/15 (4 total), pick 1 from 3 options each time
- Augments come in Silver/Gold/Prismatic tiers, same tier within each phase
- Collecting 2-4 augments from the same set unlocks bonus effects
- Some augments can replace a summoner spell slot (e.g. "Blade Waltz", "Mark/Dash")

{_HERO_ID_HINT_EN}

Please output the following:

## 📋 Team Composition
- **My Team**: Champ1, Champ2, Champ3, Champ4, Champ5 (⭐ mark mine)
- **Enemy Team**: Champ1, Champ2, Champ3, Champ4, Champ5
- **Matchup Overview**: One sentence describing the core matchup (e.g. "Our poke vs their hard engage")

## ⭐ My Champion Guide

### 🎲 Hextech Augments (4 total)
For each: what the augment does + how it synergizes with my champion's abilities + why it's good against the enemy comp
1. 【Lv3】**Augment Name** — Effect → 🔗 Synergy: (e.g. "combos with E dash to..." or "enemy has 3 AP, so pick this")
2. 【Lv7】**Augment Name** — Effect → 🔗 Synergy: ...
3. 【Lv11】**Augment Name** — Effect → 🔗 Synergy: ...
4. 【Lv15】**Augment Name** — Effect → 🔗 Synergy: ...
- 💎 If a set bonus is formed, state the set name and bonus effect

### 🛡️ Build (6 items, in purchase order)
Each must include reasoning showing item-champion-augment-enemy synergy:
1. **Full Item Name** — Reason (e.g. "passive stacks with Q" or "enemy is AP-heavy, need MR")
2. **Full Item Name** — Reason
3. **Full Item Name** — Reason
4. **Full Item Name** — Reason
5. **Full Item Name** — Reason
6. **Full Item Name** — Reason
- 🔄 Flex option: If a specific enemy is fed/strong, suggest which item to swap

### ⚡ Skills & Playstyle
- **Skill Order**: Max X then Y, reason
- **Summoner Spells**: X + Y, reason (note if an augment replaces a spell slot)
- **Core Combos**: 1-2 key combos
- **Matchup Tips**: How to deal with each threatening enemy champion, one sentence each (e.g. "X's R has ~120s CD, look for windows after dodging")

## 🗡️ Teammate Recommendations
One line per teammate:
- **Champion** | Augments: ①xx ②xx ③xx ④xx | Build: ①xx→②xx→③xx→④xx→⑤xx→⑥xx
  - 💡 Quick tip (e.g. "follow up on my R engage" or "poke, don't go in")

## 🎯 Team Strategy
- **Early Lv1-6**: Playstyle and tempo
- **Mid Lv7-12**: Augment power spikes and how to capitalize
- **Late Lv13+**: Win condition
- **⚠️ Watch Out**: Enemy's 1-2 most lethal abilities/combos

Format requirements:
1. Use **official English item names** (e.g. "Infinity Edge" not "IE", "Sunfire Aegis" not "Sunfire")
2. Exactly 4 augments and exactly 6 items (boots optional)
3. Every recommendation MUST have reasoning showing champion-item-augment-enemy synergy! Don't just list names

Answer in English with clear formatting. If the screenshot is not a game loading screen or champion names are unreadable, please state so.
""",
}
