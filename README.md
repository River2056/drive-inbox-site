# Drive Inbox website

Public information site for River's personal, read-only Google Drive-to-Markdown importer.

Site: https://river2056.github.io/drive-inbox-site/
Contact: chen0625tung@gmail.com
Policy effective date: November 4, 2026

## Files

- index.html: purpose, workflow, read-only access, operator, and contact.
- privacy.html: data access, storage, retention, sharing, deletion, and GitHub Pages hosting.
- terms.html: personal-use terms and limitations.
- styles.css: responsive styles; no JavaScript, remote fonts, or analytics.
- validate.py: static-structure, contact, policy completeness markers, and local HTTP tests.
- _config.yml: excludes development files from the branch-based GitHub Pages site.

## Preview and test

    python3 validate.py
    python3 -m http.server 8080 --bind 127.0.0.1

For a headless server, use your usual SSH host from your own computer:

    ssh -N -L 8080:127.0.0.1:8080 YOUR_EXISTING_SSH_TARGET

Then visit http://localhost:8080. Do not expose the preview server publicly.

## Deployment

GitHub Pages publishes master / (root). Commit and push updates, then verify the actual public pages after deployment. A successful Git push alone does not prove that the site has been deployed.

Never add credentials, Drive contents, checkpoints, importer state, or logs to this repository. Excluding files from the Pages site does not hide them from the public Git repository.

## OAuth console

Use Drive Inbox as the consistent app name and the published homepage and privacy-policy URLs in Google Branding. App publishing, app verification, and domain ownership verification are separate. The site does not guarantee Google approval; follow any domain ownership requirements shown by Google. Changing publishing status does not revive a rejected refresh token. Reauthorize the exact importer credential afterward and preserve the existing checkpoint.

## Maintenance

Keep the policies aligned with the actual importer, downstream Obsidian Sync configuration, and backup practices. Update the effective dates and validation expectations when policy wording changes. Tests do not establish legal compliance, visual quality, domain ownership, or Google acceptance.
