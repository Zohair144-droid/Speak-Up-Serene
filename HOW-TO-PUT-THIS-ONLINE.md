# Speak Up Serene — installable app

This folder turns your suggestion box into a real app that installs on phones
with the Roots IVY icon. It is free and takes about 10 minutes.

Your Apps Script app does not change at all. This just wraps it.

---

## What you get

- **Install** works on Android instead of failing
- Your **yellow speech-bubble icon** on the home screen
- Opens **full screen**, with no browser bar
- A **short link that never changes**, even when you redeploy

---

## Step 1 — Make a free GitHub account

1. Go to **github.com** and click **Sign up**
2. Use your email, pick a username. Something like `roots-ivy-serene` looks tidy,
   because the username becomes part of your link.
3. Verify the email

## Step 2 — Make a repository

1. Click the **+** at the top right, then **New repository**
2. Repository name: **speakup**
3. Choose **Public**
4. Click **Create repository**

## Step 3 — Upload these files

1. On the new page click **uploading an existing file**
2. Drag in all six files from this folder:
   - index.html
   - manifest.webmanifest
   - sw.js
   - icon-192.png
   - icon-512.png
   - icon-maskable-512.png
3. Click **Commit changes**

Do not upload this instructions file. It does no harm, but it is not needed.

## Step 4 — Turn on GitHub Pages

1. Click **Settings** at the top of the repository
2. Click **Pages** in the left sidebar
3. Under **Branch**, choose **main** and **/ (root)**, then click **Save**
4. Wait about a minute, then refresh. It shows your live address:

   `https://YOUR-USERNAME.github.io/speakup/`

That is your new student link. It never changes.

## Step 5 — Test it

1. Open the link on an Android phone in **Chrome**
2. Tap **⋮ → Add to Home screen**
3. This time **Install** works, and the icon is yours

On iPhone, open it in **Safari**, tap **Share**, then **Add to Home Screen**.
Apple has no Install button, but the icon will be correct.

---

## Your two links from now on

- **Students:** `https://zohair144-droid.github.io/Speak-Up-Serene/`
- **Council:** `https://zohair144-droid.github.io/Speak-Up-Serene/council/`

The two install as separate apps with separate icons: the yellow speech bubble
for students, the navy mountains for the council.

Make a fresh QR code for the student link, or ask Claude for one.

---

## If your Apps Script link ever changes

Change it in **two** files: `index.html` and `council/index.html`.
Click the pencil icon on each and edit this one line:

```js
var APP_URL = "https://script.google.com/macros/s/..../exec";
```

Commit. The GitHub link stays the same, so posters and QR codes keep working.
This is the main reason to use this shell: you never have to reprint anything again.

---

## Troubleshooting

**"Opening Speak Up Serene…" never goes away**
Your Apps Script deployment must allow framing. In Code.gs this line does it,
and it is already there:
`.setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)`
Also check the deployment is set to **Anyone**.

**Install still does not appear**
GitHub Pages can take a few minutes the first time. Make sure the address
starts with `https://`, and try a new tab.

**Icon looks wrong on Android**
Android crops icons into a circle. `icon-maskable-512.png` handles that,
and it is already included.
