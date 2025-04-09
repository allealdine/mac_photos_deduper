
# 📸 macOS Photos Deduper

A Python tool to automatically delete duplicate photos and videos from the macOS Photos Library — using native Apple APIs via `pyobjc`. No risky hacks. No paid apps. Just clean results.

---

## ✨ Features

- ✅ Scans your **Photos Library** using macOS-native APIs
- ✅ Finds **duplicate media by filename**
- ✅ Keeps the **oldest version** and deletes the rest
- ✅ Uses Apple's official `Photos.framework` for safe deletion
- ✅ Works entirely offline — no export or cloud syncing needed

---

## 🔧 Requirements

- macOS Ventura or later  
- Python 3.8+  
- [pyobjc](https://pypi.org/project/pyobjc/) (installed via `pip`)  
- **Full Disk Access** & **Photos Access** granted to your terminal/IDE

---

## 📦 Installation

1. **Install pyobjc**:
    ```bash
    pip install pyobjc
    ```

2. **Give Permissions**:  
   - Go to **System Settings > Privacy & Security > Full Disk Access**
   - Add your terminal (e.g. Terminal, iTerm, VS Code)
   - Also enable access under **Photos**

---

## 🚀 Usage

> ⚠️ Close the Photos app before running for best results.

```bash
python mac_photos_deduper.py
```

The script will:

- Scan your entire Photos Library
- Identify duplicates (by filename)
- Keep the oldest, and ask for confirmation before deleting the rest

Example output:

```
Found 38 duplicate files.

Are you sure you want to delete them? (yes/no): yes
Duplicates deleted.
```

---

## ❓ How It Works

This script uses the macOS `Photos.framework` via `pyobjc`:

- Fetches all media (`PHAsset`) from the library
- Groups them by original filename
- Within each group, keeps the photo with the earliest `creationDate`
- Deletes the newer duplicates using `PHPhotoLibrary.performChangesAndWait_`

All changes are safe and handled through the official Apple API.

---

## 🛡️ Safety Disclaimer

- Deleted items go to **Recently Deleted**, where they remain for 30 days
- **DO NOT** attempt to manually delete from the `.photoslibrary` package — this can corrupt your library
- This tool **does not modify** media files directly

---

## 🧠 Future Improvements

- [ ] Dry-run mode (preview only)
- [ ] Visual deduplication using image hashes
- [ ] UI front-end (native or web)
- [ ] CLI options (`--only-images`, `--only-videos`, `--export-instead-of-delete`)

---

## 🙌 Author

Built by Alle Aldine — because Photos.app needed a smarter cleanup button.

Medium blog post: [Coming soon]

---

## 🧡 Contributions Welcome

If you’ve got improvements, ideas, or bug reports — PRs and issues are always welcome.

---

## 📜 License

MIT License – do what you want, just don't blame me if you accidentally delete your favorite cat photo 🐱
