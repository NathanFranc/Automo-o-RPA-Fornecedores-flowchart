$excludeFolders = @("venv", ".vscode", "__pycache__") 
$excludeFiles = @("Fornecedores_flow.zip", "*.xaml", "*.jproj")

$files = Get-ChildItem -Path . -Recurse | Where-Object {
    -not (
        ($_.PSIsContainer -and ($excludeFolders -contains $_.Name)) -or
        ($_.Name -like $excludeFiles)
    )
}

Compress-Archive -Path $files.FullName -DestinationPath "Fornecedores_flow.zip" -Force
