# Skill: RAG / Graph-RAG Review

Проверка retrieval-качества, чанкинга, эмбеддингов, реранка, графа и генерации.

## Что проверяю

- **Чанкинг**: стратегия осознана (token / semantic / parent-child), overlap, метаданные.
- **Retrieval**: hybrid (BM25 + dense), fusion (RRF с правильным k), top-k обоснован.
- **Rerank**: cross-encoder только на кандидатах, батчинг, latency-бюджет.
- **Embeddings**: модель, размерность, нормализация, батчинг, кэш, локально vs API.
- **Промпт**: ограничение контекста, цитирование источников, отказ при отсутствии данных.
- **Graph-RAG**: извлечение триплетов, entity resolution, обход 1–2 порядка, provenance.
- **Галлюцинации**: ответ опирается на контекст; связи имеют источник; пороги уверенности.
- **RBAC в retrieval**: pre-filtering прав до ЕСТЬ попадание в top-k (нельзя найти чужое).
- **Оценка качества**: Ragas/TruLens метрики, регрессионный прогон, golden set.
- **Экономика**: токены, стоимость запроса, кэш, TTFT.

## Красные флаги

- Пост-фильтрация прав после retrieval (утечка/пустая выдача).
- Нет citation/provenance → галлюцинации.
- Retrieval без оценки качества («на глаз»).
- Косинус без нормировки / несовпадение метрики индекса и запроса.

## Материал для изучения

- Hybrid search + Reciprocal Rank Fusion.
- Parent Document Retriever (LlamaIndex), LangGraph для agentic-обхода.
- Ragas метрики: faithfulness, answer relevance, context recall/precision.
- Microsoft GraphRAG / Neo4j + vector index.
