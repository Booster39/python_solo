from neo4j import GraphDatabase

# Définir les informations d'authentification de votre base Neo4j
uri = "neo4j+s://78ceef0e.databases.neo4j.io:7687"  # L'URL de la base de données Neo4j
username = "neo4j" # L'identifiant
password = "v_9OqmeZdboEryhr76vwx1HTvPIJl8_lkV4rNK7VJ1A" # Le mot de passe

# Créer une session pour interagir avec la base Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))

# Exemple de requête Cypher pour récupérer des données
def run_query_cypher(query):
    with driver.session() as session:
        result = session.run(query)
        return result

# Exemple de requête Cypher pour récupérer les équipes du Brésil dans les finales
def country_result():  
    country_name = input("\nEntrez le nom du pays : ")  
    query = f"MATCH (f:Final)-[r:PLAY_FINAL]-(t:Team {{name: '{country_name}'}}) RETURN f, t, r"
    result = run_query_cypher(query)
    for record in result:
        print(record)

# Exemple de requête Cypher pour récupérer toutes les finales
def finals():    
    query = "MATCH (f:Final) RETURN f;"
    result = run_query_cypher(query)
    for record in result:
        print(record)

# Exemple de requête Cypher pour récupérer toutes les équipes ayant participées aux finales
def teams():
    query = "MATCH (t:Team) RETURN t"
    result = run_query_cypher(query)
    for record in result:
        print(record)

def main_menu():
    while True:
        print("Bienvenue dans votre application Final&Team !!!\n\n")
        print("Ci-dessous toutes les actions disponibles,")
        print("il suffira de taper le numéro dans l'invite de commande pour executer l'action souhaitée :\n")
        print("1 : Afficher toutes les finales (années, pays, …)")
        print("2 : Afficher toutes les équipes ayant participées aux finales")
        print("3 : Afficher les résultats obtenus pour une équipe donnée toutes années confondues")
        print("4 : Afficher le pays, la ville, le stade, les 2 équipes finalistes et le résultat pour une finale donnée")
        print("5 : Quitter")
        action_menu()


def action_menu():
    choice = input("\nVotre choix : ")
    if choice == "1":
        finals()
    elif choice == "2":
        teams()
    elif choice == "3":
        country_result()
    elif choice == "4":
        country_result()
    elif choice == "5":
        print("\nAu Revoir !!!\n")
        quit()
    else :
        print("\nMauvaise option, veillez taper un nouveau numéro :\n")
 

if __name__ == "__main__":
    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        main_menu()
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
    finally:
        driver.close()