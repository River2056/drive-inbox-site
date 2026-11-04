# Drive Inbox — unpublished static-site draft

Files: index.html, privacy.html, terms.html, styles.css. No build step, JavaScript, remote fonts, analytics, or dependencies.

## Preview
From this directory run:

    python3 -m http.server 8080 --bind 127.0.0.1

On another device, forward the port over SSH rather than exposing the server publicly. For example, on your own computer:

    ssh -N -L 8080:127.0.0.1:8080 YOUR_EXISTING_SSH_TARGET

Then open http://localhost:8080 on that computer. Replace the SSH target with the host/account you already use.

## Before publishing
- Choose the final app name. Drive Inbox is a proposed name; match it exactly in Google Branding.
- Replace the support email placeholder on all three pages with an address you monitor.
- Confirm the operator identity, all privacy statements, and all downstream processing. In particular, this destination is separately synced through Obsidian Sync. Do not claim files never leave the server.
- Identify the actual hosting provider and link its privacy policy on privacy.html.
- Confirm retention, backups, permissions, and synchronization settings. The draft does not promise a fixed retention period or encryption configuration.
- Add an accurate publication/revision date after approval.
- Remove the draft banner and revise draft-only text on the privacy and terms pages after review. A banner alone is not the only draft marker.
- Host only the four public site files. Do not publish this README, validation script, importer, credentials, checkpoint, logs, or notes.
- Verify public HTTPS URLs and all links, and complete domain checks if Google requests them.
- Enter the homepage and privacy-policy URLs in Google Branding, then try publishing the OAuth app.
- This website does not guarantee Google approval or remove other requirements Google may apply.

## Content basis
Reviewed the existing daily_tech_posts_import.py without reading credentials or private Drive content. It uses drive.readonly; lists files and changes; exports/downloads content; uses local MarkItDown with plugins disabled; saves Markdown and progress; and prints file metadata in run output. Source filenames can collide at the destination. The destination's separate Obsidian Sync setup was previously established in this environment and should be rechecked before launch.

## Check
    python3 validate.py

This checks static structure and local asset links, not visual rendering, policy completeness, or Google acceptance.
