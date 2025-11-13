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
* This project is a modified version based on **StarResonanceAutoMod**.

* The original **StarResonanceAutoMod** itself was derived from **StarResonanceDamageCounter**.

* Therefore, this project continues to use the **AGPL v3 open-source license**.

* **Quick Start:**

  1. If you haven’t used the above tools before, install **Npcap** from the included archive or download it via the provided link.
  2. Double-click **模组求解器.exe (Module Solver.exe)**, select your network card, and click **Start Capture**.
  3. After the capture begins, switching maps, changing channels, or relogging will allow the program to obtain your module data.
  4. Once modules are captured, you can manually stop the capture, or it will stop automatically after 60 seconds of inactivity.
  5. Since the program uses an enumeration algorithm, avoid having too many modules; use **Delete Low-Level Modules** to reduce them.
  6. Set **target** and **excluded attributes** as needed — results will appear under **Target Requirement Plan**.
  7. After selecting a profession, results will also show under **Profession Attribute Plan** (affected by target/excluded attributes).
  8. For a cleaner display, you can **export results to a Word file**.

* **Note:** Profession module recommendations follow in-game defaults; if you have specific attribute goals, use the **target/exclusion** options to customize results.

---

### **Build & Optimization Calculators**

**[c0derceejay/unofficial-blueprotocol-star-resonance](https://github.com/c0derceejay/unofficial-blueprotocol-star-resonance)**
* **Unofficial Blue Protocol: Star Resonance Build Calculator** is a community tool for creating, analyzing, and sharing character builds.
* Users can customize stats, equipment, and skills for five classes: Blade Warden, Spell Weaver, Twin Striker, Heavy Smasher, and Fatal Mask.
* Builds are automatically evaluated for power rating, build type, and difficulty in real time.
* Community Build Gallery allows browsing, copying, and sharing user-created builds.
* Fully responsive, browser-based interface with Blue Protocol-themed visuals and animations.
* All data is stored locally in the browser using `localStorage`; no external servers are needed.
* Built with pure HTML, CSS, and JavaScript, compatible with modern browsers on desktop and mobile.
* To use: open `index.html` in a browser, navigate to Build Builder to create builds, and explore community builds in the gallery.

**[fudiyangjin/StarResonanceAutoMod](https://github.com/fudiyangjin/StarResonanceAutoMod)**
* This tool captures live network packets from *Star Resonance* to extract in-game module data automatically.
* It filters and optimizes module combinations using a C++ algorithm core with optional GPU (CUDA/OpenCL) acceleration.
* Users can target or exclude attributes like “Crit Focus” or “Intellect Boost” to find the best four-module sets.
* It supports both CPU and GPU builds—run the `.exe` version for quick use or Python source for development.
* Requires Npcap installed on Windows 10/11 to capture packets from the game client.
* Basic usage: open CMD, navigate to the folder, and run `.\StarResonanceAutoMod.exe -a -lang en`.
* For offline analysis, use `.\StarResonanceAutoMod.exe -lv -lang en` after one successful capture.
* Developers can clone the repo, install dependencies, build C++ extensions, and run `python star_railway_monitor.py -a`.

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
<img width="2482" height="974" alt="QQ_1754365166259" src="https://github.com/user-attachments/assets/935a6edc-f511-4d1f-93c7-4ad54dc26572" />
<img width="2338" height="723" alt="QQ_1754363666663" src="https://github.com/user-attachments/assets/552dd8d8-e10d-41e1-909b-ef61764478d7" />

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

* Some note setup complexity due to Npcap configuration.
* Generally praised for being a clean, standalone overlay tool.
---
[**ok-star-resonance**](https://github.com/Sanheiii/ok-star-resonance)
* **ok-star-resonance** automates *Star Trace Resonance* gameplay using image recognition and Windows interface simulation.
* It does **not read game memory or modify game files**, only simulates user clicks through the UI.
* The software is **open source, free, and intended for personal learning**, not for commercial use.
* It supports **fishing and simple resource collection** in-game.
* Runs at any **16:9 resolution**, windowed or fullscreen, but cannot run in the background.
* AI detects fish positions and swings the rod accurately; notifications use **PushDeer**.
* Python source requires **Python 3.12**; run via `python main.py` (release) or `main_debug.py` (debug).
* Users must follow instructions for **display settings, key bindings, and antivirus exceptions** to ensure proper operation.
---
[**BlueProtocolStarResonanceDataAnalysis**](https://github.com/Zaarrg/BlueProtocolStarResonanceDataAnalysis)
* **BlueProtocolStarResonanceDataAnalysis** is a toolkit for extracting and processing game data from *Blue Protocol: Star Resonance*.
* Currently, it provides a **complete mapping from Skill ID to English names** for core gameplay skills.
* A small subset of rare or edge-case skills is still marked as WIP; main skills are fully supported.
* Future updates aim to include **dungeon/world-boss datasets, drop tables, and cross-referencing skill sources**.
* Users extract raw game data via `bspr_data_extraction_pipline.py`, optionally specifying game DLL and metadata paths.
* Skill ID → English mapping can be generated with `skill_table_generator.py`.
* The project is **for educational and research purposes only**, with no support for cheating or violating Terms of Service.
* All processing is local; users should respect laws and game publisher rights when using this toolkit.
---
[**StarResonanceNews**](https://github.com/azmiao/StarResonanceNews)
* **StarResonanceNews** is a personal bot that pushes official *Star Resonance* game news.
* Currently, it only works with **YuiChyanBot** for news delivery.
* The bot parses web page JavaScript to extract news content and metadata.
* Returned data includes news title, description, images, author, creation time, and unique IDs.
* Supports **multi-page results**, allowing retrieval of all recent news entries.
* Developers can use the JSON-like output as a template for secondary development or integration.
* All processing is local; the bot does not modify game files or interact with gameplay.
* Intended for personal use to stay updated with official announcements and events.
