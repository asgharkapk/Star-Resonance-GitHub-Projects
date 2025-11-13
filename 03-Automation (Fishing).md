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
* **Star Resonance AutoFisher** automates fishing in *Star Resonance* using image recognition and Windows API click simulation.
* It does **not read game memory or modify game files**, interacting only through the visible game interface.
* The tool works in **any 16:9 resolution**, windowed or fullscreen, but cannot run in the background.
* AI detects fish positions and performs accurate casting for efficient fishing.
* Users must follow display and key-binding requirements, and whitelist folders in antivirus/Windows Defender to avoid issues.
* Python source requires **Python 3.12**; run CPU version with OpenVINO via `python main.py` or `main_debug.py`.
* Troubleshooting includes hiding character names, adjusting resolution, and ensuring extraction to English-only directories.
* The project is **open-source, free, and for personal use only**, with all consequences of use borne by the user.

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

[**StarAutoFish script by YHZI**](https://github.com/YHZI/StarAutoFish)

* It’s a Python‑based autofishing script designed for the game Star Resonance (or possibly a variant/related game) — repository includes `autoFish.py`, `getMousePos.py`, and various image assets (e.g., `left.png`, `right.png`, `no_cast.png`).
* The script likely uses screen image recognition (matching bait/fishing UI visuals, fish icons or fishing indicators) plus simulated mouse clicks to automate the fishing action.
* The presence of `getMousePos.py` suggests a helper tool to capture screen coordinates for the target UI elements.
* The image assets like `continueFishing.png`, `use.png`, etc., indicate the script checks for specific in‑game visuals (e.g., “use” button, “no cast” state) and acts accordingly.
* No README provides full installation or usage steps; you would need Python installed and likely run the script in administrator mode (for screen capture or UI simulation) and ensure the game is visible on screen.
* Because it automates in‑game actions via UI simulation, usage may conflict with game terms of service—use at your own risk.
* The repository is small and appears to be a personal project rather than a polished commercial tool.

If you like, I can check the repository in more detail and **write exact steps** to set it up (with caveats about risks).
