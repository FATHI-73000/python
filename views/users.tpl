<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Utilisateurs enregistrés</title>
</head>
<body>
    <h2>Liste des utilisateurs</h2>

    % if users:
        <ul>
        % for id, name in users:
            <li>ID {{id}} : {{name}}</li>
        % end
        </ul>
    % else:
        <p>Aucun utilisateur trouvé.</p>
    % end

    <p>
        <a href="/users?show=all">Voir tous</a> |
        <a href="/users?show=recent">Voir les 5 derniers</a>
    </p>
    <p><a href="/">Retour à l'accueil</a></p>
</body>
</html>
