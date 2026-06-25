@echo off
title lonesoulsurfer - Update Site
color 0A

echo ============================================
echo   lonesoulsurfer.github.io - Site Updater
echo ============================================
echo.
echo This will scrape your Instructables profile,
echo update projects.json, and push to GitHub.
echo.
echo Press any key to start, or close this window to cancel.
pause > nul

echo.
echo [1/3] Running scraper...
echo.
cd /d "%~dp0"
python3 scraper\scrape.py
if errorlevel 1 (
    echo.
    echo ERROR: Scraper failed. Check your internet connection.
    pause
    exit /b 1
)

echo.
echo [2/3] Committing changes...
echo.
git add projects.json
git diff --cached --quiet
if errorlevel 1 (
    git commit -m "update: scrape %date%"
) else (
    echo No changes detected - your site is already up to date.
    echo.
    pause
    exit /b 0
)

echo.
echo [3/3] Pushing to GitHub...
echo.
git push

echo.
echo ============================================
echo   Done! Your site will update in ~30 seconds.
echo   https://lonesoulsurfer.github.io
echo ============================================
echo.
pause
