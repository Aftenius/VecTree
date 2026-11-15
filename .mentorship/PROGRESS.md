# Прогресс по этапам

Ментор ведёт здесь статус. Обновляется по мере закрытия задач.

## Легенда
- `[ ]` — не начато
- `[~]` — в работе
- `[x]` — закрыто (сеньор-уровень подтверждён)
- `[!]` — есть блокер / вопрос к ментору

## Этап 0. Каркас и инструменты — закрыт
- [x] Инициализация проекта (uv, группа dev)
- [x] Структура каталогов (Clean Architecture)
- [x] Инструменты качества (Ruff, mypy --strict, pre-commit)

## Этап 1. ООП и проектирование домена (SOLID, DRY, KISS) — в работе
- [x] Классы и объекты (атрибуты, методы, self, __init__)
- [x] Инкапсуляция
- [x] Композиция vs наследование
- [x] Value object vs сущность (__eq__, __hash__, dataclass)
- [x] Абстракции и полиморфизм (abc/Protocol)
- [ ] SOLID (SRP, OCP, LSP, ISP, DIP)
- [ ] DRY и KISS
- [x] Сущности домена (Workspace/Folder/Document/Tag)
- [~] Агрегаты и инварианты
- [x] Порты (Protocol/ABC)
- [~] Иерархия папок (Materialized Path, чистая логика)
- [x] Доменные сервисы
- [x] In-memory репозитории

## Этап 2. Тестирование (pytest)
- [ ] Настройка pytest (конфигурация, tests/)
- [ ] Первый unit-тест домена
- [ ] Фикстуры и параметризация
- [ ] Инварианты и краевые случаи (pytest.raises)
- [ ] Покрытие ключевых сценариев

## Этап 3. Асинхронность на чистом Python
- [ ] Основы asyncio (loop, корутины, gather/TaskGroup)
- [ ] Отмена, таймауты, обработка исключений
- [ ] Async-контексты и итераторы
- [ ] Async-порты и репозитории
- [ ] CPU-bound через executor
- [ ] Async-тесты (pytest-asyncio)

## Этап 4. Локальный стек в Docker + конфигурация
- [ ] docker-compose (Postgres, Redis, MinIO)
- [ ] Multi-stage Dockerfile
- [ ] Healthchecks
- [ ] Конфигурация (Pydantic Settings, .env, профили)

## Этап 5. Персистентность (PostgreSQL + SQLAlchemy 2.0 + Alembic)
- [ ] SQLAlchemy 2.0 (asyncpg) модели
- [ ] Alembic (обратимые миграции)
- [ ] Репозитории поверх UoW
- [ ] Иерархия папок (ltree/Materialized Path, CTE)
- [ ] Индексы, пул соединений
- [ ] Интеграционные тесты (testcontainers Postgres)

## Этап 6. HTTP-слой (FastAPI)
- [ ] FastAPI маршруты + Pydantic v2
- [ ] DI (Dishka)
- [ ] Логирование (JSON, request-id)
- [ ] Middleware (request-id, RFC 7807)
- [ ] CRUD-эндпоинты (пагинация/фильтры/сортировки)
- [ ] API-тесты

## Этап 7. Аутентификация и авторизация
- [ ] JWT (access/refresh, ротация)
- [ ] Argon2
- [ ] RBAC
- [ ] Тесты auth/RBAC

## Этап 8. Файлы (MinIO/S3)
- [ ] MinIO + presigned URL
- [ ] Валидация файлов
- [ ] Checksum (SHA-256)

## Этап 9. CI
- [ ] GitHub Actions (lint + types + tests)
- [ ] Миграции + integration-тесты (testcontainers)
- [ ] Кэш зависимостей, артефакты логов

## Этап 10. Асинхронный пайплайн обработки документов
- [ ] Брокер + воркер
- [ ] Transactional Outbox
- [ ] Парсинг (PDF/DOCX/MD/web) + retries/DLQ
- [ ] Идемпотентность
- [ ] Стратегии чанкинга (свой RecursiveSplitter, семантический по косинусу)
- [ ] Эмбеддинги

## Этап 11. Гибридный поиск и RAG
- [ ] pgvector + индексы
- [ ] FTS (BM25)
- [ ] Hybrid + RRF
- [ ] Rerank (Cross-Encoder bge-reranker-base, топ-10 → топ-3)
- [ ] SSE streaming (+ CancelledError)
- [ ] `/ask`

## Этап 12. Graph-RAG и семантическое дерево
- [ ] NER + триплеты
- [ ] Схема графа
- [ ] Хранилище графа (Neo4j/NetworkX)
- [ ] Entity resolution
- [ ] Комбинированный retrieval + обход
- [ ] Контроль галлюцинаций
- [ ] Семантическое дерево
- [ ] API графа
- [ ] Тесты (testcontainers Neo4j)

## Этап 13. Агентный RAG на LangGraph
- [ ] Граф состояний (nodes/edges)
- [ ] AgentState (Pydantic v2)
- [ ] Тулы + строгая валидация аргументов
- [ ] Узел валидации (ValidationError → модели)
- [ ] Цикл самокоррекции (макс. 3 попытки)
- [ ] Checkpointer (PostgresSaver)
- [ ] Human-in-the-Loop (interrupt_before)

## Этап 14. Надёжность, масштаб, наблюдаемость
- [ ] RBAC в векторном поиске
- [ ] Consistency хранилищ
- [ ] SAGA / компенсации
- [ ] Semantic Cache
- [ ] Стоимость/задержки LLM
- [ ] Rate limiting
- [ ] OpenTelemetry
- [ ] Трейсинг LLM (Langfuse/Phoenix)
- [ ] Prometheus + Grafana
- [ ] RAG Evaluation (Ragas/TruLens/DeepEval, 20 эталонных вопросов)
- [ ] Нагрузочное тестирование
- [ ] Zero-downtime миграции
- [ ] Production-образы
