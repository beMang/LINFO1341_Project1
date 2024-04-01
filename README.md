# LINFO1341 - Analyse de Shadow Drive

## Scénarios à étudier
* création d'un dossier/fichier
* uploader un fichier
* partager un fichier
* modifier un fichier 
* déplacer un fichier
* supprimer un fichier 
* jouer avec le type, la taille,... du fichier
* jouer avec la connexion internet : Wi-Fi, Ethernet ou partage 4G
* faire pareil pour des fichiers partagés
* tentative de connexion avec un mauvais mdp
* regarder la différence entre l'application native et le navigateur web
* regarder les requetes qui sont faites de façon périodique (même en inactivité de l'appli), pour voir si des modifications ont été faites, et voir l'effet lorsqu'il y a des modifications

## Partie plus spécifique par protocole

### DNS
* Au démarrage du site/de l'application : résolution DNS du nameserver
* On observe 1 requêtes A et AAAA, on a 2 IP pour le record A (IPv4) et pas de résultat pour AAAA, le serveur ne supporte donc que IPv4, et on a 2 adresses qui restent fixes (en tt cas pendant la durée de notre étude). Les ips de ses serveurs sont : 46.105.132.157 et 46.105.132.156.
* Regarder du coté du serveur autoritatif shadow.tech

### TCP
* Taile des paquets lors d'un transfert de fichier (bcp de ACK de 54 bits et 1514 pour le contenu)

### TLS
* Type de crypto lors du Client Hello et Server Hello
* Nom du domaine permet de filtrer les requêtes

### HTTPS
* Regarder les différents Header et message échangés pour connaitre leur signification (SETTINGS, GOAWAY, MAGIC, WINDOWS_UPDATE...)

### UDP ET QUIC
* Pas de trafic QUIC et UDP

## Statistiques
* Taille
* Type de protocoles
* Volume de données échangés

## Observations générales
* Etablissment connexion sécurisée avec TLS
* Transfert des fichiers via TCP
* Requetes toutes les 30 secondes environs pour synchronisation
* 2 serveurs de dispos, l'appli en choisit un aléatoirement
* Appli native et web a l'air d'avoir le mm comportement (mais on ne voit pas les requetes HTTPS à cause du SSLKEYLOGFILE qui ne fonctionnne que sur le navigateur web...)
* Pas de différence entre Ethernet et Wifi

# Traces

Pour garder les traces, il faut sauvegarder la trace (.pcapng) et le fichier contenant les clés SSL qui permettront de décoder le contenu en mettant
le paramètre "(Pre)-Master-Secret log filename" de Wireshark pointant vers ce fichier.

# Référence
* J'ai fait un zotero pour tout gérer plus facilement