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

- [x] Инициализация проекта: `pyproject.toml` (uv), группа зависимостей dev, Python 3.14+.
- [x] Структура каталогов: Clean Architecture (domain / application / infrastructure / presentation).
- [x] Инструменты качества: Ruff (lint + format), mypy `--strict`, pre-commit hooks.

### Этап 1. ООП и проектирование домена (SOLID, DRY, KISS)

- [x] Классы и объекты: атрибуты, методы, `self`, конструктор `__init__`.
- [x] Инкапсуляция: скрытое внутреннее состояние и публичный API класса.
- [x] Композиция vs наследование: что и когда выбирать.
- [x] Value object vs сущность: идентичность и равенство (`__eq__`, `__hash__`, `@dataclass`).
- [x] Абстракции и полиморфизм: `abc` / `Protocol`, duck typing.
- [x] SOLID: SRP, OCP, LSP, ISP, DIP — на примерах домена.
- [x] DRY и KISS: как не дублировать и не усложнять.
- [x] Сущности домена: Workspace, Folder, Document, Tag.
- [x] Инварианты домена: уникальность имён, лимит вложенности, уникальность тегов.
- [x] Порты (Protocol/ABC): интерфейсы репозиториев без инфраструктуры.
- [x] Иерархия папок: вложенность, лимит глубины, рекурсивный подсчёт (adjacency list).
- [x] Доменные сервисы: `move_document`.
- [x] In-memory репозитории (dict).

### Этап 2. Тестирование (pytest)

- [ ] Настройка pytest: конфигурация, каталог `tests/`.
- [ ] Первый unit-тест домена.
- [ ] Фикстуры и параметризация.
- [ ] Инварианты и краевые случаи (`pytest.raises`).
- [ ] Покрытие (coverage) ключевых сценариев.

### Этап 3. Асинхронность на чистом Python

- [ ] Основы asyncio: event loop, корутины, `asyncio.gather` / `TaskGroup`.
- [ ] Отмена задач, таймауты (`asyncio.timeout`), обработка исключений.
- [ ] Асинхронные контекст-менеджеры и async-итераторы.
- [ ] Перевод портов и репозиториев на async.
- [ ] CPU-bound операции через `run_in_executor` / process pool.
- [ ] Async-тесты (pytest-asyncio), корректный loop scope.

### Этап 4. Локальный стек в Docker + конфигурация

- [ ] docker-compose: PostgreSQL (+pgvector), Redis, MinIO.
- [ ] Multi-stage Dockerfile для приложения.
- [ ] Healthchecks (liveness/readiness) для сервисов.
- [ ] Конфигурация: Pydantic Settings, `.env`, профили dev/test/prod.

### Этап 5. Персистентность: PostgreSQL + SQLAlchemy 2.0 + Alembic

- [ ] SQLAlchemy 2.0 (asyncpg): модели, отношения.
- [ ] Alembic: инициализация, обратимые миграции.
- [ ] Репозитории поверх Unit of Work; без lazy-load вне сессии, без N+1.
- [ ] Иерархия папок в БД: `ltree`/Materialized Path, рекурсивные CTE (дерево, поддерево, перемещение).
- [ ] Границы агрегатов и маппинг домена на таблицы.
- [ ] Индексы под реальные запросы; пул соединений и таймауты.
- [ ] Интеграционные тесты на testcontainers (Postgres).

### Этап 6. HTTP-слой: FastAPI

- [ ] FastAPI: маршруты, Pydantic v2 схемы.
- [ ] DI-контейнер (Dishka): настройки, сессии БД, репозитории.
- [ ] Логирование: structlog / stdlib JSON-логи, correlation/request-id.
- [ ] Middleware: request-id, обработка исключений, единый формат ошибок (RFC 7807).
- [ ] CRUD-эндпоинты документов/папок/тегов: пагинация, фильтры, сортировки.
- [ ] API-тесты (httpx/ASGI).

### Этап 7. Аутентификация и авторизация

- [ ] JWT: access/refresh, ротация refresh-токенов.
- [ ] Argon2-хеширование паролей.
- [ ] RBAC (owner/editor/viewer) на уровне workspace; проверка на каждом доступе.
- [ ] Тесты auth/RBAC.

### Этап 8. Файлы: MinIO/S3

- [ ] MinIO, presigned URL на загрузку/скачивание минуя backend.
- [ ] Валидация файлов: MIME-типы, ограничение размера, безопасные метаданные.
- [ ] Checksum (SHA-256).
- [ ] Внешние ссылки (URL) на документы.

### Этап 9. CI

- [ ] GitHub Actions: lint + type-check + unit-тесты на каждый PR.
- [ ] Прогон миграций и интеграционных тестов (testcontainers: Postgres, Redis, MinIO).
- [ ] Кэш зависимостей, артефакты логов.

### Этап 10. Асинхронный пайплайн обработки документов

- [ ] Брокер: RabbitMQ / Redis Streams; выбор воркера (Taskiq/Celery/ARQ), обоснование.
- [ ] Transactional Outbox: гарантия доставки задач при коммите транзакции в БД.
- [ ] Пайплайн парсинга: PDF, DOCX, Markdown, Web Scraping; retries, exponential backoff, DLX/DLQ.
- [ ] Идемпотентность воркеров: idempotency-ключи, повторная обработка без дублей.
- [ ] Стратегии чанкинга: токены vs семантический (заголовки/абзацы) vs Parent-Document; свой `RecursiveSplitter` без готовых обёрток.
- [ ] Эмбеддинги: provider-абстракция, батчинг, локальная модель vs внешний API.

### Этап 11. Гибридный поиск и RAG

- [ ] pgvector: схема, индексы HNSW/IVFFlat, метрика расстояния, tuning (m, ef_construction).
- [ ] Полнотекстовый поиск PostgreSQL: `tsvector`, GIN-индекс, BM25-подобный ранкинг.
- [ ] Гибридный поиск: объединение BM25 + dense через Reciprocal Rank Fusion (RRF).
- [ ] Реранкинг: Cross-Encoder (напр. bge-reranker-base) поверх топ-10 кандидатов; в промпт — топ-3.
- [ ] Streaming-ответ (SSE) для токенов LLM; обработка обрыва соединения (`asyncio.CancelledError`).
- [ ] API-эндпоинт `/ask`: retrieval → сборка промпта → генерация → стриминг.

### Этап 12. Graph-RAG и семантическое дерево

- [ ] NER + извлечение триплетов (subject–predicate–object) из документов.
- [ ] Схема графа: узлы (сущности/документы), рёбра (отношения), provenance (источник-документ).
- [ ] Хранилище графа: Neo4j (prod-путь) и/или NetworkX (прототип); абстракция графового репозитория.
- [ ] Разрешение сущностей (entity resolution / dedup узлов) и нормализация.
- [ ] Комбинированный retrieval: векторный поиск даёт стартовые узлы → обход графа 1–2 порядка.
- [ ] Контроль галлюцинаций связей: порог уверенности, provenance обязателен.
- [ ] Семантическое дерево/кластеризация документов поверх графа.
- [ ] API: эндпоинты навигации по графу (соседи узла, путь, подграф).
- [ ] Тесты графовых запросов на testcontainers (Neo4j).

### Этап 13. Агентный RAG на LangGraph

- [ ] Граф состояний: узлы (nodes) и рёбра (edges) — детерминированный конечный автомат вместо цепочек.
- [ ] Типизированное состояние `AgentState` через Pydantic v2.
- [ ] Тулы со строгой валидацией аргументов.
- [ ] Узел валидации: ловит `ValidationError` и возвращает ошибку модели как сообщение.
- [ ] Цикл самокоррекции: ребро на повторную генерацию, максимум 3 попытки.
- [ ] Checkpointer (`PostgresSaver`): сохранение состояния агента.
- [ ] Human-in-the-Loop: `interrupt_before` перед критическим действием + подтверждение по API.

### Этап 14. Надёжность, масштаб, наблюдаемость

- [ ] RBAC в векторном поиске: pre-filtering прав доступа на уровне SQL/индекса (нельзя найти чужое).
- [ ] Consistency разнородных хранилищ: distributed cleanup (Postgres ↔ MinIO ↔ pgvector ↔ graph).
- [ ] SAGA / compensations для multi-step операций; обработка частичных сбоев.
- [ ] Semantic Cache в Redis: кэш семантически похожих запросов + дедупликация.
- [ ] Стоимость/задержки LLM: динамический размер контекста, локальные модели для NER/эмбеддингов.
- [ ] Rate limiting, backpressure, ограничение RPS на дорогие эндпоинты.
- [ ] OpenTelemetry: сквозной трейсинг (endpoint → БД → LLM), спаны на ключевых операциях.
- [ ] Трейсинг LLM-шагов (Langfuse / Phoenix): latency, расход токенов, переходы между нодами.
- [ ] Метрики Prometheus + дашборды Grafana: TTFT, RPS, p95/p99, расход токенов, cache hit-rate.
- [ ] RAG Evaluation: Ragas/TruLens или DeepEval (Faithfulness — нет галлюцинаций, Answer Relevance — ответ по сути);
      прогон на 20 эталонных вопросах; регрессия при изменении промптов/чанкинга.
- [ ] Нагрузочное тестирование (locust/k6): профилирование узких мест, бюджет задержек.
- [ ] Миграции без даунтайма (expand/contract), zero-downtime деплой.
- [ ] Production-образы: distroless/alpine, non-root, healthchecks (liveness/readiness).

---

## Статус

Легенда: `[ ]` — не начато, `[~]` — в работе, `[x]` — готово.

| Этап | Статус |
|---|---|
| 0. Каркас и инструменты | `[x]` |
| 1. ООП и проектирование домена | `[x]` |
| 2. Тестирование (pytest) | `[ ]` |
| 3. Асинхронность на чистом Python | `[ ]` |
| 4. Локальный стек в Docker + конфигурация | `[ ]` |
| 5. Персистентность (PostgreSQL + SQLAlchemy + Alembic) | `[ ]` |
| 6. HTTP-слой (FastAPI) | `[ ]` |
| 7. Аутентификация и авторизация | `[ ]` |
| 8. Файлы (MinIO/S3) | `[ ]` |
| 9. CI | `[ ]` |
| 10. Асинхронный пайплайн | `[ ]` |
| 11. Гибридный поиск и RAG | `[ ]` |
| 12. Graph-RAG и семантическое дерево | `[ ]` |
| 13. Агентный RAG на LangGraph | `[ ]` |
| 14. Надёжность, масштаб, наблюдаемость | `[ ]` |

## Что сделано

- Репозиторий инициализирован: `pyproject.toml`, `main.py`, `.gitignore`, `.python-version`.
- Инструменты качества настроены: uv (группа dev), Ruff, mypy `--strict`, pre-commit.
- Каркас слоёв создан: `vectree/{domain, application, infrastructure, presentation}`.
- Домен: сущности `Workspace`/`Folder`/`Document`/`Tag`, инкапсуляция, value objects, порты, `move_document`, вложенные папки (лимит 5), рекурсивный подсчёт.
