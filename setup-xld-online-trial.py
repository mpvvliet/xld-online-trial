###############
# Script creating data for the XLD online trial
#
# TO DO:
# - make idempotent

def create(id, type, values):
   return factory.configurationItem(id, type, values)

def deleteIds(ids):
	for id in ids:
		repository.delete(id)

def verifyNoValidationErrors(entity):
   if entity.validations is None or len(entity.validations) == 0:
       return entity
   else:
       raise Exception("Validations are present! Id=%s, Error:\n " % (entity.id, entity.validations.toString()))

def verifyNoValidationErrorsInRepoObjectsEntity(repositoryObjects):
   for repoObject in repositoryObjects:
       verifyNoValidationErrors(repoObject)

def saveRepositoryObjectsEntity(repoObjects):
	print "Saving repository objects"
	repositoryObjects = repository.create(repoObjects)
	verifyNoValidationErrorsInRepoObjectsEntity(repositoryObjects)
	print "Saved repository objects"
	return repositoryObjects

def save(listOfCis):
	return saveRepositoryObjectsEntity(listOfCis)

def resolveInfraId(id):
	id = id if id.startswith("Infrastructure/") else "Infrastructure/%s" % id
	return id;
	
def createLocalHost(id, notes = None):
	return create(resolveInfraId(id),'overthere.LocalHost',{'os':'UNIX','temporaryDirectoryPath':'/tmp', 'notes': notes})

###############

DIRECTORY_NOTE = 'Directories represent a grouping of CIs that have the same permissions in XL Deploy. Directories are similar to folders in Windows or Unix.'

# Clean up
deleteIds(['Environments/Intro', 'Infrastructure/Intro', 'Applications/Intro'])

# Sample content
infrastructureList = []

repository.create(factory.configurationItem('Infrastructure/Intro','core.Directory',{'notes': DIRECTORY_NOTE}))
infrastructureList.append(createLocalHost('Infrastructure/Intro/localhost', 'This host CI represents a server that XL Deploy can connect and deploy to. For this introduction, the host CI is of type overthere.LocalHost which represents the host that the XLD server is running on. XL Deploy supports various other types of hosts, such as SSH hosts and WinRM hosts.'))
infrastructureList.append(create('Infrastructure/Intro/localhost/container-unix', 'intro.Server', {'home': '/tmp', 'notes': 'This CI represents a target system on its parent host that XL Deploy can deploy to. Properties specific to this container can be configured here, such as the _home_ property in the Common tab. In this case, it is configured with the Unix temporary directory, _/tmp_. '}))
infrastructureList.append(create('Infrastructure/Intro/localhost/container-windows', 'intro.Server', {'home': '%TEMP%', 'notes': 'This CI represents a target system on its parent host that XL Deploy can deploy to. Properties specific to this container can be configured here, such as the _home_ property in the Common tab. In this case, it is configured with the Windows temporary directory, _%TEMP%_. '}))

save(infrastructureList)

# Environments

environmentsList = []

repository.create(factory.configurationItem('Environments/Intro','core.Directory',{'notes': DIRECTORY_NOTE}))
environmentsList.append(create('Environments/Intro/Dictionary','udm.Dictionary', {'entries':{'key':'value'}, 'notes': 'The Dictionary CI contains environment-specific key/value pairs that are used to tailor a deployment package to a specific environment during a deployment. XL Deploy scans deployment packages during the import process and finds all environment-specific values (called placeholders) in the package. During a deployment, XL Deploy looks through the dictionaries associated with the target environment to find the correct replacement value for the placeholder.'}))
environmentsList.append(create('Environments/Intro/INTRO-WINDOWS','udm.Environment',{'dictionaries': ['Environments/Intro/Dictionary'], 
	'members':[
		'Infrastructure/Intro/localhost/container-windows']}))
environmentsList.append(create('Environments/Intro/INTRO-UNIX','udm.Environment',{'dictionaries': ['Environments/Intro/Dictionary'], 
	'members':[
		'Infrastructure/Intro/localhost/container-unix']}))
save(environmentsList)

# Applications

#from java.io import File
#from com.google.common.io import Files

#data = Files.toByteArray(File('/path/to/sql.zip'))
#sqlscripts = factory.artifact('Applications/sqlApp/1.0/sql', 'sql.SqlScripts', {}, data)
#sqlscripts.filename = 'sql.zip'
#repository.create(sqlscripts)

deployit.importPackage('/Users/martin/Dev/Workspaces/Workspace-mpvvliet/xld-online-trial/Intro-1.0.dar')
deployit.importPackage('/Users/martin/Dev/Workspaces/Workspace-mpvvliet/xld-online-trial/Intro-2.0.dar')
