# Прогресс по этапам

Ментор ведёт здесь статус. Обновляется по мере закрытия задач.

## Легенда
- `[ ]` — не начато
- `[~]` — в работе
- `[x]` — закрыто (сеньор-уровень подтверждён)
- `[!]` — есть блокер / вопрос к ментору

## Этап 0. Каркас и инструменты
- [ ] Инициализация проекта (uv, группы dev/test)
- [ ] Структура каталогов (Clean Architecture)
- [ ] Инструменты качества (Ruff, mypy --strict, pre-commit)
- [ ] Логирование (JSON, request-id)
- [ ] Базовый pytest

## Этап 1. Домен на чистом Python (ООП + SOLID/DRY/KISS)
- [ ] Сущности и value objects (Workspace/Folder/Document/Tag)
- [ ] Агрегаты и инварианты
- [ ] Порты (Protocol/ABC)
- [ ] Иерархия папок (Materialized Path, чистая логика)
- [ ] Доменные сервисы
- [ ] In-memory репозитории
- [ ] Unit-тесты домена

## Этап 2. Асинхронность на чистом Python
- [ ] Основы asyncio (loop, корутины, gather/TaskGroup)
- [ ] Отмена, таймауты, обработка исключений
- [ ] Async-контексты и итераторы
- [ ] Async-порты и репозитории
- [ ] CPU-bound через executor
- [ ] Async-тесты (pytest-asyncio)

## Этап 3. Локальный стек в Docker + конфигурация
- [ ] docker-compose (Postgres, Redis, MinIO)
- [ ] Multi-stage Dockerfile
- [ ] Healthchecks
- [ ] Конфигурация (Pydantic Settings, .env, профили)

## Этап 4. Персистентность (PostgreSQL + SQLAlchemy 2.0 + Alembic)
- [ ] SQLAlchemy 2.0 (asyncpg) модели
- [ ] Alembic (обратимые миграции)
- [ ] Репозитории поверх UoW
- [ ] Иерархия папок (ltree/Materialized Path, CTE)
- [ ] Индексы, пул соединений
- [ ] Интеграционные тесты (testcontainers Postgres)

## Этап 5. HTTP-слой (FastAPI)
- [ ] FastAPI маршруты + Pydantic v2
- [ ] DI (Dishka)
- [ ] Middleware (request-id, RFC 7807)
- [ ] CRUD-эндпоинты (пагинация/фильтры/сортировки)
- [ ] API-тесты

## Этап 6. Аутентификация и авторизация
- [ ] JWT (access/refresh, ротация)
- [ ] Argon2
- [ ] RBAC
- [ ] Тесты auth/RBAC

## Этап 7. Файлы (MinIO/S3)
- [ ] MinIO + presigned URL
- [ ] Валидация файлов
- [ ] Checksum (SHA-256)

## Этап 8. CI
- [ ] GitHub Actions (lint + types + tests)
- [ ] Миграции + integration-тесты (testcontainers)
- [ ] Кэш зависимостей, артефакты логов

## Этап 9. Асинхронный пайплайн обработки документов
- [ ] Брокер + воркер
- [ ] Transactional Outbox
- [ ] Парсинг (PDF/DOCX/MD/web) + retries/DLQ
- [ ] Идемпотентность
- [ ] Стратегии чанкинга
- [ ] Эмбеддинги

## Этап 10. Гибридный поиск и RAG
- [ ] pgvector + индексы
- [ ] FTS (BM25)
- [ ] Hybrid + RRF
- [ ] Rerank
- [ ] SSE streaming
- [ ] `/ask`

## Этап 11. Graph-RAG и семантическое дерево
- [ ] NER + триплеты
- [ ] Схема графа
- [ ] Хранилище графа (Neo4j/NetworkX)
- [ ] Entity resolution
- [ ] Комбинированный retrieval + обход
- [ ] Контроль галлюцинаций
- [ ] Семантическое дерево
- [ ] API графа
- [ ] Тесты (testcontainers Neo4j)

## Этап 12. Надёжность, масштаб, наблюдаемость
- [ ] RBAC в векторном поиске
- [ ] Consistency хранилищ
- [ ] SAGA / компенсации
- [ ] Semantic Cache
- [ ] Стоимость/задержки LLM
- [ ] Rate limiting
- [ ] OpenTelemetry
- [ ] Prometheus + Grafana
- [ ] RAG Evaluation (Ragas/TruLens)
- [ ] Нагрузочное тестирование
- [ ] Zero-downtime миграции
- [ ] Production-образы
