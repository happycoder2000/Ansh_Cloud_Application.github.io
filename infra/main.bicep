param location string = resourceGroup().location
param appName string
param storageAccountName string
param appServicePlanName string

module resourcesModule './resources.bicep' = {
  name: 'resourcesModule'
  params: {
    location: location
    appName: appName
    storageAccountName: storageAccountName
    appServicePlanName: appServicePlanName
  }
}
