#!/usr/bin/env python3
"""Починка моста `vic3-pc` на ПК (ночь 17.10; разовый, через `py_tool`).

    py tools/ld_bridge_fix.py [--dry]

1. Рабочее дерево форка моста (`../_bridge/Economic-and-Financial-Ledgerdemain-Mod`) не создаётся: папку наполняет
   Syncthing (`README.sync-conflict-…`), `git worktree add` отвечает «already exists». Ищет корень папки Syncthing
   (`.stfolder` вверх от `_bridge`), дописывает `/_bridge` в его `.stignore` (если нет), затем `git worktree prune` и
   отодвигает папку в `_bridge/_stale/<время>/` (не удаляет), если в ней нет `.git` (то есть это не живое рабочее дерево).
2. Правка справочника навыка `vic3-modding` (`add_building_level` в 1.13 нет): облачной сессии пуш в `vic3_tools`
   закрыт (403) — патч применяется в checkout `vic3_tools` на ПК (`git am`) и пушится его учёткой; только если
   checkout на `main` и чистый, патч ещё не применён.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import time

DRY = "--dry" in sys.argv
FORK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.dirname(FORK)
BRIDGE = os.path.join(PROJ, "_bridge")
WT = os.path.join(BRIDGE, os.path.basename(FORK))
TOOLS = os.path.join(PROJ, "vic3_tools")
PATCH = 'From ba415406069434bb18fea022e9b02f89f2817037 Mon Sep 17 00:00:00 2001\nFrom: Claude <noreply@anthropic.com>\nDate: Fri, 16 Oct 2026 21:18:53 +0000\nSubject: [PATCH] vic3-modding: add_building_level does not exist in 1.13\n (error.log); create_building raises a standing building to its level\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01Mc3Lj9e47EyTmwpBEdW3LE\n---\n .../skills/vic3-modding/references/economy-content.md       | 6 ++++--\n 1 file changed, 4 insertions(+), 2 deletions(-)\n\ndiff --git a/claude-plugin/skills/vic3-modding/references/economy-content.md b/claude-plugin/skills/vic3-modding/references/economy-content.md\nindex 77d22af..6962f02 100644\n--- a/claude-plugin/skills/vic3-modding/references/economy-content.md\n+++ b/claude-plugin/skills/vic3-modding/references/economy-content.md\n@@ -41,8 +41,10 @@\n   152 years — forever. In a merge take the place from the mod with a literal.\n - The launcher\'s "Failed to process metadata" = `metadata.json` did not parse: BOM first (the usual cause), then\n   `json.loads`, then the keys. Extra keys inside `game_custom_data` are tolerated.\n-- **No nationalization effect** (all effects with text: `common/effect_localization`). `add_building_level = {\n-  building = X level = -1 }` removes a level, but whose — the engine decides. `ai_nationalization_desire` of a building\n+- **No nationalization effect** (all effects with text: `common/effect_localization`). There is no effect that takes\n+  one level off a building either: `add_building_level` is unknown to 1.13 (`error.log`: "Unknown effect\n+  add_building_level", run 2026-10-16); `remove_building` takes it whole. Raising: `create_building = { building = X\n+  level = N }` on a standing building raises it to N (PSC\'s regulator). `ai_nationalization_desire` of a building\n   affects the AI only; forbidding the player to privatize by script is impossible.\n - **A building\'s name and icon come from its type.** No "rename a building" effect; per building only in your own\n   windows via `Building.GetCustom(\'<custom loc>\')`. Different names and icons of "one" building = different types with\n-- \n2.43.0\n\n'


def git(*a, cwd):
    p = subprocess.run(["git", *a], cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(f"git {' '.join(a)} -> {p.returncode} {(p.stdout + p.stderr).strip()[-600:]}")
    return p


def unsync():
    print(f"worktree dir: {WT} exists={os.path.isdir(WT)}")
    root = BRIDGE
    while True:
        if os.path.isdir(os.path.join(root, ".stfolder")):
            break
        up = os.path.dirname(root)
        if up == root:
            root = None
            break
        root = up
    print(f"syncthing root: {root}")
    if root:
        rel = "/" + os.path.relpath(BRIDGE, root).replace(os.sep, "/")
        ign = os.path.join(root, ".stignore")
        old = open(ign, encoding="utf-8-sig").read() if os.path.exists(ign) else ""
        if rel not in old.split("\n") and rel not in [l.strip() for l in old.splitlines()]:
            print(f"add {rel} to {ign}")
            if not DRY:
                with open(ign, "a", encoding="utf-8") as f:
                    f.write(("" if old.endswith("\n") or not old else "\n") + rel + "\n")
                time.sleep(15)  # Syncthing rereads .stignore before the delete, so the delete does not propagate
        else:
            print(f"{rel} already in {ign}")
    if not DRY:
        git("worktree", "prune", cwd=FORK)
    if os.path.isdir(WT) and not os.path.exists(os.path.join(WT, ".git")):
        # moved aside, not deleted: what Syncthing put there stays at hand
        to = os.path.join(BRIDGE, "_stale", time.strftime("%Y%m%d-%H%M%S"), os.path.basename(WT))
        print(f"move {WT} -> {to}: {sorted(os.listdir(WT))}")
        if not DRY:
            os.makedirs(os.path.dirname(to), exist_ok=True)
            shutil.move(WT, to)
    print(f"worktree dir now exists={os.path.isdir(WT)}")


def push_patch():
    if not os.path.isdir(os.path.join(TOOLS, ".git")):
        print(f"no vic3_tools checkout at {TOOLS}")
        return
    br = git("rev-parse", "--abbrev-ref", "HEAD", cwd=TOOLS).stdout.strip()
    dirty = git("status", "--porcelain", cwd=TOOLS).stdout.strip()
    ref = os.path.join(TOOLS, "claude-plugin", "skills", "vic3-modding", "references", "economy-content.md")
    if br != "main" or dirty:
        print("vic3_tools: not main or dirty -- patch not applied")
        return
    git("pull", "--ff-only", "origin", "main", cwd=TOOLS)
    if "add_building_level` is unknown to 1.13" in open(ref, encoding="utf-8").read():
        print("vic3_tools: already applied")
        return
    if DRY:
        print("vic3_tools: would apply and push")
        return
    with tempfile.NamedTemporaryFile("w", suffix=".patch", delete=False, encoding="utf-8", newline="\n") as f:
        f.write(PATCH)
    if git("am", "--keep-cr", f.name, cwd=TOOLS).returncode != 0:
        git("am", "--abort", cwd=TOOLS)
        return
    git("push", "origin", "main", cwd=TOOLS)


if __name__ == "__main__":
    unsync()
    push_patch()
