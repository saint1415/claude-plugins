# Add claude-plugins to PATH
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
$newDir = "C:\Users\crissantos\claude-plugins"

if ($currentPath -notlike "*$newDir*") {
    [Environment]::SetEnvironmentVariable("Path", "$currentPath;$newDir", "User")
    Write-Host "Added to PATH successfully!" -ForegroundColor Green
    Write-Host "Restart your terminal to use 'claude-yolo' and 'claude-full' from anywhere."
} else {
    Write-Host "Already in PATH" -ForegroundColor Yellow
}
