### Quiz project

Для развертывания выполните
```bash
    docker compose up
```

Для остановки и полной очистки выполните
```bash
    docker compose down --remove-orphans -v
```

--- 

Полезные скрипты хранятся в директории `scripts`

 -  Создание новой миграции linux:
```bash
    source ./scripts/create_migration.sh
```

- Создание новой миграции windows:
```bash
    .\scripts\create_migration.bat
```
---

[Открыть quiz](http://localhost:8000)

[Открыть adminer](http://localhost:8080)
