# MQR 42 — 2026-11-21 판본 판정과 00 정리 영수증

Research OS 원칙: `00_INTAKE`는 임시 서가, 논문 정본은 `10_PAPERS`, 원전 단행본은 `11_BOOKS`, 보고서는 `11_SOURCES`. 파일 ID와 PDF 바이트는 메타데이터 이동으로 보존한다. 관련성이 없거나 판본 확인이 안 된 파일을 편의상 승격하지 않는다.

## 이 차례에 처리한 00 서가

현재 00 재검색의 직접 자식은 25개였으며, 2026-11-20 19:22 UTC 이후 새로 생성된 파일은 검색 결과에 없었다. 직전 단계의 다섯 MQR 원전 입고는 GitHub HEAD `0c88d8c3...`의 원장에 이미 기록되어 있었다. Jones (1941) I, Chalmers (1986), Talone (2016)은 `10_PAPERS`; Kerns (1948) 보고서는 `11_SOURCES`; Marcuvitz (1951)은 `11_BOOKS`. 이 파일을 다시 복사하거나 중복으로 커밋하지 않았다.

| 이번 정리 대상 | 현지 판정 / 위치 | 구분 근거 |
|---|---|---|
| [Porter, *Trust in Numbers*, 2020 신판](https://drive.google.com/file/d/16AJbAioeRAovbeUBbLR6EtI2pch64rle/view) | `11_BOOKS`; `Porter (2020) — Trust in Numbers - The Pursuit of Objectivity in Science and Public Life (New Edition with Preface).pdf` | 표제지/저작권 면에 2020년 신판과 ISBN 978-0-691-20841-1, 저자의 새 서문을 명시. [기존 1995판](https://drive.google.com/file/d/1xjUTIfg-ESa8bwaVhCtUEquuZPCGQxRt/view)은 별도 정본으로 유지 |
| [Buneman, Khanna & Tan (2001) 연구자판](https://drive.google.com/file/d/1AQ_Rsg1HpmBZR1Rjew6yXfz-9uWHaHpV/view) | `90_SOURCE_VERSIONS`; Peer-Reviewed Manuscript suffix | Edinburgh Research Explorer 표지에 peer-reviewed version 명시. [출판판](https://drive.google.com/file/d/1IDVAD8G1wtqwWvTXTywzu5UDHuxhFklB/view) 이미 정본; DOI 10.1007/3-540-44503-X_20 |
| [Grundmann (2009) 저자 원고](https://drive.google.com/file/d/1wfro5XhTwIsDI2tefS49dGCEgFvd3H2x/view) | `90_SOURCE_VERSIONS`; Author Manuscript suffix | 저자 원고 4,454단어/11면, 출판본 [*Grazer Philosophische Studien* 79:65–76](https://drive.google.com/file/d/11BKjHzfl0DYbBY_yrJzrwNSZGDPRAVjL/view)과 문서판 차이 |
| [Greenberg (2009) BMJ 재다운로드](https://drive.google.com/file/d/1VjvdiGv06sF5VJpGSr1PZp_tf_5f1k-H/view) | `90_SOURCE_VERSIONS`; BMJ Download 2026-10-17 suffix | 기존 [논문 PDF](https://drive.google.com/file/d/1aOCtqq3CDL9htYZTogJJ10ux9LgPDxih/view)와 별도 PDF 바이트; 다운로드 시각 표시/푸터 차이. 동일 논문 DOI 10.1136/bmj.b2680 |
| [Debreu (1959) 별도 이미지 스캔](https://drive.google.com/file/d/1n3KYxb_VuSNyU6io9_NsvZhnXNbsyDDJ/view) | `90_SOURCE_VERSIONS`; Alternate Image Scan suffix | [기존 원전](https://drive.google.com/file/d/1v5-0wllrTXmIbocTAsTtVcK5nDTY47Qc/view)이 `11_BOOKS`에 있음; 광학적 페이지 동등성은 미검증 |

모든 5건의 이동은 기존 Drive ID를 유지했고, 직후 동일 이름으로 재검색해 ID·목적지 부모·바이트 크기를 확인했다. SHA-256 별도 재계산은 이 차례에 수행하지 않았으므로 바이트 내용의 동일성을 **추정하지 않는다**. 어떤 PDF도 삭제하지 않았다. `90_SOURCE_VERSIONS`는 정본이 아니라 판본·다운로드 차이를 보존하는 서가다. 이미 보관된 다섯 MQR 입고 원전의 SHA-256은 이전 영수증에 따르며 이번 작업의 성과로 재집계하지 않는다.

## MQR의 실제 연구 접점

Porter의 2020 새 서문은 숫자의 객관성이 '수치에 대한 무비판적 믿음'이 아니라 불신/이해관계 속의 표준화와 비인격적 절차의 신뢰성에 관계함을 직접 설명한다. 이것은 세계에 대한 진리 조건과 조직적으로 수용 가능한 증거의 조건을 구분하게 만든다. Greenberg 논문은 인용이 데이터의 직접 반복 검증이 아닌 권위 전파 경로가 될 수 있음을 사례 연구로 보인다. Buneman 등은 출력이 존재하는 이유(why)와 어떤 입력 위치에서 값이 왔는가(where)를 구별한다. 이 세 갈래는 서로 다른 논리적 문제이고 '숫자/인용/원장으로 진리가 확정된다'는 주장으로 합쳐서는 안 된다.

**다음 판별:** 한 출력의 동일성, 그 출력의 생성·인용 계보, 출력의 새로운 실험에서의 예측력을 따로 추적한다. 이에 대응하는 유한 관측 모형은 [new observable bootstrap](mqr_54_mqr42_new_observable_partition_bootstrap.md)에서 구성한다.
