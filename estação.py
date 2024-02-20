mes = input("Digite o seu mês: ")
if mes in ("Dezembro","Janeiro","Fevereiro"):
    estacao = "Verão"
elif mes in ("Março", "Abril", "Maio"):
    estacao = "Outono"
elif mes in ("Junho","Julho","Agosto"):
    estacao = "Inverno"
elif mes in ("Setembro", "Julho","Novembro"):
    estacao = "Primavera"
print(f"A estação é:{estacao}.")