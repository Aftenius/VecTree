# VecTree — мультимодальная база знаний с Graph-RAG

VecTree — backend-система управления знаниями: документы, папки, теги и ссылки.
Загруженные файлы превращаются в связанный смысловой граф, а ответы на вопросы по базе
строятся через гибридный поиск (BM25 + vector + rerank) и обход графа (Graph-RAG).

## Стек

Python 3.14+, FastAPI, Pydantic v2, Dishka, SQLAlchemy 2.0 (asyncpg), PostgreSQL + pgvector,
Redis, MinIO (S3), RabbitMQ / Redis Streams, Taskiq/Celery/ARQ, LlamaIndex/LangGraph,
Neo4j/NetworkX, Docker, GitHub Actions, OpenTelemetry, Prometheus, Grafana, Ragas/TruLens.

---

## Этапы и задачи

### Этап 0. Каркас и инструменты

- [ ] Инициализация проекта: `pyproject.toml` (uv), группы зависимостей (dev/test), Python 3.14+.
- [ ] Структура каталогов: Clean Architecture (domain / application / infrastructure / presentation).
- [ ] Инструменты качества: Ruff (lint + format), mypy `--strict`, pre-commit hooks.
- [ ] Логирование: structlog / stdlib JSON-логи, correlation/request-id.
- [ ] Базовый pytest: конфигурация, первый smoke-тест.

### Этап 1. Домен на чистом Python (ООП + SOLID/DRY/KISS)

- [ ] Сущности и value objects: Workspace, Folder, Document, Tag, внешние ссылки.
- [ ] Агрегаты, инварианты домена; доменные исключения и типы ошибок.
- [ ] Порты (Protocol/ABC): репозитории и сервисы без привязки к инфраструктуре.
- [ ] Иерархия папок: Materialized Path как чистая логика (без SQL).
- [ ] Доменные сервисы: перемещение поддерева, теги, права.
- [ ] In-memory реализации репозиториев (dict).
- [ ] Unit-тесты домена (pytest): инварианты и краевые случаи.

### Этап 2. Асинхронность на чистом Python

- [ ] Основы asyncio: event loop, корутины, `asyncio.gather` / `TaskGroup`.
- [ ] Отмена задач, таймауты (`asyncio.timeout`), обработка исключений.
- [ ] Асинхронные контекст-менеджеры и async-итераторы.
- [ ] Перевод портов и репозиториев на async.
- [ ] CPU-bound операции через `run_in_executor` / process pool.
- [ ] Async-тесты (pytest-asyncio), корректный loop scope.

### Этап 3. Локальный стек в Docker + конфигурация

- [ ] docker-compose: PostgreSQL (+pgvector), Redis, MinIO.
- [ ] Multi-stage Dockerfile для приложения.
- [ ] Healthchecks (liveness/readiness) для сервисов.
- [ ] Конфигурация: Pydantic Settings, `.env`, профили dev/test/prod.

### Этап 4. Персистентность: PostgreSQL + SQLAlchemy 2.0 + Alembic

- [ ] SQLAlchemy 2.0 (asyncpg): модели, отношения.
- [ ] Alembic: инициализация, обратимые миграции.
- [ ] Репозитории поверх Unit of Work; без lazy-load вне сессии, без N+1.
- [ ] Иерархия папок в БД: `ltree`/Materialized Path, рекурсивные CTE (дерево, поддерево, перемещение).
- [ ] Индексы под реальные запросы; пул соединений и таймауты.
- [ ] Интеграционные тесты на testcontainers (Postgres).

### Этап 5. HTTP-слой: FastAPI

- [ ] FastAPI: маршруты, Pydantic v2 схемы.
- [ ] DI-контейнер (Dishka): настройки, сессии БД, репозитории.
- [ ] Middleware: request-id, обработка исключений, единый формат ошибок (RFC 7807).
- [ ] CRUD-эндпоинты документов/папок/тегов: пагинация, фильтры, сортировки.
- [ ] API-тесты (httpx/ASGI).

### Этап 6. Аутентификация и авторизация

- [ ] JWT: access/refresh, ротация refresh-токенов.
- [ ] Argon2-хеширование паролей.
- [ ] RBAC (owner/editor/viewer) на уровне workspace; проверка на каждом доступе.
- [ ] Тесты auth/RBAC.

### Этап 7. Файлы: MinIO/S3

- [ ] MinIO, presigned URL на загрузку/скачивание минуя backend.
- [ ] Валидация файлов: MIME-типы, ограничение размера, безопасные метаданные.
- [ ] Checksum (SHA-256).

### Этап 8. CI

- [ ] GitHub Actions: lint + type-check + unit-тесты на каждый PR.
- [ ] Прогон миграций и интеграционных тестов (testcontainers: Postgres, Redis, MinIO).
- [ ] Кэш зависимостей, артефакты логов.

### Этап 9. Асинхронный пайплайн обработки документов

- [ ] Брокер: RabbitMQ / Redis Streams; выбор воркера (Taskiq/Celery/ARQ), обоснование.
- [ ] Transactional Outbox: гарантия доставки задач при коммите транзакции в БД.
- [ ] Пайплайн парсинга: PDF, DOCX, Markdown, Web Scraping; retries, exponential backoff, DLX/DLQ.
- [ ] Идемпотентность воркеров: idempotency-ключи, повторная обработка без дублей.
- [ ] Стратегии чанкинга: наивный (токены) vs семантический (заголовки/абзацы) vs Parent-Document.
- [ ] Эмбеддинги: provider-абстракция, батчинг, локальная модель vs внешний API.

### Этап 10. Гибридный поиск и RAG

- [ ] pgvector: схема, индексы HNSW/IVFFlat, метрика расстояния, tuning (m, ef_construction).
- [ ] Полнотекстовый поиск PostgreSQL: `tsvector`, GIN-индекс, BM25-подобный ранкинг.
- [ ] Гибридный поиск: объединение BM25 + dense через Reciprocal Rank Fusion (RRF).
- [ ] Реранкинг: Cross-Encoder поверх топ-K кандидатов.
- [ ] Streaming-ответ: Server-Sent Events (SSE) для токенов LLM.
- [ ] API-эндпоинт `/ask`: retrieval → сборка промпта → генерация → стриминг.

### Этап 11. Graph-RAG и семантическое дерево

- [ ] NER + извлечение триплетов (subject–predicate–object) из документов.
- [ ] Схема графа: узлы (сущности/документы), рёбра (отношения), provenance (источник-документ).
- [ ] Хранилище графа: Neo4j (prod-путь) и/или NetworkX (прототип); абстракция графового репозитория.
- [ ] Разрешение сущностей (entity resolution / dedup узлов) и нормализация.
- [ ] Комбинированный retrieval: векторный поиск даёт стартовые узлы → обход графа 1–2 порядка.
- [ ] Контроль галлюцинаций связей: порог уверенности, provenance обязателен.
- [ ] Семантическое дерево/кластеризация документов поверх графа.
- [ ] API: эндпоинты навигации по графу (соседи узла, путь, подграф).
- [ ] Тесты графовых запросов на testcontainers (Neo4j).

### Этап 12. Надёжность, масштаб, наблюдаемость

- [ ] RBAC в векторном поиске: pre-filtering прав доступа на уровне SQL/индекса (нельзя найти чужое).
- [ ] Consistency разнородных хранилищ: distributed cleanup (Postgres ↔ MinIO ↔ pgvector ↔ graph).
- [ ] SAGA / compensations для multi-step операций; обработка частичных сбоев.
- [ ] Semantic Cache в Redis: кэш семантически похожих запросов + дедупликация.
- [ ] Стоимость/задержки LLM: динамический размер контекста, локальные модели для NER/эмбеддингов.
- [ ] Rate limiting, backpressure, ограничение RPS на дорогие эндпоинты.
- [ ] OpenTelemetry: сквозной трейсинг (endpoint → БД → LLM), спаны на ключевых операциях.
- [ ] Метрики Prometheus + дашборды Grafana: TTFT, RPS, p95/p99, расход токенов, cache hit-rate.
- [ ] RAG Evaluation: Ragas/TruLens (Faithfulness, Answer Relevance, Context Recall/Precision);
      регрессионный прогон при изменении промптов/чанкинга.
- [ ] Нагрузочное тестирование (locust/k6): профилирование узких мест, бюджет задержек.
- [ ] Миграции без даунтайма (expand/contract), zero-downtime деплой.
- [ ] Production-образы: distroless/alpine, non-root, healthchecks (liveness/readiness).

---

## Статус

Легенда: `[ ]` — не начато, `[~]` — в работе, `[x]` — готово.

| Этап | Статус |
|---|---|
| 0. Каркас и инструменты | `[ ]` |
| 1. Домен на чистом Python | `[ ]` |
| 2. Асинхронность на чистом Python | `[ ]` |
| 3. Локальный стек в Docker + конфигурация | `[ ]` |
| 4. Персистентность (PostgreSQL + SQLAlchemy + Alembic) | `[ ]` |
| 5. HTTP-слой (FastAPI) | `[ ]` |
| 6. Аутентификация и авторизация | `[ ]` |
| 7. Файлы (MinIO/S3) | `[ ]` |
| 8. CI | `[ ]` |
| 9. Асинхронный пайплайн | `[ ]` |
| 10. Гибридный поиск и RAG | `[ ]` |
| 11. Graph-RAG и семантическое дерево | `[ ]` |
| 12. Надёжность, масштаб, наблюдаемость | `[ ]` |

## Что сделано

- Репозиторий инициализирован: `pyproject.toml`, `main.py`, `.gitignore`, `.python-version`.
