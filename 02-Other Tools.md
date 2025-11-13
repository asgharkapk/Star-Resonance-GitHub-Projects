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
