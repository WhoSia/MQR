#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Callable

UNICODE_CORE = [
    ("C01", 0x0041),
    ("C02", 0x00E9),
    ("C03", 0x0301),
    ("C04", 0x4E00),
]
UNICODE_REFINEMENT = [
    ("U15_0_01", 0x0CF3),
    ("U15_0_02", 0x0ECE),
    ("U15_0_03", 0x10EFD),
    ("U15_1_01", 0x2FFC),
    ("U15_1_02", 0x2FFD),
    ("U15_1_03", 0x2FFE),
    ("U16_0_01", 0x0897),
    ("U16_0_02", 0x1B4E),
    ("U16_0_03", 0x1B4F),
]

JSCHEMA_CORE = [
    ("C01", {"type": "integer"}, 3),
    ("C02", {"type": "integer"}, "3"),
    ("C03", {"type": "object", "required": ["x"], "properties": {"x": {"type": "integer"}}}, {}),
    ("C04", {"type": "number", "minimum": 5}, 6),
    ("C05", {"type": "array", "minItems": 2}, [1]),
    ("C06", {"type": "object", "properties": {"x": {"type": "integer"}}, "additionalProperties": False}, {"x": 1, "y": 2}),
]
META_2020 = "https://json-schema.org/draft/2020-12/schema"
JSCHEMA_REFINEMENT = [
    ("R01", {"$schema": META_2020, "prefixItems": [{"type": "integer"}, {"type": "string"}], "items": False}, [1, "x"]),
    ("R02", {"$schema": META_2020, "prefixItems": [{"type": "integer"}, {"type": "string"}], "items": False}, [1, 2]),
    ("R03", {"$schema": META_2020, "type": "object", "properties": {"x": {"type": "integer"}}, "unevaluatedProperties": False}, {"x": 1}),
    ("R04", {"$schema": META_2020, "type": "object", "properties": {"x": {"type": "integer"}}, "unevaluatedProperties": False}, {"x": 1, "y": 2}),
]

def oas_base(version: str) -> dict[str, Any]:
    return {"openapi": version, "info": {"title": "mqr", "version": "1.0.0"}, "paths": {}}

OAS_CORE = [
    ("C01", oas_base("3.0.3")),
    ("C02", {"openapi": "3.0.3", "paths": {}}),
    ("C03", {"openapi": "3.0.0", "info": {"title": "mqr", "version": "1.0.0"}, "paths": {"/ping": {"get": {"responses": {"200": {"description": "ok"}}}}}}),
    ("C04", {"openapi": "3.0.3", "info": {"title": "mqr", "version": "1.0.0"}, "paths": {}, "components": {"schemas": {"Maybe": {"type": "string", "nullable": True}}}}),
]
OAS_REFINEMENT = [
    ("R01", oas_base("3.1.0")),
    ("R02", {"openapi": "3.1.0", "info": {"title": "mqr", "version": "1.0.0"}, "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema", "paths": {}}),
    ("R03", {"openapi": "3.1.0", "info": {"title": "mqr", "version": "1.0.0"}, "paths": {}, "components": {"schemas": {"Maybe": {"type": ["string", "null"]}}}}),
    ("R04", {"openapi": "3.1.0", "info": {"title": "mqr", "version": "1.0.0"}, "paths": {}, "webhooks": {}}),
]

def emit(case: str, fiber: str, version: str, kind: str, pid: str, exact: Any, coarse: Any, status: str = "OK") -> None:
    print("\t".join([
        case, fiber, version, kind, pid,
        json.dumps(exact, ensure_ascii=True, sort_keys=True, separators=(",", ":")),
        json.dumps(coarse, ensure_ascii=True, sort_keys=True, separators=(",", ":")),
        status,
    ]))

def emit_all_error(case: str, fiber: str, version: str, probes: list[tuple[str, str]], exc: BaseException) -> None:
    marker = f"{type(exc).__name__}:{str(exc)[:160]}"
    for kind, pid in probes:
        emit(case, fiber, version, kind, pid, marker, marker, "EXECUTION_ERROR")

def run_jschema(version: str) -> None:
    case, fiber = "JSCHEMA-001", "F-R1"
    all_probes = [("CORE", p[0]) for p in JSCHEMA_CORE] + [("REFINEMENT", p[0]) for p in JSCHEMA_REFINEMENT]
    try:
        import jsonschema
        from jsonschema import exceptions, validators
        validator_for = getattr(validators, "validator_for")
    except BaseException as exc:
        emit_all_error(case, fiber, version, all_probes, exc)
        return

    for kind, probes in (("CORE", JSCHEMA_CORE), ("REFINEMENT", JSCHEMA_REFINEMENT)):
        for pid, schema, instance in probes:
            try:
                cls = validator_for(schema)
                cls.check_schema(schema)
                cls(schema).validate(instance)
                out = "VALID"
                emit(case, fiber, version, kind, pid, out, out)
            except exceptions.ValidationError:
                out = "INVALID"
                emit(case, fiber, version, kind, pid, out, out)
            except BaseException as exc:
                marker = f"{type(exc).__name__}:{str(exc)[:160]}"
                emit(case, fiber, version, kind, pid, marker, marker, "EXECUTION_ERROR")

def run_oas(version: str) -> None:
    case, fiber = "OASV-001", "F-R1"
    all_probes = [("CORE", p[0]) for p in OAS_CORE] + [("REFINEMENT", p[0]) for p in OAS_REFINEMENT]
    try:
        from openapi_spec_validator import validate_spec
    except BaseException as exc:
        emit_all_error(case, fiber, version, all_probes, exc)
        return

    for kind, probes in (("CORE", OAS_CORE), ("REFINEMENT", OAS_REFINEMENT)):
        for pid, doc in probes:
            try:
                validate_spec(doc)
                emit(case, fiber, version, kind, pid, "VALID", "VALID")
            except BaseException as exc:
                # Provider validation exceptions are invalidity; invocation/type errors are execution failures.
                mod = type(exc).__module__
                name = type(exc).__name__
                if mod.startswith("openapi_spec_validator") or "Validation" in name or "Duplicate" in name:
                    emit(case, fiber, version, kind, pid, "INVALID", "INVALID")
                else:
                    marker = f"{name}:{str(exc)[:160]}"
                    emit(case, fiber, version, kind, pid, marker, marker, "EXECUTION_ERROR")

def run_ucd2(version: str) -> None:
    case, fiber = "UCD2-001", "F-R2"
    probes = [("CORE", x) for x in UNICODE_CORE] + [("REFINEMENT", x) for x in UNICODE_REFINEMENT]
    try:
        import unicodedata2 as ud
    except BaseException as exc:
        emit_all_error(case, fiber, version, [(kind, p[0]) for kind, p in probes], exc)
        return
    for kind, (pid, cp) in probes:
        ch = chr(cp)
        try:
            exact = [ud.category(ch), ud.combining(ch), ud.east_asian_width(ch), ud.name(ch, None) is not None]
            coarse = "ASSIGNED" if exact[0] != "Cn" else "UNASSIGNED"
            emit(case, fiber, version, kind, pid, exact, coarse)
        except BaseException as exc:
            marker = f"{type(exc).__name__}:{str(exc)[:160]}"
            emit(case, fiber, version, kind, pid, marker, marker, "EXECUTION_ERROR")

def run_wcwidth(version: str) -> None:
    case, fiber = "WCWIDTH-001", "F-R2"
    probes = [("CORE", x) for x in UNICODE_CORE] + [("REFINEMENT", x) for x in UNICODE_REFINEMENT]
    try:
        from wcwidth import wcwidth
    except BaseException as exc:
        emit_all_error(case, fiber, version, [(kind, p[0]) for kind, p in probes], exc)
        return
    for kind, (pid, cp) in probes:
        try:
            val = wcwidth(chr(cp))
            coarse = "NEGATIVE" if val < 0 else ("ZERO" if val == 0 else "POSITIVE")
            emit(case, fiber, version, kind, pid, val, coarse)
        except BaseException as exc:
            marker = f"{type(exc).__name__}:{str(exc)[:160]}"
            emit(case, fiber, version, kind, pid, marker, marker, "EXECUTION_ERROR")

RUNNERS: dict[str, Callable[[str], None]] = {
    "JSCHEMA-001": run_jschema,
    "OASV-001": run_oas,
    "UCD2-001": run_ucd2,
    "WCWIDTH-001": run_wcwidth,
}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True, choices=sorted(RUNNERS))
    ap.add_argument("--version", required=True)
    args = ap.parse_args()
    print("case_id\tfiber\tversion\tprobe_class\tprobe_id\texact\tcoarse\tstatus")
    RUNNERS[args.case](args.version)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
