# Skill: Database & Migrations Review

Проверка схемы PostgreSQL, SQLAlchemy, миграций Alembic, производительности запросов.

## Что проверяю

- **Схема**: нормализация, типы, NOT NULL/CHECK, FK и ON DELETE, уникальные индексы.
- **Иерархия**: Materialized Path / `ltree`, корректность рекурсивных CTE, перемещение поддерева.
- **Индексы**: под реальные запросы (WHERE/ORDER/JOIN); составные индексы; partial/composite.
- **Async SQLAlchemy 2.0**: `select()`-стиль, отсутствие lazy-load вне сессии, N+1.
- **Транзакции**: Unit of Work, границы, уровень изоляции, обработка deadlock/retry.
- **Миграции**: обратимость, безопасность на проде (expand/contract), блокировки, backfill батчами.
- **pgvector**: тип `vector(N)`, размерность, индекс HNSW/IVFFlat, параметры, метрика.
- **FTS**: `tsvector`, GIN, конфигурация языка, `ts_rank`/`ts_rank_cd`.
- **Пул соединений**: размер, timeout, поведение при исчерпании.

## Красные флаги

- `SELECT *` в горячем пути; отсутствие индекса под частый фильтр.
- Миграция с `ALTER TABLE ... SET NOT NULL` на большой таблице без стратегии.
- Хранение прав доступа так, что фильтрация невозможна до ранжирования.
- Денормализация без плана синхронизации.

## Материал для изучения

- PostgreSQL docs: indexes, EXPLAIN/ANALYZE, CTE, ltree, GIN.
- pgvector README: HNSW vs IVFFlat, ef_search, recall.
- Alembic: batch mode, autogenerate pitfalls, data migrations.
