$tenantId = "<tenantId>"
$subscriptionId = "<subscriptionId>"
$congnitiveSearchKey = "<congnitiveSearchKey>"
$resouceGroupName = "<resouceGroupName>"
$functionAppName = "<functionAppName>"

az login --tenant $tenantId 
az account set --subscription $subscriptionId

az webapp config appsettings set --resource-group demo1 --name "openai-if-python" --settings congnitiveSearchKey=$congnitiveSearchKey

$pyfiles = Get-ChildItem -recurse .\* -Include function_app.py,host.json,requirements.txt,.python_packages -Force
Compress-Archive -Path $pyfiles  -DestinationPath ..\pythonapp.zip -Force
az functionapp deployment source config-zip --resource-group $resouceGroupName --name $functionAppName --src ..\pythonapp.zip --build-remote true --verbose
