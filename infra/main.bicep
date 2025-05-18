param location string = resourceGroup().location
param appServicePlanName string = 'calculator-app-plan'
param webAppName string = 'calculator-app-${uniqueString(resourceGroup().id)}'

resource plan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: 'F1'
    tier: 'Free'
  }
  kind: 'Linux'
  properties: {
    reserved: true
  }
}

resource webApp 'Microsoft.Web/sites@2022-03-01' = {
  name: webAppName
  location: location
  tags: {
    'azd-service-name': 'calculator' // ✅ REQUIRED TAG
  }
  properties: {
    serverFarmId: plan.id
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.9'
    }
    httpsOnly: true
  }
}

output webAppUrl string = 'https://${webApp.name}.azurewebsites.net'
