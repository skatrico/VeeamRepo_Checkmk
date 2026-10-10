# Copyright (C) 2024 Dragosiz ft. Mario Casero mario.casero@dragosiz.es - License: GNU General Public License v2
# Este archivo es parte de la integración con Checkmk para monitorizar los repositorios de Veeam Backup.

$Repos = Get-VBRBackupRepository
$ScaleOutRepos = Get-VBRBackupRepository -ScaleOut
#$AzureRepo = $ScaleOutRepo.CapacityExtents.Repository.Name

Write-Host '<<<veeam_repo>>>'
foreach ($Repo in $Repos) {
    $RepoName = $Repo.Name -replace " ", "_"
    if ($Repo.GetContainer().CachedTotalSpace.IsInvalid -eq "True"){
    }
    else{
        $RepoTotalSpaceBytes = $Repo.GetContainer().CachedTotalSpace.InBytes
        $RepoFreeSpaceBytes = $Repo.GetContainer().CachedFreeSpace.InBytes
        $RepoUsedSpaceBytes = ($RepoTotalSpaceBytes - $RepoFreeSpaceBytes)
        $RepoState = $Repo.IsUnavailable

        Write-Host $RepoName $RepoTotalSpaceBytes $RepoUsedSpaceBytes $RepoFreeSpaceBytes $RepoState
    }
}

foreach ($ScaleOutRepo in $ScaleOutRepos) {
    $ScaleOutRepoName = $ScaleOutRepo.Name -replace " ", "_"
    #$ScaleOutTotalSpace = 0
    #$ScaleOutFreeSpace = 0
    #$ScaleOutUsedSpace = 0

    foreach ($ScaleOutCapacity in $ScaleOutRepo.Extent.Repository){
        $ScaleOutLocalRepoName = $ScaleOutCapacity.Name -replace " ", "_"
        $ScaleOutRepoTotalSpaceBytes = $ScaleOutCapacity.GetContainer().CachedTotalSpace.InBytes
        $ScaleOutRepoFreeSpaceBytes = $ScaleOutCapacity.GetContainer().CachedFreeSpace.InBytes
        $ScaleOutRepoUsedSpaceBytes = ($ScaleOutRepoTotalSpaceBytes - $ScaleOutRepoFreeSpaceBytes)
        $ScaleOutTotalSpaceBytes += $ScaleOutRepoTotalSpaceBytes
        $ScaleOutFreeSpaceBytes += $ScaleOutRepoFreeSpaceBytes
        $ScaleOutUsedSpaceBytes += $ScaleOutRepoUsedSpaceBytes
            
        Write-Host $ScaleOutLocalRepoName $ScaleOutRepoTotalSpaceBytes $ScaleOutRepoUsedSpaceBytes $ScaleOutRepoFreeSpaceBytes
    }

    write-host $ScaleOutRepoName $ScaleOutTotalSpaceBytes $ScaleOutUsedSpaceBytes $ScaleOutFreeSpaceBytes
}
