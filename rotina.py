"""Aplica as regras do regras.md sobre dados/amostra.csv.
Uso: python rotina.py <repo> <data_execucao AAAA-MM-DD> [--sem-instrucao-de-falha]
"""
import csv, sys, os, re
from datetime import date, timedelta

repo = sys.argv[1]
hoje = date.fromisoformat(sys.argv[2])
sem_falha = "--sem-instrucao-de-falha" in sys.argv
path = os.path.join(repo, "dados", "amostra.csv")

if not os.path.exists(path):
    if sem_falha:
        print("Fonte nao encontrada em dados/amostra.csv. (sem instrucao de falha: a rotina seguiria com o que tem)")
        print("Regra 1: nao disparou, 0 registros olhados. Regra 2: nao disparou, 0 participantes. Regra 3: nao disparou.")
    else:
        print("FONTE INDISPONÍVEL: dados/amostra.csv não existe. Parei. Nada foi estimado.")
    sys.exit(0)

lidas, ignoradas, validas = 0, [], []
with open(path, newline="", encoding="utf-8") as f:
    for i, row in enumerate(csv.DictReader(f), start=2):
        lidas += 1
        motivo = None
        if not row.get("data") or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row["data"] or ""):
            motivo = f"data '{row.get('data')}' fora do formato AAAA-MM-DD"
        else:
            try:
                date.fromisoformat(row["data"])
            except ValueError:
                motivo = f"data '{row['data']}' inválida"
        if not motivo:
            try:
                it = int(row["intensidade"])
                if not 0 <= it <= 10:
                    motivo = f"intensidade {it} fora de 0 a 10"
            except (ValueError, TypeError):
                motivo = f"intensidade '{row.get('intensidade')}' não é inteiro"
        if not motivo:
            try:
                d = float(row["duracao_horas"])
                if d < 0:
                    motivo = f"duracao_horas {d} negativa"
            except (ValueError, TypeError):
                motivo = f"duracao_horas '{row.get('duracao_horas')}' vazia ou não numérica"
        if not motivo and not row.get("participante"):
            motivo = "participante vazio"
        if motivo:
            ignoradas.append((i, motivo, row))
        else:
            validas.append(row)

if lidas == 0:
    print("FONTE INDISPONÍVEL: dados/amostra.csv existe mas está vazio. Parei.")
    sys.exit(0)

print(f"Execução em {hoje.strftime('%d/%m/%Y')}. Linhas lidas: {lidas}. Ignoradas: {len(ignoradas)}.")
for ln, m, _ in ignoradas:
    print(f"  - linha {ln} ignorada: {m}")

d1 = (hoje - timedelta(days=1)).isoformat()
ontem = [r for r in validas if r["data"] == d1]
intensos = [r for r in ontem if int(r["intensidade"]) >= 7 or float(r["duracao_horas"]) > 24]

ilegiveis = [(ln, m, r) for ln, m, r in ignoradas if r.get("data") == d1 or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r.get("data") or "")]
print(f"\nRegra 1 · Sintoma intenso em D-1 ({d1}): ", end="")
if ilegiveis and not intensos:
    print(f"REGISTRO ILEGÍVEL. {len(ilegiveis)} linha(s) que podem ser de D-1 não puderam ser lidas; trato como alerta para eu conferir à mão:")
    for ln, m, r in ilegiveis:
        print(f"  - linha {ln}: {m} · conteúdo bruto: {','.join(v or '' for v in r.values())}")
elif intensos:
    print(f"DISPAROU. {len(intensos)} registro(s):")
    for r in intensos:
        print(f"  - {r['participante']} · {r['medicamento']} {r['dose_mg']} mg · {r['sintoma']} · intensidade {r['intensidade']}/10 · dura {r['duracao_horas']}h · orientação dada: {r['orientacao_dada']}")
else:
    maior = max((int(r["intensidade"]) for r in ontem), default=None)
    print(f"não disparou. {len(ontem)} registro(s) de D-1 olhados, maior intensidade: {maior if maior is not None else 'nenhum registro'}.")

ultimo = {}
for r in validas:
    ultimo[r["participante"]] = max(ultimo.get(r["participante"], r["data"]), r["data"])
parados = {p: d for p, d in ultimo.items() if (hoje - date.fromisoformat(d)).days > 7}
print(f"\nRegra 2 · Participante parou de registrar: ", end="")
if parados:
    print(f"DISPAROU. {len(parados)} participante(s):")
    for p, d in parados.items():
        print(f"  - {p} · último registro em {date.fromisoformat(d).strftime('%d/%m')} · há {(hoje - date.fromisoformat(d)).days} dias")
else:
    mais_antigo = min(ultimo.values()) if ultimo else None
    print(f"não disparou. {len(ultimo)} participantes olhados, último registro mais antigo: {mais_antigo}.")

falhas = [r for r in intensos if r["orientacao_dada"] != "fale com seu medico agora"]
print(f"\nRegra 3 · Escalonamento falhou: ", end="")
if falhas:
    print(f"DISPAROU. {len(falhas)} registro(s):")
    for r in falhas:
        print(f"  - {r['participante']} · {r['sintoma']} · intensidade {r['intensidade']}/10 · dura {r['duracao_horas']}h · orientação dada: '{r['orientacao_dada']}'. O produto respondeu 'continue monitorando' a um sintoma que devia escalar.")
else:
    print(f"não disparou. {len(intensos)} registro(s) intenso(s) em D-1 olhado(s); 100% receberam 'fale com seu medico agora'.")
