# Skill: CI/CD & Deployment Review

Проверка пайплайнов, образов, миграций в проде, релиза.

## Что проверяю

- **CI**: линт, типы, тесты, миграции — на каждый PR; fail fast; кэш.
- **Testcontainers**: реальные зависимости поднимаются в CI.
- **Docker**: multi-stage, маленький образ, distroless/alpine, non-root, healthcheck.
- **Миграции в прод**: expand/contract, обратная совместимость, zero-downtime.
- **Релиз**: версии/теги образов, rollback-стратегия, canary/blue-green (если есть).
- **Секреты в CI**: через secrets, не в логах.
- **Стенды**: dev/stage/prod, конфиг через env.

## Красные флаги

- Миграция ломает текущую версию приложения (деплой уперся в несовместимость).
- Образ `latest` без тега/дайджеста.
- Контейнер под root, без healthcheck.
- Тесты только локально, CI их не гоняет.

## Материал для изучения

- Expand/contract migrations; zero-downtime deployment.
- Docker multi-stage + distroless; hadolint.
- GitHub Actions: matrix, caching, reusable workflows.
