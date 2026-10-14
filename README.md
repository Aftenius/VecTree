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

### Этап 0. Фундамент проекта

Рабочий каркас проекта.

- [ ] Инициализация проекта: `pyproject.toml` (uv/poetry), зависимости по группам (dev/prod), Python 3.14+.
- [ ] Структура каталогов: Clean Architecture (domain / application / infrastructure / presentation).
- [ ] Конфигурация: Pydantic Settings, `.env`, разделение профилей (dev/test/prod).
- [ ] Инструменты качества: Ruff (lint + format), mypy `--strict`, pre-commit hooks.
- [ ] Логирование: structlog / stdlib JSON-логи, correlation/request-id.
- [ ] Docker: multi-stage Dockerfile, docker-compose (Postgres, Redis, MinIO).
- [ ] CI-скелет: GitHub Actions — lint + type-check + unit-тесты на каждый PR.
- [ ] Инициализация Alembic, первая пустая миграция.
- [ ] DI-контейнер (Dishka): провайдеры для настроек, БД-сессии, репозиториев.
- [ ] Middleware: request-id, обработка исключений, единый формат ошибок (RFC 7807).

### Этап 1. Базовый CRUD, файлы и аутентификация

Пользователь управляет иерархией знаний и загружает файлы.

- [ ] Модель предметной области: Workspace → Folder → Document → Tag ↔ Document, внешние ссылки.
- [ ] Иерархия папок: Materialized Path / `ltree`; рекурсивные запросы (CTE) — дерево, поддерево, перемещение.
- [ ] SQLAlchemy 2.0 (asyncpg): модели, отношения, репозитории поверх Unit of Work.
- [ ] CRUD-эндпоинты документов/папок/тегов: Pydantic-схемы, пагинация, фильтры, сортировки.
- [ ] Работа с файлами: MinIO, presigned URL на загрузку/скачивание минуя backend.
- [ ] Валидация файлов: MIME-типы, ограничение размера, безопасные метаданные, checksum (SHA-256).
- [ ] Аутентификация: JWT (access/refresh), ротация refresh-токенов, Argon2-хеширование паролей.
- [ ] Авторизация: RBAC (owner/editor/viewer) на уровне workspace.
- [ ] Unit- и API-тесты: pytest-asyncio, фикстуры, factory-boy, покрытие ключевых сценариев.

### Этап 2. Асинхронный пайплайн и гибридный RAG

Документы автоматически конвертируются в чанки и находятся через поиск.

- [ ] Брокер: RabbitMQ / Redis Streams; выбор воркера (Taskiq/Celery/ARQ), обоснование.
- [ ] Transactional Outbox: гарантия доставки задач при коммите транзакции в БД.
- [ ] Пайплайн парсинга: PDF, DOCX, Markdown, Web Scraping; retries, exponential backoff, DLX/DLQ.
- [ ] Идемпотентность воркеров: idempotency-ключи, повторная обработка без дублей.
- [ ] Стратегии чанкинга: наивный (токены) vs семантический (заголовки/абзацы) vs Parent-Document.
- [ ] Эмбеддинги: provider-абстракция, батчинг, локальная модель vs внешний API.
- [ ] pgvector: схема, индексы HNSW/IVFFlat, метрика расстояния, tuning (m, ef_construction).
- [ ] Полнотекстовый поиск PostgreSQL: `tsvector`, GIN-индекс, BM25-подобный ранкинг.
- [ ] Гибридный поиск: объединение BM25 + dense через Reciprocal Rank Fusion (RRF).
- [ ] Реранкинг: Cross-Encoder поверх топ-K кандидатов.
- [ ] Streaming-ответ: Server-Sent Events (SSE) для токенов LLM.
- [ ] API-эндпоинт `/ask`: retrieval → сборка промпта → генерация → стриминг.

### Этап 3. Graph-RAG и семантическое дерево

Документы связаны не только папками, но и смысловыми узлами.

- [ ] NER + извлечение триплетов (subject–predicate–object) из документов.
- [ ] Схема графа: узлы (сущности/документы), рёбра (отношения), provenance (источник-документ).
- [ ] Хранилище графа: Neo4j (prod-путь) и/или NetworkX (прототип); абстракция графового репозитория.
- [ ] Разрешение сущностей (entity resolution / dedup узлов) и нормализация.
- [ ] Комбинированный retrieval: векторный поиск даёт стартовые узлы → обход графа 1–2 порядка.
- [ ] Контроль галлюцинаций связей: порог уверенности, provenance обязателен.
- [ ] Семантическое дерево/кластеризация документов поверх графа.
- [ ] API: эндпоинты навигации по графу (соседи узла, путь, подграф).
- [ ] Тесты графовых запросов на testcontainers (Neo4j).

### Этап 4. Надёжность, масштаб, наблюдаемость

Система ведёт себя предсказуемо под нагрузкой и сбоями.

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
- [ ] CI/CD: полный стенд в GitHub Actions (testcontainers: Postgres, Redis, MinIO, Neo4j) + деплой.

---

## Статус

Легенда: `[ ]` — не начато, `[~]` — в работе, `[x]` — готово.

| Этап | Статус |
|---|---|
| 0. Фундамент проекта | `[ ]` |
| 1. Базовый CRUD, файлы и аутентификация | `[ ]` |
| 2. Асинхронный пайплайн и гибридный RAG | `[ ]` |
| 3. Graph-RAG и семантическое дерево | `[ ]` |
| 4. Надёжность, масштаб, наблюдаемость | `[ ]` |

## Что сделано

- Репозиторий инициализирован: `pyproject.toml`, `main.py`, `.gitignore`, `.python-version`.
