---
type: reference
description: "Заменённые и отменённые решения форка — номера и ссылки те же"
project: vic3
tags: [форк, решения]
---
# Заменённые решения форка

Решение, отменённое целиком или вошедшее в другое (`replaced`, `replaced_by`); читать по ссылке.

```base
filters:
  and:
    - file.inFolder(this.file.folder)
    - note.type == "decision"
views:
  - type: table
    name: Решения
    order:
      - file.name
      - status
      - date
    sort:
      - property: file.name
        direction: ASC
```
