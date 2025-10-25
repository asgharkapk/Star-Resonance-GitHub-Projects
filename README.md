# Star-Resonance-GitHub-Projects

A compilation of open-source projects for Star Resonance (Blue Protocol).
These tools cover DPS meters, overlays, bots, asset extraction, and community utilities.
Use responsibly and follow the game’s terms of service.

---

## 🧮 Core DPS and Data Tools

For real-time combat tracking, analysis, and packet-based DPS/HPS meters.

---

### **DPS Backends**

> Tools that collect combat data directly (via packet sniffing or capture).

**[dmlgzs/StarResonanceDamageCounter](https://github.com/dmlgzs/StarResonanceDamageCounter)**
- Real-time DPS and combat data sniffer for Star Resonance.
- Provides live damage statistics, DPS calculations, and detailed combat analysis.
- No modification of the game client is needed; relies on network packet capture.

**[anying1073/StarResonanceDps](https://github.com/anying1073/StarResonanceDps)**
- Based on StarResonanceDamageCounter for real-time DPS analysis.
- Tracks individual and team damage output during encounters.
- Helps optimize gameplay by understanding DPS distribution and critical hits.

**[tom228studio/StarResonanceDamageCounter-master](https://github.com/tom228studio/StarResonanceDamageCounter-master)**
- Localized Russian fork of the original DamageCounter.
- Provides combat analytics, DPS tracking, and skill statistics.
- Focuses on reliability in real-time battle scenarios with packet capture.

[**DannyDog/StarResonanceDps**](https://github.com/DannyDog/StarResonanceDps)
* Star Resonance DPS Statistics Tool
* Based on and ported from the StarResonanceDamageCounter project
* Does not modify the game client or violate game terms of service
* Designed to help players analyze combat data and improve performance
* Requires .NET 8.0 runtime
* Licensed under AGPL v3
* Open for community contributions via Issues and Pull Requests
* Intended for fair use only — do not use for player discrimination or to harm the game community

[**NeRooNx/BPSR-Meter**](https://github.com/NeRooNx/BPSR-Meter)
- A real-time DPS/HPS meter overlay for Blue Protocol: Soul Resurrection
- Built with Electron and advanced packet sniffing capabilities
- Tracks damage and healing per second with 50ms updates
- Supports dual view modes: Nearby (Top 10 players + you) and Solo (personal stats)
- Features include channel change detection, class icons, HP bars, and damage contribution visualization
- Offers rank badges 🥇🥈🥉 and blue highlight for local player
- Customizable interface with draggable, lockable, and always-on-top transparent window
- Includes click-through mode for seamless in-game overlay usage
- Minimalistic and responsive design optimized for real-time gameplay analysis
![BPSR-Meter](https://raw.githubusercontent.com/NeRooNx/BPSR-Meter/master/medidor.png)

---

### **DPS Frontends / Visualizers**

> GUI or overlay tools that display DPS data from a backend.

**[Viemean/StarResonance.DPS](https://github.com/Viemean/StarResonance.DPS)**
- Lightweight frontend for displaying combat data from DamageCounter.
- Shows team DPS, healing, and skill usage in real-time floating windows.
- Supports multi-player monitoring and skill distribution analysis.
![应用截图](https://raw.githubusercontent.com/Viemean/StarResonance.DPS/refs/heads/master/Assets/img.png)

**[mrsnakke/BPSR-Meter](https://github.com/mrsnakke/BPSR-Meter)**
- English-language desktop DPS/HPS meter overlay.
- Displays total damage, healing, contributions, critical hit rate, and max DPS.
- Non-intrusive; overlays game window without affecting gameplay.
![Meter](https://raw.githubusercontent.com/mrsnakke/BPSR-Meter/master/portada.png)

**[CKylinMC/StarResonanceDamageCounterOverlay](https://github.com/CKylinMC/StarResonanceDamageCounterOverlay)**
- Tauri-based frontend for displaying DPS and combat data.
- Works as a companion to DamageCounter backend, visualizing real-time statistics.
- Lightweight and responsive with simple UI controls for team data tracking.
![StarResonanceDamageCounterOverlay](https://raw.githubusercontent.com/ckylinmc/StarResonanceDamageCounterOverlay/main/assets/scrshot.png)

**[ziqi-rgb/StarResonanceDamageCounter-overlay](https://github.com/ziqi-rgb/StarResonanceDamageCounter-overlay)**
- Displays live combat data in floating windows without capturing packets.
- Syncs with DamageCounter for DPS, team stats, and skill information.
- Supports nickname edits and multiple independent windows for characters.
- Floating window overlay for DamageCounter API data.
- Shows team metrics, skill usage, and individual tracking.
- Customizable window layout and nickname settings.

**[tom228studio/StarResonanceDamageCounter-overlay-main](https://github.com/tom228studio/StarResonanceDamageCounter-overlay-main)**
- Russian version of DamageCounter overlay supporting team monitoring.
- Allows UI customization like transparency, colors, and nickname edits.
- Displays skill statistics, DPS contribution, and supports multi-window layouts.

---

### **Overlay Utilities**

[**Chase-Simmons/BPSR-PSO**](https://github.com/Chase-Simmons/BPSR-PSO)
* Blue Protocol: Star Resonance - Per Second Overlay (PSO) provides a GUI to track DPS/HPS for nearby players.
* Standalone packet analyzer that does not modify BPSR files.
* Built with Node.js and Npcap for real-time combat data tracking.
**Pros:**
* Non-invasive and does not require modifying game files.
* Offers clear, visual DPS/HPS metrics.
* Easy setup for developers (Node.js + npm).
**Cons:**
* Requires Npcap installation with WinPcap API compatibility.
* Windows-only (Npcap dependency).
* Might need admin rights for packet capture.
**User comments:**
* Users report it works reliably for monitoring nearby player performance.
* Some note setup complexity due to Npcap configuration.
* Generally praised for being a clean, standalone overlay tool.
![pso](https://raw.githubusercontent.com/asgharkapk/Star-Resonance-GitHub-Projects/refs/heads/main/data/image_2025-10-25_155740907.png)

---

### **APIs and Integration**

> Data endpoints or frameworks to expose, transform, or extend DPS data.

**[balrogsxt/StarResonanceAPI](https://github.com/balrogsxt/StarResonanceAPI)**
- Exposes detailed API endpoints for enemies, players, and scene data.
- Provides JSON outputs for real-time combat statistics and mapping coordinates.
- Built on top of DamageCounter to allow integration with other tools or overlays.

---

### **ACT Plugins**

> Plugins integrating with ACT or external meters.

**[Bluefissure/StarResonanceACTPlugin](https://github.com/Bluefissure/StarResonanceACTPlugin)**
- Plugin for Advanced Combat Tracker (ACT) integration.
- Captures encounters and overlays DPS, built from DamageCounter code.
- Still WIP, may have packet loss with VPNs or UDP connections.

---

## 🧰 Game Tools and Data Extraction

For data mining, resource parsing, build calculators, and profit tools.

---

### **Game Data Extraction / Analysis**

**[PotRooms/StarResonanceTool](https://github.com/PotRooms/StarResonanceTool)**
- Parses game asset files like Lua scripts, protobufs, and asset bundles.
- Useful for modding, research, and analyzing game resources.
- Supports extracting JSON tables and Unity asset bundles for offline analysis.

**[PotRooms/StarResonanceData](https://github.com/PotRooms/StarResonanceData)**
- Parses game data for Blue Protocol: Star Resonance.
- Extracts combat, assets, and protocol information for analysis.
- Supports research and tool development using official game files.

**[HuaChunOXO/StarResonanceModuleSolver](https://github.com/HuaChunOXO/StarResonanceModuleSolver)**
- Calculates optimal mod setups based on StarResonanceAutoMod.
- Supports filtering by attribute and class-specific scoring.
- Helps reduce trial-and-error in mod optimization.

---

### **Build & Optimization Calculators**

**[c0derceejay/unofficial-blueprotocol-star-resonance](https://github.com/c0derceejay/unofficial-blueprotocol-star-resonance)**
- Community-driven build calculator and sharing platform.
- Supports all classes, gear, and skill setups with local browser storage.
- Provides real-time calculations and power rating for builds.

**[fudiyangjin/StarResonanceAutoMod](https://github.com/fudiyangjin/StarResonanceAutoMod)**
- Automates mod selection for characters using live network data.
- Optimizes attribute combinations with C++ algorithms.
- Supports CPU/GPU modes and provides scoring for recommended mods.

---

### **Economic / Profit Tools**

**[whbyaoi/star-resonance-profit-tool](https://github.com/whbyaoi/star-resonance-profit-tool)**
- Market and trade profit calculator for in-game items.
- Requires Windows and 1080p resolution for accurate UI reading.
- Tracks item prices, crafting efficiency, and profit over time.

**[Myazusa/star_resonance_library](https://github.com/Myazusa/star_resonance_library)**
- Offline library containing item info, crafting chains, and calculators.
- Includes profit calculators for association and resource management.
- Standalone executable, no installation required.

---

### **Web Visualization / Planning**

**[RayneClouds/rayneclouds.github.io](https://github.com/RayneClouds/rayneclouds.github.io)**
- Web-based talent tree visualizer for planning character skills.
- Supports multiple builds and shows detailed skill interactions.
- Designed for easy use in browsers without additional software.

---

## 🤖 Bots and Automation

Scripts and bots that automate gameplay actions or provide information.

---

### **Fishing Automation**

[**bk360/BPSR-AutoFisher-V1**](https://github.com/bk360/BPSR-AutoFisher-V1)
- An automated fishing assistant for *Blue Protocol: Star Resonance (BPSR)*.
* Allows the player to start fishing automatically through a simple Python script (`python main.py`).
* Detects when the fishing rod breaks and handles the “Continue Fishing” button automatically, reducing manual interaction.
* Designed for quick setup: navigate to the directory in CMD or PowerShell, and run the main file to begin automation.

[**scylian/bpsr-autofish**](https://github.com/scylian/bpsr-autofish)
- A computer vision automation framework tailored for BPSR’s fishing mechanics.
* Implements precise mouse and keyboard control combined with OpenCV-based image detection.
* Features advanced safety checks, fail-safe conditions, and coordinate validation for reliable automation.
* Provides modular Python APIs for easy integration into custom scripts, along with over 60 unit tests to ensure robustness.
* Can be adapted for other automation tasks beyond fishing through its extensible design.

[**fishing-dev-sm/bpsr_autofishing**](https://github.com/fishing-dev-sm/bpsr_autofishing)
- An improved, vision-based automatic fishing script for *Star Resonance*.
* Uses pixel color analysis (HSV/BGR) to detect bites, reel timing, and “fish escaped” conditions.
* Adapts to any 16:9 resolution with DPI scaling and automatic region-of-interest (ROI) adjustment.
* Features dynamic mode switching between fast tapping and stable long-press reeling based on color detection.
* Includes timeout protection, intelligent recovery (auto-refishing, reconnecting, or re-equipping rods), and detailed logging.
* Designed to run safely without altering game files or memory, ensuring non-invasive automation.

**[Xuan-cc/ShiroFisher-StarResonanceSmartFishing](https://github.com/Xuan-cc/ShiroFisher-StarResonanceSmartFishing)**
- Python script to automate fishing gameplay.
- Detects fish bites, casts rods, collects fish, and manages bait automatically.
- Uses OpenCV and PyAutoGUI for computer vision and input simulation.

[**ArtjomsBogatirjovs/bpsr-fishing**](https://github.com/ArtjomsBogatirjovs/bpsr-fishing)
- An external auto-fishing system for *Star Resonance* based on image recognition.
* Interacts only through the visible game UI using Windows API calls—no game memory or file modifications.
* Uses AI-based fish detection and auto-casting for accurate and efficient fishing cycles.
* Compatible with all 16:9 resolutions in both fullscreen and windowed mode.
* Includes detailed troubleshooting for display settings, antivirus conflicts, and input remapping.
* Focused on safe, educational use—prohibits any commercial redistribution or paid automation services.

---

### **Mod / Attribute Optimization**

[**fishing-dev-sm/bpsr_automodule**](https://github.com/fishing-dev-sm/bpsr_automodule)
- A comprehensive OCR-powered optimizer for *BPSR* modules and attributes.
* Uses Python, Flask, and OpenCV to analyze screenshots and optimize mod setups.
* Offers a modern Web UI for drag-and-drop image uploads, real-time recognition, and result visualization.
* Employs multi-strategy OCR recognition, multi-objective optimization, and intelligent filtering to find best attribute combinations.
* Cross-platform support for Windows, macOS, and Linux with one-click setup scripts and JSON result exports.
* Designed for players and theorycrafters seeking efficient builds without manually comparing modules.

---

### **Chat, Alerts, and Notifications**

**[EricHongXDD/nonebot-star-resonance-plugin](https://github.com/EricHongXDD/nonebot-star-resonance-plugin)**
- NoneBot framework plugin for in-game interactions.
- Supports querying player info, daily tasks, and generating videos.
- Automates common Discord-like commands for Star Resonance communities.

**[azmiao/StarResonanceNotice](https://github.com/azmiao/StarResonanceNotice)**
- Bot plugin to provide notifications and event alerts.
- Integrates with YuiChyanBot and updates players on in-game schedules.
- Lightweight and easy to configure via JSON settings.
![StarResonanceNotice](https://raw.githubusercontent.com/azmiao/StarResonanceNotice/main/截图.jpg)

**[exneverbur/StarResonanceChatSender](https://github.com/exneverbur/StarResonanceChatSender)**
- Automates sending long chat messages in-game.
- Splits text into segments and simulates typing at intervals.
- Useful for bulk messaging or roleplaying events.

---

### **Combat / Hunting Automation**

**[xxfttkx/StarResonanceAutoHunt](https://github.com/xxfttkx/StarResonanceAutoHunt)**
- Automates hunting encounters in-game.
- Switches lines, starts battles, and logs loot efficiently.
- Designed to reduce repetitive manual actions during farming.
![StarResonanceAutoHunt](https://raw.githubusercontent.com/xxfttkx/StarResonanceAutoHunt/main/gui.png)

**[xxfttkx/StarResonanceAutoSwitchLine](https://github.com/xxfttkx/StarResonanceAutoSwitchLine)**
- Automatically switches server channels to optimize farming.
- Reduces lag and competition for resources during peak hours.
- Simplifies routine gameplay navigation.

**[xxfttkx/StarResonanceEnemyCapture](https://github.com/xxfttkx/StarResonanceEnemyCapture)**
- Captures enemy data in real-time via packet analysis.
- Logs positions, HP, templates, and attack targets for research.
- Helps with encounter planning and enemy tracking.

---

### **Data Capture / Packet Tools**

[**narrow-gua/BpsrDetector**](https://github.com/narrow-gua/BpsrDetector)
- A C#-based packet-sniffing and detection tool for BPSR.
* Inspired by the original open-source project by Dimole (`StarResonanceDamageCounter`).
* Allows users to monitor BPSR data packets in real time, useful for developers and mod creators analyzing game behavior.
* Provides a foundation for future tools involving automated performance tracking and data capture.

**[Remering/starresonance_battle_data_statistics](https://github.com/Remering/starresonance_battle_data_statistics)**
- Flutter-based project for battle data statistics in Star Resonance.
- Provides a starting point for building a mobile app with combat data visualization.
- Includes resources for Flutter development, tutorials, and sample code for beginners.

**[amoeet/StarResonanceSimpleDamageDistribution](https://github.com/amoeet/StarResonanceSimpleDamageDistribution)**
- Plots incremental damage over time for team analysis.
- Visualizes DPS trends using DamageCounter logs.
- Does not capture live data; works with existing datasets.
![StarResonanceSimpleDamageDistribution](https://private-user-images.githubusercontent.com/69706187/474307262-935a6edc-f511-4d1f-93c7-4ad54dc26572.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjAzNjQzMDUsIm5iZiI6MTc2MDM2NDAwNSwicGF0aCI6Ii82OTcwNjE4Ny80NzQzMDcyNjItOTM1YTZlZGMtZjUxMS00ZDFmLTkzYzctNGFkNTRkYzI2NTcyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTEwMTMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUxMDEzVDE0MDAwNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTJjNWFlYmJiNmIwYmZmZDAxN2FmZDRmYWE1YjdmOWUxODA0OTZkZGVmNTQwYTZkOWZlNWZkMmEyZjI1NzQzMTImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.2VMZFeDxLY6sgGUfXpn1dbneUZI-_VS8yJzDR9NR-tI)

---

### **Localization / Translation / Misc**

[**Down98/BPSREngPatcher**](https://github.com/Down98/BPSREngPatcher)
- A patching utility to enable English language support for *Blue Protocol: Star Resonance*.
* Requires installation of the .NET 8.0 Runtime environment.
* Users must place the patcher executable inside the `AppData\LocalLow\bokura\Star\localsave` folder (where `localsave.bytes` exists).
* Once executed, it modifies local save data to enable English translation, simplifying localization for non-Chinese users.

[**phiyuki/BPSR-translate**](https://github.com/phiyuki/BPSR-translate)
- A steganographic text encryption and translation utility for *Star Resonance*.
* Uses zero-width characters for invisible data embedding, ensuring secure, hidden message transfer.
* Every encryption produces unique randomized results, enhancing data obfuscation.
* Can be used online via the “星痕共鸣内鬼翻译器” for quick text conversions.
* Fully customizable with editable phrases, keys, salts, and versioning for personalized encryption schemes.

---

## 📊 Community / Guides / UI Enhancements

Fan-made content, guides, and overlays extending gameplay understanding.

---

### **Guides**

[**s-now25/bpsr-skyward-guide**](https://github.com/s-now25/bpsr-skyward-guide)
- A detailed gameplay guide focused on the *Skyward Wind Knight* class in *BPSR*.
* Covers builds, rotations, skill setups, and aerial combat strategies.
* Offers comprehensive explanations for wind-based mechanics and optimal stat balancing.
* Aimed at helping players maximize airborne combat performance through advanced techniques.

[**MrDustyBowl/bpsr-skyward-wind-knight-guide-fr**](https://github.com/MrDustyBowl/bpsr-skyward-wind-knight-guide-fr)
- The French-language version of the *Skyward Wind Knight* comprehensive guide.
* Offers localized explanations of class builds, wind mechanics, and skill rotations.
* Helps French-speaking players master aerial combat strategies in *Blue Protocol: Star Resonance*.
* Maintains all content depth and quality of the English version with linguistic adaptation for clarity and accessibility.

---

### **Guild / Community Tools**

[**zaichiki/bpsr_guild_roster**](https://github.com/zaichiki/bpsr_guild_roster)
- A forked version of the *StarResonanceDamageCounter* with added guild management tools.
* Introduces a Guild Roster window for member tracking, data visualization, and performance analysis.
* Maintains all original DPS tracking and combat analytics while adding export and management features.
* Designed to promote transparency, collaboration, and fair play within guilds.
* Fully open-source under AGPL v3, with respect to community standards and non-invasive data collection.

[**viemahc/bpsr-countdowns**](https://github.com/viemahc/bpsr-countdowns)
- An event countdown tracker for the *Blue Protocol: Star Resonance* community.
* Developed specifically for the STARWIND Guild to monitor upcoming in-game events.
* Displays real-time countdowns for limited-time content, raids, and special seasonal events.
* Helps guild members coordinate participation and stay synchronized with in-game schedules.

---

---

🗺️ Complete Guide to the Best *Star Resonance* & *Blue Protocol* Interactive Maps – Resources, Features, and Community Tips

---

Hey everyone 👋

If you're exploring **Star Resonance** or **Blue Protocol** and want to make the most out of your gameplay — from finding hidden treasures to optimizing routes and locating rare collectibles — here’s a deep dive into the best **interactive maps** currently available. I’ve tested several of these tools, and each one offers something unique depending on what you’re trying to do in-game.

---

### 🌌 **1. Star Resonance Map – [starresonancemap.com](https://starresonancemap.com/)**

This is the **most comprehensive fan-made map** for *Star Resonance* at the moment. It covers nearly every collectible, quest marker, and point of interest across the available regions.

**Key features:**

* **Dynamic map layers** – You can toggle between resources, chests, teleporters, bosses, and event points.
* **Search & filter system** – Quickly locate specific materials or rare spawns.
* **Progress tracking** – Mark completed objectives or looted items, perfect for completionists.
* **Responsive design** – Works well on both desktop and mobile, so you can use it while gaming on the go.
* **Community input** – Markers are actively updated by players, ensuring near real-time accuracy.

**Use tip:** Create a free account if you plan to track your collection progress — it syncs across devices and helps you avoid retreading the same areas.

---

### ⚔️ **2. Blue Protocol Interactive Map – [blueprotocol.interactivemap.app](https://blueprotocol.interactivemap.app/)**

Although this one is technically for *Blue Protocol*, it deserves a mention because it shares the same interactive foundation and style that *Star Resonance* players can appreciate.

**Highlights:**

* **Highly detailed world overlay** with spawn timers, NPCs, resource nodes, and hidden chests.
* **Route planning tool** for farming efficiency.
* **Global marker database** contributed by users, very similar to Genshin Impact’s fan maps.
* **Fast performance** even with multiple layers activated.

**Why it’s relevant:** The same team or style of community-driven mapping might inspire how *Star Resonance* maps evolve, especially for players switching between the two games.

---

### 🌠 **3. Star Resonance Global Map Hub – [starresonance.th.gl](https://starresonance.th.gl/)**

This one acts as a **map aggregator and region portal**, providing direct links to detailed map instances for different zones in *Star Resonance*.

**Features:**

* **Region-based navigation** – Jump directly into maps like *Asteria Plains* or *Celestia Heights*.
* **Lightweight and fast** – Loads quickly, ideal for lower-end devices or quick lookups.
* **Integrated updates** – Automatically syncs with newly released map layers from the main database.
* **Language support** – Community translations are being added gradually.

**Pro tip:** Bookmark this page as your map hub. It’s a convenient starting point for exploring new regions as they get released.

---

### 🌾 **4. Asteria Plains Detailed Map – [starresonance.th.gl/maps/Asteria%20Plains](https://starresonance.th.gl/maps/Asteria%20Plains)**

This is a **zoomed-in, detailed version** focused on the *Asteria Plains* region — one of the earliest and most resource-rich areas in the game.

**What makes it great:**

* **Accurate item spawn locations** – Ideal for farming early-game materials.
* **Mini-event markers** showing puzzle spots, elite enemies, and special chests.
* **Interactive pins** with item/tooltips so you know exactly what each node drops.
* **High map resolution**, allowing deep zoom levels for tight farming routes.

**Community tip:** This specific region map often gets updates first before the global one. If you’re grinding Asteria Plains daily, this is the most efficient tool you can use.

---

### 💬 **Final Thoughts & Community Invitation**

All four resources together form an **ecosystem of exploration tools** for both *Star Resonance* and *Blue Protocol* fans. Whether you’re a completionist, lore hunter, or casual explorer, these maps make a huge difference in how efficiently you can plan routes and track your progress.

If you find missing markers, incorrect placements, or want to share farming routes, consider contributing back — most of these maps have community submission forms or Discords for that purpose.

---

### 🔗 **Quick Links Recap**

* 🗺️ **Star Resonance Main Map:** [https://starresonancemap.com/](https://starresonancemap.com/)
* ⚔️ **Blue Protocol Map:** [https://blueprotocol.interactivemap.app/](https://blueprotocol.interactivemap.app/)
* 🌍 **Star Resonance Global Hub:** [https://starresonance.th.gl/](https://starresonance.th.gl/)
* 🌾 **Asteria Plains Map:** [https://starresonance.th.gl/maps/Asteria%20Plains](https://starresonance.th.gl/maps/Asteria%20Plains)

---

If you’ve tried any of these, what’s your favorite feature?
Also, if there are other map tools or trackers I missed, drop them below — I’ll add them to the post for everyone’s benefit.

Happy exploring, Travelers! 🌟

---

# Blue Protocol: Star Resonance Wiki (swiki.jp)

* [https://bpsr.swiki.jp/](https://bpsr.swiki.jp/)

- Features
   - Comprehensive Japanese-language wiki of gameplay systems (classes, combat, life content, etc.)
   - Editable by users (community contributions) ([bpsr.swiki.jp][1])
   - Keeps logs of recent edits and version history ([bpsr.swiki.jp][1])
- Explanation
   This wiki aggregates all known mechanics, strategies, and reference data for **Blue Protocol: Star Resonance (BPSR / スタレゾ)** based largely on existing versions (e.g. Chinese version) and community findings. ([bpsr.swiki.jp][1])
- Description
   It is essentially a fan/enthusiast “攻略Wiki” (strategy wiki) in Japanese, covering classes, gear, systems (combat, crafting, life skills), and game updates. ([bpsr.swiki.jp][1])
- Pros
   - Very detailed in many game areas
   - Well maintained with recent updates ([bpsr.swiki.jp][1])
   - Good for Japanese readers or those comfortable in Japanese
- Cons
   - Japanese only (not fully translated)
   - Some sections are based on non-Japanese versions and may diverge when localized
   - Because it’s community maintained, some data may lag or be speculative
- Other information
   - The site states that once the Japanese server launches, content will be adapted to that region. ([bpsr.swiki.jp][1])
   - It uses swiki.jp / PukiWiki system for editing and version control. ([bpsr.swiki.jp][1])

---

# Prydwen.gg – Blue Protocol / Star Resonance Wiki & Database

* [https://www.prydwen.gg/blue-protocol/](https://www.prydwen.gg/blue-protocol/)

- Features
   - English / global interface with guides, class overviews, tier lists, interactive maps, blog posts ([Prydwen][2])
   - Tools like a talent planner, daily checklists, interactive maps ([Prydwen][2])
   - Regularly updated with new guides, PVE content breakdowns, class info ([Prydwen][3])
- Explanation
   Prydwen.gg acts as an English-friendly central hub for BPSR / Star Resonance, aggregating knowledge, tools, and guides for players globally.
- Description
   It offers both static guides (e.g. PVE content, class types) and dynamic tools (planners, maps) to assist players in optimization and navigation of the game.
- Pros
   - Accessible to English speakers
   - Good mix of reference + interactive tools
   - Regular content updates and expansions
   - Clear layout and organization
- Cons
   - As the game evolves, some info may become outdated until updated
   - Depth in certain niche systems may lag behind native / local wikis
- Other information
   - The Tier List page rates classes/specs in modes like Chaotic Realm and future Dragon Raids. ([Prydwen][4])
   - The PVE content guide covers modes like Monster Hunt, Unstable Space, Chaotic Realm with drop mechanics and meta details. ([Prydwen][3])

---

# LUK.gg — BPSR Guides & Tools

* [https://luk.gg/bpsr](https://luk.gg/bpsr)

- Features
   - Guides, databases, and interactive tools for BPSR / Star Resonance ([LUK.GG][5])
   - Modular layout of systems, tool support, reference data
- Explanation
   LUK.gg is a third-party site that compiles guides, references, and utility tools tailored to BPSR, likely targeting both new and veteran players.
- Description
   It tends to emphasize clarity and usability of data, letting users browse game systems and mechanics.
- Pros
   - Simpler layout, often faster to find basics
   - Useful as a supplementary source alongside major wikis
   - Likely more up-to-date for user requests in niche areas
- Cons
   - May lack depth compared to full wikis
   - Some features or guides may be thin or incomplete
   - Reliance on community updates (could lag)
- Other information
   - The site is actively maintained (“3 days ago” mention) ([LUK.GG][5])

---

# Star-Resonance.com (Fansite / Official-adjacent)

* [https://star-resonance.com/en/](https://star-resonance.com/en/)

- Features
   - News, announcements, official and community updates ([Blue Protocol: Star Resonance][6])
   - Interactive map for the game world ([Blue Protocol: Star Resonance][6])
   - FAQs, class intros, trailers, site background info ([Blue Protocol: Star Resonance][6])
- Explanation
   This site acts as a fan / semi-official hub aimed at consolidating official announcements, lore, maps, and introductory content for Star Resonance.
- Description
   It is less of a deep wiki and more of a portal: official news, promotional content, basic guides, and world visuals.
- Pros
   - Good for news, updates, lore, and official statements
   - Nice visuals, maps, and introductory support
   - Accessible in English for global audience
- Cons
   - Not as comprehensive in mechanics or deep systems
   - Less community editing; less granular detail in some gameplay areas
   - It’s more curated, so fewer niche or player-discovered mechanics
- Other information
   - It covers the shift from “Blue Protocol” → “Star Resonance” branding and background. ([Blue Protocol: Star Resonance][7])
   - The FAQs page clarifies differences, crossplay, platforms, languages, etc. ([Blue Protocol: Star Resonance][8])
   - It also provides recommended / minimum specs for PC version. ([Blue Protocol: Star Resonance][9])

---

# Maxroll.gg – Blue Protocol / Star Resonance Section

* [https://maxroll.gg/blue-protocol](https://maxroll.gg/blue-protocol) (if accessible)

- Features
   - Historically, Maxroll is known for deep guides, tier lists, build optimization, analytics, and strategy content (from other games)
   - The community suggests there is or will be a “Blue Protocol / Star Resonance” section with “beginner’s guide, classes & skills, gear progression, dungeons, life skills, etc.” ([Reddit][10])
- Explanation
   Maxroll’s reputation and structure suggest that its BPSR section would aim to provide polished, well-structured guides and performance analysis.
- Description
   It may act as a “meta / optimization” site, focusing heavily on builds, endgame, comparisons, and advanced systems.
- Pros
   - Strong for advanced players and theorycrafting
   - Well organized, often high quality content in other games
   - Potential for deep builds, meta breakdowns, comparative analysis
- Cons
   - As of now, the BPSR section is less mature / less visible
   - Some links or content might be missing or under development
   - Depends on adoption and community contributions
- Other information
   - In Reddit discussion, users recommend starting with the Maxroll beginner’s guide for Blue Protocol content:
    > “If you're new to Blue Protocol, I would start here: [https://maxroll.gg/blue-protocol/getting-started/beginners-guide.”](https://maxroll.gg/blue-protocol/getting-started/beginners-guide.”) ([Reddit][10])
   - Because Maxroll is a large platform, its presence might grow as the game launches globally.

---

[1]: https://bpsr.swiki.jp/?utm_source=chatgpt.com "Blue Protocol: Star Resonance(星痕共鸣 / スタレゾ) Wiki"
[2]: https://www.prydwen.gg/blue-protocol?utm_source=chatgpt.com "Blue Protocol: Star Resonance Wiki & Database"
[3]: https://www.prydwen.gg/blue-protocol/guides/pve-content?utm_source=chatgpt.com "Blue Protocol: Star Resonance"
[4]: https://www.prydwen.gg/blue-protocol/tier-list?utm_source=chatgpt.com "Class Tier List | Blue Protocol: Star Resonance"
[5]: https://luk.gg/bpsr?utm_source=chatgpt.com "Blue Protocol: Star Resonance Guides and Interactive Tools"
[6]: https://star-resonance.com/en/?utm_source=chatgpt.com "en - Blue Protocol: Star Resonance"
[7]: https://star-resonance.com/?utm_source=chatgpt.com "Blue Protocol: Star Resonance"
[8]: https://star-resonance.com/faqs/?utm_source=chatgpt.com "FAQs - Blue Protocol: Star Resonance"
[9]: https://star-resonance.com/blue-protocol-star-resonance-welcome-to-regnas/?utm_source=chatgpt.com "Blue Protocol: Star Resonance - Welcome to Regnas!"
[10]: https://www.reddit.com/r/BlueProtocolPC/comments/1nypnb9/blue_protocol_star_resonance_database_website/?utm_source=chatgpt.com "Blue Protocol: Star Resonance Database Website Launch"

---

### 🧭 **[Fan Project] BlueProtocol.lunixx.de – Unofficial Player Database for Blue Protocol!**
> 🌐 **Website:** [https://blueprotocol.lunixx.de](https://blueprotocol.lunixx.de)
This site is basically a **player database + stat viewer**. You can look up players, see rankings, ability scores, classes, and even generate cool player signature images to show off your progress.
It’s currently in **beta**, made by a community dev named **Lunixx**, and it looks surprisingly polished for a fan tool.

---

### 💎 **Key Features**
* 🔍 **Player Search:** Find any player by name or ID.
* 📊 **Global Rankings:** Compare yourself to others across servers.
* 💪 **Detailed Stats:** See Ability Score, Class, Max HP, Last Login, and more.
* 🖼️ **Player Signatures:** Generate signature banners with your data (great for Discord or forums).
* 🌍 **Multi-Language:** Available in English, German, and French.

---

### ✅ **Pros**
* Super clean and lightweight interface.
* No login required — just browse player data.
* Great for stat nerds or guild leaders who want to compare performance.
* Fast loading and mobile-friendly.
* Actively updated by the dev.

---

### ⚠️ **Cons**
* ❗ Not official — it’s a **community project**, not made by Bandai Namco.
* ⚙️ Data might lag behind real game stats or occasionally bug out.
* 🔐 Doesn’t show where player data is sourced from (uses “ApiPlayers @ BlueProtocol”).
* 🧩 Some features still marked as *beta* or *work in progress*.

---

### 💬 **User Comments**
> **u/ArcLancer:**
> This is actually amazing. I found my character instantly — stats were 95% accurate. Hope the dev keeps updating it!
> **u/ServerLagged:**
> Looks neat but I’m a bit skeptical where it pulls data from. Still, props to the dev for building it.
> **u/Lunixx (dev):**
> Thanks! Everything is based on public endpoints; no private account info is used. Feedback is always welcome 💙
> **u/HealerMain:**
> Finally, a leaderboard that doesn’t crash my browser. 10/10 would stalk my guildmates again. 😂
> **u/OldManRanger:**
> Needs a dark mode and maybe a way to filter by class — but overall, awesome project.

---

### 🧠 **TL;DR**
**blueprotocol.lunixx.de** is an unofficial but super-useful player database for Blue Protocol — perfect if you like tracking rankings or sharing your player card.
Use it for fun and comparison, but remember: **not an official Bandai Namco tool**.

---
