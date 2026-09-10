# Browser Fingerprint Thesis Materials

Materials for the bachelor's thesis:\
Browser Fingerprinting Resistance in 2026: An Empirical Audit Across Seven Browsers\
Comparing Noise Injection, Blocking andStandardisation-Based Defences\
DiVA link: *insert*\
Author: Nour Qassim Derweesh, KTH Royal Institute of Technology, 2026\

## Contents

- 'collect.html' - data-collection tool. Open in any browser to run FingerprintJS across a standardised session protocol.
- 'fp.min.js' - the FingerprintJS v4 open source library (embedded for offline use).
- 'analyse.py' - the python analysis script. Script processes JSON session files and outputs re-identification rates and Shannon entropy per browser.
- 'system_snapshots/' - hardware and software environment documentation.
- 'benchmarks/' - EFF Cover Your Tracks screenshots for all seven browsers in both modes + the JSON files and screenshots from AmIUnique for all seven browsers in both modes.

## Requirements
- Python 3.x with pandas and scipy installed ('pip install pandas scipy')
- Place session JSON files in a 'data/' folder in the same directory as 'analyse.py'

## Raw session data
The 140 collected JSON session files are located in the 'data/' folder.
