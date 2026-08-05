import requests

def check_github_repo():
    # URL da API do GitHub que testamos na Etapa 1
    url = "https://api.github.com/repos/octocat/Hello-World"
    
    print("Consultando a API do GitHub...")
    response = requests.get(url)
    
    # Verifica se a requisição deu certo (código 200 significa sucesso)
    if response.status_code == 200:
        data = response.json()
        
        # Extraindo informações úteis do JSON
        repo_name = data.get("name")
        owner = data.get("owner", {}).get("login")
        open_issues = data.get("open_issues_count")
        
        print("\n [SUCESSO] Auditoria realizada com sucesso!")
        print(f"- Nome do Repositório: {repo_name}")
        print(f"- Dono: {owner}")
        print(f"- Issues (Problemas) Abertas: {open_issues}")
    else:
        print(f"[ERRO] Falha ao consultar a API. Código: {response.status_code}")

if __name__ == "__main__":
    check_github_repo()