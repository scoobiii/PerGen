import os

# Função para criar diretórios e arquivos necessários
def create_directory_structure(base_path):
    # Estrutura de diretórios a ser criada
    directories = [
        "tests/unit",              # Testes unitários
        "tests/integration",       # Testes de integração
        "tests/functional",        # Testes funcionais
        "tests/performance",       # Testes de performance
        "tests/stress",            # Testes de stress
        "config",                  # Configurações
        "logs"                     # Logs do sistema
    ]
    
    # Criação dos diretórios
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Diretório criado: {dir_path}")
    
    # Arquivos principais do projeto
    files = {
        "app.py": "API de Geração de Personas",
        "persona_imagem.py": "API de Geração de Imagens",
        "requirements.txt": "Dependências do projeto",
        "Dockerfile": "Dockerfile para containerização",
        "README.md": "Documentação do projeto",
        "config/config.py": "Configuração central do ambiente",
    }
    
    # Criação dos arquivos com conteúdo básico
    for file, description in files.items():
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(f"# {description}\n\n")
                f.write(f"# TODO: Implementar o conteúdo deste arquivo.\n")
            print(f"Arquivo criado: {file_path}")
    
    # Criando os arquivos de testes
    test_files = {
        "tests/unit/test_persona.py": "Testes unitários para a API de personas",
        "tests/unit/test_imagem.py": "Testes unitários para a API de imagens",
        "tests/integration/test_integration_persona.py": "Testes de integração da API de personas",
        "tests/integration/test_integration_imagem.py": "Testes de integração da API de imagens",
        "tests/functional/test_funcional_persona.py": "Testes funcionais para a geração de personas",
        "tests/functional/test_funcional_imagem.py": "Testes funcionais para a geração de imagens",
        "tests/performance/test_performance_persona.py": "Testes de performance para a geração de personas",
        "tests/performance/test_performance_imagem.py": "Testes de performance para a geração de imagens",
        "tests/stress/test_stress_persona.py": "Testes de stress para a API de personas",
        "tests/stress/test_stress_imagem.py": "Testes de stress para a API de imagens",
    }
    
    # Criação dos arquivos de teste
    for file, description in test_files.items():
        file_path = os.path.join(base_path, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write(f"# {description}\n\n")
                f.write(f"# TODO: Implementar o conteúdo deste arquivo de teste.\n")
            print(f"Arquivo de teste criado: {file_path}")

# Função principal para executar a criação da estrutura
def main():
    base_path = os.getcwd()  # Caminho base onde o projeto será criado
    create_directory_structure(base_path)

if __name__ == "__main__":
    main()
