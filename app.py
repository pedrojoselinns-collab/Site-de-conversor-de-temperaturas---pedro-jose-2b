def celsius_para_fahrenheit(temperatura):
	return (temperatura * 9 / 5) + 32


def celsius_para_kelvin(temperatura):
	return temperatura + 273.15


def fahrenheit_para_celsius(temperatura):
	return (temperatura - 32) * 5 / 9


def fahrenheit_para_kelvin(temperatura):
	return (temperatura - 32) * 5 / 9 + 273.15


def kelvin_para_celsius(temperatura):
	return temperatura - 273.15


def kelvin_para_fahrenheit(temperatura):
	return (temperatura - 273.15) * 9 / 5 + 32


def main():
	conversoes = {
		"1": ("Celsius para Fahrenheit", celsius_para_fahrenheit, "C", "F"),
		"2": ("Celsius para Kelvin", celsius_para_kelvin, "C", "K"),
		"3": ("Fahrenheit para Celsius", fahrenheit_para_celsius, "F", "C"),
		"4": ("Fahrenheit para Kelvin", fahrenheit_para_kelvin, "F", "K"),
		"5": ("Kelvin para Celsius", kelvin_para_celsius, "K", "C"),
		"6": ("Kelvin para Fahrenheit", kelvin_para_fahrenheit, "K", "F"),
	}

	while True:
		print("\n=== Conversor de Temperatura ===")
		print("1 - Celsius para Fahrenheit")
		print("2 - Celsius para Kelvin")
		print("3 - Fahrenheit para Celsius")
		print("4 - Fahrenheit para Kelvin")
		print("5 - Kelvin para Celsius")
		print("6 - Kelvin para Fahrenheit")
		print("7 - Sair")

		opcao = input("Escolha uma opção: ").strip()

		if opcao == "7":
			print("Programa encerrado.")
			break

		if opcao not in conversoes:
			print("Opção inválida. Escolha uma opção de 1 a 7.")
			continue

		nome_conversao, funcao_conversao, unidade_origem, unidade_destino = conversoes[opcao]
		try:
			temperatura = float(input("Digite a temperatura: ").replace(",", "."))
		except ValueError:
			print("Temperatura inválida. Digite um número, como 25 ou 25,5.")
			continue

		resultado = funcao_conversao(temperatura)
		print(
			f"{nome_conversao}: {temperatura:.2f} {unidade_origem} = "
			f"{resultado:.2f} {unidade_destino}"
		)


if __name__ == "__main__":
	main()
