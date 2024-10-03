from github import Github
import numpy as np
import matplotlib.pyplot as plt

# Autenticação na API do GitHub 
g = Github("Seu Token do Git")

# Verificar o limite de requisições da API do GitHub
rate_limit = g.get_rate_limit()
print(f"Limite de requisições da API: {rate_limit.core.remaining} restantes")

# Repositório do TensorFlow
repo = g.get_repo("tensorflow/tensorflow")

# Obter os commits
commits = repo.get_commits()

# Listas para armazenar tamanhos dos commits
commit_sizes = []

# Coletar informações de tamanho de commits
try:
    for i, commit in enumerate(commits[:1000]): 
        stats = commit.stats
        commit_size = stats.additions + stats.deletions
        commit_sizes.append(commit_size)

        # Exibir progresso a cada 10 commits
        if (i + 1) % 10 == 0:
            print(f"{i + 1} commits processados")
    
    print("Coleta de dados concluída.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Verificar se há commits coletados antes de gerar o gráfico
if commit_sizes:
    # Ordenar tamanhos de commits e calcular a CDF
    commit_sizes_sorted = np.sort(commit_sizes)
    cdf = np.arange(1, len(commit_sizes_sorted) + 1) / len(commit_sizes_sorted)

    # Gerar o gráfico da CDF
    plt.figure(figsize=(8,6))
    plt.plot(commit_sizes_sorted, cdf, label="Commits no TensorFlow", color='blue')

    plt.xscale('log')
    plt.title("CDF dos Tamanhos de Commits no Repositório TensorFlow")
    plt.xlabel("Tamanho do Commit (Linhas de Código)")
    plt.ylabel("Frequência Acumulada")
    plt.grid(True)
    plt.legend()

    # Salvar o gráfico em PNG
    plt.savefig("cdf_commits_tensorflow.png", format='png', dpi=300)

    # Exibir o gráfico
    plt.show()

    print("Gráfico salvo como 'cdf_commits_tensorflow.png'.")
else:
    print("Nenhum dado de commit foi coletado.")


