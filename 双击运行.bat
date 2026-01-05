@echo off
echo 正在同步最新 Skill 和 Prompt...
git pull
echo.
echo 同步完成！正在启动 AI 引擎...
python main.py
pause