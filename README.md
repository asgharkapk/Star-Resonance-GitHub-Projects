# Repository Documentation



---

## 01-DPS-METERS.md

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
![OG](https://github.com/asgharkapk/Star-Resonance-GitHub-Projects/blob/main/data/OG.jpg?raw=true)

**[anying1073/StarResonanceDps](https://github.com/anying1073/StarResonanceDps)**
- Based on StarResonanceDamageCounter for real-time DPS analysis.
- Tracks individual and team damage output during encounters.
- Helps optimize gameplay by understanding DPS distribution and critical hits.
![WOW](https://github.com/asgharkapk/Star-Resonance-GitHub-Projects/blob/main/data/WOW.jpg?raw=true)

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
![WOW](https://github.com/asgharkapk/Star-Resonance-GitHub-Projects/blob/main/data/WOW.jpg?raw=true)

**[Madbol20/StarResonanceDps](https://github.com/Madbol20/StarResonanceDps)**

* Advanced DPS analysis and combat data tool for *Star Resonance*.
* Based on and extended from **StarResonanceDamageCounter**, with additional analysis modules and UI improvements.
* Captures, parses, and visualizes combat logs for real-time and post-battle review.
* Offers multiple frontends (WPF/WinForms) for customizable user experience.
* Designed for player self-improvement and performance benchmarking.
* Does **not** modify or interfere with the game client — works through network data interpretation.
* Requires **.NET 8.0** runtime to operate.
* Distributed under the **AGPL v3.0** open-source license.
* Aimed at transparency, education, and fair gameplay analytics.
  ![mad](https://github.com/asgharkapk/Star-Resonance-GitHub-Projects/blob/main/data/mad.jpg?raw=true)

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

[**ssalihsrz/InfamousBPSRDPSMeter**](https://github.com/ssalihsrz/InfamousBPSRDPSMeter)
* Infamous Blue Protocol: Star Resonance DPS Meter
* Real-time damage tracking and performance analysis tool
* Inspired by similar DPS meters from popular online RPGs
* Built to provide transparent and fair player statistics
* Supports customizable overlays and detailed combat summaries
* Requires .NET runtime and in-game data parsing setup
* Community-driven project — feedback and contributions are welcome
* Intended for educational and analytical use only

[**Sola-Ray/BPSR-PSO-SX**](https://github.com/Sola-Ray/BPSR-PSO-SX)
* Blue Protocol: Star Resonance Plug-in System (PSO-SX)
* Modular enhancement framework for Star Resonance utilities
* Includes support for performance tracking, overlays, and UI extensions
* Focused on stability, modularity, and community plugin development
* Compatible with various Star Resonance helper tools
* Written in C# with modern architecture design
* Licensed under open-source terms for collaborative development
* For fair and transparent gameplay analytics only
Below are some example views of the overlay in action:  

<p align="center">
  <img width="399" height="221" alt="DPS overlay example" src="https://github.com/user-attachments/assets/44cd0ce2-ac2c-4b99-b371-8965ea2086f2" />
  <br/>
  <em>Real-time DPS display showing nearby players’ output.</em>
</p>

<p align="center">
  <img width="392" height="224" alt="Detailed metrics panel" src="https://github.com/user-attachments/assets/8a5a7e88-1237-4c16-a0f0-f5c0afb3eb91" />
  <br/>
  <em>Real-time HPS display showing nearby players’ output.</em>
</p>

<p align="center">
  <img width="718" height="903" alt="Extended Sola view" src="https://github.com/user-attachments/assets/c49598b7-cc21-45e6-867a-0639d847680b" />
  <br/>
  <em>“Sola Extended” view with enhanced tracking and session analytics.</em>
</p>

[**woheedev/bptimer**](https://github.com/woheedev/bptimer)
* Blue Protocol Timer Utility
* Comprehensive time tracking and boss/event scheduling tool
* Supports multiple regions and synchronized server times
* Built with web-based UI for easy access and portability
* Features countdowns, alerts, and world boss tracking
* Ideal for players and communities organizing events
* Continuously updated with global Blue Protocol content
* Open-source and community-maintained for accuracy and fairness

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

![pso](https://preview.redd.it/verdant-oracle-smite-seems-to-have-good-damage-and-healing-v0-cakpr0lb4wwf1.png?width=320&crop=smart&auto=webp&s=1b08ef2d7fc5f94d22884b2cf58441e334e05f90)

**[Denoder/BPSR-Meter](https://github.com/Denoder/BPSR-Meter)**

* Real-time DPS and combat tracker for *Blue Protocol*.
* Provides live player and monster damage statistics, DPS calculations, and detailed combat analysis.
* Tracks group damage with individual player stats and boss/monster breakdowns.
* Includes combat timers, auto-clear options, and session logging with export capabilities.
* Built using **Electron**, **React 19**, and **TypeScript** for Windows OS.
* Uses network packet capture via **Npcap** or **WinDivert**, requiring no modification to the game client.
* Multilingual support: English and Chinese interface.
* Auto-update support via GitHub releases ensures users stay on the latest version.
* Open-source under **AGPL-3.0**, allowing modification and redistribution under the same license.
* Requires Node.js v22.20.0 or higher for building from source.
* Early-stage project with limited community adoption; users should check compatibility with the latest game version.

<img width="1458" height="782" alt="image" src="https://github.com/user-attachments/assets/3f949d1e-4293-49ce-a397-b10a0c64c9e9" />

---


---

## 02-Other Tools.md

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

## 03-Automation (Fishing).md

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



---

## 04-Translation.md

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



---

## 05-Guides.md

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

# send any spreadsheets you know to be included


---

## 07-BPSR discord list.md

# 🌌 **Blue Protocol & Star Resonance Discord Server Directory**

A detailed list of the most active and resourceful Discord communities dedicated to **Blue Protocol** and **Star Resonance (BPSR)**. Whether you're looking for game guides, farming groups, database resources, or community events, these servers will help you connect with fellow players and stay up-to-date with the latest information.

---

## 🎮 **1. Star Resonance Official Community**
🔗 **Invite:** [https://discord.gg/starresonance](https://discord.gg/starresonance)  
🌟 **Focus:** Official server for *Star Resonance*, a vibrant social hub for players to discuss updates, share builds, and participate in community events.  
💬 **Features:**
- Official news, patch notes, and announcements.  
- Player support and FAQ channels.  
- Team recruitment and co-op event coordination.  
- Showcase channels for artwork, screenshots, and tips.  
- Active moderators and multilingual community support.

---

## 🌾 **2. BPSR Farmers Hub**
🔗 **Invite:** [BP:SR Farmers](https://discord.gg/bpsrfarmers)  
🔗 **Invite:** [BPSR Rarefarmers](https://discord.gg/tPb3zAVZ2Z)  
🌾 **Focus:** A community-driven hub dedicated to **farming routes**, **resource optimization**, and **crafting efficiency** in both *Blue Protocol* and *Star Resonance*.  
💬 **Features:**
- Daily farming route sharing and optimization discussions.  
- Trading and marketplace value tracking.  
- Build and resource chain discussions for efficient gameplay.  
- Farming bot alerts and spawn timer updates.  
- Collaborative guides and spreadsheets.

---

## ⚔️ **3. BPSR Global Community**
🔗 **Invite:** [https://discord.gg/3UTC4pfCyC](https://discord.gg/3UTC4pfCyC)  
🌐 **Focus:** A large international community that unites both *Blue Protocol* and *Star Resonance* players under one roof.  
💬 **Features:**
- News and update aggregation across regions (JP/Global/CN).  
- PvE and PvP coordination for major events.  
- Translation channels for non-English resources.  
- Friendly social community with meme and off-topic lounges.  
- Voice channels for live farming and group raids.

---

## 📘 **4. Star Resonance Database (SRDB)**
🔗 **Invite:** [https://discord.com/invite/srdb](https://discord.com/invite/srdb)  
📚 **Focus:** A **data-driven** server for *Star Resonance* players who enjoy analytics, drop rate analysis, and crafting path optimization.  
💬 **Features:**
- Item, gear, and crafting database discussions.  
- Drop rate research and verified data tables.  
- Spreadsheet collaboration for item chains and currency costs.  
- Technical insights into game mechanics and data mining.  
- Developer tools and fan-made utility bots.

---

## 🧭 **5. Blue Protocol Database (BPDB)**
🔗 **Invite:** [https://discord.gg/invite/blueprotocoldb](https://discord.gg/invite/blueprotocoldb)  
📘 **Focus:** The primary data and research server for *Blue Protocol*, managed by community data analysts and database maintainers.  
💬 **Features:**
- Comprehensive item, equipment, and skill databases.  
- Crafting chain analysis and stat breakdowns.  
- Automated data sync with the **Blue Protocol Database** website.  
- Patch change tracking and version comparison tools.  
- Data submission and validation community.

---

## 🗄️ **6. Blue Protocol Database (Website Discord)**
🔗 **Invite:** *(Community-managed — link available on the [Blue Protocol Database website](https://blueprotocoldb.com))*  
💡 **Focus:** Companion Discord to the Blue Protocol Database, ideal for contributing to ongoing research and updates.  
💬 **Features:**
- Data verification discussions.  
- Feedback and improvement suggestions for the site.  
- Integration of API updates and localization projects.  
- Opportunities to contribute guides, media, and translations.

---

## 🛠️ **Additional Resources**
- 🌐 **Official Sites:**  
  - [Star Resonance Global](https://www.starresonance.com/)  
  - [Blue Protocol Official](https://blue-protocol.com/)  
- 📊 **Community Databases:**  
  - [Blue Protocol Database](https://blueprotocoldb.com)  
  - [Star Resonance Crafting Database](https://asgharkapk.github.io/star-resonance-crafting-database/)

---

### 💬 **Tips for New Members**
1. Always read the rules and use the correct channels.  
2. Introduce yourself — communities are welcoming!  
3. Use server tools like `/search`, `/build`, and `/farmroute` (where available).  
4. Check pinned messages for guides and resources.  
5. Stay active — event notifications often happen in real time.

---

> ⚡ *Join these servers to connect with experts, contribute to research, and enhance your Star Resonance and Blue Protocol experience!*


---

## 08-BPSR-WIKIs-WEBSITEs-List.md

# 🌌 Blue Protocol: Star Resonance Resource Compilation

A curated collection of community sites, tools, and wikis dedicated to **Blue Protocol: Star Resonance (BPSR / スタレゾ)**.

---

## 📘 Blue Protocol: Star Resonance Wiki (swiki.jp)

🔗 **Website:** [https://bpsr.swiki.jp/](https://bpsr.swiki.jp/)

### 🧭 Features
- Comprehensive Japanese-language wiki covering classes, combat, and life systems.
- Editable by users (community contributions).
- Keeps logs of recent edits and version history.

### 🧠 Explanation
This wiki aggregates all known mechanics, strategies, and reference data for **Blue Protocol: Star Resonance**, based on existing (e.g. CN) versions and player findings.

### 📜 Description
A fan-maintained “攻略Wiki” (strategy wiki) in Japanese, covering classes, gear, combat, crafting, and updates.

### ✅ Pros
- Extremely detailed and active.
- Frequently updated with new content.
- Great for fluent Japanese readers.

### ⚠️ Cons
- Japanese-only (no full translation).
- Some data based on non-JP versions.
- As community-edited, accuracy can vary.

### 🔍 Other Information
- Will adapt content once Japanese servers launch.
- Uses **swiki.jp / PukiWiki** for editing and version control.

> 🔗 [Visit bpsr.swiki.jp »](https://bpsr.swiki.jp/?utm_source=chatgpt.com)

---

## 🌐 Prydwen.gg – Blue Protocol / Star Resonance Wiki & Database

🔗 **Website:** [https://www.prydwen.gg/blue-protocol/](https://www.prydwen.gg/blue-protocol/)

### 🧭 Features
- English/global interface with guides, tier lists, and maps.
- Talent planner, daily checklists, and class info.
- Regular updates for PVE and class systems.

### 🧠 Explanation
Acts as a global English hub combining **wiki + tools + guides** for all BPSR players.

### 📜 Description
Provides both static guides (e.g. PVE content) and dynamic tools (e.g. maps, planners).

### ✅ Pros
- English interface.
- Excellent layout and structure.
- Consistent content updates.

### ⚠️ Cons
- Some info may become outdated between patches.
- Niche details may lag behind native wikis.

### 🔍 Other Information
- Includes **tier lists** and **PVE mode breakdowns**.
- Covers Chaotic Realm, Monster Hunt, and other events.

> 🔗 [Visit Prydwen.gg »](https://www.prydwen.gg/blue-protocol/?utm_source=chatgpt.com)

---

## 💠 LUK.gg — BPSR Guides & Tools

🔗 **Website:** [https://luk.gg/bpsr](https://luk.gg/bpsr)

### 🧭 Features
- Guides, tools, and databases for BPSR.
- Modular, user-friendly layout.

### 🧠 Explanation
LUK.gg provides a simplified experience for browsing game systems and mechanics.

### ✅ Pros
- Fast and lightweight.
- Great for quick references.
- Community-maintained and frequently updated.

### ⚠️ Cons
- May lack deep or advanced details.
- Incomplete in some areas.

> 🔗 [Visit LUK.gg »](https://luk.gg/bpsr?utm_source=chatgpt.com)

---

## 🌐 Star-Resonance.com (Fansite / Semi-Official)

🔗 **Website:** [https://star-resonance.com/en/](https://star-resonance.com/en/)

### 🧭 Features
- Official news, updates, and announcements.
- Interactive map and lore.
- FAQs, trailers, and introduction content.

### 🧠 Explanation
A fan-maintained, semi-official hub consolidating **lore, news, and system overviews**.

### ✅ Pros
- Great visuals and official feel.
- English-friendly.
- Covers lore and world background.

### ⚠️ Cons
- Not as detailed as wikis.
- Focused on presentation, not mechanics.

> 🔗 [Visit Star-Resonance.com »](https://star-resonance.com/en/?utm_source=chatgpt.com)

---

## ⚔️ Maxroll.gg – Blue Protocol / Star Resonance Section

🔗 **Website:** [https://maxroll.gg/blue-protocol](https://maxroll.gg/blue-protocol)

### 🧭 Features
- Strategy site known for in-depth builds and analytics.
- Expected to include Blue Protocol beginner guides, builds, and gear systems.

### 🧠 Explanation
While still emerging, Maxroll’s coverage of BPSR is expected to match its high standard seen in other games.

### ✅ Pros
- Excellent theorycrafting and build analysis.
- Well-organized, professional design.

### ⚠️ Cons
- Section is still in development.
- Some links may be inactive or missing.

> 🔗 [Visit Maxroll.gg »](https://maxroll.gg/blue-protocol/getting-started/beginners-guide)

---

## 🧮 BlueProtocol.lunixx.de – Player Database (Fan Project)

🔗 **Website:** [https://blueprotocol.lunixx.de](https://blueprotocol.lunixx.de)

### 🧠 Description
Unofficial **player database and leaderboard**, showing stats, classes, and ability scores. Includes shareable signature banners.

### 💎 Features
- Player search and rankings.
- Stat pages and signature generator.
- Multi-language support (EN/DE/FR).
- Mobile-friendly and fast.

### ✅ Pros
- Clean UI, instant lookups.
- Actively updated.
- Great for comparing player stats.

### ⚠️ Cons
- Unofficial (community-made).
- Data sources are not transparent.
- Some stats may lag behind actual data.

> “Not official, but incredibly useful for stat tracking and rankings.”

---

## ⏱️ Natsume.io – Server Timers & Events Tracker

🔗 **Website:** [https://natsume.io/bpsr/](https://natsume.io/bpsr/)

### 🧭 Overview
Tracks **real-time events, resets, and world timers** for all BPSR servers, synced to local time.

### 💡 Features
- Live countdowns and notifications.
- Server + local time display.
- Separate tracking for Global and CN servers.

### ✅ Pros
- Simple, accurate, and auto-updating.
- Perfect for raid/guild planning.

### ⚠️ Note
Keep the tab open for live notifications.

> 🔗 [Visit Natsume.io »](https://natsume.io/bpsr/)

---

## 🗺️ QuestLog.gg – Blue Protocol Companion

🔗 **Website:** [https://questlog.gg/blue-protocol/en](https://questlog.gg/blue-protocol/en)

### 🧭 Overview
Interactive guide and map companion for **Blue Protocol**, including quests, regions, and loot tracking.

### 💎 Features
- Database of quests, items, and enemies.
- Interactive maps with filters.
- Mobile-friendly and well organized.

### ✅ Pros
- Perfect for completionists.
- Streamlined navigation and filtering.
- Community-driven and regularly updated.

> 🔗 [Visit QuestLog.gg »](https://questlog.gg/blue-protocol/en)

---

## 🌟 BPSR Talent Planner

🔗 **Website:** [https://bpsrtalent.vercel.app/](https://bpsrtalent.vercel.app/)

### 🧠 Features
- 8 playable classes with full talent trees.
- Valid build dependency checks.
- Shareable build links.

### 📋 Classes
Damage: Frost Mage, Stormblade, Marksman, Wind Knight  
Tank: Heavy Guardian, Shield Knight  
Support: Verdant Oracle, Beat Performer

> 🔗 [Try the Talent Planner »](https://bpsrtalent.vercel.app/)

---

## 🇫🇷 BlueProtocol.fr – French DPS Rankings

🔗 **Website:** [https://blueprotocol.fr/](https://blueprotocol.fr/)

### 🧠 Features
- Real-time DPS/HPS leaderboards.
- Dungeon filters and class rankings.
- Linked Discord community.

### ✅ Pros
- Competitive insight for FR players.
- Transparent and active.
- Great for improving performance.

> 🔗 [Visit BlueProtocol.fr »](https://blueprotocol.fr/)

---

## ⏰ BP Timer – Boss & Event Tracker

🔗 **Website:** [https://bptimer.com/](https://bptimer.com/)

### 💡 Features
- Live boss and magical creature spawn timers.
- Player-contributed data.
- Favorites list for quick access.
- Open-source (SvelteKit + PocketBase).

### ✅ Pros
- Real-time accuracy.
- Community-powered.
- Ideal for efficient farming.

> 🔗 [Visit BP Timer »](https://bptimer.com/)

---

## ✅ Blue Protocol Checklist

🔗 **Website / Repository:** [https://github.com/Teawase/blue-protocol-checklist](https://github.com/Teawase/blue-protocol-checklist)

### 💡 Features
- Track daily/weekly progress.
- Live reset timers.
- Local data save (no login).
- Import/export support.
- Confetti + progress visuals.

### ✅ Why Use It
Stay organized and motivated — perfect for efficient daily play.

> 🔗 [GitHub Repository »](https://github.com/Teawase/blue-protocol-checklist)

---

### 🧠 Summary
| Category | Site | Focus |
|-----------|------|--------|
| JP Wiki | [bpsr.swiki.jp](https://bpsr.swiki.jp/) | Deep mechanics (JP) |
| Global Wiki | [Prydwen.gg](https://www.prydwen.gg/blue-protocol/) | English wiki + tools |
| Tools | [LUK.gg](https://luk.gg/bpsr) | Lightweight tools |
| Events | [Natsume.io](https://natsume.io/bpsr/) | Timers |
| Builds | [bpsrtalent.vercel.app](https://bpsrtalent.vercel.app/) | Talent planner |
| Map/Quests | [QuestLog.gg](https://questlog.gg/blue-protocol/en) | Map & quest tracking |
| Rankings | [blueprotocol.fr](https://blueprotocol.fr/) | DPS/HPS leaderboards |
| Boss Timers | [bptimer.com](https://bptimer.com/) | Boss spawn tracking |
| Checklist | [Teawase Checklist](https://github.com/Teawase/blue-protocol-checklist) | Task tracking |
| Player Stats | [Lunixx DB](https://blueprotocol.lunixx.de) | Player lookup |

---

⭐ **Maintained for fans of Blue Protocol: Star Resonance**  
💙 All links verified and formatted for readability.


---

## 09-BPSR-inveractive-maps-list.md

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

## 🌟 Discover the World of Blue Protocol

Explore the full interactive map of Blue Protocol and uncover every nook and cranny of its stunning world!

🔗 Visit: [QuestLog – Blue Protocol Map](https://questlog.gg/blue-protocol/en/map)

---

### 🔍 Why You’ll Love It

* 🎮 **Comprehensive Interactive Map** — Easily navigate zones, landmarks, and hidden treasures.
* 🧭 **Detailed Guidance** — Pinpoints key points of interest so you never miss a challenge or treasure.
* 🕹️ **Perfect for Gamers** — Whether you’re a beginner or a veteran, the map helps streamline your adventures in Blue Protocol.

---

### ✨ Features at a Glance

* Fully browsable world map—zoom, pan, and explore.
* Marked areas for quests, dungeons, and secret locations.
* Clean interface and fast loading for smooth navigation.

---

### 📌 Tip for Gamers

Bookmark the map and keep it handy during your game sessions.
Use it as your on-the-fly reference when you’re out in the field and need to locate that elusive objective or side-quest point.

---

### 🚀 Get Started Now

1. Click [here](https://questlog.gg/blue-protocol/en/map) to open the map page.
2. Use the controls to zoom into your preferred zone.
3. Hover/click on icons to reveal what’s there — be it quests, dungeons, or hidden gems.
4. Dive into your next mission with clarity and purpose!

---

> “With the QuestLog map, I found all the hidden side-quest markers I’d been missing for hours!” – A satisfied gamer

---

Ready to elevate your Blue Protocol journey? Explore, strategize, and conquer the world with unmatched clarity.

— Spoiler: The treasures you’d been hunting are right under your nose 😉

---

