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

**[dmlgzs/StarResonanceDamageCounter](https://github.com/dmlgzs/StarResonanceDamageCounter)** **THE OG**
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
![pic1](https://raw.githubusercontent.com/ssalihsrz/InfamousBPSRDPSMeter/refs/heads/main/screenshots/main-interface.jpg)
![pic2](https://raw.githubusercontent.com/ssalihsrz/InfamousBPSRDPSMeter/refs/heads/main/screenshots/player-details.jpg)
![pic3](https://raw.githubusercontent.com/ssalihsrz/InfamousBPSRDPSMeter/refs/heads/main/screenshots/session-management.jpg)
![pic4](https://raw.githubusercontent.com/ssalihsrz/InfamousBPSRDPSMeter/refs/heads/main/screenshots/team-overview.jpg)

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
[**StarResonanceDPS**](https://github.com/cuteSATOU/StarResonanceDPS)
* **StarResonanceDPS** is an Electron-based third-party tool for real-time DPS tracking and analysis in *Star Resonance*.
* It captures network packets locally and parses Protocol Buffers data to compute detailed damage statistics.
* Provides **real-time DPS monitoring**, including normal, critical, and lucky damage, plus historical peak and average DPS.
* Supports **multi-player tracking** and automatically calculates critical rates and damage distributions.
* Runs as a **native desktop app** on Windows 10/11, requiring administrator permissions and WinPcap/Npcap for packet capture.
* Users can clone the repository, install dependencies with `npm install`, and launch with `npm start` in admin mode.
* The interface allows selection of network devices, starting/stopping captures, clearing stats, and viewing live DPS dashboards.
* All processing is local; the tool does **not modify game files**, and users must follow community rules while using it.
---
[**BPSR_ACT_Plugin**](https://github.com/Garash2k/BPSR_ACT_Plugin)
* **BPSR_ACT_Plugin** is an Advanced Combat Tracker (ACT) plugin for *Blue Protocol: Star Resonance*.
* It provides detailed combat analysis, including DPS, death reports, damage by combatant, and individual hit info.
* Users must install **Advanced Combat Tracker** and **Npcap**, then place the plugin DLL in `%appdata%\Advanced Combat Tracker\Plugins`.
* The plugin is loaded via ACT’s **Plugins tab**, enabling real-time combat tracking and analytics.
* Features planned include better device autodetection, class/spec display, zone handling, and improved monster/skill name translations.
* Uses **SharpPcap**, **PacketDotNet**, and **ZstdSharp.Port** for packet capture and processing.
* All networking and packet handling code is adapted from **Star Resonance Damage Counter**.
* The tool is open-source and intended for detailed combat monitoring and research, not for cheating.
![](https://files.catbox.moe/sx6atv.png)
---
[**BPSR-PSO-upd**](https://github.com/cute5051/BPSR-PSO-upd)
- Blue Protocol: Star Resonance - Per Second Overlay (BPSR-PSO) is a standalone GUI application that tracks DPS/HPS for nearby players by analyzing network packets in transit. It does not modify the game or interact directly with game files.
**Setup & Installation:**
1. Install [Node.js](https://nodejs.org/) (npm included).
2. Install Npcap (installer in `/resources` folder; enable "WinPcap API-compatible Mode").
3. Clone the repository: `git clone https://github.com/Chase-Simmons/BPSR-PSO.git`
4. Navigate to the folder and install dependencies: `npm install`
**Running:**
* Run Npcap installer and start the application.
* Latest release: [BPSR-PSO releases](https://github.com/cute5051/BPSR-PSO-upd/releases/latest)
**Features:**
* Main window for monitoring DPS/HPS.
* Monster list overview.
* Skill detail view (click DPS blocks to open).
* Settings accessible from main window.
**Note:** Designed by the developer for personal use, inspired by TERA Online's Shinra meter.
**License:** AGPL-3.0
Main window\
![main.png](https://raw.githubusercontent.com/cute5051/BPSR-PSO-upd/refs/heads/master/resources/main.png)
Monster list\
![monster-lists.png](https://raw.githubusercontent.com/cute5051/BPSR-PSO-upd/refs/heads/master/resources/monster-lists.png)
Settings in Main window\
![settings.png](https://raw.githubusercontent.com/cute5051/BPSR-PSO-upd/refs/heads/master/resources/settings.png)
![skills-details.png](https://raw.githubusercontent.com/cute5051/BPSR-PSO-upd/refs/heads/master/resources/skills-details.png)

---
[**caaatto/BlueMeter**](https://github.com/caaatto/BlueMeter)
* It’s a desktop tool called **BlueMeter** for Blue Protocol: Star Resonance that analyses real‑time combat data (DPS/HPS etc) by capturing network packets and presenting them as overlay stats.
* It does **not modify the game client or its files**—it passively monitors traffic to compute damage/healing metrics.
* How it works: you download the release ZIP or build from source (.NET 8.0 required), install and run the application, and it listens to your network adapter via a packet capture driver (e.g., Npcap) to parse combat packets.
* After launching, the overlay will display your stats such as DPS, HPS, peak damage, contribution percentage and other combat‑related numbers while you play.
* To use: extract the release to a folder, run `BlueMeter.WPF.exe` (or the built executable), ensure .NET 8.0 runtime is installed, start the game and fight as usual—stats are captured real‑time.
* Alternatively, for building from source: install .NET 8.0 SDK, clone the repo, build with `dotnet build -c Release`, or `dotnet publish` to generate the executable.
* The UI is a visible overlay you can move or resize, it reads network packets from your system’s adapter, decodes game events and shows them in meaningful metrics.
* Users must run it under their own responsibility—while it is non‑invasive (no memory injection or file modding), usage may still carry risk depending on game policy.
<img src="https://raw.githubusercontent.com/caaatto/BlueMeter/refs/heads/main/BlueMeter.Assets/Images/dpsMeter.png" alt="DPS Meter" width="200" />
<img src="https://raw.githubusercontent.com/caaatto/BlueMeter/refs/heads/main/BlueMeter.Assets/Images/menuView.png" alt="Menu" width="400" />
<img src="https://raw.githubusercontent.com/caaatto/BlueMeter/refs/heads/main/BlueMeter.Assets/Images/Settings.png" alt="Settings" width="300" />

---
[**wahfcore/bpsr-meter-wahf-edition**](https://github.com/wahfcore/bpsr-meter-wahf-edition)
* It’s a custom-branded real-time **DPS/HPS meter overlay** for Blue Protocol: Star Resonance.
* Works on **Windows 10/11** and captures network packets via **Npcap** to track player stats.
* Displays metrics for **nearby players or solo**, with rank badges and local player highlighting.
* Overlay updates every **50ms**, supports adjustable scale (100%, 70%, 50%, 30%) and click-through transparency.
* Uses **Electron framework** for the GUI, with dark theme, HP bars, class icons, and damage visualization.
* To use: install **Npcap** with WinPcap API-compatible mode and loopback support.
* Download and extract the **ZIP**, then run `BPSR Meter - WAHF Edition.exe`; overlay appears top-right.
* Change **game instance or line** to start detection; interact with overlay controls by hovering over buttons.
---
[**vegask/BPSR-Meter**](https://github.com/vegask/BPSR-Meter)
* BPSR Meter is a real‑time DPS/HPS overlay tool for Blue Protocol: Star Resonance, built on top of packet‑capture techniques from earlier meters. ([GitHub][1])
* It captures network traffic using drivers like Npcap (WinPcap‑compatible mode) to parse combat events without modifying the game client. ([GitHub][2])
* For end users: download the installer from GitHub Releases, install Npcap first, then run the application (Windows 10/11 supported). ([GitHub][2])
* For developers: clone the repo, install Node.js v22+, run `npm install`, then build or start in dev mode (`npm run dev`, `npm run build`).
* The architecture uses Electron + Vite for the renderer UI, Express for API backend, and socket.io for real‑time event updates.
* At runtime the overlay positions itself (top‑right by default), updates stats every ~50 ms, supports scaling and click‑through transparency, and highlights the local player plus top performers.
* It resets stats when you change server channels or instances (since new packet streams are detected) and may show “Unknown” for players who joined before the meter started. ([Reddit][3])
* Note: Because it listens to packets, use at your own risk; community posts mention concerns about security and compatibility with anti‑cheat systems. ([Steam Community][4])

[1]: https://github.com/Fremy-Speeddraw/BPSR-Meter?utm_source=chatgpt.com "Fremy-Speeddraw/BPSR-Meter"
[2]: https://github.com/Fremy-Speeddraw/BPSR-Meter/releases?utm_source=chatgpt.com "Releases · Fremy-Speeddraw/BPSR-Meter"
[3]: https://www.reddit.com/r/BlueProtocolPC/comments/1o9wexp/release_bpsr_meter_v100_forked/?utm_source=chatgpt.com "[Release] BPSR Meter v1.0.0 - Forked : r/BlueProtocolPC"
[4]: https://steamcommunity.com/app/3681810/discussions/0/594036760294469861/?l=russian&utm_source=chatgpt.com "DPS meter - Blue Protocol: Star Resonance"
---

