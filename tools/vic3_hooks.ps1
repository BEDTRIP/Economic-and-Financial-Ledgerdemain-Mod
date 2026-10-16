<#
Hooks of "E&F: Ledgerdemain" for the game scripts of vic3_tools (bridge/game: run_vic3_sandbox.ps1, vic3_ui.ps1).

The scripts dot-source this file ($env:VIC3_HOOKS, or vic3_hooks.ps1 next to them in the sandbox VM, where
Invoke-SandboxRun.ps1 -HooksDir copies it):
- the fork's debug logs: weekly model lines EFW / EFR / EFX / EFC … gathered into eflog.txt at the end of a run;
- after loading: "event zz_ef_logs.1" switches the logs on (off by the game rule), "zz_ef_logs.2" (-NoModLogs) keeps
  them off as in a normal game;
- a gone country's heir: the world pass logs EFH|<date>|<name>|gone|tag <Tag>, then EFH|…|heir|tag <heir>
  (scripted_effects/ld_subject_metal.txt);
- -Shots / "country <TAG>": the currency tooltip, its account cards and the budget tabs (macros in vic3_ui_points.ps1).
#>

$script:ModLogPattern = ': EF[A-Z]{1,2}\|'
$script:ModLogFile = "eflog.txt"
$script:PointsFile = Join-Path $PSScriptRoot "vic3_ui_points.ps1"

function Hook-AfterLoad($p, $noModLogs) {
    # in a game without the fork the event is unknown -- a harmless console error
    if ($noModLogs) { Console-Cmd $p "event zz_ef_logs.2" } else { Console-Cmd $p "event zz_ef_logs.1" }
    Start-Sleep 2
}

function Hook-FindHeir($tag) {
    $files = @(Get-ChildItem (Join-Path $OutDir "dbgparts") -Filter "*.log" -ErrorAction SilentlyContinue) +
        @(Get-ChildItem $Logs -Filter "debug*.log" -ErrorAction SilentlyContinue)
    $hit = $files | Select-String -Pattern (': EFH\|[^|]*\|[^|]*\|gone\|tag ' + $tag + '\s*$') -Context 0, 5 `
        -ErrorAction SilentlyContinue | Select-Object -Last 1
    if (-not $hit) { return $null }
    foreach ($l in $hit.Context.PostContext) {
        if ($l -match ': EFH\|[^|]*\|([^|]*)\|heir\|tag (\S+)') { return @($Matches[2], $Matches[1]) }
    }
    return $null
}

function Hook-ShotSteps($own) {
    return "macro currency $own; macro cards $own; macro budget $own"
}

# The points of vic3_tools are measured on a 2560x1440 window; the game's interface keeps its size in pixels, so in a
# smaller window it takes a bigger share of it: an anchored point moves by GUI.scale x 1440 / the window's height
# (1920x1080 at GUI.scale 1 -- the lobby as 2560x1440 at 1.3). Overrides Scale-Px of vic3_ui_lib.ps1; at 1440 -- as
# there.
# The console is a tool (tools_gui_scale, not GUI.scale): its boxes are measured at 2560x1440 from the top left and move
# by 1440 / the window's height only (anchor "tlT").
if ($Screens -and $Screens["console"]) { $Screens["console"].anchor = "tlT"; $Screens["console"].anchor2 = "tlT" }
function Scale-Px($x, $y, $anchor) {
    $s = if ($anchor -match 'T') { 1.0 } else { $script:UiScale }
    $g = Get-Process -Name "victoria3" -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($g -and $g.MainWindowHandle -ne [IntPtr]::Zero) {
        $r = New-Object W+RECT
        [W]::GetWindowRect($g.MainWindowHandle, [ref]$r) | Out-Null
        $h = $r.B - $r.T
        if ($h -gt 200) { $s = $s * 1440 / $h }
    }
    if (-not $anchor -or [math]::Abs($s - 1.0) -lt 0.001) { return @($x, $y) }
    $ax = if ($anchor -match 'r') { 2560 } elseif ($anchor -match 'l') { 0 } else { 1280 }
    $ay = if ($anchor -match 'b') { 1440 } elseif ($anchor -match 't') { 0 } else { 720 }
    return @(($ax + ($x - $ax) * $s), ($ay + ($y - $ay) * $s))
}
