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
