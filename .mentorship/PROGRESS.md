# Прогресс по этапам

Ментор ведёт здесь статус. Обновляется по мере закрытия задач.

## Легенда
- `[ ]` — не начато
- `[~]` — в работе
- `[x]` — закрыто (сеньор-уровень подтверждён)
- `[!]` — есть блокер / вопрос к ментору

## Этап 0. Фундамент
- [ ] Инициализация проекта
- [ ] Структура каталогов (Clean Architecture)
- [ ] Конфигурация
- [ ] Инструменты качества (Ruff, mypy, pre-commit)
- [ ] Логирование
- [ ] Docker
- [ ] CI-скелет
- [ ] Alembic
- [ ] DI (Dishka)
- [ ] Middleware

## Этап 1. CRUD, файлы, auth
- [ ] Домен (Workspace/Folder/Document/Tag)
- [ ] Иерархия папок (ltree/Materialized Path)
- [ ] SQLAlchemy 2.0 + репозитории/UoW
- [ ] CRUD-эндпоинты
- [ ] MinIO + presigned URL
- [ ] Валидация файлов
- [ ] JWT + Argon2
- [ ] RBAC
- [ ] Тесты

## Этап 2. Пайплайн и гибридный RAG
- [ ] Брокер + воркер
- [ ] Transactional Outbox
- [ ] Парсинг (PDF/DOCX/MD/web) + retries/DLQ
- [ ] Идемпотентность
- [ ] Стратегии чанкинга
- [ ] Эмбеддинги
- [ ] pgvector + индексы
- [ ] FTS (BM25)
- [ ] Hybrid + RRF
- [ ] Rerank
- [ ] SSE streaming
- [ ] `/ask`

## Этап 3. Graph-RAG
- [ ] NER + триплеты
- [ ] Схема графа
- [ ] Хранилище графа (Neo4j/NetworkX)
- [ ] Entity resolution
- [ ] Комбинированный retrieval + обход
- [ ] Контроль галлюцинаций
- [ ] Семантическое дерево
- [ ] API графа
- [ ] Тесты (testcontainers Neo4j)

## Этап 4. Сеньор-инженерия
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
- [ ] CI/CD полный стенд
