# Reaction Tester

This is a small browser project with reaction tests, typing drills, memory tasks, and a few aim-training modes.

It started as a simple reaction timer and gradually turned into a single-page practice board with different kinds of short tests. The main live file is `index.html`.

## Live Version

https://zhirkoalexander-maker.github.io/reactiontester/

## What Is Inside

The current build includes these groups of modes:

- Reaction: Classic, Focus
- Typing: Chat, Typing
- Memory / Skill: Visual, Mental, Memory
- Special: Speed, Colors
- Shooter training: Tracking, Target Burst, Micro Adjust, Target Switch

Most modes have 3 difficulty levels. Each run gives 3 attempts, and scores are saved in local storage.

## Running Locally

The project does not need a build step.

You can open `index.html` directly in a browser, or run a simple local server:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Project Notes

- Main file: `index.html`
- The repository is intentionally kept small now, with the current site centered around `index.html`
- Stats are stored in the browser with `localStorage`
- The project is plain HTML, CSS, and JavaScript with no framework

## Why This Exists

Mostly to make something hands-on instead of another throwaway demo. It is a place to test interaction ideas, timing, small game loops, and UI changes without a lot of setup.

## Author

Made by [zhirkoalexander-maker](https://github.com/zhirkoalexander-maker).
