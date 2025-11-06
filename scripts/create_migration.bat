@echo off
REM Скрипт для создания новой миграции

if "%1"=="" (
    echo Usage: create_migration.bat "migration message"
    exit /b 1
)

docker compose run --rm migration alembic revision --autogenerate -m "%1"
if %errorlevel% equ 0 (
    echo Migrations created successfully!
) else (
    echo Failed to create migrations!
)
pause