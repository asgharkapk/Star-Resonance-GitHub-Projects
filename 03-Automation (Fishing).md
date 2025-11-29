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
---
[**leo2971998/AutoFishingTool-BlueProtocolStarResonance**](https://github.com/leo2971998/AutoFishingTool-BlueProtocolStarResonance)
* It is a Python‑based automatic fishing tool for Blue Protocol: Star Resonance that casts and reels automatically, detects fish rarity, tracks catches, and can auto‑buy rods and bait.
* How it works: it uses image‑recognition to detect in‑game UI cues (like fish rarity icons or bait empty prompts) and simulates mouse actions to fish, purchase bait/rods, and log statistics.
* How to use: install Python 3.12+ (ensure “Add Python to PATH” and pip installed), then run the provided `install.bat` to set up.
* Then run `run.bat`, make sure the game is running and visible, press F5 to start fishing, F6 to pause, and ESC to stop.
* The game window must use 16:9 resolution, be in the foreground (not moved), and overlays/streaming software should be disabled.
* The tool runs in Administrator mode and relies on capturing visible UI elements (screenshots are exported in debug mode if detection fails).
* It keeps a log of catches in real time and categorises common / rare / mythical fish for statistics and tracking.
* You should follow the troubleshooting steps if it fails: ensure Python version is correct, run as admin, check screen capture assets match your resolution, and see debug screenshots for what the script sees.
---
[**mofutoshi-ctrl/blue-protocol-mining-bot**](https://github.com/mofutoshi-ctrl/blue-protocol-mining-bot)
* It’s a Python‑based advanced mining bot for Blue Protocol: Star Resonance called **blue‑protocol‑mining‑bot**, designed to automate in‑game mining tasks.
* The tool uses an **8‑tier intelligent system** to orchestrate mining actions such as locating ore, executing mining commands, and managing resources.
* To use it: install Python and dependencies (`requirements.txt`), configure your bot settings in `config.yaml`, and run `main.py` as the entry point.
* It interacts with the game via UI automation (e.g., simulated clicks or key‑presses) rather than modifying game memory or files directly.
* Before running, ensure the game window is visible and mining‑zones are accessible so the bot can detect mining nodes and mine them automatically.
* The bot requires administrator permissions (for automation UI control) and may rely on screen position/configuration matching the game’s mining interface.
* While running, the bot continuously checks for mining nodes, executes mining cycles, handles resource cooldowns, and loops based on configuration.
* Use it solely for personal learning/testing in a contained environment; be aware of any potential violation of the game’s Terms of Service.
---
[**f1shyondrugs/BlueProtocol-Autofarm**](https://github.com/f1shyondrugs/BlueProtocol-Autofarm)
* It’s an automated fishing bot for Blue Protocol: Star Resonance that uses computer‑vision to detect bobber movement and simulate fishing actions.
* It detects specific pixel coordinates to identify when a fish bites and then automatically casts, reels, and collects the catch.
* Features include a transparent always‑on‑top GUI overlay, hotkey controls (F1 to pause/resume, F2 to restart), and a fish counter tracking total catches.
* Must run at **1920×1080 resolution** since coordinate and color values are hard‑coded for that resolution only.
* Before starting, install dependencies via `pip install -r requirements.txt`, configure optional Discord webhook for notifications, and run `python fishing.py`.
* Game window must be visible and focused, no overlays or streaming apps interfering, and the bot runs in Administrator mode to properly simulate input.
* The bot monitors colors such as orange for bobber movement, gray for catch detection, and uses key presses (‘A’/’D’) for guiding fish when needed.
* It includes emergency recovery logic: if an unexpected color is detected it resets the process, and users must configure optional Discord webhook and verify screen config.
---
[**rdsp04/bpsr-fishing**](https://github.com/rdsp04/bpsr-fishing)
* It’s a Windows macro script called **BPSR Fishing Macro** for automating fishing in Blue Protocol: Star Resonance.
* You must set your game window to 1920 × 1080 resolution (fullscreen or windowed) before starting.
* The script keeps track of catches, fish types, XP gained and session duration.
* To start, open the game and the macro, then press **F9** to begin fishing and **F10** to stop.
* The player character must be positioned at a fishing spot and have sufficient rods and bait pre‑checked.
* The game window must be visible on the main monitor for the macro to work correctly.
* If the script presses “Exit” instead of “Continue,” restart it and ensure it was launched after the game.
* Recommended supplies: at least 200 baits and 10 rods for each hour of fishing.
---
[**hyuse98/BPSR-Fishing-Bot**](https://github.com/hyuse98/BPSR-Fishing-Bot)
* BPSR Fishing Bot is an automated fishing tool for Blue Protocol: Star Resonance using Python and image detection.
* It detects fishing events, plays the fishing minigame, swaps broken rods, and tracks catches automatically.
* Users control it via hotkeys: F1 to start/pause and F2 to stop the bot.
* Requires the game in windowed mode at 1920x1080 resolution.
* Installation: clone the repository and install Python dependencies with `pip install -r requirements.txt`.
* Run the bot by executing `python main.py` while the game is visible.
* Configuration allows adjusting detection regions, precision, delays, and state timeouts via files in `src/fishbot/config/`.
* The bot uses a Finite State Machine architecture to handle different fishing states, with modular detector and controller modules.
---
