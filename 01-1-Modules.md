

### **asgharkapk/star-resonance-module-optimizer**
👉 **[https://asgharkapk.github.io/star-resonance-module-optimizer/](https://asgharkapk.github.io/star-resonance-module-optimizer/)**
* Browser-only **React module optimizer** for *Blue Protocol*.
* CSV import + live editable module table.
* Role presets (DPS/Healer/Tank/Support) + Maxroll builds.
* Shows icons, color-coded levels, stat toggles.
* Generates all 4-module combinations.
* Supports **10 ranking modes**: total, highest, ability score, target level, smart, weighted, balanced, spike, efficiency, synergy.
* Exports CSV (input + results).
* No backend. Pure client-side.

---

### **asgharkapk/star-resonance-module-optimizer — converter tool**
👉 **[https://asgharkapk.github.io/star-resonance-module-optimizer/converter.html](https://asgharkapk.github.io/star-resonance-module-optimizer/converter.html)**
* Web-based log → CSV converter.
* Parses `.log` / `.txt` exported by StarResonanceAutoMod.
* Auto-names modules (X1, X2, …).
* Dark/light theme toggle.
* Drag/drop or paste log text.
* Download CSV result.
* Works offline, browser only.

---


### **HuaChunOXO/StarResonanceModuleSolver**
* [https://github.com/HuaChunOXO/StarResonanceModuleSolver](https://github.com/HuaChunOXO/StarResonanceModuleSolver)
* Modified continuation of **StarResonanceAutoMod**, originally derived from **StarResonanceDamageCounter**.
* Uses **AGPL-3.0 license** due to inheritance from previous projects.
* Captures in-game module data via Npcap and enumerates/optimizes module sets.
* Steps: install Npcap → run `模组求解器.exe` → start capture → change maps/channels to feed data → stop capture → set target/excluded attributes → view Target Requirement Plan & Profession Attribute Plan → export to Word.
* Helps players discover optimal module combinations.

---

### **fudiyangjin/StarResonanceAutoMod**
* [https://github.com/fudiyangjin/StarResonanceAutoMod](https://github.com/fudiyangjin/StarResonanceAutoMod)
* Captures live packets from *Star Resonance* to extract modules.
* Has CPU and GPU acceleration (CUDA/OpenCL).
* Optimizes four-module combinations with target/excluded attributes.
* Requires Npcap; works on Windows 10/11.
* Usage:
  `.\StarResonanceAutoMod.exe -a -lang en` — live capture
  `.\StarResonanceAutoMod.exe -lv -lang en` — offline analysis
* Developers can build Python + C++ extension version.

---

### **fishing-dev-sm/bpsr_automodule**
* [https://github.com/fishing-dev-sm/bpsr_automodule](https://github.com/fishing-dev-sm/bpsr_automodule)
* OCR-based optimizer for *BPSR* using Python + Flask + OpenCV.
* Has CLI version and Web-UI at `localhost:5000`.
* Features: intelligent OCR, attribute matching, module combination optimization, JSON export, config files for screen/ROI tuning.
* Provides threshold-based filtering & multi-objective combo scoring.
* Installation includes scripts for Windows, Linux, macOS.
* Note: OCR + automation may conflict with some games’ ToS.
* Web UI with drag-and-drop screenshots and live recognition.
* Real-time visualizer for best module combos.
* Cross-platform support, one-click setup, JSON export.
* Multi-strategy OCR + multi-objective filtering.

---

### **mrsnakke/BPSR-AutoModules**
* [https://github.com/mrsnakke/BPSR-AutoModules](https://github.com/mrsnakke/BPSR-AutoModules)
* GUI application for capturing & analyzing BPSR modules.
* Captures module data automatically from the game.
* Filters: module type (Attack/Guard/Support/All), attribute filters, presets for classes, attribute distribution (Lv5/Lv6).
* Refilter instantly without new capture.
* Shows detailed panels: module images, rarity, attributes, combo score, total distribution, combat power.
* Built-in console view.
![Application Screenshot](https://github.com/mrsnakke/gachaIMG/blob/main/imagen_2025-11-06_182613541.png?raw=true)

---

### **MessyMeshi/BPSR-AutoModules**
* [https://github.com/MessyMeshi/BPSR-AutoModules](https://github.com/MessyMeshi/BPSR-AutoModules)
* Another GUI tool similar to the above, focused on module capture and optimization.
* Attribute filtering & class presets included.
* Re-screen (refilter) without new capture.
* Shows combination fitness scores, module cards, attribute totals, estimated combat power.
* Integrated console panel for logs.
![Application Screenshot](https://github.com/mrsnakke/gachaIMG/blob/main/1%20(2).png?raw=true)

---


Just tell me.
