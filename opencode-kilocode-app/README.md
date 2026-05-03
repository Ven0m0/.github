# Opencode Kilocode Jules App

This repository contains the configuration for a custom GitHub App designed to work with **Claude Code**, **OpenCode**, **Kilocode**, and **Jules**.

## Setup Instructions

1. **Create the GitHub App:**
   - Go to [GitHub App Settings](https://github.com/settings/apps/new).
   - Scroll down to "Create from manifest".
   - Paste the contents of `manifest.json` from this repository.
   - Click "Create GitHub App".

2. **Configure Private Key:**
   - In your new app's settings, scroll down to the "Private keys" section.
   - Click "Generate a private key".
   - Download the `.pem` file. **Keep it secure!**

3. **Install the App:**
   - Go to the "Install App" section in the sidebar.
   - Click "Install" next to your account or organization.
   - Select the repositories you want to enable the app for.

4. **Add Secrets to your Target Repository:**
   - Go to the repository where you want to use the app.
   - Go to **Settings > Secrets and variables > Actions**.
   - Add the following secrets:
     - `GITHUB_TOKEN`: A GitHub PAT (optional, `secrets.GITHUB_TOKEN` is used by default).
     - `ANTHROPIC_API_KEY`: Required for Claude provider.
     - `OPENCODE_API_KEY`: Required for OpenCode provider.
     - `KILO_API_KEY`: Required for Kilocode provider.
     - `JULES_API_KEY`: Required for Jules provider.

5. **Triggering the AI:**
   - Mention `@claude` in an issue or PR comment to trigger Claude.
   - Mention `/opencode` in a comment to trigger OpenCode.
   - Mention `/kilo` in a comment to trigger Kilocode.
   - Use the **Actions** tab to manually trigger a workflow with a custom provider and prompt.

## Required Permissions

The app is pre-configured with:

- **Contents**: Read & Write
- **Issues**: Read & Write
- **Pull Requests**: Read & Write
- **Actions**: Read
- **Metadata**: Read
