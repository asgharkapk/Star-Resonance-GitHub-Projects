<img width="399" height="221" alt="image" src="https://github.com/user-attachments/assets/3248445a-4d1e-4d45-ac5e-d87f27a2f83c" /># Star-Resonance-GitHub-Projects

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

* Some note setup complexity due to Npcap configuration.
* Generally praised for being a clean, standalone overlay tool.


