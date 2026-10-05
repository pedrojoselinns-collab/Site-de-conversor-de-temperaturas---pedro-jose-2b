# Conversor de Temperatura

Projeto simples para converter temperaturas entre Celsius, Fahrenheit e Kelvin. Ele pode ser usado pelo terminal com Python ou pela interface web no navegador.

## Arquivos

- `app.py`: versão interativa para o terminal.
- `index.html`: versão web, abre diretamente no navegador.

## Usar a versão web

1. Abra a pasta do projeto no Visual Studio Code.
2. No Explorer do VS Code, clique com o botão direito em `index.html` e escolha **Reveal in File Explorer** (ou **Mostrar no Explorador de Arquivos**).
3. Abra `index.html` com o Google Chrome ou outro navegador.
4. Escolha a conversão, digite a temperatura e clique em **Converter**.

Não é necessário instalar dependências nem iniciar um servidor.

## Usar a versão Python

É necessário ter o Python 3 instalado. No terminal integrado do VS Code, dentro da pasta do projeto, execute:

```powershell
python app.py
```

Escolha uma opção de 1 a 6, informe a temperatura e pressione Enter. Para encerrar, escolha a opção 7. A versão de terminal também aceita temperatura decimal com vírgula ou ponto.

## Conversões disponíveis

1. Celsius para Fahrenheit
2. Celsius para Kelvin
3. Fahrenheit para Celsius
4. Fahrenheit para Kelvin
5. Kelvin para Celsius
6. Kelvin para Fahrenheit

Ambas as versões validam as entradas e mostram o resultado com as unidades correspondentes.