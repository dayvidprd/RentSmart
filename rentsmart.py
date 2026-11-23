import csv


class Imovel:
    def __init__(self, tipo, quartos=1, garagem=False, vagas_extra=0):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.vagas_extra = vagas_extra

    def calcular_aluguel(self):
        if self.tipo == "Apartamento":
            valor = 700

            if self.quartos == 2:
                valor += 200

            if self.garagem:
                valor += 300

        elif self.tipo == "Casa":
            valor = 900

            if self.quartos == 2:
                valor += 250

            if self.garagem:
                valor += 300

        elif self.tipo == "Studio":
            valor = 1200
            valor += 250
            valor += self.vagas_extra * 60

        return valor


class Orcamento:
    def __init__(self, imovel, possui_criancas, parcelas_contrato):
        self.imovel = imovel
        self.possui_criancas = possui_criancas
        self.parcelas_contrato = parcelas_contrato
        self.taxa_contrato = 2000

    def calcular_desconto(self):
        if self.imovel.tipo == "Apartamento" and not self.possui_criancas:
            return self.imovel.calcular_aluguel() * 0.05

        return 0

    def calcular_aluguel_final(self):
        return self.imovel.calcular_aluguel() - self.calcular_desconto()

    def calcular_parcela_contrato(self):
        return self.taxa_contrato / self.parcelas_contrato

    def exibir_resumo(self):
        print("\n===== RENTSMART =====")
        print(f"Tipo de imóvel: {self.imovel.tipo}")
        print(f"Aluguel base e adicionais: R$ {self.imovel.calcular_aluguel():.2f}")
        print(f"Desconto: R$ {self.calcular_desconto():.2f}")
        print(f"Aluguel mensal final: R$ {self.calcular_aluguel_final():.2f}")
        print(f"Taxa contratual: R$ {self.taxa_contrato:.2f}")
        print(f"Parcelas do contrato: {self.parcelas_contrato}")
        print(f"Valor da parcela: R$ {self.calcular_parcela_contrato():.2f}")

    def gerar_csv(self):
        with open("projecao_rentsmart.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo)

            escritor.writerow([
                "Mes",
                "Aluguel",
                "Parcela Contratual",
                "Total Mensal"
            ])

            for mes in range(1, 13):
                aluguel = self.calcular_aluguel_final()

                if mes <= self.parcelas_contrato:
                    parcela = self.calcular_parcela_contrato()
                else:
                    parcela = 0

                total = aluguel + parcela

                escritor.writerow([
                    mes,
                    f"{aluguel:.2f}",
                    f"{parcela:.2f}",
                    f"{total:.2f}"
                ])

        print("\nArquivo CSV gerado com sucesso!")


def solicitar_numero(mensagem, minimo, maximo):
    while True:
        try:
            numero = int(input(mensagem))

            if minimo <= numero <= maximo:
                return numero

            print(f"Digite um número entre {minimo} e {maximo}.")

        except ValueError:
            print("Digite um número válido.")


def solicitar_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta in ["s", "sim"]:
            return True

        elif resposta in ["n", "nao", "não"]:
            return False

        print("Digite S para sim ou N para não.")


def main():
    print("===== RENTSMART - R.M IMÓVEIS =====")

    print("\nTipos de imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Studio")

    tipo_opcao = solicitar_numero("Escolha o imóvel: ", 1, 3)

    if tipo_opcao == 1:
        tipo = "Apartamento"

    elif tipo_opcao == 2:
        tipo = "Casa"

    else:
        tipo = "Studio"

    quartos = 1
    garagem = False
    vagas_extra = 0
    possui_criancas = False

    if tipo in ["Apartamento", "Casa"]:
        quartos = solicitar_numero(
            "Quantidade de quartos (1 ou 2): ", 1, 2
        )

        garagem = solicitar_sim_nao(
            "Deseja vaga de garagem? (S/N): "
        )

    if tipo == "Apartamento":
        possui_criancas = solicitar_sim_nao(
            "Possui crianças? (S/N): "
        )

    if tipo == "Studio":
        vagas_extra = solicitar_numero(
            "Quantidade de vagas adicionais (0 a 10): ", 0, 10
        )

    parcelas = solicitar_numero(
        "Em quantas parcelas deseja pagar o contrato (1 a 5)? ", 1, 5
    )

    imovel = Imovel(tipo, quartos, garagem, vagas_extra)

    orcamento = Orcamento(
        imovel,
        possui_criancas,
        parcelas
    )

    orcamento.exibir_resumo()
    orcamento.gerar_csv()


if __name__ == "__main__":
    main()