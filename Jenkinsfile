def label = "mypod-${UUID.randomUUID().toString()}"

podTemplate(label: label, containers: [
  containerTemplate(name: 'jenkins-slave', image: 'ghotsgoose33/jenkins-slave:v1', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl:v1.8.8', command: 'cat', ttyEnabled: true)
], serviceAccount: "jenkins") 
{
def app
def dockerRegistry = "100.71.71.71:5000"
//def Creds = "git_cred"
def projName = "post-python"
def imageVersion = "v1"
def imageName = "100.71.71.71:5000/post-service:${imageVersion}"
def imageN = '100.71.71.71:5000/post-service:'


node(label)
{\
    try{
        stage("Git Checkout"){
            git(
                branch: "post",
                url: 'https://github.com/Kv-045DevOps/SRM-POST.git')
                //credentialsId: "${Creds}")
            sh "git rev-parse --short HEAD > .git/commit-id"
            imageTag= readFile ".git/commit-id"
        }
        stage("Info"){
            sh "echo ${imageTag}"
        }
        stage ("Unit Tests"){
            sh 'echo "Here will be unit tests"'
        }
        stage("Test code using PyLint and change version"){
	    container('python-alpine'){
	    sh "python3 ${pathTocode}/sed_python.py template.yml ${dockerRegistry}/post-service ${imageTag}"
            pathTocode = pwd()
            sh "python3 ${pathTocode}/pylint-test.py ${pathTocode}/app/app.py"
        }
	}
        stage("Build docker image"){
			container('docker'){
				pathdocker = pwd()
				sh "docker build ${pathdocker} -t ${imageName}"
				sh "docker images"
//	withCredentials([usernamePassword(credentialsId: 'docker_registry', passwordVariable: 'dockerPassword', usernameVariable: 'dockerUser')]) {
				sh "docker login -u ${env.dockerUser} -p ${env.dockerPassword}"
				sh "docker push ${imageName}"
//        }
			}
        }
        stage("Check push image to Docker Registry"){
	    container('python-alpine'){
            pathTocode = pwd()
            sh "python3 ${pathTocode}/images-registry-test.py ${dockerRegistry} ${projName} ${imageTag}"
        }
	}
        stage("Deploy to Kubernetes"){
			container('kubectl'){
				sh "kubectl apply -f template.yml"
				sh "kubectl get pods --namespace=production"
			}
        }
	stage ("Unit Tests"){
            sh 'echo "Here will be e2e tests"'
        }
    }
    catch(err){
        currentBuild.result = 'Failure'
    }
}
}
