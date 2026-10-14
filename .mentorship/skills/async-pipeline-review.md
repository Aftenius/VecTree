# Skill: Async Pipeline & Messaging Review

Проверка очередей, воркеров, надёжности фоновой обработки.

## Что проверяю

- **Доставка**: Transactional Outbox, публикация после коммита транзакции.
- **Идемпотентность**: ключи, upsert, «ровно один раз» на уровне эффекта.
- **Retries**: exponential backoff + jitter; ограничение попыток; DLQ/DLX.
- **Порядок и конкуренция**: видимость сообщений, ack/nack, prefetch, redelivery.
- **Наблюдаемость**: correlation-id через всю цепочку, метрики очереди (lag, depth, rate).
- **Отказы**: поведение при падении воркера, при недоступной БД/LLM/S3.
- **Изоляция**: тяжёлые задачи не блокируют event loop (CPU-bound → process pool).
- **Стоимость**: батчинг вызовов LLM/embeddings, кэш.

## Красные флаги

- Публикация задачи до коммита БД (потеря задач).
- Нет идемпотентности → дубли обработки.
- Бесконечные retry без backoff → шторм по внешнему API.
- Синхронный `requests`/долгий CPU внутри async-воркера.

## Материал для изучения

- Transactional Outbox pattern; idempotent consumer.
- RabbitMQ: acks, DLX, quorum queues; Redis Streams: consumer groups, XACK, XAUTOCLAIM.
- Taskiq / Celery / ARQ — сравнение.
