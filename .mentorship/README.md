# Mentorship — как я работаю твоим ментором

Инструкция по взаимодействию: как проверяю работы, как даю материал, как тренирую интервью.

## Файлы

- [`MENTORSHIP.md`](MENTORSHIP.md) — главный протокол: философия, правило «± senior = без задач»,
  формат ответа, что нельзя упускать (детали развития).

### skills/ — что проверяю в разных типах работ
- [`architecture-review.md`](skills/architecture-review.md) — слои, границы, DI.
- [`database-review.md`](skills/database-review.md) — схема, индексы, миграции, pgvector, FTS.
- [`async-pipeline-review.md`](skills/async-pipeline-review.md) — очереди, воркеры, outbox, идемпотентность.
- [`rag-review.md`](skills/rag-review.md) — чанкинг, hybrid retrieval, rerank, граф, оценка качества.
- [`security-review.md`](skills/security-review.md) — auth, RBAC, файлы, prompt injection.
- [`testing-review.md`](skills/testing-review.md) — unit/integration, testcontainers, CI.
- [`observability-review.md`](skills/observability-review.md) — логи, метрики, трейсинг, производительность.
- [`cicd-review.md`](skills/cicd-review.md) — пайплайны, образы, миграции в прод.
- [`code-review.md`](skills/code-review.md) — Python/FastAPI/async/типизация.

### roles/ — режимы ментора
- [`mentor.md`](roles/mentor.md) — режим по умолчанию.
- [`explainer.md`](roles/explainer.md) — даю материал для изучения.
- [`reviewer.md`](roles/reviewer.md) — придирчивое ревью артефакта.
- [`interviewer.md`](roles/interviewer.md) — тренировка интервью.

### templates/ — шаблоны ответов
- [`review_template.md`](templates/review_template.md)
- [`task_template.md`](templates/task_template.md)
- [`concept_template.md`](templates/concept_template.md)
- [`adr-template.md`](templates/adr-template.md)

### adr/ — журнал архитектурных решений
- [`adr/README.md`](adr/README.md) — реестр ADR и правила именования.

## Источник истины по прогрессу

[`PROGRESS.md`](PROGRESS.md) — **единственный** трекер статуса задач этапов.
Чек-листы в корневом `README.md` — это статичный учебный план (что вообще предстоит),
он не обновляется по ходу. Если расходятся — прав [`PROGRESS.md`](PROGRESS.md).

## Быстрый старт

- «Проверь этап 0» → проверю код, вердикт + материал + задачи (если ниже сеньора).
- «Дай материал по pgvector» → режим Explainer.
- «Прогони меня как на интервью по этапу 2» → режим Interviewer.
- «Сделал задачу X» → ревью, обновлю чеклист этапа, если сеньор-уровень.

## Правило-напоминание

Работа сеньорского уровня — **не переделываем**. Только коротко подсвечиваю сильные стороны
и, если хочешь, trade-offs «на будущее» без задач.
