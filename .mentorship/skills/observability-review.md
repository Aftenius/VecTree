# Skill: Observability & Performance Review

Проверка логирования, метрик, трейсинга и производительности.

## Что проверяю

- **Логи**: структурированные (JSON), уровни осмысленны, correlation/request-id сквозной, без PII.
- **Метрики**: RED (Rate, Errors, Duration) + бизнес-метрики (TTFT, tokens, cost, cache hit).
- **Гистограммы**: p50/p95/p99, а не средние.
- **Трейсинг**: OpenTelemetry, спаны на БД/LLM/S3/очереди, propagation через воркеры.
- **Производительность**: N+1, батчинг, индексы, пул соединений, бюджет латентности.
- **Нагрузка**: тест под реалистичной нагрузкой, поиск узкого места, soak test.
- **Алерты**: на SLO, а не на каждый чих.

## Красные флаги

- Логирование без correlation-id → невозможно связать запрос.
- Только средние метрики.
- Трейсинг обрывается на границе воркера.
- Оптимизация «на глаз» без профилирования.

## Материал для изучения

- OpenTelemetry Python (auto + manual instrumentation, context propagation).
- Prometheus metric types и `histogram_quantile`.
- Google SRE: SLI/SLO/error budget; USE/RED методы.
